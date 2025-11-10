import sys
import csv
import sqlite3
import os

class DatabaseMaker:
    def __init__(self, csv_file):
        self.csv_file = csv_file # filename, the only input for using the script
        self.table_name = os.path.splitext(os.path.basename(csv_file))[0]   #prepares name without extension

    def make_sql(self):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()

        with open(self.csv_file, encoding="utf8") as f:  
            reader = csv.reader(f, delimiter=';')        #read file is a local variable

            for i, row in enumerate(reader):
                if i == 0:          
                    
                    self.columns = row
                    columns_def = [f"{self.columns[0]} TEXT UNIQUE"]   # creates table with UNIQUE constraint on the first column (ID)
                    columns_def += [f"{c} TEXT" for c in self.columns[1:]] # defines the other columns

                    # preparing the CREATE command for SQLite
                    # will use defined column names
                    create_stmt = f"""     
                    CREATE TABLE IF NOT EXISTS {self.table_name} (
                        {', '.join(columns_def)}      
                    );
                    """
                    cursor.execute(create_stmt)

                    # preparing INSERT command for SQLite, it will be a method so that it works outside this block
                    placeholders = ", ".join(["?" for _ in self.columns])  # defines a string with correct number of SQLite '?' placeholders
                    self.insert_stmt = f"INSERT OR IGNORE INTO {self.table_name} ({', '.join(self.columns)}) VALUES ({placeholders})"
                else:
                    cursor.execute(self.insert_stmt, row) #creates all rows other than the first one

        connection.commit()
        connection.close()

    def count_albanian_cities(self):
        connection = sqlite3.connect('db.sqlite')   #connects to previously created database
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT COUNT(*) FROM {self.table_name} WHERE CountryCode=?",
            ('ALB',)
        )
        count = cursor.fetchone()[0]  #the count as a local variable from the previous line

        connection.close()
        return count     #this method gives count as output

if __name__ == "__main__":    #the non-module scenario

    csv_file = sys.argv[1]
    db = DatabaseMaker(csv_file)

    db.make_sql()
    print(f"How many cities in the database are from Albania? {db.count_albanian_cities()}.")
