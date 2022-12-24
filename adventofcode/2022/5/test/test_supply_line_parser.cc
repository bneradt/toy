#include "supply_line_parser.h"
#include "supply_stacks.h"

#include <catch2/catch_test_macros.hpp>

#include <string>
#include <vector>

std::vector<std::string> const line_input = {
  "    [D]    ",        "[N] [C]    ",        "[Z] [M] [P]",        " 1   2   3 ",        "",
  "move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2",
};

std::vector<std::string> const long_input = {
  "    [D]    ",         "    [C]    ", "    [M]    ", "    [A]    ", "    [B]    ", "    [C]    ", "    [D]    ",
  "    [E]    ",         "    [F]    ", "    [G]    ", "[N] [H]    ", "[Z] [I] [P]", " 1   2   3 ", "",
  "move 11 from 2 to 1",
};

TEST_CASE("Test supply line parser", "[supply_line_parser]")
{
  SupplyStacks stacks{!SupplyStacks::USE_UPDATED_MOVER};
  SupplyLineParser parser(stacks);

  for (auto const &line : line_input) {
    parser.parse(line);
  }
  auto stack_tops = stacks.get_stack_tops();
  REQUIRE(stack_tops.size() == 3);
  REQUIRE(stack_tops == std::vector<char>{'C', 'M', 'Z'});
}

TEST_CASE("Test double digits", "[supply_line_parser]")
{
  SupplyStacks stacks{!SupplyStacks::USE_UPDATED_MOVER};
  SupplyLineParser parser(stacks);

  for (auto const &line : long_input) {
    parser.parse(line);
  }
  auto stack_tops = stacks.get_stack_tops();
  REQUIRE(stack_tops.size() == 3);
  REQUIRE(stack_tops == std::vector<char>{'H', 'I', 'P'});
}
