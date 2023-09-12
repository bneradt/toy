package main

import "testing"

func TestRedistribute(t *testing.T) {
	m := NewMemory()
	m.AddBank(0)
	m.AddBank(2)
	m.AddBank(7)
	m.AddBank(0)

	if m.RepeatIndex != -1 {
		t.Errorf("Expected RepeatIndex to be initialized to -1, but was: %d\n", m.RepeatIndex)
	}

	if m.GetLargestBank() != 2 {
		t.Errorf("The largest bank should be index 2, not %d", m.GetLargestBank())
	}
	isDone := m.Redistribute()
	if isDone {
		t.Errorf("There should not be a duplicate after the first redistribution: %v", m.Banks)
	}
	if m.IsDone {
		t.Errorf("Memory says it is done after one redistrbition, it should not be.\n")
	}
	if m.RedistributionCount != 1 {
		t.Errorf("Should have just 1 redistribution count, not %d", m.RedistributionCount)
	}
	if m.Redistribute() {
		t.Errorf("Should not have finished after 2 redistributions.\n")
	}
	if m.Redistribute() {
		t.Errorf("Should not have finished after 3 redistributions.\n")
	}
	if m.Redistribute() {
		t.Errorf("Should not have finished after 4 redistributions.\n")
	}

	// Fifth and final.
	if !m.Redistribute() {
		t.Errorf("Should have finished after 5 redistributions.\n")
	}
	if !m.IsDone {
		t.Errorf("IsDone should be true after 5 redistributions.\n")
	}
	if m.RedistributionCount != 5 {
		t.Errorf("The RedistributionCount should show 5, but instead has %d.\n",
			m.RedistributionCount)
	}
	if m.RepeatIndex != 1 {
		t.Errorf("Expected repeat index to be 1, but was: %d\n", m.RepeatIndex)
	}
	if m.GetLoopCount() != 4 {
		t.Errorf("Expected loop count to be 4, was: %d\n", m.GetLoopCount())
	}
}
