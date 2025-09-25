import unittest
import pandas as pd
import datetime as dt
from src.feature_engineering import calculate_rfm

class TestFeatureEngineering(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing RFM calculation."""
        data = {
            'CustomerID': [1001, 1002, 1001, 1003, 1002, 1001],
            'TransactionID': [1, 2, 3, 4, 5, 6],
            'TransactionDate': ['2023-03-12', '2023-01-16', '2023-02-10', '2023-02-21', '2023-03-05', '2023-01-15'],
            'TransactionAmount': [2200, 250, 750, 500, 1200, 1500]
        }
        self.df = pd.DataFrame(data)
        self.df['TransactionDate'] = pd.to_datetime(self.df['TransactionDate'])

    def test_calculate_rfm(self):
        """Test the RFM calculation logic."""
        rfm_result = calculate_rfm(self.df)
        
        # Expected values
        snapshot_date = self.df['TransactionDate'].max() + dt.timedelta(days=1)
        
        # Customer 1001
        recency_1001 = (snapshot_date - pd.to_datetime('2023-03-12')).days
        freq_1001 = 3
        monetary_1001 = 2200 + 750 + 1500
        
        # Check for customer 1001
        self.assertEqual(rfm_result.loc[1001]['Recency'], recency_1001)
        self.assertEqual(rfm_result.loc[1001]['Frequency'], freq_1001)
        self.assertEqual(rfm_result.loc[1001]['MonetaryValue'], monetary_1001)
        
        self.assertEqual(len(rfm_result), 3) # 3 unique customers

if __name__ == '__main__':
    unittest.main()
