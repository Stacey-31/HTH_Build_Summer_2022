import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data19 = pandas.read_csv("Finding-an-Interesting-Dataset/Happiness_data_2019.csv")

csv_data21 = pandas.read_csv("Finding-an-Interesting-Dataset/Happiness_data_2021.csv")

print(csv_data19)
print(csv_data21)