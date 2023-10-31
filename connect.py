import pandas as pd

class connection:
   def getprop(self):
      df= pd.read_excel('zoetisexport.xlsx')
      return df



