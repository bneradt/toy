package main

import (
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

// SumMatchingDigits returns the sum of all digits that match the next digit in
// the list.
// If the last digit matches the first digit, it is included in the sum.
func SumMatchingDigits(digits []int) int {
	sum := 0
	for i, v := range digits {
		next_i := (i + 1) % len(digits)
		if v == digits[next_i] {
			sum += v
		}
	}
	return sum
}

func main() {
	if len(os.Args) != 2 {
		log.Fatalf("Usage: %s <digits>", os.Args[0])
	}
	input := os.Args[1]
	digits, err := StringToDigits(input)
	if err != nil {
		log.Fatalf("Error converting %q to digits: %v", input, err)
	}
	sum := SumMatchingDigits(digits)
	fmt.Println(sum)
}
