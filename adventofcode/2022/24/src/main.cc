#include "valley.h"

#include <fstream>
#include <string>
#include <string_view>
#include <tclap/CmdLine.h>

namespace {

class ArgumentParser
{
public:
  ArgumentParser(int argc, char **argv)
  {
    TCLAP::CmdLine cmd("Find the shortest path through the valley", ' ', "0.9");
    TCLAP::UnlabeledValueArg<std::string> input_file_arg(
      "input_file", "Input file", true, "", "input file");
    cmd.add(input_file_arg);
    cmd.parse(argc, argv);
    input_file_ = input_file_arg.getValue();
  }

  std::string get_input_file() const
  {
    return input_file_;
  }

private:
  std::string input_file_;
};

Valley
parse_valley(std::string_view input_file)
{
  std::ifstream input(input_file.data());
  if (!input) {
    std::string message = "Could not open input file: ";
    message += input_file;
    throw std::runtime_error(message);
  }

  Valley valley;
  std::string line;
  while (std::getline(input, line)) {
    if (line.empty()) {
      continue;
    }
    break;
  }
  return valley;
}

} // anonymous namespace

int
main(int argc, char* argv[])
{
  ArgumentParser parser(argc, argv);
  Valley valley = parse_valley(parser.get_input_file());

  return 0;
}
