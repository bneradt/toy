package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Must provide an integer to add commas to.")
	}

	input := os.Args[1]
	input_len := len(input)
	if input_len <= 3 {
		fmt.Println(input)
		return
	}
	var output bytes.Buffer
	var i, s int
	for i = input_len % 3; i <= input_len; i = i + 3 {
		if s > 0 {
			output.WriteByte(',')
		}
		output.WriteString(input[s:i])
		s = i
	}
	fmt.Println(output.String())
}
