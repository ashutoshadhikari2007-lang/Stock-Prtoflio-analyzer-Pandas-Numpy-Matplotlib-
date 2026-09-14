import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class stock:
    def __init__(self,stock_id,stock_name,sector,buy_price,current_price,quantity,buy_date):
        self.stock_id=stock_id
        self.stock_name=stock_name
        self.sector=sector
        self.buy_price=buy_price
        self.current_price=current_price
        self.quantity=quantity
        self.buy_date=buy_date

    def display_stock(self):
        print("The stock id is",self.stock_id)
        print("The name of stock is",self.stock_name)
        print("The sector of stock is",self.sector)
        print("The buying price of stock is",self.buy_price)
        print("The current price of stock is",self.current_price)
        print("THe quantity of share is",self.quantity)
        print("The date of buying is",self.buy_date)

    def update_quantity(self):
        new_quantity=float(input("Enter the quantity"))
        if new_quantity<=0:
            print("Invalid quanity entered")
        else:
            self.quantity=new_quantity
            print("Succesfully updated the quantity")

    def calculate_investment(self):
        total_investemnt=self.buy_price*self.quantity
        return total_investemnt
    
    def calculate_current_value(self):
        currrent_protfolio=self.current_price*self.quantity
        return currrent_protfolio
    
    def calculate_profit_loss(self):
        Investment=self.calculate_investment()
        currentprice=self.calculate_current_value()
        profit1=currentprice-Investment
        return profit1

    def calculate_return(self):
        x=self.calculate_profit_loss()
        Investment=self.calculate_investment()
        divide=(x/Investment)*100
        return divide

class Portfolio:
    def __init__(self, portfolio_name):
        self.portfolio_name = portfolio_name
        self.stocks = []
        self.stock_transactions = []

    def add_stock(self, stock):
        self.stocks.append(stock)
        print("Stock successfully added")

    def remove_stock(self):
        id=(input("Enter the stock id"))
        for x in self.stocks:
            if x.stock_id==id:
                self.stocks.remove(x)
                print("Successfully removed")
                return
        print("Not found")

    def search_stock(self):
        name=input("Enter the stock name")
        for x in self.stocks:
            if x.stock_name==name:
                x.display_stock()
                return
      
        print("Stock not found")

    def display_protfolio(self):
        if len(self.stocks)==0:
            print("Empty")
        else:
            for x in self.stocks:
                x.display_stock()

    def update_stock(self):
        id= (input("Enter the stock id"))
        for x in self.stocks:
            if x.stock_id==id:
                print("1. Update Buy Price")
                print("2. Update Current Price")
                print("3. Update Quantity")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_price = float(input("Enter new buy price: "))
                x.buy_price = new_price
                print("Buy price updated successfully")

            elif choice == 2:
                new_price = float(input("Enter new current price: "))
                x.current_price = new_price
                print("Current price updated successfully")

            elif choice == 3:
                x.update_quantity()

            else:
                print("Invalid choice")

            return

    print("Stock not found")

    def calculate_total_investment(self):
        total=0
        for x in self.stocks:
            total=total+(x.buy_price*x.quantity)
        return total

    def calculate_total_value(self):
        total=0
        for x in self.stocks:
            total=total+(x.current_price*x.quantity)
        return total

    def calculate_total_profit_loss(self):
        total_investment = self.calculate_total_investment()
        total_value = self.calculate_total_value()

        profit_loss = total_value - total_investment

        return profit_loss
    
    def calculate_portfolio_return(self):
        profit_loss = self.calculate_total_profit_loss()
        investment = self.calculate_total_investment()

        if investment == 0:
            return 0

        return (profit_loss / investment) * 100

    def portfolio_summary(self):
        total_investment = self.calculate_total_investment()
        total_value = self.calculate_total_value()
        profit_loss = self.calculate_total_profit_loss()
        portfolio_return = self.calculate_portfolio_return()

        print("----- Portfolio Summary -----")
        print("Portfolio Name:", self.portfolio_name)
        print("Total Investment:", total_investment)
        print("Current Portfolio Value:", total_value)
        print("Total Profit/Loss:", profit_loss)
        print("Portfolio Return:", portfolio_return, "%")

