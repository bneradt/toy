#include "snafu.h"

#include <catch2/catch_test_macros.hpp>

using namespace snafu;

TEST_CASE("Snafu", "[snafu]")
{
  SECTION("Constructors")
  {
    SECTION("Default")
    {
      Snafu snafu;
      CHECK(snafu.get_decimal() == 0);
      CHECK(snafu.get_snafu() == "0");
    }

    SECTION("Decimal")
    {
      Snafu snafu{2022};
      CHECK(snafu.get_decimal() == 2022);
      CHECK(snafu.get_snafu() == "1=11-2");

      snafu = Snafu{314159265};
      CHECK(snafu.get_decimal() == 314159265);
      CHECK(snafu.get_snafu() == "1121-1110-1=0");
    }

    SECTION("Snafu")
    {
      Snafu snafu{"1121-1110-1=0", Snafu::Base_t::SNAFU};
      CHECK(snafu.get_decimal() == 314159265);
      CHECK(snafu.get_snafu() == "1121-1110-1=0");

      snafu = Snafu{"1=11-2", Snafu::Base_t::SNAFU};
      CHECK(snafu.get_decimal() == 2022);
      CHECK(snafu.get_snafu() == "1=11-2");
    }
  }

  SECTION("Addition")
  {
    SECTION("Decimal")
    {
      Snafu snafu{10};
      snafu += Snafu{5};
      CHECK(snafu.get_decimal() == 15);
      CHECK(snafu.get_snafu() == "1=0");
    }

    SECTION("Snafu")
    {
      Snafu snafu{"1-", Snafu::Base_t::SNAFU};
      snafu += Snafu{"11", Snafu::Base_t::SNAFU};
      CHECK(snafu.get_decimal() == 10);
      CHECK(snafu.get_snafu() == "20");
    }
  }

  SECTION("Subtraction")
  {
    SECTION("Decimal")
    {
      Snafu snafu{30};
      snafu -= Snafu{15};
      CHECK(snafu.get_decimal() == 15);
      CHECK(snafu.get_snafu() == "1=0");
    }

    SECTION("Snafu")
    {
      Snafu snafu{"1=0", Snafu::Base_t::SNAFU};
      snafu -= Snafu{"20", Snafu::Base_t::SNAFU};
      CHECK(snafu.get_decimal() == 5);
      CHECK(snafu.get_snafu() == "10");
    }

    SECTION("Zero")
    {
      Snafu snafu{"1=0", Snafu::Base_t::SNAFU};
      snafu -= Snafu{"1=0", Snafu::Base_t::SNAFU};
      CHECK(snafu.get_decimal() == 0);
      CHECK(snafu.get_snafu() == "0");
    }

    SECTION("Negative")
    {
      Snafu smaller{"1=0", Snafu::Base_t::SNAFU};
      Snafu larger{"1-0", Snafu::Base_t::SNAFU};
      CHECK_THROWS(smaller -= larger);
      CHECK_THROWS(smaller - larger);
    }
  }
}
