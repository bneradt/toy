package main

import (
	"fmt"
	"os"
	"strconv"
)

func findGCD(x, y int) int {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Two integers must be provided.")
		os.Exit(1)
	}

	x, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Printf("First parameter is not an integer: %d", os.Args[1])
		os.Exit(1)
	}
	y, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Printf("Second parameter is not an integer: %d", os.Args[2])
		os.Exit(1)
	}

	gcd := findGCD(x, y)
	fmt.Println(gcd)
}