class transactions:
    def __init__(self,transactions_id,stock_id,transaction_type,quantity,price,date):
        self.transactions_id=transactions_id
        self.stock_id=stock_id
        self.transaction_type=transaction_type
        self.quantity=quantity
        self.price=price
        self.date=date

    def display_transaction(self):
        print("The transaction id is", self.transactions_id)
        print("The stock id is", self.stock_id)
        print("The transaction type is", self.transaction_type)
        print("The quantity is", self.quantity)
        print("The price is", self.price)
        print("The date is", self.date)

    def calculate_transaction_value(self):
        transaction_val=self.quantity*self.price
        return transaction_val

class TransactionManager:
    def __init__(self):
        self.transaction = []

    def add_transaction(self, transaction):
        self.transaction.append(transaction)
        print("Transaction successfully added")

    def remove_transactions(self):
        id=(input("Enter the transaction id"))
        for x in self.transaction:
            if x.transactions_id==id:
                self.transaction.remove(x)
                return
        print("Not found")

    def search_transactions(self):
        transaction_id = input("Enter the transaction id: ")

        for x in self.transaction:
            if x.transactions_id == transaction_id:
                x.display_transaction()
                return

        print("ID not found")

    def display_transactions(self):
        if len(self.transaction) == 0:
            print("No transactions available")
        else:
            for x in self.transaction:
                x.display_transaction()

    def calculate_total_buy(self):
        total_buy = 0

        for x in self.transaction:
            if x.transaction_type.upper() == "BUY":
                total_buy += x.quantity * x.price

        return total_buy

    def calculate_total_sell(self):
        total_sell = 0

        for x in self.transaction:
            if x.transaction_type.upper() == "SELL":
                total_sell += x.quantity * x.price

        return total_sell
# ================= OOP TESTING =================

portfolio1 = Portfolio("My Portfolio")

# Create stocks
stock1 = stock(
    "S001",
    "NABIL",
    "Banking",
    500,
    575,
    20,
    "2026-09-10"
)

stock2 = stock(
    "S002",
    "NTC",
    "Telecom",
    900,
    850,
    10,
    "2026-09-11"
)

stock3 = stock(
    "S003",
    "HIDCL",
    "Hydropower",
    300,
    350,
    15,
    "2026-09-12"
)

stock4 = stock(
    "S004",
    "CHCL",
    "Hydropower",
    550,
    500,
    8,
    "2026-09-12"
)

# Add stocks
portfolio1.add_stock(stock1)
portfolio1.add_stock(stock2)
portfolio1.add_stock(stock3)
portfolio1.add_stock(stock4)

# Display portfolio
print("\n----- Display Portfolio -----")
portfolio1.display_protfolio()

# Search stock
print("\n----- Search Stock -----")
portfolio1.search_stock()

# Update stock
print("\n----- Update Stock -----")
portfolio1.update_stock()

# Portfolio calculations
print("\n----- Portfolio Calculations -----")
print("Total Investment:", portfolio1.calculate_total_investment())
print("Total Current Value:", portfolio1.calculate_total_value())
print("Total Profit/Loss:", portfolio1.calculate_total_profit_loss())
print("Portfolio Return:", portfolio1.calculate_portfolio_return(), "%")

# Portfolio summary
print("\n----- Portfolio Summary -----")
portfolio1.portfolio_summary()

# Remove stock
print("\n----- Remove Stock -----")
portfolio1.remove_stock()

# Display after removing
print("\n----- Portfolio After Removal -----")
portfolio1.display_protfolio()


# ================= TRANSACTION TESTING =================

transaction_manager = TransactionManager()

