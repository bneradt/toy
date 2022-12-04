#include <algorithm>
#include <compare>
#include <cstdint>
#include <fstream>
#include <numeric>
#include <string>
#include <iostream>
#include <string_view>
#include <vector>

/// A class representing the inventory of calories held by an elf.
class Inventory
{
public:

  /// Add an item with some calories to the inventory.
  void add_item(uint32_t calories)
  {
    calories_ += calories;
  }

  /// Retrieve the total number of calories in the inventory.
  uint32_t get_total_calories() const
  {
    return calories_;
  }

  auto operator<=>(Inventory const& rhs) const
  {
    return calories_ <=> rhs.calories_;
  }

private:
  uint32_t calories_ = 0;
};

/// A file parser returning a vector of Inventory objects.
class FileParser
{
public:
  FileParser(std::string_view filename)
    : filename_{filename}
    , infile_{filename_}
  {
  }

  bool is_valid() const
  {
    return infile_.is_open();
  }

  /// Parse a file and return a vector of Inventory objects.
  std::vector<Inventory> parse_file()
  {
    std::ifstream infile{filename_};

    if (!infile.is_open()) {
      throw std::runtime_error{"Could not open file"};
    }

    std::vector<Inventory> inventories;

    std::string line;
    inventories.emplace_back();
    while (std::getline(infile_, line)) {
      if (line.empty()) {
        inventories.emplace_back();
      } else {
        auto const calories = std::stoul(line);
        inventories.back().add_item(calories);
      }
    }
    return inventories;
  }

private:
  std::string filename_;
  std::ifstream infile_;
};

int
main(int argc, char* argv[])
{
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
    return 1;
  }

  std::string_view filename{argv[1]};
  FileParser parser{filename};

  if (!parser.is_valid()) {
    std::cerr << "Could not open file " << filename << std::endl;
    return 1;
  }

  auto inventories = parser.parse_file();
  std::sort(inventories.begin(), inventories.end());

  auto const &max_inventory = inventories.back();
  std::cout << "Out of " << inventories.size() << " inventory with the maximum of calories has: " << std::endl << max_inventory.get_total_calories() << std::endl;

  // Sum the last three elements.
  uint32_t sum = 0;
  std::for_each(inventories.end() - 3, inventories.end(), [&sum](auto const& inventory) {
    sum += inventory.get_total_calories();
  });

  std::cout << "The sum of the last three inventories is: " << sum << std::endl;

  return 0;
}
