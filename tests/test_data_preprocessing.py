import unittest
import pandas as pd
from src.data_preprocessing import load_data, clean_data, preprocess_transactions

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing."""
        data = {
            'CustomerID': [1001, 1002, 1001, None, 1002],
            'TransactionID': [1, 2, 1, 4, 5],
            'TransactionDate': ['2023-01-15', '2023-01-16', '2023-01-15', '2023-01-21', '2023-02-05'],
            'TransactionAmount': [1500.00, 250.50, 1500.00, 500.00, '1200.00']
        }
        self.df = pd.DataFrame(data)

    def test_clean_data(self):
        """Test the data cleaning function."""
        cleaned = clean_data(self.df.copy())
        # Should drop row with None and one duplicate row
        self.assertEqual(len(cleaned), 3)
        self.assertFalse(cleaned.isnull().values.any())
        self.assertFalse(cleaned.duplicated().values.any())

    def test_preprocess_transactions(self):
        """Test the data preprocessing function."""
        # First, clean the data to remove issues that would cause errors
        df_clean = self.df.dropna()
        df_clean = df_clean.drop_duplicates()

        preprocessed = preprocess_transactions(df_clean.copy())
        # Check data types
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(preprocessed['TransactionDate']))
        self.assertTrue(pd.api.types.is_integer_dtype(preprocessed['CustomerID']))
        self.assertTrue(pd.api.types.is_numeric_dtype(preprocessed['TransactionAmount']))

if __name__ == '__main__':
    unittest.main()
