#include "argument_parser.h"

#include <tclap/CmdLine.h>

ArgumentParser::ArgumentParser(int argc, char **argv) : argc_(argc), argv_(argv) {}

bool
ArgumentParser::parse()
{
  try {
    TCLAP::CmdLine cmd("Supply stack Solver", ' ', "0.1");

    // Take a file name as a positional argument.
    TCLAP::UnlabeledValueArg<std::string> input_file_arg("input_file", "The input file name", true, "", "input filename");
    cmd.add(input_file_arg);

    // Take a switch to use the updated mover.
    TCLAP::SwitchArg updated_mover_arg("u", "updated_mover", "Use the updated mover", cmd, false);

    cmd.parse(argc_, argv_);

    input_file_    = input_file_arg.getValue();
    updated_mover_ = updated_mover_arg.getValue();
  } catch (TCLAP::ArgException &e) {
    std::cerr << "Failed to parse command line arguments: " << e.error() << std::endl;
    return false;
  }
  return true;
}

std::string_view
ArgumentParser::get_input_filename() const
{
  return input_file_;
}

bool
ArgumentParser::use_updated_mover() const
{
  return updated_mover_;
}
