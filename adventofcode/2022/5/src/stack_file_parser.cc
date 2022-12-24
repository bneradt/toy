#include "stack_file_parser.h"
#include "supply_stacks.h"
#include "supply_line_parser.h"

#include <iostream>

StackFileParser::StackFileParser(std::string_view input_file_path, SupplyStacks &supply_stacks)
  : input_file_path_(input_file_path), input_file_(input_file_path), supply_stacks_(supply_stacks)
{
}

bool
StackFileParser::parse()
{
  if (!input_file_.is_open()) {
    std::cerr << "Failed to open input file: " << input_file_path_ << std::endl;
    return false;
  }
  SupplyLineParser parser(supply_stacks_);
  std::string line;
  int line_count = 0;
  while (std::getline(input_file_, line)) {
    ++line_count;
    if (!parser.parse(line)) {
      std::cerr << "Failed to parse line " << line_count << ":\n" << line << std::endl;
      return false;
    }
  }
  return true;
}
