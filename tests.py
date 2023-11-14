import lib


def test_sort():
    mass = lib.bubbleSort([3, 2, 1])
    assert mass == [1, 2, 3]


def test_reverse_sort():
    assert lib.reverseBubbleSort([1, 7, 4, 8, 3, 0]) == [8, 7, 4, 3, 1, 0]
