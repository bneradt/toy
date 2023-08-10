package main

import (
	"flag"
	"fmt"
	"strings"
)

func main() {
	var n = flag.Bool("n", false, "omit the trailing newline")
	var sep = flag.String("sep", " ", "separator")
	flag.Parse()

	fmt.Print(strings.Join(flag.Args(), *sep))
	if !*n {
		fmt.Println()
	}
}
