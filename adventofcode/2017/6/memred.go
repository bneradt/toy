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
	IsDone              bool
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

// Detect whether the given memory banks is a repeat of a set in history.
// Returns true if the given banks is a repeat, false otherwise.
func (m *Memory) IsRepeat(banks []int) bool {
	for _, historicBanks := range m.History {
		matches := true
		for i, bank := range banks {
			if bank != historicBanks[i] {
				matches = false
				break
			}
		}
		if matches {
			return true
		}
	}
	return false
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
	if m.IsRepeat(m.Banks) {
		m.IsDone = true
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
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatalln("A file containing the initial memory banks must be provided.")
	}
	filename := flag.Arg(0)
	m := ParseInput(filename)
	for !m.Redistribute() {
	}
	fmt.Println(m.RedistributionCount)
}
