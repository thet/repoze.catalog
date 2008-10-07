import unittest

class TestCatalogKeywordIndex(unittest.TestCase):
    def _getTargetClass(self):
        from repoze.catalog.indexes.keyword import CatalogKeywordIndex
        return CatalogKeywordIndex

    def _makeOne(self):
        klass = self._getTargetClass()
        return klass(lambda x, default: x)

    def test_apply_with_dict_operator_or(self):
        index = self._makeOne()
        index.index_doc(1, [1,2,3])
        index.index_doc(2, [3,4,5])
        index.index_doc(3, [5,6,7])
        index.index_doc(4, [7,8,9]) 
        index.index_doc(5, [9,10])
        result = index.apply({'operator':'or', 'query':[5]})
        self.assertEqual(list(result), [2,3])

    def test_apply_with_dict_operator_and(self):
        index = self._makeOne()
        index.index_doc(1, [1,2,3])
        index.index_doc(2, [3,4,5])
        index.index_doc(3, [5,6,7])
        index.index_doc(4, [7,8,9]) 
        index.index_doc(5, [9,10])
        result = index.apply({'operator':'and', 'query':[5, 6]})
        self.assertEqual(list(result), [3])

    def test_apply_with_empty_result_first(self):
        index = self._makeOne()
        index.index_doc(1, [1,2,3])
        index.index_doc(2, [3,4,5])
        index.index_doc(3, [5,6,7])
        index.index_doc(4, [7,8,9]) 
        index.index_doc(5, [9,10])
        result = index.apply({'operator':'and', 'query':[11,5]})
        self.assertEqual(list(result), [])
        
    def test_apply_with_empty_result_last(self):
        index = self._makeOne()
        index.index_doc(1, [1,2,3])
        index.index_doc(2, [3,4,5])
        index.index_doc(3, [5,6,7])
        index.index_doc(4, [7,8,9]) 
        index.index_doc(5, [9,10])
        result = index.apply({'operator':'and', 'query':[5,11]})
        self.assertEqual(list(result), [])