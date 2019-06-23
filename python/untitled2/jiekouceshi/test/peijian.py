# !/usr/bin/puthon
# _*_coding:utf_8  _*_



#配件查询


import requests
import  sys
sys.path.append(r'C:\Users\hanwl\PycharmProjects\untitled2\aaa.xlsx')
class    P_jian(object):
    def  Ming_xi(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail"

        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderPartDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "4393ebee1f6dee093dd01923d12d86ab",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "e49f7eed-a7c5-4e98-bafd-b01495ee8823,2056ff20-6f25-4947-bfb0-c6cb4f63e227",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=c909d3541a63a46b75f314a4e94828c0; dapp.sgm.com:qa:=c909d3541a63a46b75f314a4e94828c0; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd",
            'accept-encoding': "gzip, deflate",
            'content-length': "30",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        payload = "{\r\n \"partOrderItemId\": %s\r\n}" % (num)
        res = requests.post(url=url,headers=headers,data=payload)
        return res.json()
if __name__ == '__main__':
    print(P_jian().Ming_xi(1))