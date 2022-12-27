#include "snafu.h"

#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <tclap/CmdLine.h>

using namespace snafu;

namespace {

class ArgumentParser {
public:
  /** Constructor.
   *
   * @param[in] argc The number of arguments.
   * @param[in] argv The arguments.
   *
   * @raises TCLAP::ArgException
   */
  ArgumentParser(int argc, char **argv)
  {
    TCLAP::CmdLine cmd{"Fuel requirement parser", ' ', "0.1"};

    TCLAP::UnlabeledValueArg<std::string> input_file_arg{
      "input_file", "The name of the file with fuel requirements", true, "",
      "input_file"};
    cmd.add(input_file_arg);

    cmd.parse(argc, argv);
    filename_ = input_file_arg.getValue();
  }

  /** Get the input filename containing the fuel requirements.
   *
   * @return The input filename.
   */
  std::string
  get_filename() const
  {
    return filename_;
  }

private:
  std::string filename_;
};

Snafu
sum_fuel_requirements(std::string_view filename)
{
  std::ifstream input_file{filename.data()};

  if (!input_file.is_open()) {
    std::cerr << "Unable to open fuel requirement file: " << filename
              << std::endl;
    exit(1);
  }

  int64_t total = 0;
  std::string line;
  int line_counter = 0;
  while (std::getline(input_file, line)) {
    ++line_counter;
    Snafu snafu{line, Snafu::Base_t::SNAFU};
    auto const decimal_value = snafu.get_decimal();
    if (decimal_value < 0) {
      std::cerr << "Invalid fuel requirement, line " << line_counter << ":\n"
                << line << std::endl;
      exit(1);
    }
    assert(decimal_value + total < std::numeric_limits<int64_t>::max());
    total += snafu.get_decimal();
  }
  return Snafu{total};
}

} // anonymous namespace

int
main(int argc, char *argv[])
{
  ArgumentParser parser{argc, argv};
  std::string filename = parser.get_filename();
  Snafu const total = sum_fuel_requirements(filename);
  std::cout << total.get_snafu() << std::endl;
  return 0;
}
