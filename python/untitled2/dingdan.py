# !/usr/bin/puthon
# _*_coding:utf_8  _*_

#所有的订单配置文件

from duqu  import  shuju
import  sys
sys.path.append(r'C:\Users\hanwl\PycharmProjects\untitled2\test_1\data\a.xlsx')
import  requests
class   Ding_dan(object):
    def  Cha_mingxi(self,sum):
         url ='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'
         header = {
             'Content-Type': "application/json",
    'x-dealer-code': "2100001",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrder_orderList",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "d6a5abdb98fd2ee203a4ddcd7ae47d07",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "385b4a94-5523-4098-a0bc-23b32e3c1aa2,5db9fc47-5fd5-437c-87f7-a9c5011691f4",
    'Host': "mobileqa.dms.saic-gm.com",
    'cookie': "dapp.sgm.com:qa:=a38cbf0109c94e03b38d9f405abdeae7; dapp.sgm.com:qa:=a38cbf0109c94e03b38d9f405abdeae7; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd",
    'accept-encoding': "gzip, deflate",
    'content-length': "194",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
         }
         payload = "{\r\n \"pageNum\": %s,\r\n \"pageSize\": 10,\r\n \"queryTerms\": {\r\n  \"orderType\": \"\",\r\n  \"orderStatus\": \"\",\r\n  \"orderDelayFlag\": \"\",\r\n  \"orderNo\": \"\",\r\n  \"startReportDate\": \"\",\r\n  \"endReportDate\": \"\"\r\n }\r\n}" %  (sum)
         res = requests.post(url=url,headers=header,data=payload)
         return res.json()
if __name__ == '__main__':
    print(Ding_dan().Cha_mingxi(1))
    # for   sum  in  shuju():
    #     Ding_dan().Cha_mingxi(1)













































































