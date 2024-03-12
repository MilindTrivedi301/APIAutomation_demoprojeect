from Methods.loginPage import loginPage
import requests

class TestLogin(loginPage):
    def test_login_api_with_correct_cred(self):

        flag = self.check_login_api_with_correct_cred()
        # print(r.status_code)
        #status_code = r.status_code
        #print(r.json())
        assert flag is True

    def test_login_api_with_incorrect_pass(self):

        flag = self.test_login_api_with_incorrect_cred()
        #print(r.status_code)
        #status_code = r.status_code
        #print(r.json())
        assert flag is True