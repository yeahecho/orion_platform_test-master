import unittest
import requests
from NBAI_dev_base_api import BaseApi


class TestGetOderId(unittest.TestCase):
    path = "http://192.168.88.216:8080/orionboot"

    def setUp(self):
        self.base_api = BaseApi()
        self.token_id = self.base_api.get_token()

        print("Setup method execute")
    def test_get_order_id(self):
        end_point = self.path + "/orders/create"

        payload = {
            "order": {"lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                      "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                          "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                          "zip": "H3A",
                                          "phone": 5141231234, "firstName": "Ting", "lastName": "Yu", "note": "note",
                                          "isDefault": False}}, "shopId": 403}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.token_id,
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url=end_point, json=payload, headers=headers)
        order_id = response.json()['order']['id']

        print('$$$$$$$')
        print('OrderID ', order_id)
        return order_id

    def tearDown(self):
        print("TearDown method execute")


if __name__ == '__main__':
    unittest.main()
