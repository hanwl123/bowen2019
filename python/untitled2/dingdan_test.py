# !/usr/bin/puthon
# _*_coding:utf_8  _*_
from  dingdan import  Ding_dan
from  duqu  import  shuju
import   unittest
class  D_dan(unittest.TestCase):
    ss = shuju()
    def   test_1(self):
        aaa = Ding_dan().Cha_mingxi(int(self.ss[0][0]))
        self.assertEqual(aaa['errMsg'],'处理成功')
    def   test_2(self):
        aaa = Ding_dan().Cha_mingxi(self.ss[1][0])
        self.assertNotIn('处理成功',aaa)


if  __name__ == '__main__':
    unittest.main()









