package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

// This program relates to spirals like the following:
//
//   38 37 36 35 34 33 32
//   39 17 16 15 14 13 31
//   40 18  5  4  3 12 30
//   41 19  6  1  2 11 29
//   42 20  7  8  9 10 27
//   43 21 22 23 24 25 26
//   44 45 46 47 48 49 50

// Return the layer index that contains the given value.
//
// Each layer n contains (2n + 1)^2.
//
// layer : num
//
//	0 : 1
//	1 : 9
//	2 : 25
func CalculateNumNeededLayers(val int) int {
	var layer int
	for {
		inside := 2*layer + 1
		numValues := inside * inside
		if numValues >= val {
			return layer
		}
		layer += 1
	}
	// Not reached.
}

// Generate a two dimensional spiral with enough values in it to contain the
// given value. Return the locations of every value in the spiral as well as
// the location of the center of the spiral.
func generate(val int) (map[int][2]int, [2]int) {
	// Note that center is not counted as a layer.
	numLayers := CalculateNumNeededLayers(val)
	numPerSide := 2*numLayers + 1
	numValues := numPerSide * numPerSide
	locations := make(map[int][2]int, numValues)

	// Pre-allocate the rows and columns of the spiral.
	spiral := make([][]int, numPerSide)
	for i := range spiral {
		spiral[i] = make([]int, numPerSide)
	}
	center := [2]int{numPerSide / 2, numPerSide / 2}
	counter := 1
	spiral[center[0]][center[1]] = counter
	locations[counter] = center

	currentSquareSideSize := 1
	if val == 1 {
		return locations, center
	}
	counter += 1

	x, y := center[0], center[1]
	for currentLayer := 1; currentLayer < numLayers+1; currentLayer += 1 {
		currentSquareSideSize += 2
		x += 1
		spiral[x][y] = counter
		counter += 1
		for i := 0; i < currentSquareSideSize-2; i++ {
			y -= 1
			spiral[x][y] = counter
			locations[counter] = [2]int{x, y}
			counter += 1
		}
		for i := 0; i < currentSquareSideSize-1; i++ {
			x -= 1
			spiral[x][y] = counter
			locations[counter] = [2]int{x, y}
			counter += 1
		}
		for i := 0; i < currentSquareSideSize-1; i++ {
			y += 1
			spiral[x][y] = counter
			locations[counter] = [2]int{x, y}
			counter += 1
		}
		for i := 0; i < currentSquareSideSize-1; i++ {
			x += 1
			spiral[x][y] = counter
			locations[counter] = [2]int{x, y}
			counter += 1
		}
	}
	return locations, center
}

// Given the value, calculate its distance from the center.
func CalculateDistance(input int) int {
	locations, center := generate(input)
	location := locations[input]
	rise := int(math.Abs(float64(center[0] - location[0])))
	run := int(math.Abs(float64(center[1] - location[1])))
	return rise + run
}

func main() {
	if len(os.Args) != 2 {
		log.Fatalln("Must provide a value to calculate the distance from center.")
	}
	value, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatalf("Value is not an integer: %s\n", os.Args[1])
	}
	distance := CalculateDistance(value)
	fmt.Println(distance)
}
