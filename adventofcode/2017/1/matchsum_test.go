package main

import (
	"testing"
)

func TestStringToDigits(t *testing.T) {
	testCases := []struct {
		input         string
		expected      []int
		expectedError bool
	}{
		{"121212", []int{1, 2, 1, 2, 1, 2}, false},
		{"", []int{}, false},
		{"1", []int{1}, false},
		{"a", nil, true},
	}
	for _, tc := range testCases {
		actual, actualErr := StringToDigits(tc.input)
		if tc.expectedError && actualErr == nil {
			t.Errorf("StringToDigits(%q) expected an error, got none", tc.input)
		}
		if len(actual) != len(tc.expected) {
			t.Errorf("StringToDigits(%q) expected %v, got %v", tc.input, tc.expected, actual)
		}
		for i, v := range actual {
			if v != tc.expected[i] {
				t.Errorf("StringToDigits(%q) expected %v, got %v", tc.input, tc.expected, actual)
			}
		}
	}
}

func TestSumMatchingDigits(t *testing.T) {
	testCases := []struct {
		input       []int
		expectedSum int
	}{
		{[]int{1, 1, 1, 1}, 4},
		{[]int{1, 1, 2, 2}, 3},
		{[]int{1, 2, 3, 4}, 0},
		{[]int{9, 1, 2, 1, 2, 1, 2, 9}, 9},
	}

	for _, tc := range testCases {
		actual := SumMatchingDigits(tc.input, !USE_ACROSS)
		if actual != tc.expectedSum {
			t.Errorf("SumMatchingDigits(%v, !USE_ACROSS) expected %d, got %d", tc.input, tc.expectedSum, actual)
		}
	}
}

func TestSumMatchingDigitsUseAcross(t *testing.T) {
	testCases := []struct {
		input       []int
		expectedSum int
	}{
		{[]int{1, 2, 1, 2}, 6},
		{[]int{1, 2, 2, 1}, 0},
		{[]int{1, 2, 3, 4, 2, 5}, 4},
		{[]int{1, 2, 3, 1, 2, 3}, 12},
		{[]int{1, 2, 1, 3, 1, 4, 1, 5}, 4},
	}

	for _, tc := range testCases {
		actual := SumMatchingDigits(tc.input, USE_ACROSS)
		if actual != tc.expectedSum {
			t.Errorf("SumMatchingDigits(%v, USE_ACROSS) expected %d, got %d", tc.input, tc.expectedSum, actual)
		}
	}
}
