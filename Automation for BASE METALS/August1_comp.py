import csv

def compare_csv_files(file1, file2):
    output = []

    # Read the CSV files and store the data as dictionaries with index as key
    data1 = {}
    data2 = {}

    # Read file1 and store data
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        header1 = next(reader1)
        for row in reader1:
            data1[row[1]] = row[2:]

    # Read file2 and store data
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        header2 = next(reader2)
        for row in reader2:
            data2[row[1]] = row[2:]

    # Compare the data from both files
    for index_value in data1.keys() & data2.keys():
        row1 = data1[index_value]
        row2 = data2[index_value]

        mismatch_values = []  # List to store mismatching values and their headers for the current row

        for i in range(len(row1)):
            value1 = row1[i].strip()
            value2 = row2[i].strip()

            if value1 == "" and value2 == "":
                continue  # Skip comparison if both values are blank

            if "%" in value1 and "%" in value2:
                value1_float = float(value1.rstrip("%"))
                value2_float = float(value2.rstrip("%"))

                if round(value1_float, 2) != round(value2_float, 2):
                    column_header = header1[i + 2]  # Fetch column header from header row of file1
                    mismatch_values.append((column_header, value1, value2))
            else:
                # Handle special case: if one value is blank and the other is 0 or 0.00%
                if (value1 == "" and (value2 == "0" or value2 == "0.00%")) or \
                   (value2 == "" and (value1 == "0" or value1 == "0.00%")):
                    continue  # Skip comparison

                if value1 != value2:
                    column_header = header1[i + 2]  # Fetch column header from header row of file1
                    mismatch_values.append((column_header, value1, value2))

        # If mismatching values are found, append the row to the output list
        if mismatch_values:
            output.append((index_value, mismatch_values))

    return output

def write_to_csv(output_file, comparison_result):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Index Value", "Column Header", "Source", "Target"])
        for index_value, mismatch_values in comparison_result:
            for column_header, value1, value2 in mismatch_values:
                writer.writerow([index_value, column_header, value1, value2])

# Usage example
file1_path = r"C:\Users\hthakur2\OneDrive - Teck Resources Limited\Documents\Automation for BASE METALS\Test_Source.csv"
file2_path = r"C:\Users\hthakur2\OneDrive - Teck Resources Limited\Documents\Automation for BASE METALS\Test_Target.csv"
output_file_path = "results_analysis_Aug.csv"

comparison_result = compare_csv_files(file1_path, file2_path)

if comparison_result:
    write_to_csv(output_file_path, comparison_result)
    print("Differences found. Results saved to 'results_analysis.csv'")
else:
    print("No differences found.")
