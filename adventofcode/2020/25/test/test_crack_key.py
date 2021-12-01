#!/usr/bin/env python3

import unittest
from crack_key import derive_loop_size, derive_encryption_key

class TestDeriveLoopSize(unittest.TestCase):

    def test_card_example(self):
        self.assertEqual(8, derive_loop_size(7, 5764801))

    def test_door_example(self):
        self.assertEqual(11, derive_loop_size(7, 17807724))


class TestDeriveEncryptionKey(unittest.TestCase):

    def test_door_public_key(self):
        doors_public_key = 17807724
        cards_loop_size = 8
        self.assertEqual(14897079, derive_encryption_key(
            cards_loop_size,
            doors_public_key))

    def test_card_public_key(self):
        cards_public_key = 5764801
        doors_loop_size = 11
        self.assertEqual(14897079, derive_encryption_key(
            doors_loop_size,
            cards_public_key))


if __name__ == '__name__':
    unittest.main()
