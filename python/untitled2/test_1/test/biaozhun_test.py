# !/usr/bin/puthon
# _*_coding:utf_8  _*_
from  test_1.test.biaozhun import Biao_zhun
from  test_1.confing.shuju_1 import  shuju
from  test_1.confing.baogao import Bao_gao
import  unittest
class  Biao(unittest.TestCase):
    ss = shuju()
    def test_1(self):
        aaa = Biao_zhun().Cha_mingxi(self.ss[0][0])
        print(aaa)
        self.assertEqual(aaa['errMsg'], '处理成功')

    def test_2(self):
        aaa = Biao_zhun().Cha_mingxi(self.ss[1][0])
        self.assertNotIn('处理成功', aaa)
if  __name__ == '__main__':
    #unittest.main()
    Bao_gao((Biao('test_1'),Biao('test_2')),report_path=r'C:\Users\hanwl\PycharmProjects\untitled2\test_1\report\aaa.html')