transaction1 = transactions(
    "T001",
    "S001",
    "BUY",
    20,
    500,
    "2026-09-10"
)

transaction2 = transactions(
    "T002",
    "S002",
    "BUY",
    10,
    900,
    "2026-09-11"
)

transaction3 = transactions(
    "T003",
    "S003",
    "BUY",
    15,
    300,
    "2026-09-12"
)

transaction4 = transactions(
    "T004",
    "S004",
    "SELL",
    5,
    500,
    "2026-09-12"
)

# Add transactions
transaction_manager.add_transaction(transaction1)
transaction_manager.add_transaction(transaction2)
transaction_manager.add_transaction(transaction3)
transaction_manager.add_transaction(transaction4)

# Display transactions
print("\n----- Display Transactions -----")
transaction_manager.display_transactions()

# Search transaction
print("\n----- Search Transaction -----")
transaction_manager.search_transactions()

# Transaction calculations
print("\n----- Transaction Calculations -----")
print("Total Buy:", transaction_manager.calculate_total_buy())
print("Total Sell:", transaction_manager.calculate_total_sell())

# Remove transaction
print("\n----- Remove Transaction -----")
transaction_manager.remove_transactions()

# Display transactions after removal
print("\n----- Transactions After Removal -----")
transaction_manager.display_transactions()
#Pandas

df=pd.read_csv("Stock_Portfolio_Analysis.csv")
print("Missing values",df.isnull().sum())
print("Duplicated values",df.duplicated().sum())
print("Data types ",df.dtypes)
df=df.drop_duplicates()

df["Sector"]=df["Sector"].fillna("Unkown")
median_buy=df["Buy_Price"].median()
df["Buy_Price"]=df["Buy_Price"].fillna(median_buy)

median_current=df["Current_Price"]
df["Current_Price"]=df["Current_Price"].fillna(median_current)

median_quantity=df["Quantity"]
df["Quantity"]=df["Quantity"].fillna(median_quantity)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df["Investment"]=df["Buy_Price"]*df["Quantity"]
df["Current_Value"]=df["Current_Price"]*df["Quantity"]
df["Profit_Loss"]=df["Current_Value"]-df["Investment"]
df["Return_Percentage"]=(df["Profit_Loss"]/df["Investment"])*100

df["Investment"] = df["Investment"].fillna(0)
df["Current_Value"] = df["Current_Value"].fillna(0)
df["Profit_Loss"] = df["Profit_Loss"].fillna(0)
df["Return_Percentage"] = df["Return_Percentage"].fillna(0)

total_Investement=df["Investment"].sum()
print("Total investement is",total_Investement)

total_current_value=df["Current_Value"].sum()
print("Total current value is",total_current_value)

total_pf=total_current_value-total_Investement
if total_pf<0:
    print("loss")
else:
    print("Profit")

overall_return=(total_pf/total_Investement)*100
print("overall return",overall_return)

numeric_array=df[["Investment","Current_Value","Profit_Loss","Return_Percentage"]].to_numpy()

df.to_csv("Stock_Portfolio_Analysis.csv1",index=False)

print("Total Investemnt",np.nansum(numeric_array[:,0]))
print("Average Investemnt",np.nanmean(numeric_array[:,0]))
print("Highest Investemnt",np.nanmax(numeric_array[:,0]))
print("Lowest Investemnt",np.nanmin(numeric_array[:,0]))
print("Total profit and loss",np.nansum(numeric_array[:,2]))
print("Avg return",np.nanmean(numeric_array[:,3]))
print("Heighst return",np.nanmax(numeric_array[:,3]))
print("Lowest return",np.nanmin(numeric_array[:,3]))

#numpy

print(df[["Company_Name", "Investment", "Current_Value", "Profit_Loss", "Return_Percentage"]])
h_p = np.argmax(numeric_array[:, 2])
print("Highest profit stock is:", df["Company_Name"].iloc[h_p])

