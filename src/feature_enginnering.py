import pandas as pd
import datetime as dt

def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates Recency, Frequency, and Monetary (RFM) features for each customer.

    Args:
        df (pd.DataFrame): Preprocessed transaction DataFrame with 'CustomerID',
                           'TransactionDate', and 'TransactionAmount'.

    Returns:
        pd.DataFrame: A DataFrame with CustomerID and RFM features.
    """
    # Set a snapshot date for recency calculation (e.g., one day after the last transaction)
    snapshot_date = df['TransactionDate'].max() + dt.timedelta(days=1)
    
    # Calculate Recency, Frequency, and Monetary values
    rfm_df = df.groupby('CustomerID').agg({
        'TransactionDate': lambda date: (snapshot_date - date.max()).days,
        'TransactionID': 'count',
        'TransactionAmount': 'sum'
    })
    
    # Rename the columns
    rfm_df.rename(columns={'TransactionDate': 'Recency',
                           'TransactionID': 'Frequency',
                           'TransactionAmount': 'MonetaryValue'}, inplace=True)
    
    print("RFM features calculated successfully.")
    return rfm_df

if __name__ == '__main__':
    # Example Usage
    # Create a sample dataframe for testing
    data = {
        'CustomerID': [1001, 1002, 1001, 1003, 1002, 1001],
        'TransactionID': [1, 2, 3, 4, 5, 6],
        'TransactionDate': ['2023-01-15', '2023-01-16', '2023-02-10', '2023-02-21', '2023-03-05', '2023-03-12'],
        'TransactionAmount': [1500, 250, 750, 500, 1200, 2200]
    }
    sample_df = pd.DataFrame(data)
    sample_df['TransactionDate'] = pd.to_datetime(sample_df['TransactionDate'])
    
    rfm_features = calculate_rfm(sample_df)
    
    print("\nCalculated RFM Features:")
    print(rfm_features)
