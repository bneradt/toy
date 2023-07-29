package main

import "fmt"

type ColorT int

// Note the parens
const (
	// When there is not default, make 0 _ to indicate that uninitialized data isn't Red.
	_ ColorT = iota
	Red
	Green
	Blue
	Yellow
	Purple
)

func getString(color ColorT) string {
	switch color {
	case Red:
		return "red"
	case Green:
		return "green"
	case Blue:
		return "blue"
	case Yellow:
		return "yellow"
	case Purple:
		return "purple"
	default:
		return "not recognized"
	}
}

func main() {
	var color ColorT = Green

	fmt.Println("color: ", getString(color))
}
