package main

import "fmt"

func main() {
	type person struct {
		first_name string
		last_name  string
		age        int
	}

	var carl person
	fmt.Println("first name: ", carl.first_name)
	carl.first_name = "carl"
	fmt.Println("first name: ", carl.first_name)

	fred := person{"fred", "neradt", 23}
	fmt.Println("first name: ", fred.first_name)
}
