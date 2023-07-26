package main

import "fmt"

func main() {

	// Complete for.
	fmt.Println("Complete for:")
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Condition-only for. Basically while.
	fmt.Println("\nCondition-only for:")
	i := 0
	for i < 5 {
		fmt.Println(i)
		i += 2
	}

	// Infinite for.
	fmt.Println("\nInfinite for:")
	j := 0
	for {
		fmt.Println("j: ", j)
		j++
		if j > 3 {
			break
		}
	}

	// for-range
	fmt.Println()
	myslice := []int{3, 4, 2, 2, 3, 9}
	for i, j := range myslice {
		fmt.Println("i: ", i, ", value: ", j)
	}

	// for-range, ignoring the key
	fmt.Println()
	mymap := map[int]string{
		1: "one",
		2: "two",
		3: "three",
	}
	for _, v := range mymap {
		fmt.Println("value: ", v)
	}

	// for over a string
	s := "hi, there"
	for _, c := range s {
		fmt.Println("c: ", string(c))
	}

	// labeled for
outer:
	for i := 0; i < 5; i++ {
		for j := 100; j < 500; j += 100 {
			sum := j + i
			if sum%100 < 3 {
				fmt.Println("outer continue, i: ", i, ", j: ", j)
				continue outer
			}
			fmt.Println("sum: ", sum)
		}
	}

}
