import pandas as pd
import csv
import numpy

# 1.Create an output file "filteredCountry.csv" inside a folder named "output". 
# This file should contain only those records where country contains the word USA.


file_obj = open('input/main.csv')    
#read csv file

data = pd.read_csv(file_obj)
#convert it into pandas dataframe

data['COUNTRY']=data.COUNTRY.str[0:3]
# from column country,extracting first three string indeces to get "usa"

data = data[data.COUNTRY == 'USA' ]
# getting a dataframe that has country as "USA"

data['PRICE']=data.PRICE.str[1:]
data['PRICE'] = data['PRICE'].str.replace('?', '')
data['PRICE'] = data['PRICE'].str.replace(',', '')
data['PRICE'] = pd.to_numeric(data['PRICE'])
# from price column removing the "$" sign and removing "," and converting the column to numeric from string 



csv_data = data.to_csv('output/filteredCountry.csv', index = True) 
# to save file in folder output with name "filteredcountry" in csv format

##################################################################################################


# 1.	Now consider "filteredCountry.csv" as the input file.
#  For each group of "SKU" find 2 minimum prices and store this result in "lowestPrice.csv" inside a folder named "output"


with open('output/filteredCountry.csv')as file_obj :
    file_data =  csv.DictReader(file_obj,skipinitialspace=True)
    file_list = list(file_data)

    d = {}
    for j in file_list:
        if j['SKU'] in d:
            d[j['SKU']].append(float(j['PRICE']))
        else :
            d[j['SKU']] = [float(j['PRICE'])]
# made a dictionary with sku as key list of price as value
# also converted the price in float value


lowest_price = {'SKU':[],'FIRST_MINIMUM_PRICE':[],'SECOND_MINIMUM_PRICE':[]}
for i in d:
    sort_price = numpy.array(d[i])
    sort_price.sort()
    if len(sort_price)>1 :
        lowest_price['SKU'].append(i)
        lowest_price['FIRST_MINIMUM_PRICE'].append(sort_price[0])
        lowest_price['SECOND_MINIMUM_PRICE'].append(sort_price[1])
df = pd.DataFrame(lowest_price, columns = ['SKU','FIRST_MINIMUM_PRICE','SECOND_MINIMUM_PRICE'])
# made a dictionary with sku , first minimum price and second minimum price based on sorted price list


csv_data = df.to_csv('output/lowest_price.csv', index = True) 
# saved it to lowest_price.csv in output folder













# file_obj = open('output/filteredCountry.csv')  
# #read csv file

# data = pd.read_csv(file_obj)
# #convert it into pandas dataframe


# new_data = data[['SKU','PRICE']].copy()

# df1 = new_data.groupby(["SKU"])
# df2= df1.apply(lambda x: x.sort_values(["PRICE"]))
# # df2=df2.reset_index(drop=True)
# print(df2["SKU"])















# lowest = data[['SKU']].copy()
# lowest['FIRST_MINIMUM_PRICE'] = 0
# lowest['SECOND_MINIMUM_PRICE'] = 0


# dict={}
# for i in range(len(data)):
#     # if i in dict:
#     #     dict[i].append(j)
#     # else:
#     #     dict[i] = []
    
#     print(data[i])

