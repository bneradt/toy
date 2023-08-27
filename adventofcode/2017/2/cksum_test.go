package main

import "testing"

func TestParseLine(t *testing.T) {
	testCases := []struct {
		input       string
		expectedMin int
		expectedMax int
	}{
		{"5 1 9 5", 1, 9},
		{"7 5 3", 3, 7},
		{"2 4 6 8", 2, 8},
		{"104 240 147", 104, 240},
	}

	for _, tc := range testCases {
		min, max := ParseLine(tc.input)
		if min != tc.expectedMin {
			t.Errorf("ParseLine(%s): expected min: %d, got %d", tc.input, tc.expectedMin, min)
		}
		if max != tc.expectedMax {
			t.Errorf("ParseLine(%s): expected max: %d, got %d", tc.input, tc.expectedMax, max)
		}
	}
}

func TestCalculateCksum(t *testing.T) {
	cksum := CalculateCksum(2, 9)
	if cksum != 7 {
		t.Errorf("CalculateCksum(9, 2): expected: 7, got %d", cksum)
	}
}
