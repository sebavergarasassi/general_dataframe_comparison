import unittest
import pandas as pd
import dataframe_working as dfw  # Importamos las funciones desde dataframe_working

class Test_compare_columns(unittest.TestCase):
    
    def setUp(self):
        self.df1 = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })

        self.df2 = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })

        self.df4 = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, None, 8],
            "columna_3": [9, 10, 11, 12],
            "columna_4": [13, 14, 15, 16]
        })

    def test_compare_columns_same_columns(self):
        result = dfw.compare_columns(self.df1, self.df2)
        self.assertEqual(result, "Ambos DataFrames tienen las mismas columnas.")

    def test_compare_columns_different_columns(self):
        result = dfw.compare_columns(self.df1, self.df4)
        self.assertIn("Los DataFrames tienen columnas diferentes.", result)
        self.assertIn("Columnas extra en df2", result)

class Test_compare_rows(unittest.TestCase):
    def setUp(self):
        # Set up DataFrames for testing
        self.df1_equal = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })
        self.df2_equal = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })
        
        self.df1_more_rows = pd.DataFrame({
            "columna_1": [1, 2, 3, 4, 5],
            "columna_2": [6, 7, 8, 9, 10],
            "columna_3": [11, 12, 13, 14, 15]
        })
        self.df2_fewer_rows = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })
        
        self.df1_fewer_rows = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, 5, 6],
            "columna_3": [7, 8, 9]
        })
        self.df2_more_rows = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })

    def test_rows_equal(self):
        result = dfw.compare_rows(self.df1_equal, self.df2_equal)
        self.assertEqual(result, "Both DataFrames have the same number of rows.")

    def test_df1_more_rows(self):
        result = dfw.compare_rows(self.df1_more_rows, self.df2_fewer_rows)
        self.assertEqual(result, "The DataFrames do not have the same number of rows.\nThe first DataFrame has 1 additional row(s).")

    def test_df2_more_rows(self):
        result = dfw.compare_rows(self.df1_fewer_rows, self.df2_more_rows)
        self.assertEqual(result, "The DataFrames do not have the same number of rows.\nThe second DataFrame has 1 additional row(s).")

class Test_compare_content(unittest.TestCase):
    
    def setUp(self):
        self.df1 = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })

        self.df2 = pd.DataFrame({
            "columna_1": [1, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })

        self.df3 = pd.DataFrame({
            "columna_1": [11234, 2, 3, 4],
            "columna_2": [5, 6, 7, 8],
            "columna_3": [9, 10, 11, 12]
        })
        self.df4 = pd.DataFrame({"columna_1": [1, 2, 3, 4],
                                 "columna_2":[5, 6,None, 8],
                                 "columna_3":[9, 10, 11, 12]})

    def test_compare_content_same_content(self):
        result = dfw.compare_content(self.df1, self.df2)
        self.assertEqual(result, "El contenido de ambos DataFrames es el mismo.")

    def test_compare_content_different_content(self):
        result = dfw.compare_content(self.df1, self.df3)
        self.assertIn("Diferencias encontradas en las siguientes filas y columnas:", result)

    def test_compare_content_different_content_with_null(self):
        result = dfw.compare_content(self.df1, self.df4)
        self.assertIn("Diferencias encontradas en las siguientes filas y columnas:", result)
    
if __name__ == "__main__":
    unittest.main()
