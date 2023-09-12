package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Program struct {
	Name     string
	Weight   int
	Parent   *Program
	Children []*Program
}

type ProgramTree struct {
	Programs map[string]*Program
	aProgram *Program
}

func (pt *ProgramTree) GetRoot() *Program {
	if pt.aProgram == nil {
		return nil
	}
	root := pt.aProgram
	for root.Parent != nil {
		root = root.Parent
	}
	return root
}

func (pt *ProgramTree) ParseLine(line string) (*Program, error) {
	if pt.Programs == nil {
		pt.Programs = make(map[string]*Program)
	}
	fields := strings.Fields(line)
	if len(fields) < 2 {
		return nil, fmt.Errorf("a line should have at least two words: %s", line)
	}
	name := fields[0]
	var program *Program
	if p, ok := pt.Programs[name]; ok {
		program = p
	} else {
		program = &Program{Name: name}
		pt.Programs[name] = program
	}
	if pt.aProgram == nil {
		pt.aProgram = program
	}
	weightString := fields[1]
	if weightString[0] != '(' || weightString[len(weightString)-1] != ')' {
		return nil, fmt.Errorf("weight should be in parentheses: %s", weightString)
	}
	weightString = weightString[1 : len(weightString)-1]
	weight, err := strconv.Atoi(weightString)
	if err != nil {
		return nil, fmt.Errorf("weight should be an integer: %s", weightString)
	}
	program.Weight = weight
	if len(fields) == 2 {
		return program, nil
	}
	if fields[2] != "->" {
		return nil, fmt.Errorf("expected '->' but got '%s'", fields[2])
	}
	for _, childName := range fields[3:] {
		if childName[len(childName)-1] == ',' {
			childName = childName[:len(childName)-1]
		}
		var child *Program
		if p, ok := pt.Programs[childName]; ok {
			child = p
		} else {
			child = &Program{Name: childName}
			pt.Programs[childName] = child
		}
		if child == nil {
			log.Fatalf("How? %s's child %s is nil\n", program.Name, childName)
		}
		program.Children = append(program.Children, child)
		child.Parent = program
	}
	return program, nil
}

func ParseFile(filename string) (*ProgramTree, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, fmt.Errorf("could not open %s: %v", filename, err)
	}
	scanner := bufio.NewScanner(file)
	lineNumber := 0

	var pt ProgramTree
	for scanner.Scan() {
		lineNumber++
		line := scanner.Text()
		_, err := pt.ParseLine(line)
		if err != nil {
			return nil, fmt.Errorf("error parsing line %d: %v", lineNumber, err)
		}
	}
	return &pt, nil
}

func main() {
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatalf("Expected a file containing the Program tree.")
	}
	filename := flag.Arg(0)
	pt, err := ParseFile(filename)
	if err != nil {
		log.Fatalf("Error parsing file %s: %v", filename, err)
	}
	root := pt.GetRoot()
	fmt.Println(root.Name)
}
