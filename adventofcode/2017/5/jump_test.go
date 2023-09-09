package main

import "testing"

func TestCPU(t *testing.T) {
	c := CPU{}
	c.AddInstruction(0)
	c.AddInstruction(3)
	c.AddInstruction(0)
	c.AddInstruction(1)
	c.AddInstruction(-3)

	if len(c.Instructions) != 5 {
		t.Errorf("Unexpected initial Instructions size: expected %d, got %d", 5, len(c.Instructions))
	}
	if c.Offset != 0 || c.Counter != 0 || c.JumpedOut != false {
		t.Errorf("Unexpced CPU state before running instructions.")
	}

	c.FollowNextInstruction()
	if c.Offset != 0 {
		t.Errorf("Offset after the first instruction should be 0, not %d", c.Offset)
	}
	if c.Counter != 1 {
		t.Errorf("Counter after the first instruction should be 1, not %d", c.Counter)
	}
	if c.JumpedOut {
		t.Errorf("JumpedOut after the first instruction should be false.")
	}
	if c.Instructions[0] != 1 {
		t.Errorf("First jump value should have been incremented to 1.")
	}

	c.FollowNextInstruction()
	if c.Offset != 1 {
		t.Errorf("Offset after the second instruction should be 1, not %d", c.Offset)
	}
	if c.Counter != 2 {
		t.Errorf("Counter after the second instruction should be 2, not %d", c.Counter)
	}
	if c.JumpedOut {
		t.Errorf("JumpedOut after the second instruction should be false.")
	}

	c.FollowNextInstruction()
	if c.Offset != 4 {
		t.Errorf("Offset after the third instruction should be 4, not %d", c.Offset)
	}
	if c.Counter != 3 {
		t.Errorf("Counter after the third instruction should be 3, not %d", c.Counter)
	}
	if c.JumpedOut {
		t.Errorf("JumpedOut after the third instruction should be false.")
	}

	c.FollowNextInstruction()
	if c.Offset != 1 {
		t.Errorf("Offset after the fourth instruction should be 1, not %d", c.Offset)
	}
	if c.Counter != 4 {
		t.Errorf("Counter after the fourth instruction should be 4, not %d", c.Counter)
	}
	if c.JumpedOut {
		t.Errorf("JumpedOut after the fourth instruction should be false.")
	}

	c.FollowNextInstruction()
	if c.Offset != 5 {
		t.Errorf("Offset after the fifth instruction should be 5, not %d", c.Offset)
	}
	if c.Counter != 5 {
		t.Errorf("Counter after the fifth instruction should be 5, not %d", c.Counter)
	}
	if !c.JumpedOut {
		t.Errorf("JumpedOut after the fifth instruction should be true.")
	}
}
