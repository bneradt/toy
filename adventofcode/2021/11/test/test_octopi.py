#!/usr/bin/env python3

import unittest
from octopi import Octopus, OctopusPod

class TestOctopus(unittest.TestCase):

    def test_construction(self):
        o = Octopus(8)
        self.assertEqual(8, o.get_energy_level())
        self.assertEqual(0, o.get_flash_count())

    def test_neighbor(self):
        o1 = Octopus(8)
        self.assertFalse(o1.is_neighbor_with(o1))

        o2 = Octopus(8)
        self.assertFalse(o1.is_neighbor_with(o2))
        self.assertFalse(o2.is_neighbor_with(o1))

        o1.add_neighbor(o2)
        self.assertTrue(o1.is_neighbor_with(o2))
        self.assertTrue(o2.is_neighbor_with(o1))

    def test_get_shined_on(self):
        o = Octopus(8)
        o.get_shined_on()
        self.assertEqual(9, o.get_energy_level())
        self.assertEqual(0, o.get_flash_count())

        o.get_shined_on()
        self.assertEqual(10, o.get_energy_level())
        self.assertEqual(1, o.get_flash_count())

    def test_get_flash_count(self):
        o = Octopus(8)
        o.start_step()
        o.finish_step()
        self.assertEqual(0, o.get_flash_count())

        o.start_step()
        o.finish_step()
        self.assertEqual(1, o.get_flash_count())

        for i in range(12):
            o.start_step()
            o.finish_step()
        self.assertEqual(2, o.get_flash_count())

class TestOctopusPod(unittest.TestCase):

    def test_construction(self):
        p = OctopusPod()
        self.assertEqual('', str(p))
        self.assertEqual(0, p.get_historic_flash_count())

    def test_equality(self):
        p1 = OctopusPod(3)
        p1.add_octopi([4, 0, 5])
        p1.add_octopi([9, 8, 9])
        p1.add_octopi([1, 5, 3])

        p2 = OctopusPod(3)
        p2.add_octopi([3, 8, 9])
        p2.add_octopi([9, 8, 4])
        p2.add_octopi([1, 5, 3])

        p3 = OctopusPod(3)
        p3.add_octopi([3, 8, 9])
        p3.add_octopi([9, 8, 4])
        p3.add_octopi([1, 5, 3])

        self.assertNotEqual(p1, p2)
        self.assertEqual(p2, p3)

    def test_get_historic_flash_count(self):
        p = OctopusPod()
        p.add_octopi([int(i) for i in '5483143223'])
        p.add_octopi([int(i) for i in '2745854711'])
        p.add_octopi([int(i) for i in '5264556173'])
        p.add_octopi([int(i) for i in '6141336146'])
        p.add_octopi([int(i) for i in '6357385478'])
        p.add_octopi([int(i) for i in '4167524645'])
        p.add_octopi([int(i) for i in '2176841721'])
        p.add_octopi([int(i) for i in '6882881134'])
        p.add_octopi([int(i) for i in '4846848554'])
        p.add_octopi([int(i) for i in '5283751526'])

        p.step()
        self.assertEqual(0, p.get_historic_flash_count())

        for i in range(9):
            p.step()
        self.assertEqual(204, p.get_historic_flash_count())
