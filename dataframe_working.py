import pandas as pd
import datetime as dt

"""
def compare_columns(df1, df2):
    cols_df1 = set(df1.columns)
    cols_df2 = set(df2.columns)

    result = ""
    if cols_df1 == cols_df2:
        result = "Ambos DataFrames tienen las mismas columnas."
    else:
        result = "Los DataFrames tienen columnas diferentes.\n"
        
        if len(cols_df1) > len(cols_df2):
            result += "df1 tiene más columnas.\n"
        elif len(cols_df1) < len(cols_df2):
            result += "df2 tiene más columnas.\n"
        else:
            result += "Ambos tienen el mismo número de columnas.\n"

        extra_cols_df1 = cols_df1 - cols_df2
        extra_cols_df2 = cols_df2 - cols_df1

        if extra_cols_df1:
            result += f"Columnas extra en df1: {extra_cols_df1}\n"
        if extra_cols_df2:
            result += f"Columnas extra en df2: {extra_cols_df2}\n"

    return result.strip()

def compare_rows(df1, df2):
    rows_df1 = len(df1)
    rows_df2 = len(df2)

    result = ""
    if rows_df1 == rows_df2:
        result = "Ambos DataFrames tienen el mismo número de filas."
    else:
        result = "Los DataFrames tienen un número diferente de filas.\n"
        
        if rows_df1 > rows_df2:
            result += "df1 tiene más filas.\n"
            extra_row = df1.iloc[rows_df2:]
            result += f"Contenido de la(s) fila(s) extra en df1:\n{extra_row.to_string(index=False)}"
        else:
            result += "df2 tiene más filas.\n"
            extra_row = df2.iloc[rows_df1:]
            result += f"Contenido de la(s) fila(s) extra en df2:\n{extra_row.to_string(index=False)}"

    return result.strip()

def compare_content(df1, df2):
    if df1.shape != df2.shape:
        result = f"Los DataFrames tienen dimensiones diferentes.\nDimensiones de df1: {df1.shape}\nDimensiones de df2: {df2.shape}\n"
        result += "Comparando el contenido de las dimensiones compatibles:\n"
        
        # Limitar el tamaño de la comparación a las dimensiones más pequeñas
        min_rows = min(df1.shape[0], df2.shape[0])
        min_cols = min(df1.shape[1], df2.shape[1])
        
        df1_trimmed = df1.iloc[:min_rows, :min_cols]
        df2_trimmed = df2.iloc[:min_rows, :min_cols]
        
        # Comparar los DataFrames recortados
        differences = []
        for col in df1_trimmed.columns:
            for row in df1_trimmed.index:
                if df1_trimmed.at[row, col] != df2_trimmed.at[row, col]:
                    differences.append({
                        "Fila": row,
                        "Columna": col,
                        "Valor_df1": df1_trimmed.at[row, col],
                        "Valor_df2": df2_trimmed.at[row, col]
                    })
        
        if differences:
            result += "Diferencias encontradas en las siguientes filas y columnas:\n"
            diff_df = pd.DataFrame(differences)
            result += diff_df.to_string(index=False)
        else:
            result += "El contenido de ambos DataFrames es el mismo en las dimensiones comparables."

        # Verificar filas con valores nulos en ambos DataFrames
        null_rows_df1 = df1[df1.isnull().any(axis=1)]
        null_rows_df2 = df2[df2.isnull().any(axis=1)]

        if not null_rows_df1.empty:
            result += f"\ndf1 tiene filas con valores nulos:\n{null_rows_df1.to_string(index=False)}"
        
        if not null_rows_df2.empty:
            result += f"\ndf2 tiene filas con valores nulos:\n{null_rows_df2.to_string(index=False)}"
        
        return result.strip()
    
    # Si tienen las mismas dimensiones, comparar directamente
    else:
        result = "Los DataFrames tienen las mismas dimensiones.\n"
        
        differences = []
        for col in df1.columns:
            for row in df1.index:
                if df1.at[row, col] != df2.at[row, col]:
                    differences.append({
                        "Fila": row,
                        "Columna": col,
                        "Valor_df1": df1.at[row, col],
                        "Valor_df2": df2.at[row, col]
                    })
        
        if differences:
            result += "Diferencias encontradas en las siguientes filas y columnas:\n"
            diff_df = pd.DataFrame(differences)
            result += diff_df.to_string(index=False)
        else:
            result += "El contenido de ambos DataFrames es el mismo."
        
        # Verificar filas con valores nulos en ambos DataFrames
        null_rows_df1 = df1[df1.isnull().any(axis=1)]
        null_rows_df2 = df2[df2.isnull().any(axis=1)]

        if not null_rows_df1.empty:
            result += f"\ndf1 tiene filas con valores nulos:\n{null_rows_df1.to_string(index=False)}"
        
        if not null_rows_df2.empty:
            result += f"\ndf2 tiene filas con valores nulos:\n{null_rows_df2.to_string(index=False)}"
        
        return result.strip()    
"""

