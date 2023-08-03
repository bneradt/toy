package main

import (
	"fmt"
	"sync"
	"time"
)

func count(name string) {
	for i := 0; i < 5; i++ {
		fmt.Println(name)
		time.Sleep(500 * time.Millisecond)
	}
}

func main() {
	var wg sync.WaitGroup
	wg.Add(2) // How many Dones (threads) you expect.
	go func() {
		count("sheep")
		wg.Done()
	}()
	go func() {
		count("fish")
		wg.Done()
	}()

	// Wait for the threads to finish.
	wg.Wait()

	fmt.Println("Finished the two threads")
}
