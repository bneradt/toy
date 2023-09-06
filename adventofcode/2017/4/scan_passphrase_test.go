package main

import "testing"

func TestIsValidDuplicates(t *testing.T) {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"aa bb cc dd ee", true},
		{" aa   bb  cc dd ee", true},
		{"aa bb cc dd aa", false},
		{"  aa   bb  cc  dd aa ", false},
		{"aa bb cc dd aaa", true},
	}

	for _, testCase := range testCases {
		isValid := IsValidDuplicates(testCase.input)
		if isValid != testCase.expected {
			t.Errorf("IsValidDuplicates(\"%s\"): got: %v, expected: %v\n",
				testCase.input, isValid, testCase.expected)
		}
	}
}

func TestInvalidAnagrams(t *testing.T) {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"abcde fghij", true},
		{"abcde xyz ecdab", false},
		{"a ab abc abd abf abj", true},
		{"iiii oiii ooii oooi oooo", true},
		{"oiii ioii iioi iiio", false},
	}
	for _, testCase := range testCases {
		isValid := IsValidAnagrams(testCase.input)
		if isValid != testCase.expected {
			t.Errorf("IsValidAnagrams(\"%s\"): got %v, expected %v\n",
				testCase.input, isValid, testCase.expected)
		}
	}
}
