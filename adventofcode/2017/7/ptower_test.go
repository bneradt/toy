package main

import "testing"

func TestProgramTree(t *testing.T) {
	var pt ProgramTree
	pt.ParseLine("pbga (66)")
	pt.ParseLine("xhth (57)")
	pt.ParseLine("ebii (61)")
	pt.ParseLine("havc (66)")
	pt.ParseLine("ktlj (57)")
	pt.ParseLine("fwft (72) -> ktlj, cntj, xhth")
	pt.ParseLine("qoyq (66)")
	pt.ParseLine("padx (45) -> pbga, havc, qoyq")
	pt.ParseLine("tknk (41) -> ugml, padx, fwft")
	pt.ParseLine("jptl (61)")
	pt.ParseLine("ugml (68) -> gyxo, ebii, jptl")
	pt.ParseLine("gyxo (61)")
	pt.ParseLine("cntj (57)")

	root := pt.GetRoot()
	if root == nil {
		t.Errorf("root should not be nil")
		return
	}
	if root.Name != "tknk" {
		t.Errorf("root should be tknk, not %s", root.Name)
	}
}
