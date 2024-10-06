import pandas as pd

class ProductDataProcessor:
    @staticmethod
    def get_latest_sales_rank(sales_ranks):
        if sales_ranks and isinstance(sales_ranks, dict):
            for category_id, ranks in sales_ranks.items():
                if ranks:  
                    return ranks[-1]  
        return 'N/A'
   
    @staticmethod
    def get_buy_box_current_price(product):
        if product and isinstance(product, dict):
            suggested_price = product.get('suggestedLowerPrice')
            if suggested_price is not None:
                return suggested_price / 100  # Convert cents to dollars
        return 'N/A'
   
    @staticmethod
    def get_total_fba_stock(live_offers):
        total_stock = 0
        if live_offers and isinstance(live_offers, list):
            for offer in live_offers:
                if isinstance(offer, dict):
                    # Safely get stock, default to 0 if missing
                    total_stock += offer.get('stock', 0)  
        return total_stock
   
    @staticmethod
    def get_field_safe(product, field_name, default='N/A'):
        if product and isinstance(product, dict):
            # Safely get the field value
            return product.get(field_name, default)  
        return default
   
    @staticmethod
    def parse_product_data(product_data):
        if not isinstance(product_data, list):  
            # Ensure product_data is a list
            raise ValueError("Expected a list for product_data.")
       
        products = []
        for product in product_data:
            # Check if product is a valid dictionary
            if not isinstance(product, dict):  
                # Skip invalid product entries
                continue  
           
            buy_box_price = ProductDataProcessor.get_buy_box_current_price(product)

            # Get historic FBA sellers
        
            historic_fba_sellers = product.get('buyBoxSellerIdHistory', [])
            if isinstance(historic_fba_sellers, list):
                # Process the list only if it's valid
                historic_fba_sellers = [sellerId for i, sellerId in enumerate(historic_fba_sellers) if i % 2 != 0]
                # If the list ends up being empty after filtering, set it to 'N/A'
                if not historic_fba_sellers:
                    historic_fba_sellers = 'N/A'
            else:
                historic_fba_sellers = 'N/A'
           
            # Get live FBA sellers count
            live_fba_sellers_list = product.get('liveOffersOrder', [])
            if isinstance(live_fba_sellers_list, list):
                # Count the number of live sellers
                current_live_fba_sellers = len(live_fba_sellers_list)  
            else:
                current_live_fba_sellers = 'N/A'
           
            # Use an empty list if 'offers' is None or not a list
            offers = product.get('offers', []) if product and isinstance(product, dict) else []
            total_fba_stock = ProductDataProcessor.get_total_fba_stock(offers)
           
            fba_fees = product.get('fbaFees', {})
            pick_and_pack_fee = fba_fees.get('pickAndPackFee', 'N/A') if fba_fees else 'N/A'

            products.append({
                'ASIN': product.get('asin', 'N/A'),
                'Image': product.get('imagesCSV', 'N/A'),
                'Title': product.get('title', 'N/A'),
                'Weight grams': product.get('packageWeight', 'N/A'),
                'Buy Box Current': buy_box_price,
                'Sales Rank: Most Recent': ProductDataProcessor.get_latest_sales_rank(product.get('salesRanks', {})),
                'Historic FBA sellers': historic_fba_sellers,
                'Referral fee %': product.get('referralFeePercentage', 'N/A'),
                '#FBA Sellers Live': current_live_fba_sellers,
                'Saturation Score': ProductDataProcessor.get_field_safe(product, 'saturationScore'),
                'FBA fees': pick_and_pack_fee,
                'TOTAL FBA STOCK': total_fba_stock,
                'PURCHASABLE UNITS': ProductDataProcessor.get_field_safe(product, 'purchasableUnits'),
            })
       
        return products
   
    @staticmethod
    def save_to_excel(products, filename='../data/amazon_product_data.xlsx'):
        df = pd.DataFrame(products)
        df.to_excel(filename, index=False)