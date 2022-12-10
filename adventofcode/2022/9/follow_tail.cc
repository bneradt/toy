#include <array>
#include <cassert>
#include <chrono>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_set>
#include <vector>

class Position
{
public:
  Position() = default;

  bool operator==(const Position& other) const
  {
    return x_ == other.x_ && y_ == other.y_;
  }

  int get_x() const { return x_; }
  int get_y() const { return y_; }

  void go_up() { ++y_; }
  void go_down() { --y_; }
  void go_left() { --x_; }
  void go_right() { ++x_; }

  void follow(Position const &other)
  {
    // Make sure that we did make a mistake following such that other got too
    // far away from us.
    assert(abs(other.x_ - x_) <= 2);
    assert(abs(other.y_ - y_) <= 2);

    if (abs(other.x_ - x_) > 1) {
      if (other.x_ > x_) {
        go_right();
      } else {
        go_left();
      }

      // See whether y should be adjusted as well.
      if (abs(other.y_ - y_) > 0) {
        if (other.y_ > y_) {
          go_up();
        } else {
          go_down();
        }
      }
    }

    if (abs(other.y_ - y_) > 1) {
      if (other.y_ > y_) {
        go_up();
      } else {
        go_down();
      }

      // See whether x should be adjusted as well.
      if (abs(other.x_ - x_) > 0) {
        if (other.x_ > x_) {
          go_right();
        } else {
          go_left();
        }
      }
    }
  }

private:
  int x_ = 0;
  int y_ = 0;
};

// Specialize std::hash for Position so it can go in a std::unordered_set.
namespace std {
template <>
struct hash<Position> {
  size_t operator()(Position const& p) const {
    return hash<int>()(p.get_x()) ^ hash<int>()(p.get_y());
  }
};
}

class Node
{
public:
  Node() = default;
  Node(Node *tail)
    : tail_(tail)
  {}

  void set_tail(Node *tail) { tail_ = tail; }

  size_t get_tail_position_count() const
  {
    return visited_.size();
  }

  void follow(Position const &other)
  {
    position_.follow(other);
    visited_.insert(position_);
    if (tail_) {
      tail_->follow(position_);
    }
  }

  void go_up()
  {
    position_.go_up();
    visited_.insert(position_);
    if (tail_) {
      tail_->follow(position_);
    }
  }

  void go_down()
  {
    position_.go_down();
    visited_.insert(position_);
    if (tail_) {
      tail_->follow(position_);
    }
  }

  void go_left()
  {
    position_.go_left();
    visited_.insert(position_);
    if (tail_) {
      tail_->follow(position_);
    }
  }

  void go_right()
  {
    position_.go_right();
    visited_.insert(position_);
    if (tail_) {
      tail_->follow(position_);
    }
  }

private:
  Node *tail_ = nullptr;
  Position position_;

  std::unordered_set<Position> visited_;
};


class State
{
public:
  State(int num_tails)
  {
    head_ = Node();

    for (int i = 0; i < num_tails; ++i) {
      tails_.emplace_back();
    }

    Node *head = &head_;
    for (auto &tail: tails_) {
      head->set_tail(&tail);
      head = &tail;
    }
    tail_ = &tails_.back();
  }

  void move_head_up()
  {
    head_.go_up();
  }

  void move_head_down()
  {
    head_.go_down();
  }

  void move_head_left()
  {
    head_.go_left();
  }

  void move_head_right()
  {
    head_.go_right();
  }

  size_t get_tail_position_count() const { return tail_->get_tail_position_count(); }

private:
  Node head_;
  std::vector<Node> tails_;
  Node *tail_;
};

std::vector<std::string>
parse_instruction_file(std::string_view filename)
{
  std::vector<std::string> instructions;

  std::ifstream file(filename.data());
  if (!file.is_open()) {
    std::cerr << "Could not open file " << filename << std::endl;
    std::exit(1);
  }

  std::string line;
  while (std::getline(file, line)) {
    instructions.push_back(line);
  }

  return instructions;
}


void
dispatch_instruction(std::string_view instruction, State& state)
{
  char const direction = instruction[0];
  auto const magnitude = std::stoi(std::string(instruction.substr(2)));

  switch (direction)
  {
  case 'U':
    for (int i = 0; i < magnitude; ++i) {
      state.move_head_up();
    }
    break;
  case 'D':
    for (int i = 0; i < magnitude; ++i) {
      state.move_head_down();
    }
    break;
  case 'L':
    for (int i = 0; i < magnitude; ++i) {
      state.move_head_left();
    }
    break;
  case 'R':
    for (int i = 0; i < magnitude; ++i) {
      state.move_head_right();
    }
    break;
  default:
    std::cerr << "Invalid direction: " << direction << std::endl;
    assert(!"Invalid direction");
  }
}

int
main(int argc, char *argv[])
{
  // Get the name of the input file.
  if (argc != 3) {
    std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
    return 1;
  }
  auto const tail_count = std::stoi(argv[1]);
  State state(tail_count);

  std::string_view directions_file = argv[2];
  auto const instructions = parse_instruction_file(directions_file);

  for (auto const& instruction : instructions) {
    dispatch_instruction(instruction, state);
  }

  std::cout << "Tail position count: " << state.get_tail_position_count()
            << std::endl;
  return 0;
}
