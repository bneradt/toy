#include "occupant.h"
#include "square.h"

#include <catch2/catch_test_macros.hpp>
#include <memory>

TEST_CASE("Occupant", "[occupant_factory]") {
  Square s;

  SECTION("Empty") {
    auto o = Occupant::occupant_factory('.', &s);
    REQUIRE(o == nullptr);
  }

  SECTION("Expedition") {
    auto o = Occupant::occupant_factory('E', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->is_expedition());
  }

  SECTION("Wall") {
    auto o = Occupant::occupant_factory('#', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->is_wall());
  }

  SECTION("NorthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('^', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->is_blizzard());
    Occupant &base = *o;
    REQUIRE(typeid(base) == typeid(NorthBlowingBlizzard));
  }

  SECTION("SouthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('v', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->is_blizzard());
    Occupant &base = *o;
    REQUIRE(typeid(base) == typeid(SouthBlowingBlizzard));
  }

  SECTION("EastBlowingBlizzard") {
    auto o = Occupant::occupant_factory('>', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->is_blizzard());
    Occupant &base = *o;
    REQUIRE(typeid(base) == typeid(EastBlowingBlizzard));
  }

  SECTION("WestBlowingBlizzard") {
    auto o = Occupant::occupant_factory('<', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->is_blizzard());
    Occupant &base = *o;
    REQUIRE(typeid(base) == typeid(WestBlowingBlizzard));
  }
  SECTION("Unrecognized Occupant") {
    REQUIRE_THROWS_AS(Occupant::occupant_factory('r', &s), std::invalid_argument);
  }
}

TEST_CASE("Occupant", "[get_string]") {
  Square s;

  SECTION("Empty") {
    auto o = Occupant::occupant_factory('.', &s);
    REQUIRE(o == nullptr);
  }

  SECTION("Expedition") {
    auto o = Occupant::occupant_factory('E', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->get_string() == "E");
  }

  SECTION("Wall") {
    auto o = Occupant::occupant_factory('#', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->get_string() == "#");
  }

  SECTION("NorthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('^', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->get_string() == "^");
  }

  SECTION("SouthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('v', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->get_string() == "v");
  }

  SECTION("EastBlowingBlizzard") {
    auto o = Occupant::occupant_factory('>', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->get_string() == ">");
  }

  SECTION("WestBlowingBlizzard") {
    auto o = Occupant::occupant_factory('<', &s);
    REQUIRE(o != nullptr);
    REQUIRE(o->get_string() == "<");
  }
}

TEST_CASE("Occupant", "[advance]") {
  Square s;

  Square north_square;
  north_square.set_south_neighbor(&s);
  s.set_north_neighbor(&north_square);

  Square south_square;
  south_square.set_north_neighbor(&s);
  s.set_south_neighbor(&south_square);

  Square east_square;
  east_square.set_west_neighbor(&s);
  s.set_east_neighbor(&east_square);

  Square west_square;
  west_square.set_east_neighbor(&s);
  s.set_west_neighbor(&west_square);

  SECTION("Wall") {
    auto o = Occupant::occupant_factory('#', &s);
    s.add_occupant(o.get());
    REQUIRE(s.is_wall());
    o->advance();
    REQUIRE(s.is_wall());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("Expedition") {
    auto o = Occupant::occupant_factory('E', &s);
    s.add_occupant(o.get());
    REQUIRE(s.has_expedition());
    o->advance();
    REQUIRE(s.has_expedition());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("NorthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('^', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "^");
    o->advance();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.get_string() == "^");
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("SouthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('v', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "v");
    o->advance();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.get_string() == "v");
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("EastBlowingBlizzard") {
    auto o = Occupant::occupant_factory('>', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == ">");
    o->advance();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.get_string() == ">");
    REQUIRE(west_square.is_empty());
  }

  SECTION("WestBlowingBlizzard") {
    auto o = Occupant::occupant_factory('<', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "<");
    o->advance();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.get_string() == "<");
  }
}

TEST_CASE("Occupant", "[reverse]") {

  Square s;

  Square north_square;
  north_square.set_south_neighbor(&s);
  s.set_north_neighbor(&north_square);

  Square south_square;
  south_square.set_north_neighbor(&s);
  s.set_south_neighbor(&south_square);

  Square east_square;
  east_square.set_west_neighbor(&s);
  s.set_east_neighbor(&east_square);

  Square west_square;
  west_square.set_east_neighbor(&s);
  s.set_west_neighbor(&west_square);

  SECTION("Wall") {
    auto o = Occupant::occupant_factory('#', &s);
    s.add_occupant(o.get());
    REQUIRE(s.is_wall());
    o->reverse();
    REQUIRE(s.is_wall());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("Expedition") {
    auto o = Occupant::occupant_factory('E', &s);
    s.add_occupant(o.get());
    REQUIRE(s.has_expedition());
    o->reverse();
    REQUIRE(s.has_expedition());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("NorthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('^', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "^");
    o->reverse();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.get_string() == "^");
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("SouthBlowingBlizzard") {
    auto o = Occupant::occupant_factory('v', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "v");
    o->reverse();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.get_string() == "v");
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.is_empty());
  }

  SECTION("EastBlowingBlizzard") {
    auto o = Occupant::occupant_factory('>', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == ">");
    o->reverse();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.is_empty());
    REQUIRE(west_square.get_string() == ">");
  }

  SECTION("WestBlowingBlizzard") {
    auto o = Occupant::occupant_factory('<', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "<");
    o->reverse();
    REQUIRE(s.is_empty());
    REQUIRE(north_square.is_empty());
    REQUIRE(south_square.is_empty());
    REQUIRE(east_square.get_string() == "<");
    REQUIRE(west_square.is_empty());
  }
}
