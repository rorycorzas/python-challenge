
import os
import csv
from statistics import mean 

file=("budget_data.csv")
budget_csv = os.path.join("", "Resources",file)

# Definicion Variables, gp= great profit, gl= great loss

neto =0
gp =0
gl =0
date=[]
profit=[]
loss=[]
pl = []
i=1


# Abre el archivo CSV
with open(budget_csv, newline='') as file:
    # Crea un lector CSV
    csv_reader = csv.reader(file)

    # Omitir la fila de encabezado
    next(csv_reader, None)

    # Lee las filas restantes y encuentra las filas Date, Profit/Losses
    for each_line in csv_reader:
        date.append(each_line[0])
        profit_losses=int(each_line[1])
        pl.append(each_line[1])
        neto= neto + profit_losses
        
        if profit_losses>=0:
            profit.append(int(each_line[1]))
        else:
            loss.append(int(each_line[1]))        
        
        #print(f"Date: {each_line[0]}, Profit/Losses: {each_line[1]} units")
        #print(f"Date: {date}, Profit/Losses: {profit_losses} units")

#avr=mean(pl)
months=int(len(date))

#print(avr)
print(f"\nTotal Months: {months}") 
print(f"\nTotal: ${neto}\n") 



        #date_ls= string.split(separator, maxsplit)    

        #print(f"Date: {date}, Profit/Losses: {profit_losses} units")


#string.split(-,)      

'''st_date = datetime.datetime(2018,9,16)
end_date = datetime.datetime(2020,3,24)
months = (end_date.year - st_date.year) * 12 + (end_date.month - st_date.month)
print('The difference in months is: ',months)'''
