import unittest
import requests
from NBAI_dev_base_api import BaseApi

class TestGetTaskId(unittest.TestCase):
    path = "http://192.168.88.216:8080/orionboot"

    def setUp(self):
        self.base_api = BaseApi()
        self.token_id = self.base_api.get_token()
        self.order_id = self.base_api.get_order_id(self.token_id)
        self.wallet_id = self.base_api.get_wallet_address(self.token_id)
        print("Setup method execute")

    def test_get_task_id(self):
        end_point = self.path + "/orionPay"

        payload = {
            "orderId": self.order_id,
            "subtotal": "1234",
            "walletAddress": self.wallet_id,
            "ledgerIp": "192.168.88.152:8080",
            "paymentType": 5
        }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.token_id,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url=end_point, json=payload, headers=headers)
        task_id = response.json()['taskId']

        print('TaskID ', task_id)

        return task_id

    def tearDown(self):
        print("TearDown method execute")


if __name__ == '__main__':
    unittest.main()
