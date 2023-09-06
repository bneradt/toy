package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"slices"
	"strings"
)

func IsValidDuplicates(p string) bool {
	words := strings.FieldsFunc(p, func(r rune) bool {
		return r == ' '
	})
	wordSet := make(map[string]bool, len(words))
	for _, word := range words {
		if _, ok := wordSet[word]; ok {
			return false
		}
		wordSet[word] = true
	}
	return true
}

func IsValidAnagrams(p string) bool {
	words := strings.FieldsFunc(p, func(r rune) bool {
		return r == ' '
	})
	wordSet := make(map[string]bool, len(words))
	for _, word := range words {
		letters := strings.Split(word, "")
		slices.Sort(letters)

		key := strings.Join(letters, "")
		if _, ok := wordSet[key]; ok {
			return false
		}
		wordSet[key] = true
	}
	return true
}

func main() {
	testAnagrams := flag.Bool("s", false, "Stricly enforce passphrases: no anagrams.")
	flag.Parse()

	if flag.NArg() != 1 {
		log.Fatalln("An file with a set of passphrases, one per line, is required as input.")
	}

	filename := flag.Arg(0)
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("Could not open %s: %s", filename, err)
	}

	var isValid func(string) bool
	if *testAnagrams {
		isValid = IsValidAnagrams
	} else {
		isValid = IsValidDuplicates
	}

	scanner := bufio.NewScanner(file)
	numValid := 0
	for scanner.Scan() {
		line := scanner.Text()
		if isValid(line) {
			numValid += 1
		}
	}

	fmt.Println(numValid)
}
