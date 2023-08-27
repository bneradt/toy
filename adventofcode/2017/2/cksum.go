package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"unicode"
)

// Parse
func ParseLine(l string) (int, int) {
	min := -1
	max := -1
	for _, c := range l {
		if unicode.IsSpace(c) {
			continue
		}
		digit := int(c - '0')
		if min == -1 {
			min, max = digit, digit
			continue
		}
		if digit < min {
			min = digit
		} else if digit > max {
			max = digit
		}
	}
	return min, max
}

func CalculateCksum(min, max int) int {
	return max - min
}

func main() {
	if len(os.Args) != 2 {
		log.Fatalf("Usage: %s <input_filename>", os.Args[0])
	}
	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("Could not open %s: %s", filename, err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var cksum int
	for scanner.Scan() {
		line := scanner.Text()
		min, max := ParseLine(line)
		cksum += CalculateCksum(min, max)
	}
	fmt.Println(cksum)
}
