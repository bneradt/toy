package main

import (
	"bufio"
	"fmt"
	"os"
)

type lineT string
type filenameT string
type countT int

func countLines(f *os.File, counts map[lineT]countT, linesToFiles map[lineT]map[filenameT]bool) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		line := lineT(input.Text())
		counts[lineT(line)]++
		filename := filenameT(f.Name())
		if linesToFiles[line] == nil {
			linesToFiles[line] = make(map[filenameT]bool)
		}
		linesToFiles[line][filename] = true
	}
}

func main() {
	counts := make(map[lineT]countT)
	linesToFiles := make(map[lineT]map[filenameT]bool)

	if len(os.Args) == 1 {
		// Read from stdin.
		countLines(os.Stdin, counts, linesToFiles)
	} else {
		for _, filename := range os.Args[1:] {
			f, err := os.Open(filename)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Could not open %s: %s", filename, err)
			}
			countLines(f, counts, linesToFiles)
		}
	}

	for line, count := range counts {
		if count == 1 {
			continue
		}
		fmt.Printf("%d\t: %s\n", count, line)
		for filename, _ := range linesToFiles[line] {
			fmt.Printf("\t: %s\n", filename)
		}
	}
}
