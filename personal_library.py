
"""
    Librería personal para análisis de datos
    
    En este archivo se encuentran varios métodos usados con frecuencia.
""" 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def rename_columns(df):
    new_col_names = []
    
    for old_name in df.columns:
        # Eliminando espacios al principio y al final
        name_stripped = old_name.strip()
        # Todas las letras a minúsculas
        name_lowered = name_stripped.lower()
        # Remplazando espacios por "_"
        name_no_spaces = name_lowered.replace(' ', '_')
        # Agregamos al arreglo con los nuevos nombres
        new_col_names.append(name_no_spaces)
        
    return new_col_names
