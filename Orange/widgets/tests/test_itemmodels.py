# Test methods with long descriptive names can omit docstrings
# pylint: disable=missing-docstring

from unittest import TestCase

from PyQt4.QtCore import Qt
from Orange.widgets.utils.itemmodels import PyTableModel


class TestPyTableModel(TestCase):
    def setUp(self):
        self.model = PyTableModel([[1, 4],
                                   [2, 3]])

    def test_init(self):
        self.model = PyTableModel()
        self.assertEqual(self.model.rowCount(), 0)

    def test_rowCount(self):
        self.assertEqual(self.model.rowCount(), 2)
        self.assertEqual(len(self.model), 2)

    def test_columnCount(self):
        self.assertEqual(self.model.columnCount(), 2)

    def test_data(self):
        self.assertEqual(str(self.model.data(self.model.index(0, 0))), '1')

    def test_sort(self):
        self.model.sort(1)
        self.assertEqual(self.model[0][0], 2)

    def test_setHeaderLabels(self):
        self.model.setHorizontalHeaderLabels(['Col 1', 'Col 2'])
        self.assertEqual(self.model.headerData(1, Qt.Horizontal), 'Col 2')
        self.assertEqual(self.model.headerData(1, Qt.Vertical), '1')

    def test_removeRows(self):
        self.model.removeRows(0, 1)
        self.assertEqual(len(self.model), 1)
        self.assertEqual(self.model[0][1], 3)

    def test_removeColumns(self):
        self.model.removeColumns(0, 1)
        self.assertEqual(self.model.columnCount(), 1)
        self.assertEqual(self.model[1][0], 3)

    def test_insertRows(self):
        self.model.insertRows(0, 1)
        self.assertEqual(self.model[1][0], 1)

    def test_insertColumns(self):
        self.model.insertColumns(0, 1)
        self.assertEqual(self.model[0], ['', 1, 4])

    def test_wrap(self):
        self.model.wrap([[0]])
        self.assertEqual(self.model.rowCount(), 1)
        self.assertEqual(self.model.columnCount(), 1)

    def test_clear(self):
        self.model.clear()
        self.assertEqual(self.model.rowCount(), 0)

    def test_append(self):
        self.model.append([5, 6])
        self.assertEqual(self.model[2][1], 6)
        self.assertEqual(self.model.rowCount(), 3)

    def test_extend(self):
        self.model.extend([[5, 6]])
        self.assertEqual(self.model[2][1], 6)
        self.assertEqual(self.model.rowCount(), 3)

    def test_insert(self):
        self.model.insert(0, [5, 6])
        self.assertEqual(self.model[0][1], 6)
        self.assertEqual(self.model.rowCount(), 3)

    def test_remove(self):
        self.model.remove([2, 3])
        self.assertEqual(self.model.rowCount(), 1)