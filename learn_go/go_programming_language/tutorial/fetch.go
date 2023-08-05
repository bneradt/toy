package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

func main() {
	for _, url := range os.Args[1:] {
		const prefix string = "http://"
		if !strings.HasPrefix(url, prefix) {
			url = prefix + url
		}
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error fetching from %s: %s", url, err)
			os.Exit(1)
		}
		defer resp.Body.Close()
		fmt.Printf("Received a response of status %d:\n", resp.StatusCode)
		_, err = io.Copy(os.Stdout, resp.Body)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading body for %s: %s", url, err)
			os.Exit(1)
		}
	}
}
