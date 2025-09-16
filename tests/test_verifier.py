import unittest
from core.board import Cell, Map
from core.verifier import verify, check_rows, check_columns, check_boxes, check_unique, check_set


class TestVerifier(unittest.TestCase):
    unset_list = [[1,9],[2,8],[3,7],[4,6],[5,5],[6,4],[7,3],[8,2],[9,1]]
    set_list = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    partialy_set_list = [Cell.create([1]),Cell.create([2,1]),Cell.create([3]),Cell.create([4,5,6]),Cell.create([5]),Cell.create([6]),Cell.create([7]),Cell.create([8]),Cell.create([9])]
    unset_cells = [Cell.create([1,9]),Cell.create([2,8]),Cell.create([3,7]),Cell.create([4,6]),Cell.create([5,5]),Cell.create([6,4]),Cell.create([7,3]),Cell.create([8,2]),Cell.create([9,1])]
    set_cells = [Cell.create([1]),Cell.create([2]),Cell.create([3]),Cell.create([4]),Cell.create([5]),Cell.create([6]),Cell.create([7]),Cell.create([8]),Cell.create([9])]
    partialy_set_cells = [Cell.create([1]),Cell.create([2,1]),Cell.create([3]),Cell.create([4,5,6]),Cell.create([5]),Cell.create([6]),Cell.create([7]),Cell.create([8]),Cell.create([9])]
    
    unique_list = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    non_unique_list = [[1],[1],[3],[5],[5],[6],[3],[8],[9]]
    unique_cells = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    non_unique_cells = [[1],[1],[3],[5],[5],[6],[3],[8],[9]]
    
    
    empty_map = Map.create()
    resolved_map = Map.create([4,3,5, 2,6,9, 7,8,1,
                           6,8,2, 5,7,1, 4,9,3,
                           1,9,7, 8,3,4, 5,6,2,
                           8,2,6, 1,9,5, 3,4,7,
                           3,7,4, 6,8,2, 9,1,5,
                           9,5,1, 7,4,3, 6,2,8,
                           5,1,9, 3,2,6, 8,7,4,
                           2,4,8, 9,5,7, 1,3,6,
                           7,6,3, 4,1,8, 2,5,9])
    bad_map = Map.create([4,5,5, 2,6,9, 7,8,1,
                          6,8,5, 5,7,8, 4,9,3,
                          1,9,7, 1,3,4, 5,1,2,
                          8,2,6, 1,9,9, 3,4,7,
                          3,7,4, 3,2,2, 9,1,5,
                          9,5,1, 7,4,3, 6,2,8,
                          5,4,3, 3,2,6, 8,7,4,
                          2,4,8, 6,8,7, 1,9,6,
                          7,6,3, 4,1,8, 2,5,9])
    
    def test_check_set(self):
        self.assertTrue(check_set(self.set_list))
        self.assertFalse(check_set(self.unset_list))
        self.assertFalse(check_set(self.partialy_set_list))
        self.assertTrue(check_set(self.set_cells))
        self.assertFalse(check_set(self.unset_cells))
        self.assertFalse(check_set(self.partialy_set_cells))
    
    def test_check_unique(self):
        self.assertTrue(check_unique(self.unique_list))
        self.assertFalse(check_unique(self.non_unique_list))
        self.assertTrue(check_unique(self.unique_cells))
        self.assertFalse(check_unique(self.non_unique_cells))
    
    def test_check_boxes(self):
        self.assertTrue(check_boxes(self.resolved_map))
        self.assertFalse(check_boxes(self.empty_map))
        self.assertFalse(check_boxes(self.bad_map))
    
    def test_check_columns(self):
        self.assertTrue(check_columns(self.resolved_map))
        self.assertFalse(check_columns(self.empty_map))
        self.assertFalse(check_columns(self.bad_map))
    
    def test_check_rows(self):
        self.assertTrue(check_rows(self.resolved_map))
        self.assertFalse(check_rows(self.empty_map))
        self.assertFalse(check_rows(self.bad_map))
    
    def test_verify(self):
        self.assertTrue(verify(self.resolved_map))
        self.assertFalse(verify(self.empty_map))
        self.assertFalse(verify(self.bad_map))