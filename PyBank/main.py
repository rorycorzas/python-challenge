
import os
import csv
from statistics import mean 


file=("budget_data.csv")
budget_csv = os.path.join("", "Resources",file)

# Definicion Variables

neto =0
gp =0
gl =0
date=[]
profit=[]
loss=[]
pl=[]
delta_pl=[]
i=0
prev_profit = None
change_total = 0
max_inc_value = -999999
min_inc_value = 999999
current_change = 0

# Abre el archivo CSV
with open(budget_csv, newline='') as file:
    # Crea un lector CSV
    csv_reader = csv.reader(file)

    # Omitir la fila de encabezado
    next(csv_reader, None)

    # Lee las filas restantes y encuentra las filas Date, Profit/Losses
    for each_line in csv_reader:
        date.append(each_line[0])
        current_month = each_line[0]
        profit_losses=int(each_line[1])
        pl.append(int(each_line[1]))

        neto= neto + profit_losses
        
        if prev_profit is not None:
            current_change = profit_losses - prev_profit        
            change_total += current_change        
          
            if current_change > max_inc_value:
                max_inc_month = current_month               
                max_inc_value = current_change

            if current_change < min_inc_value:
                min_inc_month = current_month
                min_inc_value = current_change
        
        prev_profit = profit_losses

months = int(len(date))

for i in range(months-1):
        delta_pl.append(pl[i+1]-pl[i])
avr_change=round(mean(delta_pl),2)

print(f"\nFinancial Analysis") 
print(f"---------------------------------------------------")
print(f"\nTotal Months: {months}") 
print(f"\nTotal: ${neto}") 
print(f"\nAverage Change: ${avr_change}")
print(f"\n")
print("Greatest Increase in Profits:", max_inc_month, "${:,.2f}".format(max_inc_value))
print(f"\n")
print("Greatest Decrease in Profits:", min_inc_month, "|", "${:,.2f}".format(min_inc_value))