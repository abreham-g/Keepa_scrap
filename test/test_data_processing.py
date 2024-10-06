
import unittest
from scripts.data_processing import ProductDataProcessor

class TestProductDataProcessor(unittest.TestCase):
    def test_parse_product_data(self):
        products = [
            {
                'asin': 'B0716LYWXG',
                'images': ['image_url'],
                'title': 'Sample Product',
                'weight': 500,
                'buyBoxSellerId': 'seller_id',
                'salesRankDrop': {'30_days': 10},
                'historicalFBASellers': 5,
                'fee': {'referralFeePercent': 15},
                'liveFBASellers': 3,
                'saturationScore': 75,
                'fbaFees': 10,
                'totalFBAStock': 20,
                'purchasableUnits': 5,
            }
        ]
        parsed = ProductDataProcessor.parse_product_data(products)
        self.assertEqual(parsed[0]['ASIN'], 'B0716LYWXG')
        self.assertEqual(parsed[0]['Weight grams'], 500)

if __name__ == '__main__':
    unittest.main()