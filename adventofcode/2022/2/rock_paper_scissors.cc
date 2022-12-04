#include <fstream>
#include <iostream>
#include <string_view>
#include <vector>

class Round {
public:
  Round(std::string_view description)
  {
    if (description.find(" ") == std::string_view::npos) {
      throw std::invalid_argument("Invalid description: no space");
    }
    auto space_pos = description.find(" ");
    auto their_string = description.substr(0, space_pos);
    auto my_input = description.substr(space_pos + 1);

    theirs_ = parse_option(their_string);
    mine_ = parse_option(my_input);
  }

  void adjust()
  {
    Result result{Result::Draw};
    // First, determine the desired outcome.
    switch (mine_) {
    case Option::Rock:
      result = Result::Lose;
      break;
    case Option::Paper:
      result = Result::Draw;
      break;
    case Option::Scissors:
      result = Result::Win;
      break;
    }

    // Now adjust the choice accordingly.
    if (result == Result::Win) {
      if (theirs_ == Option::Rock) {
        mine_ = Option::Paper;
      } else if (theirs_ == Option::Paper) {
        mine_ = Option::Scissors;
      } else if (theirs_ == Option::Scissors) {
        mine_ = Option::Rock;
      }
    } else if (result == Result::Lose) {
      if (theirs_ == Option::Rock) {
        mine_ = Option::Scissors;
      } else if (theirs_ == Option::Paper) {
        mine_ = Option::Rock;
      } else if (theirs_ == Option::Scissors) {
        mine_ = Option::Paper;
      }
    } else if (result == Result::Draw) {
      mine_ = theirs_;
    }
  }

  uint32_t get_score() const
  {
    uint32_t score = 0;
    score += get_score_from_my_choice(mine_);
    score += get_score_from_outcome(theirs_, mine_);

    // Compute the outcome value.

    return score;
  }

private:
    enum class Option {
      Rock,
      Paper,
      Scissors,
    };

    enum class Result {
      Win,
      Lose,
      Draw,
    };

    static Option parse_option(std::string_view option)
    {
      if (option == "A" || option == "X") {
        return Option::Rock;
      } else if (option == "B" || option == "Y") {
        return Option::Paper;
      } else if (option == "C" || option == "Z") {
        return Option::Scissors;
      } else {
        throw std::invalid_argument("Invalid option");
      }
    }

    static uint32_t get_score_from_my_choice(Option my_choice)
    {
      switch (my_choice) {
        case Option::Rock:
          return 1;
          break;
        case Option::Paper:
          return 2;
          break;
        case Option::Scissors:
          return 3;
          break;
      }
    }

    static constexpr uint32_t LOSE_SCORE = 0;
    static constexpr uint32_t DRAW_SCORE = 3;
    static constexpr uint32_t WIN_SCORE = 6;

    static uint32_t get_score_from_outcome(Option their_choice, Option my_choice)
    {
      if (my_choice == their_choice) {
        return DRAW_SCORE;
      } else {
        if (their_choice == Option::Rock) {
          if (my_choice == Option::Paper) {
            return WIN_SCORE;
          } else {
            return LOSE_SCORE;
          }
        } else if (their_choice == Option::Paper) {
          if (my_choice == Option::Scissors) {
            return WIN_SCORE;
          } else {
            return LOSE_SCORE;
          }
        } else if (their_choice == Option::Scissors) {
          if (my_choice == Option::Rock) {
            return WIN_SCORE;
          } else {
            return LOSE_SCORE;
          }
        }
      }
      // Should never get here.
      return 0;
    }

private:
    Option theirs_;
    Option mine_;
};

class StrategyGuide {
public:
  StrategyGuide(std::string_view filename)
  {
    std::ifstream input(filename.data());
    if (!input) {
      throw std::invalid_argument(std::string("Invalid file: ") + std::string(filename));
    }

    std::string line;
    while (std::getline(input, line)) {
      if (line.empty()) {
        continue;
      }
      rounds_.emplace_back(line);
    }
  }

  void adjust()
  {
    for (auto& round : rounds_) {
      round.adjust();
    }
  }

  uint32_t get_score() const
  {
    uint32_t score = 0;
    for (const auto& round : rounds_) {
      score += round.get_score();
    }
    return score;
  }

private:
  std::vector<Round> rounds_;
};



int main(int argc, char* argv[])
{
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
    return 1;
  }

  StrategyGuide guide(argv[1]);
  std::cout << "Original: " << guide.get_score() << std::endl;
  guide.adjust();
  std::cout << "Adjusted: " << guide.get_score() << std::endl;

  return 0;
}
