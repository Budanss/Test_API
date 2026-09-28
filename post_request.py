import requests

import configuration as conf
import data as d

def post_new_user(body):
    return requests.post(conf.BASE_URL + conf.CREATE_USER_PATH,
                         json=body,
                         headers=d.headers)

response = post_new_user(d.user_body)

print(response.status_code)
print(response.json())

# def post_products_kits(products_ids):
#     return requests.post(conf.BASE_URL + conf.PRODUCTS_KITS_PATH,
#                          json=products_ids,
#                          headers=d.headers)
#
# response_prod_kits = post_products_kits(d.product_ids)
#
# print(response_prod_kits.status_code)
# print(response_prod_kits.json())
# print(response_prod_kits.url)

