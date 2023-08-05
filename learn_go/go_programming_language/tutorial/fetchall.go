package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprintf("Could not fetch from %s: %s", url, err)
		return
	}
	defer resp.Body.Close()
	numRead, err := io.Copy(io.Discard, resp.Body)
	if err != nil {
		ch <- fmt.Sprintf("Error reading from %s: %s", url, err)
		return
	}
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs %d %s", secs, numRead, url)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Must provide at least one URL to fetch.")
		os.Exit(1)
	}
	ch := make(chan string)
	start := time.Now()
	for _, url := range os.Args[1:] {
		go fetch(url, ch)
	}
	for range os.Args[1:] {
		fmt.Println(<-ch)
	}
	secs := time.Since(start).Seconds()
	fmt.Printf("%.2fs elapsed", secs)
}
