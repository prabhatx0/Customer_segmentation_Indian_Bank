import pandas as pd
from typing import Optional

def load_data(filepath: str) -> Optional[pd.DataFrame]:
    """
    Loads transaction data from a CSV file.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        Optional[pd.DataFrame]: A pandas DataFrame with the transaction data,
                               or None if the file is not found.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the transaction DataFrame by handling missing values and duplicates.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Handle missing values
    if df.isnull().sum().any():
        print("Missing values found. Dropping rows with nulls.")
        df.dropna(inplace=True)

    # Remove duplicates
    if df.duplicated().any():
        print("Duplicate rows found. Removing duplicates.")
        df.drop_duplicates(inplace=True)

    print("Data cleaning complete.")
    return df

def preprocess_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the transaction data by converting data types.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    # Convert TransactionDate to datetime objects
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

    # Ensure CustomerID is of integer type
    df['CustomerID'] = df['CustomerID'].astype(int)

    # Ensure TransactionAmount is numeric
    df['TransactionAmount'] = pd.to_numeric(df['TransactionAmount'])
    
    print("Data preprocessing complete. Date and numeric conversions are done.")
    return df

if __name__ == '__main__':
    # Example usage
    data_path = '../data/transactions.csv'
    transactions_df = load_data(data_path)
    if transactions_df is not None:
        cleaned_df = clean_data(transactions_df)
        preprocessed_df = preprocess_transactions(cleaned_df)
        print("\nPreprocessed Data Head:")
        print(preprocessed_df.head())
        print("\nData Info:")
        preprocessed_df.info()
