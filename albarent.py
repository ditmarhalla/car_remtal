import pandas as pd
import numpy as np
import PySimpleGUI as sg

pd.set_option('max_columns', None)
pd.set_option('max_row',None)

database = pd.read_csv('database.csv')

header_list = database.columns.values.tolist()
data = database[0:].values.tolist()

layout = [[sg.Button('Database'), sg.Button('Shto Makine'), sg.Button('Quit')]]

def show_database():

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window('Alba Rent', layout, grab_anywhere=False)
    event, values = window.read()
    window.close()

def add_car ():

    layout = [  [sg.Text("Targa: ",size=(10,1)),sg.Text("Modeli: ",size=(10,1)),sg.Text("Viti Prodhimit: ",size=(10,1)),sg.Text("Fuqia Motorike (cc): ",size=(10,1)),sg.Text("Naft/Benzin: ",size=(10,1)),sg.Text("Vendet: ",size=(10,1))],
            [sg.Input(size=(10,1)),sg.Input(size=(10,1)),sg.Input(size=(10,1)),sg.Input(size=(10,1)),sg.Input(size=(10,1)),sg.Input(size=(10,1)),],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('SHTO  MAKINE'),  sg.Button('Mbyll')] ]

    window = sg.Window('Alba Rent', layout, margins =(100,50))

    while True:
        event, value = window.read()
        print(value[0][0:2])
        print("This is the test: ",value[0][0:2]== str())
        #print("This is the test: ",value[0][0:2]!= str(), int(value[0][3:6]) != int(), value[0][7:9] != str())
        if value[0][0:2]== str()  and int(value[0][3:6]) == int()  and value[0][7:9] == str():
            window['-OUTPUT-'].update("Targa nuk eshte e sakte")

        if int(value[2])>2030 or int(value[2])<1990:
            window['-OUTPUT-'].update("Viti nuk eshte i sakte")


        database.loc[len(database.index)] = [value[0].upper(),
                                            value[1].capitalize(),value[2],value[3],value[4].capitalize(),value[5]]
        
        
        #database.to_csv('database.csv',index = False)

        if event == sg.WINDOW_CLOSED or event == 'Mbyll':
            break        
    window.close()

'''

def change_data():
'''

window = sg.Window('Alba Rent', layout,margins =(100,50))

while True:
    event, value = window.read()
    if event == "Database":
        show_database()
    elif event == "Shto Makine":
        add_car()
    elif event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()


