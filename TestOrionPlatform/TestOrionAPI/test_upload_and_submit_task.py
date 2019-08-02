import requests
import unittest
import os
from NBAI_dev_base_api import BaseApi


class TestUploadScript(unittest.TestCase):
    path = "http://192.168.88.216:8080"

    def setUp(self):
        self.base_api = BaseApi()
        self.get_token = self.base_api.get_token()
        self.get_orderid = self.base_api.get_order_id(self.get_token)
        self.get_walletid = self.base_api.get_wallet_address(self.get_token)
        self.get_taskid = self.base_api.get_task_id(self.get_token, self.get_walletid, self.get_orderid)
        self.url = "http://192.168.88.216:8080/orionboot/uploadScript"
        # self.task_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './FilesOfAPI'))
        self.task_file_path = 'FilesOfAPI/orion-word2vec-master.zip'
        self.task_name = "NUBIA999"
        print("Setup method execute")

    def test_1_get_upload_script(self):
        end_point = self.path + "/orionboot/uploadScript"
        headers = {
            'Authorization': "Bearer " + self.get_token,
        }
        order_id = self.get_orderid
        task_name = self.task_name
        ledgerIP = '192.168.88.152:8080'
        with open(self.task_file_path, 'rb') as body:
            response = requests.post(end_point,
                                     files={'data': body},
                                     headers=headers,
                                     params={'duration': int(3600),
                                             'taskName': task_name,
                                             'Id': order_id,
                                             'gpuCount': 1,
                                             'ledgerIp': ledgerIP,
                                             'taskId': self.get_taskid,
                                             'unitFee': str(5000000000000000)}
                                     )
            # print(response.text)
        self.assertEqual(200, response.status_code, "test failed")

    def tearDown(self):
        pass

    print("TearDown method execute")


if __name__ == '__main__':
    unittest.main()
