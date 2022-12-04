#include <cassert>
#include <chrono>
#include <fstream>
#include <iostream>
#include <string_view>
#include <vector>

using std::chrono::duration_cast;
using std::chrono::microseconds;

class Range {
public:
  Range(int start, int end) : start_(start), end_(end) {}

  bool contains(Range const &other) const {
    return start_ <= other.start_ && other.end_ <= end_;
  }

  bool is_contained_by(Range const &other) const {
    return other.contains(*this);
  }

  bool overlaps(Range const &other) const {
    return start_ <= other.end_ && other.start_ <= end_;
  }

private:
  int start_;
  int end_;
};

void
test_Range()
{
  Range r0(0, 10);
  Range r1(10, 20);
  assert(!r0.contains(r1));
  assert(!r0.is_contained_by(r1));
  assert(!r1.contains(r0));
  assert(!r1.is_contained_by(r0));

  assert(r0.overlaps(r1));
  assert(r1.overlaps(r0));

  Range r2(5, 10);
  assert(r0.contains(r2));
  assert(!r0.is_contained_by(r2));
  assert(r2.is_contained_by(r0));
  assert(!r2.contains(r0));

  assert(r0.overlaps(r2));
  assert(r2.overlaps(r0));

  Range r3(11, 20);
  assert(!r0.overlaps(r3));
  assert(!r3.overlaps(r0));
  assert(r1.overlaps(r3));
  assert(r3.overlaps(r1));
}

class Pair {
public:
  Pair(Range const &first, Range const &second) : first_(first), second_(second) {}

  bool one_is_a_subset_of_the_other() const {
    return first_.contains(second_) || second_.contains(first_);
  }

  bool overlaps() const {
    return first_.overlaps(second_);
  }

private:
  Range first_;
  Range second_;
};

void
test_Pair()
{

  Range r0(0, 10);
  Range r1(10, 20);
  Range r2(5, 10);
  Range r3(11, 20);

  Pair p0(r0, r1);
  assert(!p0.one_is_a_subset_of_the_other());
  assert(p0.overlaps());

  Pair p1(r0, r2);
  assert(p1.one_is_a_subset_of_the_other());
  assert(p1.overlaps());

  Pair p2(r0, r3);
  assert(!p2.overlaps());
}

class FileProcessor {
public:
  FileProcessor(std::string_view filename)
    : filename_{filename}
    , file_{filename.data()}
  {}

  bool is_valid() {
    return file_.is_open();
  }

  std::vector<Pair> get_pairs() {
    std::string line;
    std::vector<Pair> pairs;
    while (std::getline(file_, line)) {
      auto comma_position = line.find(',');

      auto first_dash = line.find('-');
      auto first_start = std::stoi(line.substr(0, first_dash));
      auto first_end = std::stoi(line.substr(first_dash + 1, comma_position - first_dash - 1));
      Range range1{first_start, first_end};

      auto second_dash = line.find('-', comma_position);
      auto second_start = std::stoi(line.substr(comma_position + 1, second_dash - comma_position - 1));
      auto second_end = std::stoi(line.substr(second_dash + 1));
      Range range2{second_start, second_end};

      pairs.emplace_back(range1, range2);
    }
    return pairs;
  }

private:
  std::string_view filename_;
  std::ifstream file_;
};

int
main(int argc, char *argv[])
{
#if TEST
  test_Range();
  test_Pair();
#endif

  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " filename" << std::endl;
    return 1;
  }

#if TIMING
  auto const start_time = std::chrono::high_resolution_clock::now();
#endif
  FileProcessor processor{argv[1]};
  if (!processor.is_valid()) {
    std::cerr << "Could not open file " << argv[1] << std::endl;
    return 1;
  }

  auto const pairs = processor.get_pairs();
  uint32_t subset_count = 0;
  uint32_t overlap_count = 0;
  for (auto const &pair : pairs) {
    if (pair.one_is_a_subset_of_the_other()) {
      ++subset_count;
    }
    if (pair.overlaps()) {
      ++overlap_count;
    }
  }
#if TIMING
  auto const end_time = std::chrono::high_resolution_clock::now();
#endif

  std::cout << "subsets: " << subset_count << std::endl;
  std::cout << "overlaps: " << overlap_count << std::endl;
#if TIMING
  std::cout << "time: " << duration_cast<microseconds>(end_time - start_time).count() << "us" << std::endl;
#endif
}
