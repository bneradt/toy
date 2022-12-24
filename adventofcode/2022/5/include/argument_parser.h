#pragma once

#include <string>
#include <string_view>

/** A class parse command line arguments. */
class ArgumentParser
{
public:
  /** Construct an ArgumentParser.
   *
   * @param argc The number of command line arguments.
   * @param argv The command line arguments.
   */
  ArgumentParser(int argc, char **argv);

  /** Parse the command line arguments.
   *
   * @return True if the arguments were parsed successfully, false otherwise.
   */
  bool parse();

  /** Retrieve the input file name.
   *
   * @return The input file name.
   */
  std::string_view get_input_filename() const;

  /** Retrieve whether the updated mover should be used.
   *
   * @return True if the updated mover should be used, false otherwise.
   */
  bool use_updated_mover() const;

private:
  /** The number of command line arguments passed to the program. */
  int argc_;

  /** The command line arguments passed to the program. */
  char **argv_;

  /** The input file name with the description of the supply stacks and the
   * crate movement. */
  std::string input_file_;

  /** Whether to use the updated moving capabilities. */
  bool updated_mover_;
};
