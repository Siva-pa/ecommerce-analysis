import sqlite3

def create_connection():
    return sqlite3.connect("ecommerce.db")


def load_data(df):
    conn = create_connection()
    df.to_sql("orders", conn, if_exists="replace", index=False)
    print("Data loaded into database")


if __name__ == "__main__":
    from data_cleaning import clean_data

    df = clean_data("../data/ecommerce.csv")
    load_data(df)