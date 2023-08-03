package main

import (
	"fmt"
	"time"
)

func fast(pipe chan string) {
	for i := 0; i < 23; i++ {
		time.Sleep(500 * time.Millisecond)
		pipe <- "500 ms"
	}
	close(pipe)
}

func slow(pipe chan string) {
	for i := 0; i < 4; i++ {
		time.Sleep(2 * time.Second)
		pipe <- "2 seconds"
	}
	close(pipe)
}

func main() {
	ch1 := make(chan string)
	go fast(ch1)

	ch2 := make(chan string)
	go slow(ch2)

	fastIsDone := false
	slowIsDone := false
	for !fastIsDone || !slowIsDone {
		select {
		case msgFast, openFast := <-ch1:
			if fastIsDone {
				continue
			}
			if !openFast {
				fmt.Println("Fast is done.")
				fastIsDone = true
				continue
			}
			fmt.Println(msgFast)
		case msgSlow, openSlow := <-ch2:
			if slowIsDone {
				continue
			}
			if !openSlow {
				fmt.Println("Slow is done.")
				slowIsDone = true
				continue
			}
			fmt.Println(msgSlow)
		}
	}
	fmt.Println("Both fast and slow are done. slow: ", slowIsDone, ", fast: ", fastIsDone)
	fmt.Println("Result: ", !slowIsDone || !fastIsDone)
}
