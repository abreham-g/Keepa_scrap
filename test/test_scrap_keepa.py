
import unittest

from scripts.scrap_keepa import KeepaAPI

class TestKeepaAPI(unittest.TestCase):
    def setUp(self):
        self.api = KeepaAPI('ftl9rmbprserlkqios5sv3md5bfrf5jpu2uahr7k6r854i78o56h939i2pcpv8r0')  

    def test_fetch_product_data(self):
        asins = ['B0716LYWXG']  # Example ASIN
        result = self.api.fetch_product_data(asins)
        self.assertIn('products', result)

if __name__ == '__main__':
    unittest.main()