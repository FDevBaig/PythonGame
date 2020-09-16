#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from pokergame import PokerHand

class TestCase(unittest.TestCase):
    def test_higher_two_pair_wins(self):
        hand = PokerHand("TC TS TH 8C 4D")
        opponent = PokerHand("9D 9S 2C JD TD")
        print (opponent.hand)
        self.assertEqual(hand.compare_with(opponent), 1)

if __name__ == '__main__':

    unittest.main()