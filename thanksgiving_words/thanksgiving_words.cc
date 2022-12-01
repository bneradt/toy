#if TIMING
#include <chrono>
#endif
#include <iostream>
#include <memory>
#include <string>
#include <string_view>
#include <vector>

#if TEST
#include <assert.h>
#endif
#include <fcntl.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>

constexpr std::string_view DEFAULT_DICTIONARY_FILE = "en-filtered.wl";
// The word "thanksgiving", but sorted.
constexpr std::string_view WORD_TO_ANALYZE = "agghiiknnstv";

constexpr int MAX_WORD_LENGTH = 32;
using word_t = char[MAX_WORD_LENGTH];

/// Represents a list of words parsed from a file.
class WordList
{
public:
  WordList(std::string_view filename)
  {
    words = std::make_unique<word_t[]>(MAX_WORDS);

    // From https://stackoverflow.com/a/17925143/629530
    // The author says he was inspired by the code for wc.
    static const auto BUFFER_SIZE = 16 * 1024;
    int fd = ::open(filename.data(), O_RDONLY);
    if (fd == -1) {
      std::cerr << "Error opening file: " << filename << std::endl;
      exit(1);
    }

#if defined(__linux__)
    /* Advise the kernel of our access pattern.  */
    posix_fadvise(fd, 0, 0, 1); // FDADVICE_SEQUENTIAL
#endif

    char buf[BUFFER_SIZE + 1];

    std::string leftover;
    while (size_t bytes_read = ::read(fd, buf, BUFFER_SIZE)) {
      if (bytes_read == (size_t)-1) {
        std::cerr << "Error reading a line from file: " << filename << std::endl;
        exit(1);
      }
      if (!bytes_read)
        break;


      // Split the buffer into lines terminated by '\n'.
      char *line = buf;
      char *line_end = (char*)memchr(line, '\n', bytes_read);
      while (line_end) {
        if (!leftover.empty()) {
          push_back(leftover + std::string(line, line_end - line));
          leftover.clear();
        } else {
          push_back(std::string{line, static_cast<size_t>(line_end - line)});
        }
        line = line_end + 1;
        line_end = (char*)memchr(line, '\n', buf + bytes_read - line);
      }
      leftover = std::string{line, static_cast<size_t>(buf + bytes_read - line)};
    }
  }

  word_t* begin() const { return &words[0]; }
  word_t* end() const { return &words[num_words]; }
  bool is_empty() const { return num_words == 0; }
  size_t size() const { return num_words; }

private:
  void push_back(std::string_view word)
  {
    [[likely]] assert(word.size() <= MAX_WORD_LENGTH);
    auto& new_word = words[num_words++];
    [[likely]] assert(num_words <= MAX_WORDS);
    for (size_t i = 0; i < word.size(); ++i) {
      new_word[i] = word[i];
    }
    new_word[word.size()] = '\0';
  }

private:
  constexpr static int MAX_WORDS = 100'000;

  std::unique_ptr<word_t[]> words;
  unsigned int num_words = 0;
};

// Determine whether the given word is in word_to_analyze.
bool
word_is_in(std::string_view needle, std::string_view haystack)
{
  char const* used_characters[WORD_TO_ANALYZE.size()];
  size_t used_character_count = 0;
  for (char const *finding_char = needle.data(); *finding_char; ++finding_char) {
    auto start = std::lower_bound(haystack.begin(), haystack.end(), *finding_char);
    if (start == haystack.end() || *start != *finding_char) {
      return false;
    }
    // Make sure we haven't used the letter already.
    while (std::find(used_characters, used_characters + used_character_count, start) != used_characters + used_character_count) {
      ++start;
      if (start == haystack.end() || *start != *finding_char) {
        return false;
      }
    }
    used_characters[used_character_count++] = start;
  }
  return true;
}

/// Detect all the words in the given word_list that are in word_to_analyze.
std::vector<std::string>
find_words_in_thanksgiving(WordList const &word_list, std::string_view word_to_analyze)
{
  std::vector<std::string> unique_words;
  for (auto const &word: word_list) {
    if (strlen(word) == 1) {
      // Skip single-letter words.
      continue;
    }
    if (word_is_in(word, word_to_analyze)) {
      unique_words.push_back(word);
    }
  }
  return unique_words;
}

void
run_tests()
{
  assert(word_is_in("abc", "abc"));
  assert(word_is_in("abc", "abcdz"));
  assert(word_is_in("abc", "abcduz"));
  assert(word_is_in("cab", "abcduz"));
  assert(word_is_in("cab", "aabccduz"));
  assert(!word_is_in("cat", "abcduz"));

  assert(word_is_in("giving", WORD_TO_ANALYZE));
  assert(word_is_in("sat", WORD_TO_ANALYZE));
  assert(!word_is_in("never", WORD_TO_ANALYZE));
}

int
main(int argc, char *argv[])
{
  auto dictionary_file = DEFAULT_DICTIONARY_FILE;
  if (argc == 2) {
    dictionary_file = argv[1];
  }

#if TEST
  run_tests();
#endif

#if TIMING
  auto const start = std::chrono::high_resolution_clock::now();
#endif
  WordList word_list{dictionary_file};
  if (word_list.is_empty()) {
    std::cerr << "Unable to parse word list file: " << dictionary_file << std::endl;
    return 1;
  }

#if TIMING
  auto const after_parse = std::chrono::high_resolution_clock::now();
#endif
  std::cout << "Found " << word_list.size() << " words in dictionary." << std::endl;
  auto unique_words = find_words_in_thanksgiving(word_list, WORD_TO_ANALYZE);
#if TIMING
  auto const after_find_words = std::chrono::high_resolution_clock::now();
#endif

  std::cout << "Found " << unique_words.size() << " words in thanksgiving" << std::endl;
  for (auto const &word: unique_words) {
    //std::cout << word << std::endl;
    (void)word;
  }

#if TIMING
  std::cerr << "Parsed dictionary in "
            << std::chrono::duration_cast<std::chrono::microseconds>(after_parse - start).count()
            << "us" << std::endl;
  std::cerr << "Found words in "
            << std::chrono::duration_cast<std::chrono::microseconds>(after_find_words - after_parse).count()
            << "us" << std::endl;
#endif

  return 0;
}
