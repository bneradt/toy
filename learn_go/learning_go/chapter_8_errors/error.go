package main

import (
	"fmt"
)

// Errors can be returned via errors.New or fmt.Errorf
func doubleEven(even int) (int, error) {
	if even%2 != 0 {
		return 0, fmt.Errorf("%d is not even", even)
	}
	return even * 2, nil
}

// Panics can be captured in defer blocks using recover.
func div60(denonimator int) {
	defer func() {
		if v := recover(); v != nil {
			// a panic happened.
			fmt.Println("Handled a panic: ", v)
		}
	}()
	fmt.Println(60 / denonimator)
}

func main() {
	d, e := doubleEven(5)
	if e != nil {
		fmt.Println("Whoops")
	} else {
		fmt.Println("5 * 2: ", d)
	}

	for _, val := range []int{120, 30, 0, 6} {
		div60(val)
	}
}
