package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "At least one filename must be provided.")
		os.Exit(1)
	}

	counts := make(map[string]int)
	for _, filename := range os.Args[1:] {
		f, err := os.Open(filename)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Could not open: %s", filename)
			os.Exit(1)
		}
		content, err := io.ReadAll(f)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Could not read: %s", filename)
			os.Exit(1)
		}
		lines := strings.Split(string(content), "\n")
		for _, line := range lines {
			counts[line]++
		}
	}

	for line, count := range counts {
		if count == 1 {
			continue
		}
		fmt.Printf("%d: %s\n", count, line)
	}
}
