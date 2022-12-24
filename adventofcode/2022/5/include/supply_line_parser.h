#pragma once

#include "supply_stacks.h"
#include <string_view>

/** Parse input lines to initialize a SupplyStacks object. */
class SupplyLineParser
{
public:
  /** Create a parser for the given stacks.
   *
   * @param[in] stacks The stacks to initialize manipulate per the line input.
   */
  SupplyLineParser(SupplyStacks &stacks);

  /** Parse a line of input. */
  bool parse(std::string_view line);

private:
  /** Add crates to each specified stack.
   *
   * @a line is expected to be of the form like this:
   *
   *   [Z] [M] [P]
   *
   * @param[in] line The line to parse.
   *
   * @return true if the line was parsed successfully, false otherwise.
   */
  bool parse_stack_line(std::string_view line);

  /** Parse and apply a crate move command.
   * @a line is expected to be of the form like this:
   *
   *   move 2 from 2 to 1
   *
   * In this example, the top two crates from stack 2 are moved to stack 1.
   *
   * @param[in] line The line to parse.
   *
   * @return true if the line was parsed successfully, false otherwise.
   */
  bool parse_move_line(std::string_view line);

private:
  SupplyStacks &stacks_;
  bool am_initializing_stacks_ = true;
};
