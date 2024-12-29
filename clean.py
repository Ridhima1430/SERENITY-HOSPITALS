import pandas as pd
import mysql.connector as ms

# Step 1: Load the data from the Excel file
file_path = '/mnt/data/healthcare_dataset.xlsx'
df = pd.read_excel(file_path)

# Step 2: Display the first few rows to understand the structure
print(df.head())

# Step 3: Data Cleaning

# 3.1 Handle Missing Values
df_cleaned = df.dropna()


# 3.2 Remove Duplicates
col=df_cleaned.columns
df_cleaned[df_cleaned.duplicated(subset=col,keep='first')]


# Step 4: Display the cleaned data

print(df_cleaned.head())
# Step 5: Connect to MySQL Database

conn = ms.connect(
    host='loacalhost',    
    user='root',
    password='root',
    database='healthcare_db' 
)

cursor = conn.cursor()

# Step 6: Create a new SQL table and load the cleaned data
df_cleaned.to_sql('healthcare_data', conn, if_exists='replace', index=False, 
                  method='multi')

# Step 7: Verify that the data has been loaded
cursor.execute("SHOW TABLES;")
print("Tables in the database:")
print(cursor.fetchall())

# Step 8: Display the first few rows from the SQL table
cursor.execute("SELECT * FROM healthcare_data;")
print("Data from SQL Table:")
print(cursor.fetchall())

# Step 9: Close the connection
conn.close()