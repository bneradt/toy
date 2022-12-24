#include "supply_line_parser.h"
#include <iostream>

SupplyLineParser::SupplyLineParser(SupplyStacks &stacks) : stacks_(stacks) {}

bool
SupplyLineParser::parse(std::string_view line)
{
  if (line.empty()) {
    return true;
  }

  if (line.starts_with(" 1")) {
    // This marks the end of the stack initialization.
    am_initializing_stacks_ = false;
    return true;
  }

  if (am_initializing_stacks_) {
    if (!parse_stack_line(line)) {
      std::cerr << "Failed to parse stack initialization line: " << line << std::endl;
      return false;
    }
  } else {
    if (!parse_move_line(line)) {
      std::cerr << "Failed to parse stack move line: " << line << std::endl;
      return false;
    }
  }
  return true;
}

bool
SupplyLineParser::parse_stack_line(std::string_view line)
{
  auto index = 1;
  while (!line.empty()) {
    if (line.starts_with("    ")) {
      ++index;
      line.remove_prefix(4);
      continue;
    }
    if (line[0] == ' ') {
      line.remove_prefix(1);
    }
    if (line.size() < 3) {
      std::cerr << "Invalid crate specification: " << line << std::endl;
      return false;
    }
    // Take the first three characters.
    char crate_name = line[1];
    stacks_.add_crate(index, crate_name);
    ++index;
    line.remove_prefix(3);
  }
  return true;
}

bool
SupplyLineParser::parse_move_line(std::string_view line)
{
  // The command should start with "move".
  if (!line.starts_with("move ")) {
    std::cerr << "Line does not start with \"move\": " << line << std::endl;
    return false;
  }

  // Parse the stack size.
  line.remove_prefix(5);
  auto next_space       = line.find(' ');
  auto const stack_size = std::stoul(std::string{line.substr(0, next_space)});
  line.remove_prefix(next_space + 1);

  // The next word should be "from".
  if (!line.starts_with("from ")) {
    std::cerr << "Line does not contain \"from\": " << line << std::endl;
    return false;
  }
  line.remove_prefix(5);
  next_space      = line.find(' ');
  auto const from = std::stoul(std::string{line.substr(0, next_space)});
  line.remove_prefix(next_space + 1);

  // The next word should be "to".
  if (!line.starts_with("to ")) {
    std::cerr << "Line does not contain \"to\": " << line << std::endl;
    return false;
  }
  line.remove_prefix(3);
  auto const to = std::stoul(std::string{line});

  stacks_.move_crate(stack_size, from, to);
  return true;
}
