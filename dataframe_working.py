import pandas as pd
import datetime as dt

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
    """
    Compares the number of rows between two DataFrames and indicates which DataFrame is missing rows if they do not have the same number of rows.
    
    Args:
    df1 (pd.DataFrame): First DataFrame.
    df2 (pd.DataFrame): Second DataFrame.
    
    Returns:
    str: Message indicating if the DataFrames have the same number of rows or which DataFrame is missing rows.
    """
    rows_df1 = len(df1)
    rows_df2 = len(df2)
    
    if rows_df1 == rows_df2:
        return "Both DataFrames have the same number of rows."
    else:
        message = "The DataFrames do not have the same number of rows.\n"
        if rows_df1 > rows_df2:
            message += f"The first DataFrame has {rows_df1 - rows_df2} additional row(s)."
        else:
            message += f"The second DataFrame has {rows_df2 - rows_df1} additional row(s)."
        return message

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

    df1=pd.DataFrame({
         "columna_1":[1, 2, 3, 4],
         "columna_2": [5, 6, 7, 8],
         "columna_3": [9, 10, 11, 12]})

    #directory path
    path=r"C:\Users\Administrador\Desktop\DataFrame work"
    registro_name="registro.csv"
    path_registro=path+chr(92)+registro_name

    #Registro de modificaciones
    try:
        registro_df=pd.read_csv(registro_name,index_col=0)
    except:
        print("no se encontro registro, se crea uno nuevo")
        registro_df=pd.DataFrame(columns=["fecha","info_columnas","info_filas","info_contenido"])
       
    
    actual_day=00
    #cuando cambia el dia ejecuta el siguiente codigo

    while True:

        if dt.datetime.today().day!=actual_day:

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
         
            try:
                #leemos df anterior
                df2=pd.read_csv(yesterday_path,index_col=0)
                #Comparar columnas
                dif_columns=compare_columns(df1,df2)
                #Comparar filas
                dif_rows=compare_rows(df1,df2)
                #Comparar celdas
                dif_content=compare_content(df1,df2)

                print("")
                print("--->dif_columns:",str(dif_columns))
                print("")
                print("--->dif_rows:",str(dif_rows))
                print("")
                print("--->dif_content:",str(dif_content))
                print("")

                #Registro
                nuevo_registro= {'fecha': today_str, 
                                 'info_columnas': dif_columns,
                                 'info_filas': dif_columns,
                                 'info_contenido': dif_content}
                #guardar registro
                nuevo_registro_df=pd.DataFrame([nuevo_registro])
                registro_df = pd.concat([registro_df, nuevo_registro_df], ignore_index=True)
                registro_df.to_csv(path_registro)
   
     
            except Exception as e:
                print("")
                print(e)
            
            actual_day=dt.datetime.today().day
            




            
        
        

