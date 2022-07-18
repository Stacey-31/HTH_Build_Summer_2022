import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data = pandas.read_csv("Finding-an-Interesting-Dataset/Happiness_data.csv")

print(csv_data)