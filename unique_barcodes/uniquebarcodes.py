import pandas as pd

# Read the three spreadsheets into pandas dataframes
df1 = pd.read_csv("EMPprimers_purchase_Dec2022.xlsx-16S_515rcbc.csv")
df2 = pd.read_csv("515f_ITS_barcode_list_OCT2014_JWW.xlsx-ITS-Barcodes.csv")
df3 = pd.read_csv("EMPprimers_purchase_Dec2022.xlsx-ITS_kabir.csv")

# Extract unique barcodes from spreadsheet two
unique_barcodes_spreadsheet_two = set(df2["Barcode"])

# Extract barcodes from spreadsheets one and three
barcodes_spreadsheet_one = set(df1["Golay Barcode"])
barcodes_spreadsheet_three = set(df3["Golay Barcode"])

# Combine barcodes from spreadsheets one and three
combined_barcodes = barcodes_spreadsheet_one.union(barcodes_spreadsheet_three)

# Find barcodes unique to spreadsheet two
unique_to_spreadsheet_two = unique_barcodes_spreadsheet_two.difference(combined_barcodes)

# Filter the entire line corresponding to unique barcodes in spreadsheet two
unique_lines = df2[df2["Barcode"].isin(unique_to_spreadsheet_two)]

# Write the unique lines to a file
unique_lines.to_csv("unique_barcodes.csv", index=False)
