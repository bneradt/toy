package main

import "fmt"

type person struct {
	firstName string
	lastName  string
	age       int
}

func modifyPerson(p person) {
	p.firstName = "Brian"
	p.lastName = "Neradt"
	p.age = 42
}

func modSlice(s []int) {
	s = append(s, 50)
}

func modMap(m map[int]string) {
	m[4] = "four"
}

func main() {
	p := person{
		firstName: "Joel",
		lastName:  "Vanderzee",
		age:       54,
	}
	modifyPerson(p)
	fmt.Println(p.firstName, " ", p.lastName, ", ", p.age)

	m := map[int]string{1: "one", 2: "two"}
	modMap(m)
	fmt.Println(m)

	var s []int = []int{1, 2, 3}
	modSlice(s)
	fmt.Println(s)
}
