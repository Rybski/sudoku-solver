import unittest
from core.board import Digit, Cell, Map


class TestDigit(unittest.TestCase):
    
    def test_valid_digit(self):
        d = Digit(5)
        self.assertEqual(d, 5)
        self.assertIsInstance(d, int)
        self.assertIsInstance(d, Digit)
            
    def test_invalid_digit(self):
        with self.assertRaises(Exception):
            Digit(0)
        with self.assertRaises(Exception):
            Digit(10)
        with self.assertRaises(Exception):
            Digit(None)
        with self.assertRaises(Exception):
            Digit("5")

            
            
# class TestCell(unittest.TestCase):
    
#     def test_valid_cell(self):
#         c = Cell.create(5)
        
        
class TestMap(unittest.TestCase):
    empty_cell = Cell.create()
    test_row = [Cell.create(9),Cell.create(5),Cell.create(1), Cell.create(7),Cell.create(4),Cell.create(3), Cell.create(6),Cell.create(2),Cell.create(8)]
    test_column = [Cell.create(9),Cell.create(1),Cell.create(4), Cell.create(5),Cell.create(2),Cell.create(3), Cell.create(6),Cell.create(7),Cell.create(8)]
    test_box = [Cell.create(1),Cell.create(9),Cell.create(5),
                Cell.create(6),Cell.create(8),Cell.create(2),
                Cell.create(7),Cell.create(4),Cell.create(3)]
    test_list = [Cell.create(4),Cell.create(3),Cell.create(5), Cell.create(2),Cell.create(6),Cell.create(9), Cell.create(7),Cell.create(8),Cell.create(1),
                 Cell.create(6),Cell.create(8),Cell.create(2), Cell.create(5),Cell.create(7),Cell.create(1), Cell.create(4),Cell.create(9),Cell.create(3),
                 Cell.create(1),Cell.create(9),Cell.create(7), Cell.create(8),Cell.create(3),Cell.create(4), Cell.create(5),Cell.create(6),Cell.create(2),
                 Cell.create(8),Cell.create(2),Cell.create(6), Cell.create(1),Cell.create(9),Cell.create(5), Cell.create(3),Cell.create(4),Cell.create(7),
                 Cell.create(3),Cell.create(7),Cell.create(4), Cell.create(6),Cell.create(8),Cell.create(2), Cell.create(9),Cell.create(1),Cell.create(5),
                 Cell.create(9),Cell.create(5),Cell.create(1), Cell.create(7),Cell.create(4),Cell.create(3), Cell.create(6),Cell.create(2),Cell.create(8),
                 Cell.create(5),Cell.create(1),Cell.create(9), Cell.create(3),Cell.create(2),Cell.create(6), Cell.create(8),Cell.create(7),Cell.create(4),
                 Cell.create(2),Cell.create(4),Cell.create(8), Cell.create(9),Cell.create(5),Cell.create(7), Cell.create(1),Cell.create(3),Cell.create(6),
                 Cell.create(7),Cell.create(6),Cell.create(3), Cell.create(4),Cell.create(1),Cell.create(8), Cell.create(2),Cell.create(5),Cell.create(9)]
    test_empty_list = [Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(),
                       Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create(), Cell.create()]
    test_map = [4,3,5, 2,6,9, 7,8,1,
                6,8,2, 5,7,1, 4,9,3,
                1,9,7, 8,3,4, 5,6,2,
                8,2,6, 1,9,5, 3,4,7,
                3,7,4, 6,8,2, 9,1,5,
                9,5,1, 7,4,3, 6,2,8,
                5,1,9, 3,2,6, 8,7,4,
                2,4,8, 9,5,7, 1,3,6,
                7,6,3, 4,1,8, 2,5,9]
    test_map_by_rows = [[Cell.create(4),Cell.create(3),Cell.create(5), Cell.create(2),Cell.create(6),Cell.create(9), Cell.create(7),Cell.create(8),Cell.create(1)],
                        [Cell.create(6),Cell.create(8),Cell.create(2), Cell.create(5),Cell.create(7),Cell.create(1), Cell.create(4),Cell.create(9),Cell.create(3)],
                        [Cell.create(1),Cell.create(9),Cell.create(7), Cell.create(8),Cell.create(3),Cell.create(4), Cell.create(5),Cell.create(6),Cell.create(2)],
                        [Cell.create(8),Cell.create(2),Cell.create(6), Cell.create(1),Cell.create(9),Cell.create(5), Cell.create(3),Cell.create(4),Cell.create(7)],
                        [Cell.create(3),Cell.create(7),Cell.create(4), Cell.create(6),Cell.create(8),Cell.create(2), Cell.create(9),Cell.create(1),Cell.create(5)],
                        [Cell.create(9),Cell.create(5),Cell.create(1), Cell.create(7),Cell.create(4),Cell.create(3), Cell.create(6),Cell.create(2),Cell.create(8)],
                        [Cell.create(5),Cell.create(1),Cell.create(9), Cell.create(3),Cell.create(2),Cell.create(6), Cell.create(8),Cell.create(7),Cell.create(4)],
                        [Cell.create(2),Cell.create(4),Cell.create(8), Cell.create(9),Cell.create(5),Cell.create(7), Cell.create(1),Cell.create(3),Cell.create(6)],
                        [Cell.create(7),Cell.create(6),Cell.create(3), Cell.create(4),Cell.create(1),Cell.create(8), Cell.create(2),Cell.create(5),Cell.create(9)]]
    test_map_by_columns = [[Cell.create(4),Cell.create(6),Cell.create(1), Cell.create(8),Cell.create(3),Cell.create(9), Cell.create(5),Cell.create(2),Cell.create(7)],
                           [Cell.create(3),Cell.create(8),Cell.create(9), Cell.create(2),Cell.create(7),Cell.create(5), Cell.create(1),Cell.create(4),Cell.create(6)],
                           [Cell.create(5),Cell.create(2),Cell.create(7), Cell.create(6),Cell.create(4),Cell.create(1), Cell.create(9),Cell.create(8),Cell.create(3)],
                           [Cell.create(2),Cell.create(5),Cell.create(8), Cell.create(1),Cell.create(6),Cell.create(7), Cell.create(3),Cell.create(9),Cell.create(4)],
                           [Cell.create(6),Cell.create(7),Cell.create(3), Cell.create(9),Cell.create(8),Cell.create(4), Cell.create(2),Cell.create(5),Cell.create(1)],
                           [Cell.create(9),Cell.create(1),Cell.create(4), Cell.create(5),Cell.create(2),Cell.create(3), Cell.create(6),Cell.create(7),Cell.create(8)],
                           [Cell.create(7),Cell.create(4),Cell.create(5), Cell.create(3),Cell.create(9),Cell.create(6), Cell.create(8),Cell.create(1),Cell.create(2)],
                           [Cell.create(8),Cell.create(9),Cell.create(6), Cell.create(4),Cell.create(1),Cell.create(2), Cell.create(7),Cell.create(3),Cell.create(5)],
                           [Cell.create(1),Cell.create(3),Cell.create(2), Cell.create(7),Cell.create(5),Cell.create(8), Cell.create(4),Cell.create(6),Cell.create(9)]]
    test_map_by_boxes = [[Cell.create(4),Cell.create(3),Cell.create(5), Cell.create(6),Cell.create(8),Cell.create(2), Cell.create(1),Cell.create(9),Cell.create(7)],
                         [Cell.create(2),Cell.create(6),Cell.create(9), Cell.create(5),Cell.create(7),Cell.create(1), Cell.create(8),Cell.create(3),Cell.create(4)],
                         [Cell.create(7),Cell.create(8),Cell.create(1), Cell.create(4),Cell.create(9),Cell.create(3), Cell.create(5),Cell.create(6),Cell.create(2)],
                         [Cell.create(8),Cell.create(2),Cell.create(6), Cell.create(3),Cell.create(7),Cell.create(4), Cell.create(9),Cell.create(5),Cell.create(1)],
                         [Cell.create(1),Cell.create(9),Cell.create(5), Cell.create(6),Cell.create(8),Cell.create(2), Cell.create(7),Cell.create(4),Cell.create(3)],
                         [Cell.create(3),Cell.create(4),Cell.create(7), Cell.create(9),Cell.create(1),Cell.create(5), Cell.create(6),Cell.create(2),Cell.create(8)],
                         [Cell.create(5),Cell.create(1),Cell.create(9), Cell.create(2),Cell.create(4),Cell.create(8), Cell.create(7),Cell.create(6),Cell.create(3)],
                         [Cell.create(3),Cell.create(2),Cell.create(6), Cell.create(9),Cell.create(5),Cell.create(7), Cell.create(4),Cell.create(1),Cell.create(8)],
                         [Cell.create(8),Cell.create(7),Cell.create(4), Cell.create(1),Cell.create(3),Cell.create(6), Cell.create(2),Cell.create(5),Cell.create(9)]]
    def test_valid_map(self):
        m = Map.create()
        self.assertListEqual(m, self.test_empty_list)
        self.assertIsInstance(m, list)
        self.assertIsInstance(m, Map)
        m = Map.create(self.test_map)
        self.assertListEqual(m, self.test_list)
        self.assertIsInstance(m, list)
        self.assertIsInstance(m, Map)
        
    def test_get_cell(self):
        m = Map.create(self.test_map)
        self.assertEqual(m.get_cell_by_index(50), Cell.create(3))
        self.assertEqual(m.get_cell(5,5), Cell.create(3))
        self.assertIsInstance(m.get_cell(5,5), Cell)
        
    def test_rows(self):
        m = Map.create(self.test_map)
        self.assertEqual(m.get_row(50), 5)
        self.assertIsInstance(m.get_row(50), int)
        # self.assertIsInstance(m.get_row(50), Digit)
        self.assertListEqual(m.get_row_cells(5), self.test_row)
        self.assertListEqual(m.get_rows(), self.test_map_by_rows)
        
    def test_columns(self):
        m = Map.create(self.test_map)
        self.assertEqual(m.get_column(50), 5)
        self.assertIsInstance(m.get_column(50), int)
        # self.assertIsInstance(m.get_column(50), Digit)
        self.assertListEqual(m.get_column_cells(5), self.test_column)
        self.assertListEqual(m.get_columns(), self.test_map_by_columns)
        
    def test_boxes(self):
        m = Map.create(self.test_map)
        self.assertEqual(m.get_box(50), 4)
        self.assertIsInstance(m.get_box(50), int)
        # self.assertIsInstance(m.get_box(50), Digit)
        self.assertListEqual(m.get_box_cells(4), self.test_box)
        self.assertListEqual(m.get_boxes(), self.test_map_by_boxes)