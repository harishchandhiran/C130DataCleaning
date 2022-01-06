#The code deleted incomplete data rows from data.csv 
#and copied the complete data rows to dataset.csv
import csv
import pandas as pd

data = []

with open("data.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

#Listing columns of the data
headers = data[0]

new_data = []

removed_data = []
distance_corrected = []
mass_corrected = []
#removing nan values of distance
for i in data:
    if(i[2]=="" or i[2]=="?"):
        removed_data.append(i)
    else:
        distance_corrected.append(i)

#removing nan values of mass
for i in distance_corrected:
    if(i[3]=="" or i[3]=="?"):
        removed_data.append(i)
    else:
        mass_corrected.append(i)

removed_data_2 = []
#removing nan values of radius
for i in mass_corrected:
    if(i[4]=="" or i[4]=="?"):
        removed_data_2.append(i)
    else:
        new_data.append(i)

with open("dataset.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(new_data)