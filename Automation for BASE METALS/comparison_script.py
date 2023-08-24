import csv
import pandas as pd

def compare_csv_files(file1, file2):
    output = []

    # Read the CSV files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)

        # Extract the header row in each file
        header1 = next(reader1)
        header2 = next(reader2)

        # Determine the range of columns to compare
        num_columns = min(len(header1), len(header2))
        compare_range = range(3, num_columns)

        # Iterate over rows in both files
        for row1, row2 in zip(reader1, reader2):
            # Extract the value in column C (index 2)
            value1 = row1[2]
            value2 = row2[2]

            # Compare the values in the determined range of columns
            for i in compare_range:
                try:
                    value1_col = round(float(row1[i]))
                    value2_col = round(float(row2[i]))

                    if value1_col != value2_col:
                        column_header = header1[i]  # Fetch column header from header row of file1
                        output.append((value1, value2, column_header, value1_col, value2_col))
                except ValueError:
                    # Handle cases where the value is not convertible to float
                    pass

    return output

# Usage example
file1_path = r"C:\Users\hthakur2\OneDrive - Teck Resources Limited\Documents\Automation for BASE METALS\AutoSource.csv"
file2_path = r"C:\Users\hthakur2\OneDrive - Teck Resources Limited\Documents\Automation for BASE METALS\AutoTarget.csv"

comparison_result = compare_csv_files(file1_path, file2_path)

if comparison_result:
    print("Differences found:")
    for row in comparison_result:
        column_header = row[2]  # Get the column header
        values = row[0:2] + (column_header,) + row[3:]
        print(values)
else:
    print("No differences found.")


# Create a DataFrame from the comparison result
df_comparison = pd.DataFrame(comparison_result, columns=['Owner Group- Source', 'Owner Group- Target', 'Column Header', 'SOURCE', 'TARGET'])

# Save the DataFrame to an Excel file
df_comparison.to_excel('comparison_result.xlsx', index=False)