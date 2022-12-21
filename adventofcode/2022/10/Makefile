FLAGS = #-DTEST -DTIMING
NAME = compute
$(NAME): $(NAME).cc
	clang++ -std=c++20 -Wall -Werror -Wextra -O3 $(FLAGS) -g -o $@ $<
