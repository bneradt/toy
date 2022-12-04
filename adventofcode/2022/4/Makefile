FLAGS = #-DTEST -DTIMING
analyze_ranges: analyze_ranges.cc
	clang++ -std=c++20 -Wall -Werror -Wextra -O3 $(FLAGS) -g -o $@ $<
