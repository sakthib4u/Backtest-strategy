from lib2to3.pgen2.token import OP
import pandas as pd

inp_file = pd.read_csv("C:/Users/Yogeswaran/Desktop/historical_data.csv")

Open=[]
Close=[]
SellOrBuy=[]
ProfitOrLoss=[]
BoughtIndex=[]
# these two for refernces
sold = 0
bought=0

for i in range(len(inp_file)):
    openPrice = inp_file.loc[i,'Open']
    closePrice = inp_file.loc[i,'Close']
    percentage =  ((closePrice/openPrice)*100)
    if percentage > 100:
        if (percentage - 100) >= 0.5:
            Open.append(openPrice)
            Close.append(closePrice)
            SellOrBuy.append("Bought")
            ProfitOrLoss.append("")
            BoughtIndex.append(i)
            bought =bought+1 

for i in BoughtIndex:
    openPrice = inp_file.loc[i,'Open']
    closePrice = inp_file.loc[i,'Close']
    percentage =  ((closePrice/openPrice)*100)
    if percentage > 100 :
        if (percentage - 100) >= 2:
            print("Inside 1")
            cell = "+"+str(round(percentage-100,3)) + " Profit"
            ProfitOrLoss.append(cell)
            Open.append(openPrice)
            Close.append(closePrice)
            SellOrBuy.append("Sold")
            sold =sold+1
    else:
        if (100 - percentage) > 1:
            print("Inside 2")
            cell = "-"+str(round(100-percentage,3)) + " Loss"
            ProfitOrLoss.append(cell)
            Open.append(openPrice)
            Close.append(closePrice)
            SellOrBuy.append("Sold")
            sold =sold+1

dict={'OPEN':Open,'CLOSE':Close,'BUY/SELL':SellOrBuy ,'Profit / Loss':ProfitOrLoss}
DATA = pd.DataFrame(dict)
DATA.to_csv("C:/Users/Yogeswaran/Desktop/Output2.csv")
print(bought, sold)