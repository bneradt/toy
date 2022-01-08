import unittest
from best_path import Cave, Caves

class TestCave(unittest.TestCase):

    def test_example_paths(self):
        r"""Test the given example cave network.

            start
            /   \
        c--A-----b--d
            \   /
             end

        """
        start = Cave('start')
        A = Cave('A')
        b = Cave('b')
        c = Cave('c')
        d = Cave('d')
        end = Cave('end')

        start.add_connection(A)
        start.add_connection(b)

        A.add_connection(b)
        A.add_connection(c)
        A.add_connection(end)

        b.add_connection(d)
        b.add_connection(end)

        expected = [
            [Cave("start"), Cave("A"), Cave("b"), Cave("A"), Cave("c"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("b"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("b"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("c"), Cave("A"), Cave("b"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("c"), Cave("A"), Cave("b"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("c"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("b"), Cave("A"), Cave("c"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("b"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("b"), Cave("end")]
        ]
        self.assertEqual(expected, start.find_all_paths_to_end([start]))

class TestCaves(unittest.TestCase):

    def test_example_paths(self):
        caves = Caves()
        caves.add_connection('start-A')
        caves.add_connection('start-b')
        caves.add_connection('A-c')
        caves.add_connection('A-b')
        caves.add_connection('b-d')
        caves.add_connection('A-end')
        caves.add_connection('b-end')

        expected = [
            [Cave("start"), Cave("A"), Cave("b"), Cave("A"), Cave("c"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("b"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("b"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("c"), Cave("A"), Cave("b"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("c"), Cave("A"), Cave("b"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("c"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("b"), Cave("A"), Cave("c"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("b"), Cave("A"), Cave("end")],
            [Cave("start"), Cave("b"), Cave("end")]
        ]
        self.assertEqual(expected, caves.find_all_paths_to_end())
