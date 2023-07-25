package main

import (
	"fmt"
	"math/rand"
)

func main() {

	// Note the special if scope of n because it's declared in the if.
	if n := rand.Intn(10); n == 0 {
		fmt.Println("That's too low: ", n)
	} else if n > 5 {
		fmt.Println("That's too high: ", n)
	} else {
		fmt.Println("That's just right: ", n)
	}
}
