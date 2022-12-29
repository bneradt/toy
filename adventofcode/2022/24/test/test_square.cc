#include "square.h"
#include "occupant.h"

#include <catch2/catch_test_macros.hpp>

TEST_CASE("Square", "[constructor]") {
  SECTION("Default") {
    Square s;
    REQUIRE(s.is_empty());
    REQUIRE(s.is_empty_except_for_expediton() == false);
    REQUIRE(s.get_string() == ".");
    REQUIRE(s.get_number_of_occupants() == 0);
    REQUIRE(s.has_expedition() == false);
    REQUIRE(s.is_wall() == false);

    REQUIRE(s.get_north_neighbor() == nullptr);
    REQUIRE(s.get_south_neighbor() == nullptr);
    REQUIRE(s.get_east_neighbor() == nullptr);
    REQUIRE(s.get_west_neighbor() == nullptr);

    REQUIRE(s.get_next_nonwall_west_square() == nullptr);
    REQUIRE(s.get_next_nonwall_east_square() == nullptr);
    REQUIRE(s.get_next_nonwall_north_square() == nullptr);
    REQUIRE(s.get_next_nonwall_south_square() == nullptr);
  }

  SECTION("Wall") {
    Square s;
    auto o = Occupant::occupant_factory('#', &s);
    s.add_occupant(o.get());
    REQUIRE(s.is_wall());
    REQUIRE(s.get_string() == "#");
    REQUIRE(s.get_number_of_occupants() == 1);
    REQUIRE(s.has_expedition() == false);
  }

  SECTION("Expedition") {
    Square s;
    auto o = Occupant::occupant_factory('E', &s);
    s.add_occupant(o.get());
    REQUIRE(s.has_expedition());
    REQUIRE(s.get_string() == "E");
    REQUIRE(s.get_number_of_occupants() == 1);
    REQUIRE(s.is_empty_except_for_expediton());
  }

  SECTION("NorthBlowingBlizzard") {
    Square s;
    auto o = Occupant::occupant_factory('^', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "^");
    REQUIRE(s.get_number_of_occupants() == 1);
    REQUIRE(s.is_empty_except_for_expediton() == false);
  }

  SECTION("SouthBlowingBlizzard") {
    Square s;
    auto o = Occupant::occupant_factory('v', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "v");
    REQUIRE(s.get_number_of_occupants() == 1);
    REQUIRE(s.is_empty_except_for_expediton() == false);
  }

  SECTION("EastBlowingBlizzard") {
    Square s;
    auto o = Occupant::occupant_factory('>', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == ">");
    REQUIRE(s.get_number_of_occupants() == 1);
    REQUIRE(s.is_empty_except_for_expediton() == false);
  }

  SECTION("WestBlowingBlizzard") {
    Square s;
    auto o = Occupant::occupant_factory('<', &s);
    s.add_occupant(o.get());
    REQUIRE(s.get_string() == "<");
    REQUIRE(s.get_number_of_occupants() == 1);
    REQUIRE(s.is_empty_except_for_expediton() == false);
  }
}

TEST_CASE("Square", "[get_number_of_occupants]") {
  Square s;
  REQUIRE(s.get_number_of_occupants() == 0);
  auto o = Occupant::occupant_factory('v', &s);
  s.add_occupant(o.get());
  REQUIRE(s.get_number_of_occupants() == 1);
  auto o2 = Occupant::occupant_factory('<', &s);
  s.add_occupant(o2.get());
  REQUIRE(s.get_number_of_occupants() == 2);

  s.remove_occupant(o.get());
  REQUIRE(s.get_number_of_occupants() == 1);
  s.remove_occupant(o2.get());
  REQUIRE(s.get_number_of_occupants() == 0);
}

TEST_CASE("Square", "[neighbor]") {
  Square s;
  Square south_neighbor;
  s.set_south_neighbor(&south_neighbor);
  south_neighbor.set_north_neighbor(&s);

  Square north_neighbor;
  s.set_north_neighbor(&north_neighbor);
  north_neighbor.set_south_neighbor(&s);

  Square east_neighbor;
  s.set_east_neighbor(&east_neighbor);
  east_neighbor.set_west_neighbor(&s);

  Square west_neighbor;
  s.set_west_neighbor(&west_neighbor);
  west_neighbor.set_east_neighbor(&s);

  SECTION("NorthNeighbor") {
    REQUIRE(s.get_north_neighbor() == &north_neighbor);
    REQUIRE(s.get_next_nonwall_north_square() == &north_neighbor);
    REQUIRE(north_neighbor.get_south_neighbor() == &s);
  }

  SECTION("SouthNeighbor") {
    REQUIRE(s.get_south_neighbor() == &south_neighbor);
    REQUIRE(s.get_next_nonwall_south_square() == &south_neighbor);
    REQUIRE(south_neighbor.get_north_neighbor() == &s);
  }

  SECTION("EastNeighbor") {
    REQUIRE(s.get_east_neighbor() == &east_neighbor);
    REQUIRE(s.get_next_nonwall_east_square() == &east_neighbor);
    REQUIRE(east_neighbor.get_west_neighbor() == &s);
  }

  SECTION("WestNeighbor") {
    REQUIRE(s.get_west_neighbor() == &west_neighbor);
    REQUIRE(s.get_next_nonwall_west_square() == &west_neighbor);
    REQUIRE(west_neighbor.get_east_neighbor() == &s);
  }
}

TEST_CASE("Square", "[next_nonwall]") {

  SECTION("get_next_nonwall_north_square") {
    Square s;

    Square north;
    s.set_north_neighbor(&north);
    north.set_south_neighbor(&s);
    auto wall = Occupant::occupant_factory('#', &north);
    north.add_occupant(wall.get());

    Square south;
    s.set_south_neighbor(&south);
    south.set_north_neighbor(&s);

    north.set_north_neighbor(&south);
    south.set_south_neighbor(&north);

    REQUIRE(s.get_next_nonwall_north_square() == &south);
  }

  SECTION("get_next_nonwall_south_square") {
    Square s;

    Square north;
    s.set_north_neighbor(&north);
    north.set_south_neighbor(&s);

    Square south;
    s.set_south_neighbor(&south);
    south.set_north_neighbor(&s);
    auto wall = Occupant::occupant_factory('#', &south);
    south.add_occupant(wall.get());

    north.set_north_neighbor(&south);
    south.set_south_neighbor(&north);

    REQUIRE(s.get_next_nonwall_south_square() == &north);
  }

  SECTION("get_next_nonwall_east_square") {
    Square s;

    Square east;
    s.set_east_neighbor(&east);
    east.set_west_neighbor(&s);
    auto wall = Occupant::occupant_factory('#', &east);
    east.add_occupant(wall.get());

    Square west;
    s.set_west_neighbor(&west);
    west.set_east_neighbor(&s);

    east.set_east_neighbor(&west);
    west.set_west_neighbor(&east);

    REQUIRE(s.get_next_nonwall_east_square() == &west);
  }

  SECTION("get_next_nonwall_west_square") {
    Square s;

    Square east;
    s.set_east_neighbor(&east);
    east.set_west_neighbor(&s);

    Square west;
    s.set_west_neighbor(&west);
    west.set_east_neighbor(&s);
    auto wall = Occupant::occupant_factory('#', &west);
    west.add_occupant(wall.get());

    east.set_east_neighbor(&west);
    west.set_west_neighbor(&east);

    REQUIRE(s.get_next_nonwall_west_square() == &east);
  }
}
