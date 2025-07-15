import pandas as pd
import os


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """




    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)

  
    columnas = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "monto_del_credito",
        "línea_credito",
    ]

    for columna in columnas:


        df[columna] = (
            df[columna]
            .str.lower()
            .str.strip()
            .str.replace("_", " ")
            .str.replace("-", " ")
            .str.replace(",", "")
            .str.replace(".00", "")
            .str.replace("$", "")
            .str.strip()
        )
    




   

    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(
        pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )

    df = df.drop_duplicates()
    df = df.dropna()

    


    output_directory="files/output"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    df.to_csv(
        f"{output_directory}/solicitudes_de_credito.csv",
        sep=";",
        index=False,
    )


