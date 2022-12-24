#include "argument_parser.h"
#include "supply_stacks.h"
#include "stack_file_parser.h"

#include <iostream>
#include <fstream>
#include <string>
#include <string_view>

int
main(int argc, char **argv)
{
  ArgumentParser argument_parser(argc, argv);
  if (!argument_parser.parse()) {
    return 1;
  }

  std::string_view input_file{argument_parser.get_input_filename()};
  SupplyStacks stacks{argument_parser.use_updated_mover()};
  StackFileParser parser(input_file, stacks);
  if (!parser.parse()) {
    std::cerr << "Failed to parse input file: " << input_file << std::endl;
    return 1;
  }

  auto const tops = stacks.get_stack_tops();
  for (auto const &top : tops) {
    std::cout << top;
  }
  std::cout << std::endl;
  return 0;
}
