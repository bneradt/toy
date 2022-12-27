#include "snafu_internals.h"

#include <cassert>
#include <stdexcept>
#include <string>
#include <string_view>
#include <vector>

namespace snafu {

int
convert_snafu_char_to_int(char snafu_char)
{
  switch (snafu_char) {
    case '=':
      return -2;
    case '-':
      return -1;
    case '0':
      return 0;
    case '1':
      return 1;
    case '2':
      return 2;
  }
  std::string message = "Invalid SNAFU character: ";
  message += snafu_char;
  throw std::invalid_argument(message);
  return 0;
}

int64_t
convert_snafu_to_decimal(std::string_view snafu)
{
  int64_t decimal = 0;
  uint64_t multiplier = 1;
  for (auto it = snafu.rbegin(); it != snafu.rend(); ++it) {
    char c = *it;
    int64_t delta = 0;
    switch (c) {
      case '0':
        break;
      case '2':
        delta += multiplier;
        // fallthrough
      case '1':
        delta += multiplier;
        break;
      case '=':
        delta -= multiplier;
        // fallthrough
      case '-':
        delta -= multiplier;
        break;
      default:
        std::string message = "Invalid SNAFU character: ";
        message += c;
        throw std::invalid_argument(message);
    }
    // Make sure we don't overflow our multiplier uint64_t.
    if (multiplier > (std::numeric_limits<uint64_t>::max() / 5)) {
      throw std::overflow_error("Overflow in SNAFU multiplier value");
    }
    multiplier *= 5;
    // Make sure we don't overflow our int64_t.
    if (delta > 0 && decimal > std::numeric_limits<int64_t>::max() - delta) {
      throw std::overflow_error("SNAFU overflow");
    }

    // Conversely, make sure we don't underflow our int64_t either.
    if (delta < 0 && decimal < std::numeric_limits<int64_t>::min() - delta) {
      throw std::underflow_error("SNAFU underflow");
    }
    decimal += delta;
  }
  return decimal;
}

std::string
sum_two_snafus(std::string_view snafu1, std::string_view snafu2)
{
  std::vector<char> sum;
  int carry = 0;

  std::string snafu1_reversed{snafu1};
  std::reverse(snafu1_reversed.begin(), snafu1_reversed.end());

  std::string snafu2_reversed{snafu2};
  std::reverse(snafu2_reversed.begin(), snafu2_reversed.end());

  std::string_view longer_snafu = snafu1.size() > snafu2.size() ? snafu1_reversed : snafu2_reversed;
  std::string_view shorter_snafu = snafu1.size() > snafu2.size() ? snafu2_reversed : snafu1_reversed;
  auto const max_size = longer_snafu.size();
  for (auto place = 0u; place < max_size; ++place) {
    int value1 = convert_snafu_char_to_int(longer_snafu[place]);
    int value2 = 0;
    if (place < shorter_snafu.size()) {
      value2 = convert_snafu_char_to_int(shorter_snafu[place]);
    }
    int place_sum = value1 + value2 + carry;

    switch (place_sum) {
      case -5:
        sum.push_back('0');
        carry = -1;
        break;
      case -4:
        sum.push_back('1');
        carry = -1;
        break;
      case -3:
        sum.push_back('2');
        carry = -1;
        break;
      case -2:
        sum.push_back('=');
        carry = 0;
        break;
      case -1:
        sum.push_back('-');
        carry = 0;
        break;
      case 0:
        sum.push_back('0');
        carry = 0;
        break;
      case 1:
        sum.push_back('1');
        carry = 0;
        break;
      case 2:
        sum.push_back('2');
        carry = 0;
        break;
      case 3:
        sum.push_back('=');
        carry = 1;
        break;
      case 4:
        sum.push_back('-');
        carry = 1;
        break;
      case 5:
        sum.push_back('=');
        carry = 1;
        break;
      default:
        // We must be missing a case.
        assert(false);
    }
  }

  // Handle any leftover carry.
  switch (carry) {
    case -2:
      sum.push_back('=');
      break;
    case -1:
      sum.push_back('-');
      break;
    case 0:
      break;
    case 1:
      sum.push_back('1');
      break;
    case 2:
      sum.push_back('2');
      break;
    default:
      // We must be missing a case.
      assert(false);
  }

  // Put the vector in a string, reversing it so that it is in the expected
  // human readable order.
  std::string sum_str;
  for (auto it = sum.rbegin(); it != sum.rend(); ++it) {
    sum_str.push_back(*it);
  }
  return sum_str;
}

std::string
convert_decimal_to_snafu(int64_t decimal)
{
  std::string snafu;
  assert(decimal >= 0);

  if (decimal == 0) {
    return "0";
  }

  while (decimal != 0) {

    std::string this_snafu;

    // Find the largest power of five that is less than the decimal value.
    int exponent_of_five = 0;
    int64_t power_of_five = 1;
    while ((power_of_five * 5) <= decimal) {
      power_of_five *= 5;
      ++exponent_of_five;
    }
    int64_t multiplier = 0;
    while ((power_of_five * (multiplier + 1)) <= decimal) {
      ++multiplier;
    }
    // The multiplier should be between 0 and 4, inclusive.
    assert(0 <= multiplier && multiplier < 5);

    // We have our value. Now convert to a SNAFU for this iteration.
    if (multiplier == 3 || multiplier == 4) {
      ++exponent_of_five;
      power_of_five *= 5;
      this_snafu = "1";
      for (int i = 0; i < exponent_of_five; ++i) {
        this_snafu += "0";
      }
      if (multiplier == 3) {
        this_snafu[1] = '=';
      } else {
        this_snafu[1] = '-';
      }
    } else {
      // Start with the digit {0,1,2}.
      this_snafu = std::to_string(multiplier);
      // Pad with 0s.
      for (int i = 0; i < exponent_of_five; ++i) {
        this_snafu += "0";
      }
    }
    auto const snafu_value = convert_snafu_to_decimal(this_snafu);
    assert(snafu_value <= decimal);
    decimal -= snafu_value;

    // Add this iteration's SNAFU to the total.
    if (snafu.empty()) {
      snafu = this_snafu;
    } else {
      snafu = sum_two_snafus(snafu, this_snafu);
    }
  }
  return snafu;
}

} // namespace snafu
