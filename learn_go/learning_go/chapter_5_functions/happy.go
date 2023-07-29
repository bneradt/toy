package main

import (
	"errors"
	"fmt"
	"os"
)

func div(numerator int, denominator int) (result int, remainder int, err error) {
	if denominator == 0 {
		return result, remainder, errors.New("Cannot divide by zero")
	}
	result, remainder = numerator/denominator, numerator%denominator
	return result, remainder, err
}

func add(first int, second int) (result int, err error) {
	var sum int = first + second
	return sum, nil
}

func sub(first int, second int) (result int, err error) {
	var sum int = first - second
	return sum, nil
}

func get_next_happy_number(n int) int {
	result := 0
	for {
		var digit int = n % 10
		result += digit * digit
		n /= 10
		if n == 0 {
			break
		}
	}
	return result
}

func get_happy_sequence(n int) []int {
	if n == 0 || n == 1 {
		return []int{n}
	}
	var next int = get_next_happy_number(n)
	var rest []int = get_happy_sequence(next)
	var sequence []int = append([]int{n}, rest...)
	return sequence
}

func addTo(base int, vals ...int) []int {
	var out []int = make([]int, 0, len(vals))
	for _, v := range vals {
		out = append(out, base+v)
	}
	return out
}

func main() {
	var n int = 7
	var sequence []int = get_happy_sequence(n)
	fmt.Println(sequence)

	result, remainder, err := div(3, 2)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println("3/2 = ", result, ", remainder: ", remainder)

	fmt.Println("huh?")
	fmt.Println(addTo(3))
	fmt.Println(addTo(3, 4))
	fmt.Println(addTo(3, 4, 5, 6, 7))
	fmt.Println(addTo(3, []int{8, 9, 10, 11}...))

	type operationType func(int, int) (int, error)
	var func_to_use operationType
	var func_description string = "+"
	switch func_description {
	case "+":
		func_to_use = add
	case "-":
		func_to_use = sub
	default:
		fmt.Println("Unrecognized function description.")
		os.Exit(1)
	}
	result, _ = func_to_use(3, 4)
	fmt.Println("3 ", func_description, " 4 = ", result)
}
