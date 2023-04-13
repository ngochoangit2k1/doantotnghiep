import  gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import  pandas

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]



creds = ServiceAccountCredentials.from_json_keyfile_name("face-api.json")
file = gspread.authorize(creds)

workbook= file.open('dataface')
sheet = workbook.sheet1

data1 = [ 4 ,    1   , 'bit' , 'Computer'  , '12:42:12'  ,'05/04/2023' , 'Preset']
sheet.insert_row(data1, len(sheet.get_all_values())+1)

workbook.url
data = pd.DataFrame(sheet.get_all_records())
print(data)
