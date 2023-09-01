package main

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
// given value.
func Generate(val int) [][]int {
	numLayers := CalculateNumNeededLayers(val)
	numPerSide := 2*numLayers + 1

	// Pre-allocate the rows and columns of the spiral.
	spiral := make([][]int, numPerSide)
	for i := range spiral {
		spiral[i] = make([]int, numPerSide)
	}
	center := numPerSide / 2
	counter := 1
	spiral[center][center] = counter

	currentSquareSideSize := 1
	if val == 1 {
		return spiral
	}
	counter += 1

	currentRow, currentColumn := counter, counter
	for currentLayer := 1; currentLayer < numLayers; currentLayer += 1 {
		currentSquareSideSize += 2

	}
}