l_p = np.argmin(numeric_array[:, 2])
print("Lowest profit stock is:", df["Company_Name"].iloc[l_p])

h_r = np.argmax(numeric_array[:, 3])
print("Highest return stock is:", df["Company_Name"].iloc[h_r])

l_r = np.argmin(numeric_array[:, 3])
print("Lowest return stock is:", df["Company_Name"].iloc[l_r])

#matplotib
#Bar-graph
x=df["Company_Name"]
y=df["Investment"]
plt.barh(x,y)
plt.title("Company Vs Investment",font="Arial",size=20)
plt.xlabel("Comapny",font="Arial",size=20,color="Black")
plt.ylabel("Investment",font="Arial",size=20,color="Black")
plt.show()

#bar-graph2
x = df["Company_Name"]
y = df["Current_Value"]
plt.barh(x, y)
plt.title("Current Value vs Company Name", font="Arial", size=20)
plt.xlabel("Current Value", font="Arial", size=20)
plt.ylabel("Company Name", font="Arial", size=15)
plt.show()

x=df["Company_Name"]
y=df["Profit_Loss"]
plt.barh(x,y)
plt.title("Profit loss vs Company Name", font="Arial", size=20)
plt.xlabel("Company", font="Arial", size=20)
plt.ylabel("Profit Loss", font="Arial", size=15)
plt.show()

x=df["Company_Name"]
y=df["Investment"]
plt.barh(x,y)
plt.title("Company Name VS Investment", font="Arial", size=20)
plt.xlabel("Investment", font="Arial", size=20)
plt.ylabel("Company Name", font="Arial", size=15)
plt.show()

x=df["Profit_Loss"]
plt.title("Profit and Loss histrogram")
plt.hist(x)
plt.show()

x = np.arange(len(df["Company_Name"]))
width = 0.35
plt.bar(x - width/2, df["Investment"], width, label="Investment")
plt.bar(x + width/2, df["Current_Value"], width, label="Current Value")
plt.xticks(x, df["Company_Name"])
plt.title("Investment vs Current Value")
plt.xlabel("Company Name")
plt.ylabel("Amount")
plt.legend()
plt.show()

Investment=df.groupby("Sector")["Investment"].sum()
x=Investment.index
y=Investment.values
plt.bar(x,y)
plt.title("Sector-Wise Investment",font="Arial", size=20)
plt.xlabel("Sector",font="Arial", size=20)
plt.ylabel("Investment",font="Arial", size=20)
plt.show()

p_f=df.groupby("Sector")["Profit_Loss"].sum()
x=p_f.index
y=p_f.values
plt.title("Sector-Wise Profit and Loss",font="Arial", size=20)
plt.xlabel("Sector",font="Arial", size=20)
plt.ylabel("Profit and Loss",font="Arial", size=20)
plt.bar(x,y)
plt.show()

x=df["Company_Name"]
y=df["Return_Percentage"]
plt.barh(x,y)
plt.title("Company and Return_Percentage",font="Arial", size=20)
plt.xlabel("Company",font="Arial", size=20)
plt.ylabel("Return Percentage",font="Arial", size=20)
plt.show()

pro=df.groupby("Company_Name")["Investment"].sum()
x=pro.index
y=pro.values
plt.pie(y,labels=x,autopct="%1.1f%%")
plt.title("Company and Investment",font="Arial", size=20)
plt.legend()
plt.show()

x=df["Investment"]
y=df["Current_Value"]
plt.scatter(x,y)
plt.title("Investment vs current value",font="Arial", size=20)
plt.xlabel("Investment",font="Arial", size=20)
plt.ylabel("Current value",font="Arial", size=20)
plt.show()

x = df["Return_Percentage"]
plt.hist(x)
plt.title("Return Percentage Histogram", font="Arial", size=20)
plt.xlabel("Return Percentage", font="Arial", size=20)
plt.ylabel("Number of Stocks", font="Arial", size=20)
plt.show()

