import sys
import csv
import sqlite3
import os

class DatabaseMaker:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.table_name = os.path.splitext(os.path.basename(csv_file))[0]

    def make_sql(self):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()

        with open(self.csv_file, encoding="utf8") as f:
            reader = csv.reader(f, delimiter=';')

            for i, row in enumerate(reader):
                if i == 0:
                    # First row → column names
                    self.columns = [col.strip().strip('"') for col in row]

                    # Create table with UNIQUE constraint on the first column (ID)
                    columns_def = [f"{self.columns[0]} TEXT UNIQUE"]
                    columns_def += [f"{c} TEXT" for c in self.columns[1:]]

                    create_stmt = f"""
                    CREATE TABLE IF NOT EXISTS {self.table_name} (
                        {', '.join(columns_def)}
                    );
                    """
                    cursor.execute(create_stmt)

                    # Prepare insert statement with INSERT OR IGNORE
                    placeholders = ", ".join(["?" for _ in self.columns])
                    self.insert_stmt = f"INSERT OR IGNORE INTO {self.table_name} ({', '.join(self.columns)}) VALUES ({placeholders})"
                else:
                    # Clean each cell
                    cleaned_row = [value.strip().strip('"') for value in row]

                    # Skip rows that are empty or malformed
                    if len(cleaned_row) != len(self.columns):
                        continue
                    if all(cell == '' for cell in cleaned_row):
                        continue

                    cursor.execute(self.insert_stmt, cleaned_row)

        connection.commit()
        connection.close()

    def count_cities_by_country(self, country_code):
        """Return the number of cities for a given CountryCode"""
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT COUNT(*) FROM {self.table_name} WHERE CountryCode=?",
            (country_code,)
        )
        result = cursor.fetchone()[0]

        connection.close()
        return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python db.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    db = DatabaseMaker(csv_file)

    db.make_sql()
    # Count cities in Albania (ALB)
    count_alb = db.count_cities_by_country("ALB")
    print(f"How many cities in the database are from Albania? {count_alb}.")
