#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

class Rucksack {
public:
  Rucksack() = delete;

  // Since each of the compartments are string_views pointing to memory owned
  // by contents_, we have to be careful to re-home them with every
  // constructor. The default constructor will wind up having the string_views
  // point to invalid memory.

  Rucksack& operator=(Rucksack const& other)
  {
    contents_ = other.contents_;
    populate_compartments();
    return *this;
  }

  Rucksack(Rucksack&& other)
    : contents_{std::move(other.contents_)}
  {
    populate_compartments();
  }

  Rucksack(Rucksack const& other)
    : contents_(other.contents_)
  {
    populate_compartments();
  }


  Rucksack(std::string_view contents)
    : contents_(contents)
  {
    if (std::any_of(contents_.begin(), contents_.end(),
                    [](char c) { return !std::isalpha(c); })) {
      throw std::invalid_argument("Invalid character in contents");
    }
    populate_compartments();
  }

  /** Find the common item in the two compartments.
   *
   * @return The common item, or '\0' if there is none.
   */
  char find_common_item() const
  {
    // Find the first item that is in both compartments.
    for (auto const item: first_compartment_) {
      if (second_compartment_.find(item) != std::string_view::npos) {
        return item;
      }
    }
    return '\0';
  }

  /** A getter for the contents of the rucksack.
   *
   * @return The contents of the rucksack.
   */
  std::string_view get_contents() const
  {
    return contents_;
  }

private:
  /** Populate the std::string_view compartments from the memory in the
   * std::string contents_. */
  void populate_compartments()
  {
    // Evenly divide the contents into the two compartments.
    auto const half_size = contents_.size() / 2;

    // Populate the std::string_view from the memory in the std::string contents_.
    first_compartment_ = std::string_view(contents_.data(), half_size);
    second_compartment_ = std::string_view(contents_.data() + half_size, half_size);
  }

private:
  std::string contents_;
  std::string_view first_compartment_;
  std::string_view second_compartment_;
};

class Group {
public:

  /** A Group is made up of three Rucksacks.
   *
   * @param rucksack1 The first Rucksack.
   * @param rucksack2 The second Rucksack.
   * @param rucksack3 The third Rucksack.
   */
  Group(Rucksack const &rucksack1, Rucksack const &rucksack2, Rucksack const &rucksack3)
    : rucksack1_(rucksack1)
    , rucksack2_(rucksack2)
    , rucksack3_(rucksack3)
  {
  }

  /** Find the item that is in all three Rucksacks.
   *
   * @return The common item, or '\0' if there is none.
   */
  char find_common_item() const
  {
    // Find the first item that is in all three Rucksacks.
    for (auto const item: rucksack1_.get_contents()) {
      if (rucksack2_.get_contents().find(item) != std::string_view::npos &&
          rucksack3_.get_contents().find(item) != std::string_view::npos)
      {
        assert(('a' <= item && item <= 'z') || ('A' <= item && item <= 'Z'));
        return item;
      }
    }
    return '\0';
  }

private:
  Rucksack const rucksack1_;
  Rucksack const rucksack2_;
  Rucksack const rucksack3_;
};

std::vector<Rucksack>
parse_rucksacks(std::string_view input_file)
{
  std::vector<Rucksack> rucksacks;
  std::ifstream input{input_file.data()};

  if (!input) {
    throw std::runtime_error{"Unable to open input file"};
  }

  std::string line;
  while (std::getline(input, line)) {
    rucksacks.emplace_back(line);
  }
  return rucksacks;
}

int
get_item_priority(char item)
{
  if (item == '\0') {
    return 0;
  }
  if (item >= 'a' && item <= 'z') {
    return item - 'a' + 1;
  } else if (item >= 'A' && item <= 'Z') {
    return item - 'A' + 27;
  } else {
    throw std::runtime_error{"Invalid item"};
  }

  // Not reached.
  return 0;
}

void
test_get_item_priority()
{
  assert(get_item_priority('a') == 1);
  assert(get_item_priority('b') == 2);
  assert(get_item_priority('c') == 3);
  assert(get_item_priority('z') == 26);
  assert(get_item_priority('A') == 27);
  assert(get_item_priority('B') == 28);
  assert(get_item_priority('Z') == 52);
  assert(get_item_priority('\0') == 0);
}

int
count_rucksack_priorities(std::vector<Rucksack> const& rucksacks)
{
  int item_number = 0;
  int priority_count = 0;
  for (auto const& rucksack: rucksacks) {
    ++item_number;
    auto const common_item = rucksack.find_common_item();
    if (common_item == '\0') {
      std::cerr << "No common item found in rucksack: " << item_number << ", contents: " << rucksack.get_contents() << std::endl;
      continue;
    }
    auto const value = get_item_priority(common_item);
    priority_count += value;
  }
  return priority_count;
}

int
count_group_priorities(std::vector<Group> const &groups)
{
  int item_number = 0;
  int priority_count = 0;
  for (auto const& group: groups) {
    ++item_number;
    auto const common_item = group.find_common_item();
    if (common_item == '\0') {
      std::cerr << "No common item found in group: " << item_number << std::endl;
      continue;
    }
    auto const value = get_item_priority(common_item);
    priority_count += value;
  }
  return priority_count;
}

int
main(int argc, char* argv[])
{
  test_get_item_priority();

  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
    return 1;
  }

  auto file_input = std::string_view{argv[1]};
  auto const rucksacks = parse_rucksacks(file_input);
  auto const priority_count = count_rucksack_priorities(rucksacks);
  std::cout << "Total priority count: " << priority_count << std::endl;

  // Make groups from every three rucksacks.
  std::vector<Group> groups;
  for (auto i = 0u; i < rucksacks.size(); i += 3) {
    groups.emplace_back(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]);
  }
  auto const group_priority_count = count_group_priorities(groups);
  std::cout << "Total group priority count: " << group_priority_count << std::endl;

  return 0;
}
