#include <cstdint>
#include <fstream>
#include <iostream>
#include <string_view>
#include <vector>

class Tree {
public:

    Tree(uint32_t height) : height_(height) {}

    // Delete all other constructors and assignment operators.
    Tree(const Tree&) = delete;
    Tree(Tree&&) = default;
    Tree& operator=(const Tree&) = delete;
    Tree& operator=(Tree&&) = default;


    uint32_t get_height() const {
        return height_;
    }
    bool is_visible() const {
        if (tree_to_north_ == nullptr ||
                tree_to_east_ == nullptr ||
                tree_to_south_ == nullptr ||
                tree_to_west_ == nullptr) {
            return true;
        }
        bool is_blocked = false;
        for (auto *tree = tree_to_north_; tree != nullptr; tree = tree->tree_to_north_) {
            if (tree->height_ >= height_) {
                is_blocked = true;
                break;
            }
        }
        if (!is_blocked) {
            return true;
        }

        is_blocked = false;
        for (auto *tree = tree_to_south_; tree != nullptr; tree = tree->tree_to_south_) {
            if (tree->height_ >= height_) {
                is_blocked = true;
                break;
            }
        }
        if (!is_blocked) {
            return true;
        }

        is_blocked = false;
        for (auto *tree = tree_to_west_; tree != nullptr; tree = tree->tree_to_west_) {
            if (tree->height_ >= height_) {
                is_blocked = true;
                break;
            }
        }
        if (!is_blocked) {
            return true;
        }

        is_blocked = false;
        for (auto *tree = tree_to_east_; tree != nullptr; tree = tree->tree_to_east_) {
            if (tree->height_ >= height_) {
                is_blocked = true;
                break;
            }
        }
        if (!is_blocked) {
            return true;
        }
        return false;
    }

    void set_tree_to_north(Tree const *tree) {
        tree_to_north_ = tree;
    }

    void set_tree_to_south(Tree const *tree) {
        tree_to_south_ = tree;
    }

    void set_tree_to_west(Tree const *tree) {
        tree_to_west_ = tree;
    }

    void set_tree_to_east(Tree const *tree) {
        tree_to_east_ = tree;
    }

private:
    uint32_t height_ = 0;

    Tree const *tree_to_north_ = nullptr;
    Tree const *tree_to_south_ = nullptr;
    Tree const *tree_to_west_ = nullptr;
    Tree const *tree_to_east_ = nullptr;
};

class Forest {
public:
    Forest()
    {
      forest_.reserve(1000);
      forest_.reserve(1000);
    }

    void start_new_column() {
        auto &new_column = forest_.emplace_back();
        new_column.reserve(1000);
    }

    void add_tree(uint32_t height) {
        if (forest_.empty()) {
            forest_.emplace_back();
        }
        auto &current_tree = forest_.back().emplace_back(height);

        auto const current_row = forest_.size() - 1;
        auto const current_column = forest_.back().size() - 1;

        if (current_row > 0) {
            auto &tree_to_north = forest_.at(current_row - 1).at(current_column);
            current_tree.set_tree_to_north(&tree_to_north);
            tree_to_north.set_tree_to_south(&current_tree);
        }
        if (current_column > 0) {
            auto &tree_to_west = forest_.at(current_row).at(current_column - 1);
            current_tree.set_tree_to_west(&tree_to_west);
            tree_to_west.set_tree_to_east(&current_tree);
        }
    }

    size_t count_visible_trees() const {
        size_t count = 0;
        for (auto const &row : forest_) {
            for (auto const &tree : row) {
                if (tree.is_visible())
                    ++count;
            }
        }
        return count;
    }

    void print_forest() const {
        for (auto const &row : forest_) {
            for (auto const &tree : row) {
                auto const height = tree.get_height();
                std::cout << height << "," << std::boolalpha << tree.is_visible() << " ";
            }
            std::cout << std::endl;
        }
    }

private:
    using Row_t = std::vector<Tree>;
    using Forest_t = std::vector<Row_t>;
    Forest_t forest_;
};

Forest
parse_input_file(std::string_view input_file)
{
    Forest forest;
    std::ifstream input(input_file.data());
    if (!input) {
        std::cerr << "Error: could not open input file " << input_file << std::endl;
        return forest;
    }
    std::string line;
    while (std::getline(input, line)) {
        forest.start_new_column();
        for (auto &c : line) {
            auto const height = c - '0';
            if (height < 0 || height > 9) {
                std::cerr << "Error: invalid height " << height << std::endl;
                return forest;
            }
            forest.add_tree(height);
        }
    }
    return forest;
}

int
main(int argc, char *argv[])
{
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
        return 1;
    }

    auto const forest = parse_input_file(argv[1]);
    forest.print_forest();
    std::cout << "Number of visible trees:\n" << forest.count_visible_trees() << std::endl;
    return 0;
}
