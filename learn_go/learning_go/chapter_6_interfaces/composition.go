package main

import (
	"errors"
	"fmt"
)

type Human struct {
	firstName string
	lastName  string
	spouse    *Human
	age       int
	isMale    bool
}

func (p *Human) Marry(spouse *Human) error {
	if spouse == nil {
		return errors.New("A person cannot marry no one")
	}
	if !spouse.isMale {
		spouse.lastName = p.lastName
		spouse.spouse = p
	}
	p.spouse = spouse
	return nil
}

type Employee struct {
	Human    // Embedded in Employee
	employer string
}

// Interfaces!
type Marrier interface {
	Marry(spouse *Human) error
}

func alope(m Marrier, s *Human) error {
	return m.Marry(s)
}

func main() {
	e := Employee{
		Human: Human{
			firstName: "Brian",
			lastName:  "Neradt",
			age:       42,
			spouse:    nil,
		},
		employer: "Yahoo",
	}
	hanna := Human{
		firstName: "Hanna",
		lastName:  "Joy",
		age:       45,
	}
	e.Marry(&hanna)
	fmt.Println(e.firstName, "'s wife: ", e.spouse.firstName, " ", e.spouse.lastName)

	hanna2 := Human{
		firstName: "HannaNoH",
		lastName:  "Bannanna",
		age:       45,
	}

	// Note '&' before e, because e.Marry is a pointer receiver.
	alope(&e, &hanna2)
	fmt.Println(e.firstName, "'s wife: ", e.spouse.firstName, " ", e.spouse.lastName)
}
