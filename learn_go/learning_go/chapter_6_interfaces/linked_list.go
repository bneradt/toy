package main

import (
	"fmt"
)

type LinkedList struct {
	val  int
	next *LinkedList
}

func (l *LinkedList) Append(newVal int) *LinkedList {
	if l == nil {
		return &LinkedList{val: newVal}
	}
	l.next = l.next.Append(newVal)
	return l
}

func (l *LinkedList) InsertAfter(newVal int) *LinkedList {
	if l == nil {
		return &LinkedList{val: newVal}
	}
	newNode := &LinkedList{val: newVal, next: l.next}
	l.next = newNode
	return l
}

func (l *LinkedList) Prepend(newVal int) *LinkedList {
	if l == nil {
		return &LinkedList{val: newVal}
	}
	var newNode *LinkedList = &LinkedList{
		val:  newVal,
		next: l,
	}
	return newNode
}

func (l *LinkedList) Find(needle int) *LinkedList {
	if l.val == needle {
		return l
	}
	if l == nil {
		return nil
	}
	return l.next.Find(needle)
}

func (l *LinkedList) ToString() string {
	if l == nil {
		return ""
	}
	return fmt.Sprintf("%d %s", l.val, l.next.ToString())
}

func main() {
	l := &LinkedList{val: 1}
	l = l.Append(2)
	l = l.Append(3)
	l = l.Append(4)
	l = l.Prepend(0)
	l = l.Prepend(-1)

	n := l.Find(3)
	n = n.InsertAfter(103)
	fmt.Println(l.ToString())
}
