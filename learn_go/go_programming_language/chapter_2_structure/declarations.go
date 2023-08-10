package main

import (
	"fmt"
	"io"
)

func main() {

	// Various types of declarations.
	var a string = "hi there"

	// Note from the following, either the type or the expression can be left off,
	// but not both.
	var b string    // zero initialized.
	var c = "candy" // "Type inference"

	d := "cane" // short hand
	fmt.Fprintf(io.Discard, "%s", []string{a, b, c, d})

	// Multiple variables
	var m, n, o = 0, 1, true
	fmt.Fprintf(io.Discard, "%d, %d, %t", m, n, o)

	// short hand with multiple variables
	i, j, k := 1, true, "candy"
	fmt.Fprintf(io.Discard, "%d, %t, %s", i, j, k)

	// swap m and n
	fmt.Printf("m, n: %d, %d\n", m, n)
	m, n = n, m
	fmt.Printf("m, n: %d, %d\n", m, n)

	var h *int = showItsSafe()
	fmt.Printf("should be 32: %d\n", *h)

	fibCount := 10
	fmt.Printf("First %d fib numbers", fibCount)
	for i := 1; i < fibCount; i++ {
		fmt.Println(fib(i))
	}
}

// Pointers can be returned from local variables
func showItsSafe() *int {
	v := 32
	return &v // go keeps extends the lifetime for this
	// Say: v "escapes" from the function.
}

// A handy use of tuple assignment.
// **All right side evaluations are done before left side.**
func fib(n int) int {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		x, y = y, x+y // Convenient!
	}
	return x
}
