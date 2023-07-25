package main

import "fmt"

func main() {
	family := map[string]int{}
	family["sons"] = 2
	family["daughters"] = 2
	family["nephews"] = 5
	family["wives"] = 1

	fmt.Println("sons: ", family["sons"])
	family["sons"]++
	fmt.Println("sons: ", family["sons"])

	num_step_sons, ok := family["step_sons"]
	fmt.Println("step_sons: ", num_step_sons, ", ok: ", ok)

	fmt.Println("nephews: ", family["nephews"])

	// Delete from a set:
	delete(family, "nephews")
	fmt.Println("nephews: ", family["nephews"])

	// Using a map as a set, set the value to bool.
	myset := map[int]bool{}
	myset[3] = true
	fmt.Println("3 is in: ", myset[3])
	fmt.Println("2 is in: ", myset[2])
}
