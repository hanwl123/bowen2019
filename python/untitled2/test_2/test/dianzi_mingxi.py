# import  sys
# sys.path.append(r'C:\Users\hanwl\PycharmProjects\untitled2\bbb.xlsx')
import requests
class  Ming_xi(object):
    def Cha_mingxi(self,sum):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderElectricInvoice"
        headers = {
        'Content-Type': "application/json",
        'x-dealer-code': "2100001",
        'x-position-code': "D_PO_1028",
        'x-resource-code': "pol4s_partOrder_orderElectricInvoice",
        'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
        'x-user-code': "dhxc1u",
        'x-access-token': "f488a55d0cb0327b8acd1bae4a3a587f",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "42d0a954-0975-40ae-b957-d4d2936a22b3,7d18cf7f-ef8b-4d80-9bd8-198550fcc307",
        'Host': "mobileqa.dms.saic-gm.com",
        'cookie': "dapp.sgm.com:qa:=d6a5abdb98fd2ee203a4ddcd7ae47d07; dapp.sgm.com:qa:=d6a5abdb98fd2ee203a4ddcd7ae47d07; a689baa2b7060531c4d0be5b10aa7055=a3a54f569b14d5196ef24d5b4b890058; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd",
        'accept-encoding': "gzip, deflate",
        'content-length': "37",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
        payload = "{\r\n \"orderNo\": \"%s\"\r\n}"%(sum)
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()
if __name__ == '__mian__':
   print(Ming_xi().Cha_mingxi('R2100005181116190'))

