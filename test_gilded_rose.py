#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from subprocess import check_output

from gilded_rose import Item, GildedRose



class GildedRoseTest(unittest.TestCase):
    def test_30_days_output(self):
        self.assertEqual(check_output("texttest_fixture.py"), open("stdout.gr").read())

    def test_standard_item(self):
        item = Item(name="standard item", sell_in=5, quality=7)
        GildedRose([item,]).update_quality()

if __name__ == '__main__':
    unittest.main()
