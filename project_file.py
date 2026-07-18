import polars as pl
employees=pl.read_csv("employees.csv")
# print(employees.head())
salaries=pl.read_csv("salaries.csv")
# print(salaries.head())
# print(employees.shape)
# print(salaries.shape)
df = employees.join(
    salaries,
    on="Employee_ID",
    how="inner"
)
#print(df)
df=df.with_columns((pl.col('Salary')+pl.col('Bonus')).alias('Total_Salary'))
#print(df)
df=df.with_columns(
    pl.when(pl.col("Total_Salary")>=100000)
    .then(pl.col('Total_Salary')*0.10)
    .otherwise(pl.col('Total_Salary')*0.05)
    .alias('Tax')
    )
#print(df)
df=df.with_columns((pl.col('Total_Salary')-pl.col('Tax')).alias('Net_Salary'))
#print(df)
df=df.with_columns(
    pl.when(pl.col('Salary')>=100000)
    .then(pl.lit('High'))
    .when(pl.col('Salary')>=70000)
    .then(pl.lit('Medium'))
    .otherwise(pl.lit('low'))
    .alias('Salary_Category')
)
#print(df)
df=df.sort("Net_Salary", descending=True)
print(df)
# df = df.select(
#     pl.col("Salary").max().alias('max_salary'),
#     pl.col("Salary").mean().alias('Avg_salary')
# )

# print(df)
df.write_csv('processed_employee.csv')

