#!/usr/bin/env python
# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES_TAFKAL80ETC_CONCERT = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS_HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"


def adjust_min_max_quality(item):
    if item.quality > 50:
        item.quality = 50
    if item.quality < 0:
        item.quality = 0


def update_quality_aged_brie(item):
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.quality = item.quality + 2
    else:
        item.quality = item.quality + 1

    adjust_min_max_quality(item)


def update_quality_backstage_passes_TAFKAL80ETC_concert(item):
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.quality = 0
    elif item.sell_in < 5:
        item.quality = item.quality + 3
    elif item.sell_in < 10:
        item.quality = item.quality + 2
    else:
        item.quality = item.quality + 1

    adjust_min_max_quality(item)


def update_quality_sulfuras_hand_of_ragnaros(item):
    item.quality = 80


def update_quality_standard_item(item):
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.quality = item.quality - 2
    else:
        item.quality = item.quality - 1

    adjust_min_max_quality(item)


class GildedRose(object):
    QUALITY_FUNCTION = {
        AGED_BRIE: update_quality_aged_brie,
        BACKSTAGE_PASSES_TAFKAL80ETC_CONCERT: update_quality_backstage_passes_TAFKAL80ETC_concert,
        SULFURAS_HAND_OF_RAGNAROS: update_quality_sulfuras_hand_of_ragnaros
    }

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            try:
                self.QUALITY_FUNCTION[item.name](item)
            except KeyError:
                update_quality_standard_item(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
