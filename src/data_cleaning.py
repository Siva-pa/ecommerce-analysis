import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path, encoding='latin1')

    # Standardize columns
    df.columns = df.columns.str.lower().str.strip()

    # Drop missing
    df = df.dropna()

    # Convert date
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])

    # Feature engineering
    df['month'] = df['invoicedate'].dt.month
    df['year'] = df['invoicedate'].dt.year

    # Total amount
    df['total_amount'] = df['unitprice'] * df['quantity']

    return df


if __name__ == "__main__":
    df = clean_data("../data/ecommerce.csv")
    print(df.head())