package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	age       int
}

func (p Person) String() string {
	return fmt.Sprintf("%s %s, age %d", p.firstName, p.lastName, p.age)
}

func take_copy(p Person) {
	p.firstName = "David"
	fmt.Println("in copy p: ", p.String())
}

// Taking a pointer in go acts in the body like it was taken by reference. Any
// uses of a nil pointer will result in a panic like it would in C++ for a
// nullptr reference.
func take_pointer(p *Person) {
	if p == nil {
		fmt.Println("Got nil person")
		return
	}
	p.firstName = "Hanna"
	fmt.Println("in pointer p: ", p.String())
}

func main() {

	var p Person = Person{
		firstName: "Brian",
		lastName:  "Neradt",
		age:       42,
	}

	take_copy(p)
	fmt.Println("in main p: ", p.String())

	take_pointer(&p)
	fmt.Println("in main p: ", p.String())

	// The zero value for a pointer type is nil.
	var n *Person
	take_pointer(n)
}
