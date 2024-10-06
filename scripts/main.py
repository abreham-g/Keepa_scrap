import os
import sys
sys.path.append(os.path.abspath(os.path.join('./scripts')))
import asyncio
from scrap_keepa import KeepaAPI
from data_processing import ProductDataProcessor

ASINS = [
    'B0716LYWXG', 'B073M2SKKQ', 'B0746G7SBF','B092MRC5Y9', 'B09WZDVY29', 'B08KHNGVCX',
    'B074MB4X97', 'B074MCDX59', 'B074MCMM89','B0CBKJVLFB', 'B0CGV6V47P', 'B01N5WN83Y',
    'B07953J7MC', 'B07K54FH2Y', 'B07MMZ5141','B0CFLQ95BL', 'B09B7XV6SY', 'B0CJ99HNZ7',
    'B07Q23GW7W', 'B07Z8HBC19', 'B083ZJ2964','B078VD5SVJ', 'B08THPKRMY', 'B07Z8H313L',
    'B084KQTQL8', 'B0851NR414', 'B08571NLQV','B09MNH2FTG', 'B0CLM7582R', 'B09W2Q6N78',
    'B08BNC4GL6', 'B08BNGRCJS', 'B08M6DJ925','B07SV3KST2', 'B08GQGF9D7', 'B007SBBJ2M',
    'B08N5F5X91', 'B08N5FQN62', 'B08PQ7GR1V','B07V2PBJBC', 'B0BBJH8F9V', 'B09C3NTQSP',
    'B08PS67BH6', 'B08QFS24H5', 'B0BTDD6Z24','B09VM4MD9G', 'B01ETNW7PY', 'B08PZ39F9Y',
    'B08J5NZ8RH', 'B0BK9NJJFH', 'B0CB1BGFX3','B07WJHVDFC', 'B000NIDR9K', 'B0C8JH7HTS',
    'B0CB1BFQCZ', 'B09Y2DFGVK', 'B095J4W4SJ','B09VH2TW3H', 'B074WH9LX8', 'B0CHS1KPT5',
    'B0CLM8GDCQ', 'B079CMQ362', 'B08GBYD7LN','B0CLM8TSB8', 'B09RN2F7BL', 'B07TT7XVVF',
    'B01GU06PFW', 'B0C243R7JY', 'B095J89LR4','B0B8ZMMP54', 'B0CJS2VYVQ', 'B08KHQ2T6G',
    'B08VHDJMBK', 'B07LB8S9LL', 'B00MR2K43W','B016DOIXB4', 'B00PQJ59GU', 'B0B4K9B9Q4',
    'B08BNPCD55', 'B0B8ZPGN7F', 'B00PM9R87W','B0968PW797', 'B0CHS34LVP', 'B00U2MZCGI',
    'B0BVMGYQJJ', 'B011KPL5BQ', 'B07QN8DJFK','B0BSFPTZWJ', 'B0763KR5DM', 'B09WCHJNK5',
    'B08KHP79L7', 'B0C9NKS78X', 'B0CJS1HRQY','B0CJS1VS6C', 'B0CCPCNLWF', 'B07GWYYXD3',
    'B0763KGZ9W', 'B095J8FYZP', 'B08MVMPLJQ','B09SZMQV11'
]

async def main():
    api_key = 'ftl9rmbprserlkqios5sv3md5bfrf5jpu2uahr7k6r854i78o56h939i2pcpv8r0'  
    keepa_api = KeepaAPI(api_key)
    try:
        product_data = keepa_api.featch_product_data(ASINS)
        if product_data:
            print("Type of product_data:", type(product_data))  
            print("Full response:", product_data)  
            
            if isinstance(product_data, list):
                print("Received a list of products. Length:", len(product_data))
                
                for index, product in enumerate(product_data):
                    if product is None:
                        print(f"Product at index {index} is None.")
                        # Skip None values
                        continue  
                    print(f"Product at index {index}: {product}")

                parsed_products = ProductDataProcessor.parse_product_data(product_data)
                ProductDataProcessor.save_to_excel(parsed_products)
                print("Data successfully fetched and saved to amazon_product_data.xlsx")
            else:
                print("Unexpected structure in the API response.")
        else:
            print("No data returned from the API.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
