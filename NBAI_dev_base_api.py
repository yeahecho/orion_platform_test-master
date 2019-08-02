import requests




class BaseApi(object):
    path = "http://192.168.88.216:8080/orionboot"


    def get_token(self):
        end_point = self.path + "/get_access_token"
        payload = {
            "userName": "mikesiwer01@gmail.com",
            "password": "a123456"
        }  # payload for json
        headers = {
            'Content-Type': "application/json",
        }

        response = requests.request("POST", end_point, json=payload, headers=headers)

        token_id = str(response.json()['access_token'])

        return token_id

    def get_order_id(self, token_id):

        end_point = self.path + "/orders/create"

        payload = {"order":{"lineItemInOrderList":[{"product":{"id":1},"quantity":2,"ledgerLineItemOrder":{"id":1}}],"shippingAddress":{"province":{"code":"QC"},"country":{"code":"CA"},"address1":"1625 Maisonneuve","address2":"","city":"Montreal","zip":"H3A","phone":5141231234,"firstName":"Ting","lastName":"Yu","note":"note","isDefault":False}},"shopId":403}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token_id,
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url=end_point, json=payload, headers=headers)

        order_id = response.json()['order']['id']

        print('$$$$$$$')
        print('OrderID ', order_id)

        return order_id

    def get_wallet_address(self, token_id):
        end_point = self.path + "/userProfile"

        payload = "{\"order\":{\"lineItemInOrderList\":[{\"product\":{\"id\":1},\"quantity\":2,\"ledgerLineItemOrder\":{\"id\":1}}],\"shippingAddress\":{\"province\":{\"code\":\"QC\"},\"country\":{\"code\":\"CA\"},\"address1\":\"1625 Maisonneuve\",\"address2\":\"\",\"city\":\"Montreal\",\"zip\":\"H3A\",\"phone\":5141231234,\"firstName\":\"Ting\",\"lastName\":\"Yu\",\"note\":\"note\",\"isDefault\":false}},\"shopId\":403} "
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token_id,
            'cache-control': "no-cache"
        }

        response = requests.request("GET", end_point, data=payload, headers=headers)

        wallet_id = response.json()

        wallet_id = wallet_id['account'][0]['wallet_address_lists'][0]['wallet_address']

        print('WalletID ', wallet_id)

        return wallet_id

    def get_task_id(self, token_id, wallet_id, order_id):
        end_point = self.path + "/orionPay"


        payload={
                "orderId": order_id,
                "subtotal":"1234",
                "walletAddress":wallet_id,
                "ledgerIp":"192.168.88.152:8080",
                "paymentType":5
                }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token_id,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url=end_point, json=payload, headers=headers)
        task_id = response.json()['taskId']

        print('TaskID ', task_id)

        return task_id


if __name__=='__main__':
    BaseApi()
