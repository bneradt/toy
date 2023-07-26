package main

import "fmt"

func main() {
	// Four ways to declar a slice/variable.

	// Zero initiialization
	var a []int

	// With initialization
	var b []int = []int{1, 2, 3, 4}

	// Type inference
	var c = []int{1, 2, 3, 4}

	// Short hand
	d := []int{1, 2, 3, 4}

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)

	var s string = "hi there"
	fmt.Println("s: ", s)
}
