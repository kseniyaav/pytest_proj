from utils import arrs


def test_get():
    # Test with valid index
    assert arrs.get([1, 2, 3], 1, "test") == 2

    # Test with invalid index
    assert arrs.get([1, 2, 3], 3, "test") == "test"

    # Test with empty list
    assert arrs.get([], 0, "test") == "test"




def test_slice():
    # Test with start and end specified
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]

    # Test with only start specified
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

    # Test with only end specified
    assert arrs.my_slice([1, 2, 3, 4], end=2) == [1, 2]

    # Test with negative start and end values
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]

    # Test with end value greater than length of list
    assert arrs.my_slice([1, 2, 3, 4], 11) == []

    # Test with empty list
    assert arrs.my_slice([], 1) == []
