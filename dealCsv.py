import csv
import pandas as pd

class dealCsv:

    def __init__(self, file) -> None:
        self.file=open(file, mode='r')
    
    def __del__(self):
        self.file.close()
    
    def header(self):
        self.file.seek(0,0)
        reader=csv.reader(self.file)
        header=next(reader)
        return header


    def data_by_index(self, list):
        self.file.seek(0,0)
        df=pd.read_csv(self.file,sep=',')
        result = df[list]
        return result