def compare_columns(df1: pd.DataFrame, df2: pd.DataFrame) -> str:
    """
    Compara las columnas de dos DataFrames y devuelve un mensaje indicando si las columnas son iguales o diferentes.
    """
    columns_df1 = set(df1.columns)
    columns_df2 = set(df2.columns)
    
    if columns_df1 == columns_df2:
        return "Ambos DataFrames tienen las mismas columnas."
    
    result = "Los DataFrames tienen columnas diferentes.\n"
    
    if columns_df1 != columns_df2:
        extra_in_df1 = columns_df1 - columns_df2
        extra_in_df2 = columns_df2 - columns_df1
        
        if extra_in_df1:
            result += f"Columnas extra en df1: {extra_in_df1}\n"
        if extra_in_df2:
            result += f"Columnas extra en df2: {extra_in_df2}\n"
    
    return result

def compare_rows(df1, df2):
    if df1.shape[0] == df2.shape[0]:
        return "Los DataFrames tienen el mismo número de filas."
    
    result = "Los DataFrames tienen un número diferente de filas.\n"
    
    if df1.shape[0] > df2.shape[0]:
        result += "df1 tiene más filas.\n"
        result += "Contenido de la(s) fila(s) extra en df1:\n"
        result += df1.iloc[len(df2):].to_string()
    else:
        result += "df2 tiene más filas.\n"
        result += "Contenido de la(s) fila(s) extra en df2:\n"
        result += df2.iloc[len(df1):].to_string()
    
    return result

def compare_content(df1, df2):
    if df1.shape != df2.shape:
        return "Los DataFrames tienen dimensiones diferentes y no se pueden comparar directamente."
    
    differences = []
    for i in range(df1.shape[0]):
        for j in range(df1.shape[1]):
            val1 = df1.iat[i, j]
            val2 = df2.iat[i, j]
            if val1 != val2:
                differences.append(f"Fila {i} Columna {df1.columns[j]} Valor_df1: {val1} Valor_df2: {val2}")
    
    if not differences:
        return "El contenido de ambos DataFrames es el mismo."
    
    result = "Diferencias encontradas en las siguientes filas y columnas:\n"
    result += "\n".join(differences)
    
    nulls_df1 = df1[df1.isnull().any(axis=1)]
    nulls_df2 = df2[df2.isnull().any(axis=1)]
    
    if not nulls_df1.empty:
        result += "\ndf1 tiene filas con valores nulos:\n"
        result += nulls_df1.to_string(index=False)
    
    if not nulls_df2.empty:
        result += "\ndf2 tiene filas con valores nulos:\n"
        result += nulls_df2.to_string(index=False)
    
    return result


if __name__=="__main__":

    df1=pd.DataFrame({"columna_1":[1,2,3,4],
                  "columna_2":[5,6,7,8],
                  "columna_3":[9,10,11,12]})

                
    #directory path
    path=r"C:\Users\Administrador\Desktop\DataFrame work"

    #today info
    today=dt.date.today()
    today_str=today.strftime("%d_%m_%Y")
    today_path=path+chr(92)+today_str+".csv"
    print("today_str:",today_str)
    print("today_path:",today_path)

    #yesterday info
    yesterday=dt.date.today()-dt.timedelta(days=1)
    yesterday_str=yesterday.strftime("%d_%m_%Y")
    yesterday_path=path+chr(92)+yesterday_str+".csv"
    print("yesterday_str:",yesterday_str)
    print("yesterday_path:",yesterday_path)

    actual_day=00
    #cuando cambia el dia ejecuta el siguiente codigo

    while not dt.date.today().day==actual_day:

        #today info
        today=dt.date.today()
        today_str=today.strftime("%d_%m_%Y")
        today_path=path+chr(92)+today_str+".csv"
        print("")
        print("today_str:",today_str)
        print("today_path:",today_path)
        #grabamos la info de hoy
        df1.to_csv(today_path)

        #yesterday info
        yesterday=dt.date.today()-dt.timedelta(days=1)
        yesterday_str=yesterday.strftime("%d_%m_%Y")
        yesterday_path=path+chr(92)+yesterday_str+".csv"
        print("")
        print("yesterday_str:",yesterday_str)
        print("yesterday_path:",yesterday_path)
        #tretamos de leer la info de ayer
        try:
            df2=pd.read_csv(yesterday_path,index_col=0)
            print(df1)
            print(df2)

            #1)comprobar si el contenido de columnas es el mismo
            #cual tiene mas columnas?
            #en que columnas difieren?
            dif_columns=compare_columns(df1,df2)
            
            #2)comprobar si el numero de filas es el mismo
            #cual tiene mas filas?
            #que contiene la fila extra?
            dif_rows=compare_rows(df1,df2)

            #3)comprueba que el contenido de los df sean iguales
            #podrias identificar columna y fila diferente? mostrando el contenido de cada df en dicha fila y columna
            #existe una fila con contenido nulo
            dif_content=compare_content(df1,df2)

            print(dif_columns)
            print(dif_rows)
            print(dif_content)
            #compuruba la falta de rows
            #guarda registro en un log

        except Exception as e:
            print("")
            print(f"No se encuentra df de fecha {yesterday_str}")
            actual_day=dt.date.today().day
        actual_day=dt.date.today().day
        




        
        
        

