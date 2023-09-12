package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
)

type Memory struct {
	Banks               []int
	History             [][]int
	RedistributionCount int
	RepeatIndex         int
	IsDone              bool
}

func NewMemory() *Memory {
	return &Memory{RepeatIndex: -1}
}

// Return the memory bank with the most blocks.
func (m *Memory) GetLargestBank() int {
	largestIndex := 0
	for i, bank := range m.Banks {
		if bank > m.Banks[largestIndex] {
			largestIndex = i
		}
	}
	return largestIndex
}

func (m *Memory) AddBank(bankSize int) {
	m.Banks = append(m.Banks, bankSize)
}

// Detect the index wherein there is a repeat with the banks input.
// Returns -1 if there is no repeat, the index in the history to the repeat if
// it exists.
func (m *Memory) GetRepeatIndex(banks []int) int {
	for h, historicBanks := range m.History {
		matches := true
		for i, bank := range banks {
			if bank != historicBanks[i] {
				matches = false
				break
			}
		}
		if matches {
			return h
		}
	}
	return -1
}

// Set the RepeatIndex to the give value.
func (m *Memory) SetRepeatIndex(i int) {
	m.IsDone = true
	m.RepeatIndex = i
}

func (m *Memory) GetLoopCount() int {
	if !m.IsDone {
		return 0
	}
	return m.RedistributionCount - m.RepeatIndex
}

// Redistribute the memory.
// Returns true if this redistribution resulted in a duplicate memory pattern,
// false otherwise.
func (m *Memory) Redistribute() bool {
	if len(m.History) == 0 {
		m.History = append(m.History, slices.Clone(m.Banks))
	}
	if m.IsDone {
		return true
	}
	largestIndex := m.GetLargestBank()
	numBlocks := m.Banks[largestIndex]
	m.Banks[largestIndex] = 0
	startingBank := (largestIndex + 1) % len(m.Banks)
	m.RedistributionCount++
	for i, j := 0, startingBank; i < numBlocks; i, j = i+1, (j+1)%len(m.Banks) {
		m.Banks[j]++
	}
	repeatIndex := m.GetRepeatIndex(m.Banks)
	if repeatIndex != -1 {
		m.SetRepeatIndex(repeatIndex)
	} else {
		m.History = append(m.History, slices.Clone(m.Banks))
	}
	return m.IsDone
}

// Parse the given input file to create an initialized Memory object.
func ParseInput(filename string) Memory {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("Could not open %s: %s\n", filename, err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)
	memory := Memory{}
	memory.Banks = []int{}
	for scanner.Scan() {
		bankSizeInput := scanner.Text()
		bankSize, err := strconv.Atoi(bankSizeInput)
		if err != nil {
			log.Fatalf("Bank size input is not an integer value: %s\n", bankSizeInput)
		}
		memory.AddBank(bankSize)
	}
	return memory
}

func main() {
	countLoopSize := flag.Bool("l", false, "Count the loop size rather than redistribution size.")
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatalln("A file containing the initial memory banks must be provided.")
	}
	filename := flag.Arg(0)
	m := ParseInput(filename)
	for !m.Redistribute() {
	}
	if *countLoopSize {
		fmt.Println(m.GetLoopCount())
	} else {
		fmt.Println(m.RedistributionCount)
	}
}
