package main

import "testing"

func TestCalculateNumNeededLayers(t *testing.T) {
	testCases := []struct {
		input             int
		expectedNumLayers int
	}{
		{1, 0},
		{2, 1},
		{3, 1},
		{4, 1},
		{8, 1},
		{9, 1},
		{10, 2},
		{25, 2},
		{26, 3},
	}

	for _, testCase := range testCases {
		numLayers := CalculateNumNeededLayers(testCase.input)
		if numLayers != testCase.expectedNumLayers {
			t.Errorf("CalculateNumNeededLayers(%d): got %d, expected %d", testCase.input, numLayers, testCase.expectedNumLayers)
		}
	}
}

func TestCalculateDistance(t *testing.T) {
	testCases := []struct {
		input            int
		expectedDistance int
	}{
		{1, 0},
		{6, 1},
		{17, 4},
		{12, 3},
		{19, 2},
		{21, 4},
		{25, 4},
		{24, 3},
	}

	for _, testCase := range testCases {
		distance := CalculateDistance(testCase.input)
		if distance != testCase.expectedDistance {
			t.Errorf("CalculateDistance(%d): got %d, expected %d", testCase.input, distance, testCase.expectedDistance)
		}
	}
}
