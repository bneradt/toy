#include "snafu_internals.h"

#include <catch2/catch_test_macros.hpp>

TEST_CASE("Snafu Internals", "[convert_snafu_char_to_decimal]")
{
  CHECK(snafu::convert_snafu_char_to_int('=') == -2);
  CHECK(snafu::convert_snafu_char_to_int('-') == -1);
  CHECK(snafu::convert_snafu_char_to_int('0') == 0);
  CHECK(snafu::convert_snafu_char_to_int('1') == 1);
  CHECK(snafu::convert_snafu_char_to_int('2') == 2);

  CHECK_THROWS(snafu::convert_snafu_char_to_int('3'));
}

TEST_CASE("Snafu Internals", "[convert_snafu_to_decimal]")
{
  CHECK(snafu::convert_snafu_to_decimal("0") == 0);
  CHECK(snafu::convert_snafu_to_decimal("1") == 1);
  CHECK(snafu::convert_snafu_to_decimal("2") == 2);
  CHECK(snafu::convert_snafu_to_decimal("1=") == 3);
  CHECK(snafu::convert_snafu_to_decimal("1-") == 4);
  CHECK(snafu::convert_snafu_to_decimal("10") == 5);
  CHECK(snafu::convert_snafu_to_decimal("11") == 6);
  CHECK(snafu::convert_snafu_to_decimal("12") == 7);
  CHECK(snafu::convert_snafu_to_decimal("2=") == 8);
  CHECK(snafu::convert_snafu_to_decimal("2-") == 9);
  CHECK(snafu::convert_snafu_to_decimal("20") == 10);
  CHECK(snafu::convert_snafu_to_decimal("1=0") == 15);
  CHECK(snafu::convert_snafu_to_decimal("1-0") == 20);
  CHECK(snafu::convert_snafu_to_decimal("1=11-2") == 2022);
  CHECK(snafu::convert_snafu_to_decimal("1-0---0") == 12345);
  CHECK(snafu::convert_snafu_to_decimal("1121-1110-1=0") == 314159265);

  /*
   * 1=12=0202-000-=0
   *
   * 0           1     0
   * =           5   -10
   * -          25  -125
   * 0         125
   * 0         625
   * 0        3125
   * -       15625
   * 2       78125
   * 0      390625
   * 2     1953125
   * 0     9765625
   * =    48828125
   * 2   244140625
   * 1  1220703125
   * =  6103515625
   * 1 30517578125
   *
   * 30517578125 - 2* 6103515625 + 1220703125 + 2 * 244140625 - 2 * 48828125 +
   *     2 * 1953125 + 2 * 78125 - 15625 - 25 - 2 * 5 = 19925921840
   */
  CHECK(snafu::convert_snafu_to_decimal("1=12=0202-000-=0") == 19925921840);

  // We don't technically support negative numbers, but for now it's helpful to
  // make sure the single digit negative SNAFU numbers work.
  CHECK(snafu::convert_snafu_to_decimal("-") == -1);
  CHECK(snafu::convert_snafu_to_decimal("=") == -2);
}

TEST_CASE("Snafu Internals", "[convert_decimal_to_snafu]")
{
  CHECK(snafu::convert_decimal_to_snafu(0) == "0");
  CHECK(snafu::convert_decimal_to_snafu(1) == "1");
  CHECK(snafu::convert_decimal_to_snafu(2) == "2");
  CHECK(snafu::convert_decimal_to_snafu(3) == "1=");
  CHECK(snafu::convert_decimal_to_snafu(4) == "1-");
  CHECK(snafu::convert_decimal_to_snafu(5) == "10");
  CHECK(snafu::convert_decimal_to_snafu(6) == "11");
  CHECK(snafu::convert_decimal_to_snafu(7) == "12");
  CHECK(snafu::convert_decimal_to_snafu(8) == "2=");
  CHECK(snafu::convert_decimal_to_snafu(9) == "2-");
  CHECK(snafu::convert_decimal_to_snafu(10) == "20");
  CHECK(snafu::convert_decimal_to_snafu(15) == "1=0");
  CHECK(snafu::convert_decimal_to_snafu(20) == "1-0");
  CHECK(snafu::convert_decimal_to_snafu(2022) == "1=11-2");
  CHECK(snafu::convert_decimal_to_snafu(12345) == "1-0---0");
  CHECK(snafu::convert_decimal_to_snafu(314159265) == "1121-1110-1=0");
}

TEST_CASE("Snafu Internals", "[sum_two_snafus]")
{
  CHECK(snafu::sum_two_snafus("0", "0") == "0");
  CHECK(snafu::sum_two_snafus("1", "0") == "1");
  CHECK(snafu::sum_two_snafus("0", "1") == "1");
  CHECK(snafu::sum_two_snafus("-", "0") == "-");
  CHECK(snafu::sum_two_snafus("=", "0") == "=");
  CHECK(snafu::sum_two_snafus("2", "1") == "1=");
  CHECK(snafu::sum_two_snafus("2", "2") == "1-");
  CHECK(snafu::sum_two_snafus("10", "2") == "12");
  CHECK(snafu::sum_two_snafus("1=", "10") == "2=");

  // Test carry scenarios.
  CHECK(snafu::sum_two_snafus("20", "20") == "1-0");
  CHECK(snafu::sum_two_snafus("22", "22") == "1=-");
  CHECK(snafu::sum_two_snafus("2222", "1") == "1====");

  // Test some basic additions that sum to negative numbers and verify we
  // handle carrying negative values correctly.
  CHECK(snafu::sum_two_snafus("-", "-") == "=");
  CHECK(snafu::sum_two_snafus("-", "=") == "-2");
  CHECK(snafu::sum_two_snafus("=", "=") == "-1");
  CHECK(snafu::sum_two_snafus("==", "==") == "-01");
  CHECK(snafu::sum_two_snafus("===", "===") == "-001");
}
