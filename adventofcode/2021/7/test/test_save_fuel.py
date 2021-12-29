from save_fuel import Swarm
import unittest


class TestSwarm(unittest.TestCase):

    def test_find_least_cost_position(self):
        swarm = Swarm([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(2, swarm.find_least_cost_position())
        self.assertEqual(37, swarm.calculate_position_cost(2))

    def test_find_least_compounding_cost_position(self):
        swarm = Swarm([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(5, swarm.find_least_compounding_cost_position())
        self.assertEqual(168, swarm.calculate_compounding_position_cost(5))
