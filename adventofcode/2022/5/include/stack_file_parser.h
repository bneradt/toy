#pragma once

#include <fstream>
#include <string_view>

class SupplyStacks;

/** Parse the input file for the program. */
class StackFileParser
{
public:
  /** Constructor.
   *
   * @param input_file_path Path to the input file to parse.
   */
  StackFileParser(std::string_view input_file_path, SupplyStacks &supply_stacks);

  /** Parse the input file and update the SupplyStacks object.
   *
   * @return true if the file was parsed successfully, false otherwise.
   */
  bool parse();

private:
  /** The name of the file to parse. */
  std::string input_file_path_;

  /** The stream for the input file. */
  std::ifstream input_file_;

  /** The supply stacks that are populated and manipulated as the file is
   * parsed. */
  SupplyStacks &supply_stacks_;
};
