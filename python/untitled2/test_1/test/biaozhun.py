# !/usr/bin/puthon
# _*_coding:utf_8  _*_
import  sys
sys.path.append(r'C:\Users\hanwl\PycharmProjects\untitled2\bbb.xlsx')
import  requests
class   Biao_zhun(object):
    def  Cha_mingxi(self,sum):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderStandardOngoingInfo"

        payload = "{\r\n \"orderNo\": \"%s\"\r\n}"%(sum)
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderStandardOngoingInfo",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "d6a5abdb98fd2ee203a4ddcd7ae47d07",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "3c8b8439-1e73-484b-aeb6-a9427e48a547,06eb5490-e526-4050-8af5-a4e23c6f20a1",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=3f07a82d5eae75dbc3d41da9224523b6; dapp.sgm.com:qa:=3f07a82d5eae75dbc3d41da9224523b6; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd",
            'accept-encoding': "gzip, deflate",
            'content-length': "37",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        return  response.json()
if __name__ == '__main__':
    print((Biao_zhun().Cha_mingxi('R2100005181116190')))















