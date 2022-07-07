import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data = pandas.read_csv("Finding-an-Interesting-Dataset/student_data.csv")

print(csv_data)