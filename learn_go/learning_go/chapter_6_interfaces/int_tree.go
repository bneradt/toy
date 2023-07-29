package main

import "fmt"

type IntTree struct {
	value int
	left  *IntTree
	right *IntTree
}

func (it *IntTree) Insert(value int) *IntTree {
	if it == nil {
		return &IntTree{value: value, left: nil, right: nil}
	}
	if value <= it.value {
		it.left = it.left.Insert(value)
	} else {
		it.right = it.right.Insert(value)
	}
	return it
}

func (it *IntTree) GetString() string {
	var result string
	if it == nil {
		return ""
	}
	result += it.left.GetString()
	result += fmt.Sprintf("%d, ", it.value)
	result += it.right.GetString()
	return result
}

func (it *IntTree) Contains(needle int) bool {
	if it == nil {
		return false
	}
	if it.value == needle {
		return true
	}
	if needle <= it.value {
		return it.left.Contains(needle)
	}
	return it.right.Contains(needle)
}

func main() {
	var tree *IntTree
	tree = tree.Insert(9)
	tree = tree.Insert(3)
	tree = tree.Insert(5)
	tree = tree.Insert(10)
	tree = tree.Insert(20)
	tree = tree.Insert(15)
	tree = tree.Insert(2)
	tree = tree.Insert(9)
	tree = tree.Insert(5)
	tree = tree.Insert(6)

	fmt.Println("tree: ", tree.GetString())
	fmt.Println("tree contains 9: ", tree.Contains(9))
	fmt.Println("tree contains 30: ", tree.Contains(30))
}
