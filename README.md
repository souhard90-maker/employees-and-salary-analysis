# Employee Salary Analysis using Polars

## 📌 Project Overview

This project demonstrates how to perform employee salary analysis using the **Polars** DataFrame library in Python. It covers data loading, joining multiple datasets, creating new columns, conditional transformations, aggregations, and exporting processed data.

The project is designed as a beginner-to-intermediate Polars project and showcases common data analysis tasks performed in real-world applications.

---

## 🚀 Features

* Read CSV files using Polars
* Inspect datasets (`head`, `shape`, `columns`, `dtypes`, `describe`)
* Join multiple DataFrames
* Create calculated columns
* Apply conditional logic using `when().then().otherwise()`
* Perform aggregations
* Export processed results to CSV

---

## 📂 Project Structure

```text
employees-and-salary-analysis/
│
├── data/
│   ├── employees.csv
│   └── salaries.csv
│
├── output/
│   └── processed_employee.csv
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

### employees.csv

* Employee_ID
* Name
* Department
* Age
* Experience
* City

### salaries.csv

* Employee_ID
* Salary
* Bonus

---

## ⚙️ Operations Performed

### Data Loading

* Read CSV files
* Inspect dataset

### Data Transformation

* Joined datasets using `Employee_ID`
* Created `Total_Salary`
* Calculated `Tax`
* Calculated `Net_Salary`

### Conditional Columns

* Salary Category
* Experience Level

### Data Analysis

* Highest Salary
* Lowest Salary
* Average Salary
* Employee Count

### Export

* Save processed dataset as CSV

---

## 🛠 Technologies Used

* Python
* Polars

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/souhard90-maker/employees-and-salary-analysis.git
```

Move into the project directory

```bash
cd employees-and-salary-analysis
```

Install dependencies

```bash
pip install polars
```

Run the project

```bash
python main.py
```

---

## 📈 Concepts Covered

* DataFrames
* CSV Handling
* Joins
* Column Expressions
* Conditional Expressions
* Aggregations
* Exporting Data

---

## 🎯 Learning Outcome

After completing this project, I gained hands-on experience with:

* Polars DataFrame operations
* Data cleaning and transformation
* Business calculations
* Aggregation and summarization
* Working with multiple datasets
* Writing efficient data analysis pipelines

---

## 📜 License

This project is created for learning and portfolio purposes.
