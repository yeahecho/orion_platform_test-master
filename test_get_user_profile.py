import unittest
import requests
from NBAI_dev_base_api import BaseApi

class TestGetWalletId(unittest.TestCase):
    path = "http://192.168.88.216:8080/orionboot"

    def setUp(self):
        self.base_api = BaseApi()
        self.token_id = self.base_api.get_token()

        print("Setup method execute")

    def test_get_wallet_address(self):
        end_point = self.path + "/userProfile"

        payload = "{\"order\":{\"lineItemInOrderList\":[{\"product\":{\"id\":1},\"quantity\":2,\"ledgerLineItemOrder\":{\"id\":1}}],\"shippingAddress\":{\"province\":{\"code\":\"QC\"},\"country\":{\"code\":\"CA\"},\"address1\":\"1625 Maisonneuve\",\"address2\":\"\",\"city\":\"Montreal\",\"zip\":\"H3A\",\"phone\":5141231234,\"firstName\":\"Ting\",\"lastName\":\"Yu\",\"note\":\"note\",\"isDefault\":false}},\"shopId\":403} "
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.token_id,
            'cache-control': "no-cache"
        }

        response = requests.request("GET", end_point, data=payload, headers=headers)

        wallet_id = response.json()

        wallet_id = wallet_id['account'][0]['wallet_address_lists'][0]['wallet_address']

        print('WalletID ', wallet_id)

        return wallet_id

    def tearDown(self):
        print("TearDown method execute")

if __name__ == '__main__':
    unittest.main()
