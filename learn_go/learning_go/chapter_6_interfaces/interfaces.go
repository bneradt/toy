package main

import "fmt"

// types aren't just for structs. They can name variables, like using declarations.
type Age int

type Person struct {
	firstName string
	lastName  string
	age       Age
}

// Method receives.

// Take Person by copy, non-mutable. "Value receiver".
func (p Person) String() string {
	return fmt.Sprintf("%s %s, age %d", p.firstName, p.lastName, p.age)
}

// Take Person by pointer, mutable. "Pointer receiver".
//
// It's idiomatic to make all method receivers either value or pointer receives.
func (p *Person) StringPointer() string {
	return fmt.Sprintf("%s %s, age %d", p.firstName, p.lastName, p.age)
}

// Although, keep in mind, it is idiomatic in go to access fields directly from
// a type.
func (p *Person) advanceAge() Age {
	p.age++
	return p.age
}

func main() {

	var p Person = Person{
		firstName: "Brian",
		lastName:  "Neradt",
		age:       42,
	}

	fmt.Println("in main p: ", p.String())
	fmt.Println("in main p: ", p.StringPointer())

	var new_age Age = p.advanceAge()
	fmt.Println("in main p: ", p.StringPointer(), "/", new_age)
}
