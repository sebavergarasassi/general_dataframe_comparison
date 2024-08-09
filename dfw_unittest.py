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
            "columna_1": [1, 2, 3],
            "columna_2": [5, 6, 7]
        })

    def test_compare_rows_same_rows(self):
        result = dfw.compare_rows(self.df1, self.df2)
        self.assertEqual(result, "Los DataFrames tienen el mismo número de filas.")

    def test_compare_rows_different_rows(self):
        result = dfw.compare_rows(self.df1, self.df3)
        self.assertIn("df1 tiene más filas.", result)

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
