import requests


class BaseApi(object):
    host = "http://192.168.88.216:8080/orionboot"

    def get_response(self, method, end_point, payload, headers, data_type):
        url = self.host + end_point

        if data_type == 'json':
            response = requests.request(method, url, json=payload, headers=headers)
        else:
            response = requests.request(method, url, data=payload, headers=headers)

        return response

    def get_token(self):
        end_point = "/get_access_token"
        payload = {
            "userName": "mikesiwer01@gmail.com",
            "password": "a123456"
        }
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",

        }

        response = self.get_response("POST", end_point, payload, headers, 'json')
        login_json = response.json()
        access_token = login_json['access_token']
        return access_token

    def get_order_id(self, token):
        endpoint = '/orders/create'
        payload = {
            "order": {"lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                      "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                          "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                          "zip": "H3A", "phone": 5141231234, "firstName": "Ting", "lastName": "Yu",
                                          "note": "note", "isDefault": False}}, "shopId": 403}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token,
            'cache-control': "no-cache",
        }
        response = self.get_response("POST", endpoint, payload, headers, 'json')
        result = response.json()
        order_id = result['order']['id']
        return order_id

    def get_wallet_address(self, access_token):
        # token = self.get_token()
        endpoint = "/userProfile"
        payload = {
            "order": {"lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                      "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                          "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                          "zip": "H3A", "phone": 5141231234, "firstName": "Ting", "lastName": "Yu",
                                          "note": "note", "isDefault": False}}, "shopId": 403}
        headers = {
            'Authorization': "Bearer " + access_token,
            'cache-control': "no-cache"
        }
        response = self.get_response("GET", endpoint, payload, headers, 'json')
        result = response.json()
        # print('###########')
        # print(result)
        # print('###########')
        account = result['account'][0]

        wallet = account['wallet_address_lists']
        # print('###########')
        # print(wallet)
        # print('###########')
        wallet_address = wallet[0]['wallet_address']

        return wallet_address

    # get the task id
    def get_task_id(self, access_token, order_id, wallet_address):
        endpoint = "/orionPay"

        # payload = "{\n\"orderId\":" + str(order_id) + ", \n\"subtotal\":\"12\",\n\"walletAddress\":\"" + wallet_address + "\",\n\"ledgerIp\":\"192.168.88.152:8080\"\n}"
        # payload = "{\n\"orderId\":" + str(order_id) + ", \n\"subtotal\":\"12\",\n\"paymentType\":\"1\",\n\"walletAddress\":\"" + wallet_address + "\",\n\"ledgerIp\":\"192.168.88.152:8080\"\n}"
        payload = {
            "orderId": order_id,
            "subtotal": "1234",
            "paymentType": 5,
            "walletAddress": wallet_address,
            "ledgerIp": "192.168.88.152:8080"
        }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + access_token,
            'cache-control': "no-cache"
        }
        response = self.get_response("POST", endpoint, payload, headers, 'json')
        result = response.json()

        task_id = result['taskId']
        print(task_id)
        return task_id
