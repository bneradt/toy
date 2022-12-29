#include "valley.h"

#include <catch2/catch_test_macros.hpp>

TEST_CASE("Valley", "[constructor]") {
  Valley v;
  REQUIRE(v.get_string() == "\n");
  REQUIRE(v.get_expedition_coordinates() == std::make_pair(0, 0));
}

TEST_CASE("Valley", "[add_square]") {
  Valley v;
  v.add_square('#');
  REQUIRE(v.get_string() == "#\n");

  v.add_square('E');
  REQUIRE(v.get_string() == "#E\n");
  REQUIRE(v.get_expedition_coordinates() == std::make_pair(0, 1));

  v.add_square('#');
  REQUIRE(v.get_string() == "#E#\n");
  v.add_square('#');
  REQUIRE(v.get_string() == "#E##\n");
}

TEST_CASE("Valley", "[start_new_row]") {
  Valley v;
  v.add_square('#');
  v.add_square('E');
  v.add_square('#');
  v.add_square('#');

  v.start_new_row();

  v.add_square('#');
  v.add_square('.');
  v.add_square('<');
  v.add_square('#');

  v.start_new_row();

  v.add_square('#');
  v.add_square('#');
  v.add_square('.');
  v.add_square('#');

  REQUIRE(v.get_string() == "#E##\n#.<#\n##.#\n");
  REQUIRE(v.get_expedition_coordinates() == std::make_pair(0, 1));
}

TEST_CASE("Valley", "[advance_weather_one_minute]") {
  Valley v;
  v.add_square('#');
  v.add_square('E');
  v.add_square('#');
  v.add_square('#');

  v.start_new_row();

  v.add_square('#');
  v.add_square('.');
  v.add_square('<');
  v.add_square('#');

  v.start_new_row();

  v.add_square('#');
  v.add_square('#');
  v.add_square('.');
  v.add_square('#');

  v.set_neighbors();
  v.advance_weather_one_minute();
  REQUIRE(v.get_string() == "#E##\n#<.#\n##.#\n");
  REQUIRE(v.get_expedition_coordinates() == std::make_pair(0, 1));

  v.advance_weather_one_minute();
  REQUIRE(v.get_string() == "#E##\n#.<#\n##.#\n");
}

TEST_CASE("Valley", "[reverse_weather_one_minute]") {
  Valley v;
  v.add_square('#');
  v.add_square('E');
  v.add_square('#');
  v.add_square('#');

  v.start_new_row();

  v.add_square('#');
  v.add_square('.');
  v.add_square('<');
  v.add_square('#');

  v.start_new_row();

  v.add_square('#');
  v.add_square('#');
  v.add_square('.');
  v.add_square('#');

  v.set_neighbors();
  v.reverse_weather_one_minute();
  REQUIRE(v.get_string() == "#E##\n#<.#\n##.#\n");
  REQUIRE(v.get_expedition_coordinates() == std::make_pair(0, 1));

  v.reverse_weather_one_minute();
  REQUIRE(v.get_string() == "#E##\n#.<#\n##.#\n");
}
