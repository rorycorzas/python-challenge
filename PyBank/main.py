
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
pl=[]
delta_pl=[]
i=0


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
        pl.append(int(each_line[1]))

        neto= neto + profit_losses
        
        if profit_losses>=0:
            profit.append(int(each_line[1]))

        else:
            loss.append(int(each_line[1]))        

        #print(f"Date: {each_line[0]}, Profit/Losses: {each_line[1]} units")
        #print(f"Date: {date}, Profit/Losses: {profit_losses} units")

months=int(len(date))
gp=max(profit)


for i in range(months-1):
        delta_pl.append(pl[i+1]-pl[i])

avr_change=round(mean(delta_pl),2)


#print(gp.index)


print(f"\nFinancial Analysis") 
print(f"---------------------------------------------------")
print(f"\nTotal Months: {months}") 
print(f"\nTotal: ${neto}") 
print(f"\nAverage Change: ${avr_change}")
