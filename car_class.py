import pandas as pd

class Car:
    def __init__(self): 
       self.df =  pd.read_csv('database.csv')

    def add_car(self):
        print(self.df)
        targa = input("Targa: ")
        modeli = input("Modeli: ").capitalize()
        viti = input("Viti prodhimit: ")
        cc = input("Fuqia motorrit (cc): ")
        karburanti = input("Naft apo Benzin: ").capitalize()
        vende = input("Numri I vendeve: ")
                
        df2 = pd.DataFrame({'Targa': [targa],'Modeli': [modeli], 'Viti Prodhimit' : [viti], 'Kapacitetti CC' : [cc], 'Karburanti' : [karburanti], 'Numri i vendeve' : [vende]})    
        #self.df.loc[len(self.df.index)] = [targa,modeli,viti,cc,karburanti,vende]

        return self.df.append(df2, ignore_index = True)


new = Car().add_car()

print(new)