#include "snafu.h"
#include "snafu_internals.h"

#include <cassert>
#include <stdexcept>
#include <string>
#include <string_view>
#include <vector>

namespace snafu {

Snafu::Snafu() : decimal_{0}, snafu_{"0"} {}

Snafu::Snafu(int64_t value)
  : decimal_{value}
  , snafu_{convert_decimal_to_snafu(value)}
{
}

Snafu::Snafu(std::string_view value, Base_t base)
{
  switch (base) {
  case Base_t::TEN:
    decimal_ = std::stoi(std::string{value});
    snafu_ = convert_decimal_to_snafu(decimal_);
    break;
  case Base_t::SNAFU:
    decimal_ = convert_snafu_to_decimal(value);
    snafu_ = std::string{value};
    break;
  }
}

Snafu
Snafu::operator+(Snafu const &rhs) const
{
  return Snafu{decimal_ + rhs.decimal_};
}

Snafu&
Snafu::operator+=(Snafu const &rhs)
{
  decimal_ += rhs.decimal_;
  snafu_ = convert_decimal_to_snafu(decimal_);
  return *this;
}

Snafu
Snafu::operator-(Snafu const &rhs) const
{
  auto const difference = decimal_ - rhs.decimal_;
  if (difference < 0) {
    std::string message = "Cannot subtract " + rhs.snafu_ + " from " + snafu_ +
                          " because the result is negative.";
    throw std::runtime_error(message);
  }
  return Snafu{decimal_ - rhs.decimal_};
}

Snafu&
Snafu::operator-=(Snafu const &rhs)
{
  if ((decimal_ - rhs.decimal_) < 0) {
    std::string message = "Cannot subtract " + rhs.snafu_ + " from " + snafu_ +
                          " because the result is negative.";
    throw std::runtime_error(message);
  }
  decimal_ -= rhs.decimal_;
  snafu_ = convert_decimal_to_snafu(decimal_);
  return *this;
}

int64_t
Snafu::get_decimal() const
{
  return decimal_;
}

std::string
Snafu::get_snafu() const
{
  return snafu_;
}

} // namespace snafu
