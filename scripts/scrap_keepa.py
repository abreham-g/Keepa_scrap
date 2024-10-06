import keepa

class KeepaAPI:

    def __init__(self, api_key):
        self.api=keepa.Keepa(api_key)

    def featch_product_data(self,asins):
        """
        featch product data from the keepa API using the keepa library.
        """
        try:
            products = self.api.query(asins,offers=100, buybox=True)
            return products
        except Exception as e:
            raise Exception(f"Failed to featch product Data: {e}")

