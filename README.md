# 📈 Stock Portfolio Analysis

A Python-based **Stock Portfolio Analysis and Management System** developed using **Object-Oriented Programming (OOP), Pandas, NumPy, and Matplotlib**.

This project manages stock information and transactions, performs portfolio calculations, cleans and analyzes CSV data, and creates different visualizations to understand investment performance.

---

## 🚀 Features

### 🔹 Object-Oriented Programming (OOP)

* Create and manage stock objects
* Display stock information
* Search stocks
* Update buy price
* Update current price
* Update stock quantity
* Remove stocks
* Calculate individual stock investment
* Calculate current portfolio value
* Calculate profit/loss
* Calculate return percentage
* Manage buy and sell transactions
* Search and remove transactions
* Calculate total buy and sell values

### 🔹 Pandas

* Read stock portfolio data from CSV
* Check missing values
* Detect duplicate records
* Remove duplicate records
* Handle missing sector values
* Fill missing numerical values using median
* Convert date columns into datetime format
* Create Investment column
* Create Current Value column
* Calculate Profit/Loss
* Calculate Return Percentage
* Save cleaned data into a new CSV file
* Perform sector-wise analysis using `groupby()`

### 🔹 NumPy

* Convert selected DataFrame columns into NumPy arrays
* Calculate total investment
* Calculate average investment
* Find highest and lowest investment
* Calculate total profit/loss
* Find average, highest, and lowest return
* Find stock with highest profit
* Find stock with lowest profit
* Find stock with highest return
* Find stock with lowest return

### 🔹 Matplotlib

The project creates different charts for portfolio analysis:

* Company vs Investment Bar Chart
* Company vs Current Value Bar Chart
* Company vs Profit/Loss Bar Chart
* Profit/Loss Histogram
* Investment vs Current Value Grouped Bar Chart
* Sector-wise Investment Bar Chart
* Sector-wise Profit/Loss Bar Chart
* Company vs Return Percentage Bar Chart
* Company-wise Investment Pie Chart
* Investment vs Current Value Scatter Plot
* Return Percentage Histogram

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **CSV**

---

## 📂 Project Structure

```text
Stock_Portfolio_Analysis/
│
├── Stock_Portfolio_Analysis.py
│
├── Stock_Portfolio_Analysis.csv
│
├── Stock_Portfolio_Analysis_Cleaned.csv
│
└── README.md
```

---

## 📊 CSV Dataset

The project uses a CSV file containing stock portfolio information.

### Main Columns

| Column        | Description                        |
| ------------- | ---------------------------------- |
| Stock_ID      | Unique stock identifier            |
| Company_Name  | Name of the company                |
| Sector        | Business sector                    |
| Buy_Price     | Price at which stock was purchased |
| Current_Price | Current price of the stock         |
| Quantity      | Number of shares                   |
| Date          | Date of purchase                   |

The dataset contains missing values and duplicate records so that data-cleaning techniques can be practiced.

---

## 💰 Portfolio Calculations

### Investment

```text
Investment = Buy Price × Quantity
```

### Current Value

```text
Current Value = Current Price × Quantity
```

### Profit/Loss

```text
Profit/Loss = Current Value − Investment
```

### Return Percentage

```text
Return % = (Profit/Loss ÷ Investment) × 100
```

---

## 🧱 OOP Classes

### `Stock`

Responsible for storing and managing individual stock information.

Main methods:

```text
display_stock()
update_quantity()
calculate_investment()
calculate_current_value()
calculate_profit_loss()
calculate_return()
```

### `Portfolio`

Responsible for managing multiple stock objects.

Main methods:

```text
add_stock()
remove_stock()
search_stock()
display_portfolio()
update_stock()
calculate_total_investment()
calculate_total_value()
calculate_total_profit_loss()
calculate_portfolio_return()
portfolio_summary()
```

### `Transaction`

Stores information about individual stock transactions.

Main methods:

```text
display_transaction()
calculate_transaction_value()
```

### `TransactionManager`

Responsible for managing multiple transactions.

Main methods:

```text
add_transaction()
remove_transaction()
search_transaction()
display_transactions()
calculate_total_buy()
calculate_total_sell()
```

---

## 📈 Data Analysis

After loading the CSV file, the project performs:

1. Missing value analysis
2. Duplicate value detection
3. Data cleaning
4. Financial calculations
5. Portfolio performance analysis
6. NumPy-based statistical analysis
7. Sector-wise analysis
8. Company-wise analysis
9. Data visualization

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project folder

```bash
cd Stock_Portfolio_Analysis
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib
```

### 4. Run the Python file

```bash
python Stock_Portfolio_Analysis.py
```

Make sure the CSV file is located in the same directory as the Python file.

---

## 🎯 Learning Objectives

This project was created to practice and combine multiple Python concepts in a single project.

Through this project, I practiced:

* Python classes and objects
* Constructors
* Instance attributes and methods
* Lists of objects
* Object management
* Basic financial calculations
* CSV data handling
* Pandas data cleaning
* Pandas grouping and aggregation
* NumPy array operations
* Matplotlib visualization
* Combining OOP with data analysis libraries

---

## 🔮 Future Improvements

Possible future improvements include:

* Add a menu-driven interface
* Connect OOP stock data with CSV data
* Add transaction history to the portfolio
* Add buy/sell functionality
* Add portfolio performance dashboard
* Add more advanced financial metrics
* Add interactive charts
* Add database support
* Add a GUI using Tkinter or another framework

---

## 👨‍💻 Author

**Ashutosh Adhikari**

BCA Student | Python Learner | Interested in AI/ML

---

## 📌 Note

This project is created for **learning and educational purposes**. The stock data used in the project is sample data and should not be considered financial advice.
