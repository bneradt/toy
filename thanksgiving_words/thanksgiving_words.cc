#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_set>
#include <vector>

std::string_view DEFAULT_DICTIONARY_FILE = "en-common.wl";
std::string_view WORD_TO_ANALYZE = "thanksgiving";

// Parse a dictionary file into an unordered set of words.
std::vector<std::string>
parse_dictionary(std::string_view filename)
{
  std::vector<std::string> words;
  words.reserve(250'000);
  std::ifstream file(filename.data());
  if (!file.is_open()) {
    std::cerr << "Unable to open file: " << filename << std::endl;
    return words;
  }
  std::string word;
  while (file >> word) {
    words.push_back(word);
  }
  return words;
}

// Determine whether the given word is in word_to_analyze.
bool
find(std::string_view needle, std::string_view haystack)
{
  std::vector<char const*> used_characters;
  for (char const *finding = needle.data(); *finding; ++finding) {
    bool found_finding = false;
    for (char const *hay = haystack.data(); *hay; ++hay) {
      if (*finding == *hay) {
        if (std::find(used_characters.begin(), used_characters.end(), hay) != used_characters.end()) {
          continue;
        }
        used_characters.push_back(hay);
        found_finding = true;
        break;
      }
    }
    if (!found_finding) {
      return false;
    }
  }
  return true;
}

// Detect all the words in the given dictionary that are in word_to_analyze.
std::vector<std::string>
find_unique_words(std::vector<std::string> const &dictionary, std::string_view word_to_analyze)
{
  std::vector<std::string> unique_words;
  for (auto const &word: dictionary) {
    if (find(word, word_to_analyze)) {
      unique_words.push_back(word);
    }
  }
  return unique_words;
}

int
main(int argc, char *argv[])
{
  auto dictionary_file = DEFAULT_DICTIONARY_FILE;
  if (argc == 2) {
    dictionary_file = argv[1];
  }

#if TIMING
  auto const start = std::chrono::high_resolution_clock::now();
#endif
  auto const dictionary = parse_dictionary(dictionary_file);
  if (dictionary.empty()) {
    std::cerr << "Unable to parse dictionary file: " << dictionary_file << std::endl;
    return 1;
  }

#if TIMING
  auto const after_parse = std::chrono::high_resolution_clock::now();
#endif
  auto unique_words = find_unique_words(dictionary, WORD_TO_ANALYZE);
#if TIMING
  auto const after_find_words = std::chrono::high_resolution_clock::now();
#endif

  for (auto const &word: unique_words) {
    std::cout << word << std::endl;
  }

#if TIMING
  std::cerr << "Parsed dictionary in "
            << std::chrono::duration_cast<std::chrono::milliseconds>(after_parse - start).count()
            << "ms" << std::endl;
  std::cerr << "Found words in "
            << std::chrono::duration_cast<std::chrono::milliseconds>(after_find_words - after_parse).count()
            << "ms" << std::endl;
#endif

  return 0;
}
