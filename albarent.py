import pandas as pd
import numpy as np
import PySimpleGUI as sg

pd.set_option('max_columns', None)
pd.set_option('max_row',None)

database = pd.read_csv('database.csv')

header_list = database.iloc[0].tolist()
data = database[1:].values.tolist()


def table_example():

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()
    window.close()


table_example()