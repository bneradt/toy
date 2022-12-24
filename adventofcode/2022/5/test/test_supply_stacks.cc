#include "supply_stacks.h"
#include <catch2/catch_test_macros.hpp>

TEST_CASE("Test supply stacks", "[supply_stacks]")
{
  SupplyStacks stacks{!SupplyStacks::USE_UPDATED_MOVER};

  stacks.add_crate(2, 'D');

  stacks.add_crate(1, 'N');
  stacks.add_crate(2, 'C');

  stacks.add_crate(1, 'Z');
  stacks.add_crate(2, 'M');
  stacks.add_crate(3, 'P');

  /*

     This should have configured the stacks like so:

         [D]
     [N] [C]
     [Z] [M] [P]
      1   2   3
  */

  auto heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'N', 'D', 'P'});

  // Calling a second time should not change the result.
  heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'N', 'D', 'P'});

  stacks.move_crate(1, 2, 1);
  heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'D', 'C', 'P'});

  stacks.move_crate(3, 1, 3);
  heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'\0', 'C', 'Z'});

  stacks.move_crate(2, 2, 1);
  heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'M', '\0', 'Z'});

  stacks.move_crate(1, 1, 2);
  heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'C', 'M', 'Z'});
}

TEST_CASE("Test supply stacks", "[double_digits]")
{
  SupplyStacks stacks{!SupplyStacks::USE_UPDATED_MOVER};

  stacks.add_crate(2, 'D');

  stacks.add_crate(1, 'N');
  stacks.add_crate(2, 'C');

  stacks.add_crate(1, 'Z');
  stacks.add_crate(2, 'M');
  stacks.add_crate(3, 'P');

  stacks.add_crate(2, 'A');
  stacks.add_crate(2, 'B');
  stacks.add_crate(2, 'C');
  stacks.add_crate(2, 'D');
  stacks.add_crate(2, 'E');
  stacks.add_crate(2, 'F');
  stacks.add_crate(2, 'G');
  stacks.add_crate(2, 'H');
  stacks.add_crate(2, 'I');

  stacks.move_crate(11, 2, 1);
  auto heads = stacks.get_stack_tops();
  REQUIRE(heads.size() == 3);
  REQUIRE(heads == std::vector<char>{'H', 'I', 'P'});
}
