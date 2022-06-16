import seldom
from seldom import file_data


class SampleTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://sit.rpasys.com/login")
        self.assertText('登录')
    def test_login(self):
        self.type(css='')


# class DDTTest(seldom.TestCase):
#
#     @file_data(file="data.json", key="bing")
#     def test_data_driver(self, _, keyword):
#         """ data driver case """
#         self.open("https://cn.bing.com")
#         self.type(id_="sb_form_q", text=keyword, enter=True)
#         self.assertInTitle(keyword)

if __name__ == '__main__':
    seldom.main(case=SampleTest.test_case,debug=True,browser='chrome')
