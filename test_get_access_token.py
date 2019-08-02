
import unittest
import requests




class TestGetAccessToken(unittest.TestCase):


    def setUp(self):
        self.url = "http://192.168.88.216:8080/orionboot/get_access_token"
        self.valid_username = "mikesiwer01@gmail.com"
        self.valid_password = "a123456"
        print("Setup method execute")


    def test_get_access_token_with_valid_argument(self):
        headers = {'Content-Type': "application/json"}
        payload = {"userName": self.valid_username, "password": self.valid_password}

        response = requests.post(self.url, json=payload, headers=headers)
        test_result = response.json()["access_token"]
        print(test_result)
    def tearDown(self):
        print("TearDown method execute")





if __name__ == '__main__':
    unittest.main()

# os.system('py.test ComboAPITest/test_get_access_token.py --html=./TestReport/My_test_report.html')
    # py.test ComboAPITest/test_get_access_token.py --html=./TestReport/My_test_report.html
    # py.test sum.py - -html = name_of_html_file.html

