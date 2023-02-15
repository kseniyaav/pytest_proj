import unittest
from utils.arrs import get, my_slice

class TestGet(unittest.TestCase):
    def test_get_existing_index(self):
        array = [1, 2, 3]
        index = 2
        self.assertEqual(get(array, index), 3)

    def test_get_nonexisting_index(self):
        array = [1, 2, 3]
        index = 3
        default = "default"
        self.assertEqual(get(array, index, default), default)

    def test_get_negative_index(self):
        array = [1, 2, 3]
        index = -1
        default = "default"
        self.assertEqual(get(array, index, default), default)

    def test_get_empty_array(self):
        array = []
        index = 0
        default = "default"
        self.assertEqual(get(array, index, default), default)

class TestMySlice(unittest.TestCase):
    def test_my_slice_full_list(self):
        array = [1, 2, 3, 4]
        start = 0
        end = None
        self.assertEqual(my_slice(array, start, end), [1, 2, 3, 4])

    def test_my_slice_with_start_and_end(self):
        array = [1, 2, 3, 4]
        start = 1
        end = 3
        self.assertEqual(my_slice(array, start, end), [2, 3])

    def test_my_slice_negative_indices(self):
        array = [1, 2, 3, 4]
        start = -2
        end = -1
        self.assertEqual(my_slice(array, start, end), [3])

    def test_my_slice_empty_array(self):
        array = []
        start = 0
        end = None
        self.assertEqual(my_slice(array, start, end), [])

    def test_my_slice_start_greater_than_end(self):
        array = [1, 2, 3, 4]
        start = 3
        end = 1
        self.assertEqual(my_slice(array, start, end), [])

    def test_my_slice_normalized_start(self):
        array = [1, 2, 3, 4, 5]
        start = -3
        end = 3
        expected_result = [3, 4]
        assert my_slice(array, start, end) == expected_result

    def test_my_slice_normalized_end(self):
        array = [1, 2, 3, 4, 5]
        start = 2
        end = -1
        expected_result = [3, 4]
        self.assertEqual(my_slice(array, start, end), expected_result)

    def test_my_slice_normalized_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        start = -3
        end = -1
        expected_result = [3, 4]
        self.assertEqual(my_slice(array, start, end), expected_result)

    def test_my_slice_start_out_of_range(self):
        array = [1, 2, 3, 4]
        start = 5
        end = None
        self.assertEqual(my_slice(array, start, end), [])

    def test_my_slice_end_out_of_range(self):
        array = [1, 2, 3, 4]
        start = 2
        end = 10
        self.assertEqual(my_slice(array, start, end), [3, 4])

if __name__ == '__main__':
    unittest.main()