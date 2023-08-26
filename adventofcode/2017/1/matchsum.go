package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
)

// StringToDigits converts a string of digits to a slice of ints.
// If the string contains non-digits, an error is returned.
// The returned slice is the same length as the input string
// and contains the digits in the same order.
func StringToDigits(s string) ([]int, error) {
	digits := make([]int, len(s))
	for i, c := range s {
		val, err := strconv.Atoi(string(c))
		if err != nil {
			return nil, err
		}
		digits[i] = val
	}
	return digits, nil
}

const USE_ACROSS = true

// SumMatchingDigits returns the sum of all digits that match the next digit in
// the list.
// use_across is a switch that says to compare this element with the one half
// way across the list. If it is false, then each element is compared with the
// next one in the list, with the last element compared to the first.
func SumMatchingDigits(digits []int, use_across bool) int {
	sum := 0
	for i, v := range digits {
		var num_ahead int
		if use_across {
			num_ahead = len(digits) / 2
		} else {
			num_ahead = 1
		}
		next_i := (i + num_ahead) % len(digits)
		if v == digits[next_i] {
			sum += v
		}
	}
	return sum
}

func main() {
	use_across := flag.Bool("across", false, "Look for the same value half across the list.")
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatalf("Usage: %s <digits>", os.Args[0])
	}
	input := flag.Arg(0)
	digits, err := StringToDigits(input)
	if err != nil {
		log.Fatalf("Error converting %q to digits: %v", input, err)
	}
	sum := SumMatchingDigits(digits, *use_across)
	fmt.Println(sum)
}
