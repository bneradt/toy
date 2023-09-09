package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
)

type CPU struct {

	// The set of instructions.
	Instructions []int

	// An index to the current instruction to process next.
	Offset int

	// The number of instructions processed so far.
	Counter int

	// Whether following the instructions has resulted in the CPU jumping outside
	// of the instruction set.
	JumpedOut bool

	// Whether to use complex CPU processing.
	IsComplex bool
}

// Add an instruction to the set of instructions.
// i is the instruction to add.
func (c *CPU) AddInstruction(i int) {
	c.Instructions = append(c.Instructions, i)
}

// Starting from the current offset, follow the instruction and update any
// relevant metadata.
func (c *CPU) FollowNextInstruction() {
	if c.JumpedOut {
		return
	}
	oldOffset := c.Offset
	c.Offset += c.Instructions[c.Offset]
	c.Counter++
	if c.IsComplex {
		oldValue := c.Instructions[oldOffset]
		if oldValue >= 3 {
			c.Instructions[oldOffset]--
		} else {
			c.Instructions[oldOffset]++
		}
	} else {
		c.Instructions[oldOffset]++
	}
	if c.Offset < 0 || c.Offset > len(c.Instructions)-1 {
		c.JumpedOut = true
	}
}

func readInstructionFile(filename string) CPU {
	file, err := os.Open(filename)
	defer file.Close()
	if err != nil {
		log.Fatalf("Could not open %s: %s\n", filename, err)
	}
	scanner := bufio.NewScanner(file)
	n := 0
	cpu := CPU{}
	for scanner.Scan() {
		n++
		line := scanner.Text()
		instruction, err := strconv.Atoi(line)
		if err != nil {
			log.Fatalf("Could not parse line as an integer instructions: %s\n", line)
		}
		cpu.AddInstruction(instruction)
	}
	return cpu
}

func main() {
	complex := flag.Bool("c", false, "Use complex jump processing.")
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatalln("Must provide a filename to a set of CPU instructions.")
	}
	filename := flag.Arg(0)
	cpu := readInstructionFile(filename)
	if *complex {
		cpu.IsComplex = true
	}

	for !cpu.JumpedOut {
		cpu.FollowNextInstruction()
	}
	fmt.Println(cpu.Counter)
}
