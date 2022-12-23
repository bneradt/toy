FLAGS = #-DTEST -DTIMING
NAME = fix_rucksacks
$(NAME): $(NAME).cc
	clang++ -std=c++20 -Wall -Werror -Wextra -O3 $(FLAGS) -g -o $@ $<

.PHONY: clean
clean:
	rm -f $(NAME)
