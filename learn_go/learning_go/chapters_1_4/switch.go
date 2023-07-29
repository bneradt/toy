package main

import "fmt"

func main() {
	words := []string{"a", "cow", "smile", "gopher",
		"octopus", "anthropologist"}

	for _, word := range words {
		switch size := len(word); size {
		case 2, 3, 4:
			fmt.Println(word, " is a short word")
		case 5:
			wordLen := len(word)
			fmt.Println(word, " is just right: ", wordLen, " characters")
		case 6, 7, 8, 9, 10, 11:
			fmt.Println(word, " is a long word")
		default:
			fmt.Println("What word is this? ", word)
		}
	}

	// blank switch
	for _, word := range words {
		switch size := len(word); {
		case size < 5:
			fmt.Println("small: ", word)
		case size == 5:
			fmt.Println("just right: ", word)
		case size > 5:
			fmt.Println("big: ", word)
		}
	}

	// Suggestion: favor switch statements when the comparisons are all a related
	// set of comparisons. If the comparisons are disjoint concepts, use if/else
	// chains.
}
