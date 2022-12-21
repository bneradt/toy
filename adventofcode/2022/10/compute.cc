#include <cassert>
#include <deque>
#include <iostream>
#include <fstream>
#include <string>
#include <string_view>

class Instruction {
public:
  enum class Type {
    NOOP,
    ADDX,
  };

  Instruction(Type type, int x)
    : type_(type)
    , x_(x)
    , num_cycles_consumed_{0}
    {
      switch(type) {
        case Type::NOOP:
          num_cycles_needed_ = 1;
          break;
        case Type::ADDX:
          num_cycles_needed_ = 2;
          break;
      }
    }

  bool process_cycle(int &register_out) {
    ++num_cycles_consumed_;
    assert(num_cycles_consumed_ <= num_cycles_needed_);

    switch (type_) {
    case Type::NOOP:
      return true;
    case Type::ADDX:
      if (num_cycles_consumed_ == num_cycles_needed_) {
        register_out += x_;
        return true;
      } else {
        return false;
      }
    }

    // Should never get here.
    assert(false);
    return false;
  }

private:
  Type const type_;
  int x_ = 0;

  int num_cycles_needed_ = 0;
  int num_cycles_consumed_ = 0;
};

class Processor {
public:
  Processor(std::deque<Instruction> &&instructions)
    : instructions_(std::move(instructions)) {}

  int process_cycle() {
    if (instructions_.empty()) {
      return register_value;
    }

    auto &instruction = instructions_.front();
    if (instruction.process_cycle(register_value)) {
      instructions_.pop_front();
    }

    return register_value;
  }

  int get_register_value() const {
    return register_value;
  }

  bool is_done() const {
    return instructions_.empty();
  }

private:
  int register_value = 1;
  std::deque<Instruction> instructions_;
};

class ProcessSignalStrength {
public:
  ProcessSignalStrength(Processor &processor)
    : processor_(processor) {}

  int process_until_done() {
    int cycle_count = 0;
    int signal_strength_sum = 0;
    while (!processor_.is_done()) {
      ++cycle_count;
      auto const register_value = processor_.get_register_value();
      processor_.process_cycle();
      if (cycle_count == 20) {
        int signal_strength = register_value * cycle_count;
        std::cout << "Register value during cycle 20: " << register_value << ", signal strength: " << signal_strength << std::endl;
        signal_strength_sum += signal_strength;
      } else if (cycle_count > 20 && (cycle_count - 20) % 40 == 0) {
        int signal_strength = register_value * cycle_count;
        std::cout << "Register value during cycle " << cycle_count << ": " << register_value << ", signal strength: " << signal_strength << std::endl;
        signal_strength_sum += signal_strength;
      }
    }
    return signal_strength_sum;
  }

private:
  Processor &processor_;
};

std::deque<Instruction>
parse_instructions(std::string_view filename)
{
  std::deque<Instruction> instructions;
  std::ifstream file{filename.data()};

  if (!file.is_open()) {
    std::cerr << "Failed to open file: " << filename << std::endl;
    return instructions;
  }

  int line_number = 0;
  std::string line;
  while (std::getline(file, line)) {
    if (line.empty()) {
      ++line_number;
      continue;
    }

    std::string_view line_view{line};

    if (line_view.starts_with("noop")) {
      instructions.emplace_back(Instruction::Type::NOOP, 0);
    } else if (line_view.starts_with("addx")) {
      line_view.remove_prefix(4);
      auto const x = std::stoi(std::string{line_view});
      instructions.emplace_back(Instruction::Type::ADDX, x);
    } else {
      std::cerr << "Unknown instruction at line " << line_number << ": " << line_view << std::endl;
    }
    ++line_number;
  }
  return instructions;
}

int
main(int argc, char **argv)
{
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
    return 1;
  }

  auto instructions = parse_instructions(argv[1]);
  Processor processor{std::move(instructions)};
  ProcessSignalStrength process_signal_strength{processor};
  auto const signal_strength = process_signal_strength.process_until_done();

  std::cout << "Signal strength: " << signal_strength << std::endl;

  return 0;
}
