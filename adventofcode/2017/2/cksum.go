package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

// Parse
func ParseLine(l string) (int, int) {
	min := -1
	max := -1
	numbers := strings.Fields(l)
	for _, numberString := range numbers {
		number, err := strconv.Atoi(numberString)
		if err != nil {
			log.Fatalf("Received a non-integer number in %s: %s", l, numberString)
		}
		if min == -1 {
			min, max = number, number
			continue
		}
		if number < min {
			min = number
		} else if number > max {
			max = number
		}
	}
	return min, max
}

func ParseLineDivisible(l string) (int, int) {
	numberStrings := strings.Fields(l)
	numbers := make([]int, 0, len(numberStrings))
	for _, numberString := range numberStrings {
		number, err := strconv.Atoi(numberString)
		if err != nil {
			log.Fatalf("Received a non-integer number in %s: %s", l, numberString)
		}
		numbers = append(numbers, number)
	}
	for i := 0; i < len(numbers); i++ {
		for j := 0; j < len(numbers); j++ {
			if i == j {
				continue
			}
			num, den := numbers[j], numbers[i]
			if num%den == 0 {
				return num, den
			}
		}
	}
	log.Fatalf("Could not find divisible numbers: %s", l)
	return -1, -1
}

func CalculateCksum(min, max int) int {
	return max - min
}

func CalculateCksumDivisible(num, den int) int {
	if den == 0 {
		log.Fatalf("Got a 0 denominator: %d/%d", num, den)
	}
	return num / den
}

func main() {
	useDevisible := flag.Bool("divisible", false, "Use divisible cksums.")
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatalf("Usage: %s [-divisible] <input_filename>", os.Args[0])
	}
	filename := flag.Arg(0)
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("Could not open %s: %s", filename, err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var cksum int
	for scanner.Scan() {
		line := scanner.Text()
		if *useDevisible {
			num, div := ParseLineDivisible(line)
			cksum += CalculateCksumDivisible(num, div)
		} else {
			min, max := ParseLine(line)
			cksum += CalculateCksum(min, max)
		}
	}
	fmt.Println(cksum)
}
