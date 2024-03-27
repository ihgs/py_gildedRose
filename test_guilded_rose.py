# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose



def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo"==items[0].name

def test_Sulfuras():
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 80==items[0].quality
    gilded_rose.update_quality()
    assert 80==items[0].quality

def test_AgedBrie():
    items = [Item("Aged Brie", 2, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 3==items[0].quality
    gilded_rose.update_quality()
    assert 4==items[0].quality