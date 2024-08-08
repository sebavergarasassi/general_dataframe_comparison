import unittest
import pandas as pd
import dataframe_working as dfw

class TestDataFrameComparison(unittest.TestCase):

    def setUp(self):

        self.df1 = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, 5, 6],
            "columna_3": [7, 8, 9]})

        self.df2 = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, 22, 6],
            "columna_3": [7, 8, 9]})
        
        self.df3 = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, 5, 6],
            "columna_4": [7, 8, 9]})


    def test_compare_columns_equal(self):#--->Columnas iguales
        result = dfw.compare_columns(self.df1, self.df2)
        expected = "Ambos DataFrames tienen las mismas columnas."
        self.assertEqual(result, expected)

    def test_compare_columns_different(self):#--->Columnas diferentes
        result = dfw.compare_columns(self.df1, self.df3)
        expected = (
            "Los DataFrames tienen columnas diferentes.\n"
            "Columnas extra en df1: {'columna_3'}\n"
            "Columnas extra en df2: {'columna_4'}\n")
        self.assertEqual(result, expected)

    def test_compare_rows_equal(self):#--->mismo numero de filas
        result = dfw.compare_rows(self.df1, self.df2)
        expected = "Los DataFrames tienen el mismo número de filas."
        self.assertEqual(result, expected)





        
        self.df5 = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, 5, 6]
        })
        
        self.df6 = pd.DataFrame({
            "columna_1": [1, 2],
            "columna_2": [4, 5],
            "columna_3": [7, 8]
        })
        
        self.df7 = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, None, 6],
            "columna_3": [7, 8, 9]
        })
        
        self.df8 = pd.DataFrame({
            "columna_1": [1, 2, 3],
            "columna_2": [4, 22, 6],
            "columna_3": [7, None, 9]
        })



    #2)comprobar si el numero de filas es el mismo
    #cual tiene mas filas?
    #que contiene la fila extra?

    

if __name__ == "__main__":
    unittest.main()
