


import pandas as pd
import re
import nltk
from pandas import ExcelWriter
data=pd.read_csv('C:\\Users\\pshin\\OneDrive\\Desktop\\Project\\Case 2\\Sample_Data.tsv',delimiter= '\t')
ADDRESS=data[["Source Address"]].copy()
ADDRESS=ADDRESS.drop(ADDRESS.index[0])
#Preprocessing of Data
ADDRESS['Source Address']=ADDRESS['Source Address'].str.replace('[\#\-]',' ')
ADDRESS['Source Address']=ADDRESS['Source Address'].apply(lambda x : x.strip())
ADDRESS['Source Address']=ADDRESS['Source Address'].str.replace('[\ ]','_')

pattern = '|'.join(['VILL_'])
ADDRESS['Source Address'] = ADDRESS['Source Address'].str.replace(pattern,'VILLAGE ')
pattern='|'.join(['VILLAGE '])
ADDRESS['Source Address'] = ADDRESS['Source Address'].str.replace(pattern,'VILLAGE_ ')
pattern = '|'.join(['H_NO'])
ADDRESS['Source Address'] = ADDRESS['Source Address'].str.replace(pattern,'H ')
pattern = '|'.join(['/F'])
ADDRESS['Source Address'] = ADDRESS['Source Address'].str.replace(pattern,':FLOOR')
pattern = '|'.join(['NEAR'])
ADDRESS['Source Address'] = ADDRESS['Source Address'].str.replace(pattern,'-NEAR')
pattern = '|'.join(['DELHI'])
ADDRESS['Source Address'] = ADDRESS['Source Address'].str.replace(pattern,'.DELHI')

#Converted the Source Address to Standard Address

ADDRESS['House_no']=ADDRESS['Source Address'].str.extract('(\w\_\d{2,5}\/\w|\_\w\ \_\d{2,5}|\w\_\d{2,5})')
ADDRESS['Khasra_no']=ADDRESS['Source Address'].str.extract('([A-Z]{2}\_\d{2,5}|[A-Z]{2}\ \_\d{2,5})')
ADDRESS['Floor_no']=ADDRESS['Source Address'].str.extract('([A-Z]+\:\w{5})')
ADDRESS['LANDMARK']=ADDRESS['Source Address'].str.extract('(\-\w+\w+)')
ADDRESS['Village']=ADDRESS['Source Address'].str.extract('(w*\_\ \w{5,8})')
#Could not Find a pattern for Area that can match for all addresses.
#ADDRESS['AREA']=ADDRESS['Source Address'].str.extract(pat='(\-\w+\ \w+)')
ADDRESS['CITY']=ADDRESS['Source Address'].str.extract('(\.\w{5})')
ADDRESS['Pincode']=ADDRESS['Source Address'].str.extract('(\d{6})')

import openpyxl
ADDRESS.to_excel (r'C:\\Users\\Dell\\Case_2.xlsx',header=True)



#Using NLP
document=ADDRESS['Source Address']
document=str(document)
#Some Information is lost,when converted to string.
def extract_House_no(string):
    House_no = ('(\w\_\d{2,5}\/\w|\_\w\ \_\d{2,5}|\w\_\d{2,5})')
    House_no = nltk.regexp_tokenize(document, House_no)
    return [re.sub(r'\D', '', number) for number in House_no]

def extract_Khasra_no(string):
    Khasra_no = ('([A-Z]{2}\_\d{2,5}|[A-Z]{2}\ \_\d{2,5})')
    Khasra_no = nltk.regexp_tokenize(document, Khasra_no)
    return [re.sub(r'\D', '', number) for number in Khasra_no]

def extract_Floor(string):
    Floor_no = ('([A-Z]+\:\w{5})')
    Floor_no = nltk.regexp_tokenize(document, Floor_no)
    return Floor_no

def extract_LandMark(string):
    Landmark = ('(\-\w+)')
    Landmark = nltk.regexp_tokenize(document, Landmark)
    return [re.sub(r'\W', '', number) for number in Landmark]

def extract_Village(string):
    Village = ('(w*\_\ \w{5,8})')
    Village = nltk.regexp_tokenize(document, Village)
    return [re.sub(r'\W','',number) for number in Village]

def extract_City(string):
    City = ('(\.\w{5})')
    City = nltk.regexp_tokenize(document, City)
    return [re.sub(r'\W','', number) for number in City]

def extract_Pincode(string):
    Pincode = ('(\d{6})')
    Pincode = nltk.regexp_tokenize(document, Pincode)
    return [re.sub(r'\D', '', number) for number in Pincode]

if __name__ == '__main__':
    house=extract_House_no(document)
    Khasra=extract_Khasra_no(document)
    Floor = extract_Floor(document)
    landmark= extract_LandMark(document)
    village = extract_Village(document)
    city = extract_City(document)
    pincode = extract_Pincode(document)
Sample_Data.py
Displaying Sample_Data.py. 