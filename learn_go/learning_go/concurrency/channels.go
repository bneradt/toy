package main

import (
	"fmt"
	"sync"
)

func producer(pipe chan string) {
	for i := 0; i < 5; i++ {
		var userInput string
		fmt.Print("Enter a string: ")
		fmt.Scanln(&userInput)
		pipe <- userInput
	}

	// Senders (NOT RECEIVERS) can close a channel to signal to the receiver that
	// no more information is fourthcoming.
	close(pipe)
}

func reverse(input string) string {
	var output string
	length := len(input)
	for i, _ := range input {
		output = output + string(input[length-i-1])
	}
	return output
}

func consumer(pipe chan string) {
	// Receivers can take a second variable that indicates whether the channel
	// is still open.
	// userInput, open := <-pipe
	// if !open {
	// 	break
	// }

	// But, easier than that, you can range on a pipe. The range ends when the
	// channel is closed by the sender.
	for userInput := range pipe {
		reversed := reverse(userInput)
		fmt.Println(reversed)
	}
}

func main() {
	var wg sync.WaitGroup
	wg.Add(2)
	pipe := make(chan string)
	go func() {
		producer(pipe)
		wg.Done()
	}()
	go func() {
		consumer(pipe)
		wg.Done()
	}()
	wg.Wait()
	fmt.Println("All done")
}
