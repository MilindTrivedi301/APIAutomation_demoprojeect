import logging

import requests
from TestData import test_data
from Logs import log_file

class loginPage:

    log = log_file.log_fuc()
    def check_login_api_with_correct_cred(self):
        flag = True
        try:
            r = requests.post('https://reqres.in/api/login', data=test_data.valid_credentials)
            # print(r.status_code)
            status_code = r.status_code
            #print(r.json())
            #assert status_code == 200
            #assert r.json()["token"]
            self.log.info(f"Status_code is {status_code}")
            if status_code != 200:
                self.log.error(f"Status_code is {status_code} not 200")
                flag = False
            else:
                self.log.info("Correct status code")
            if not r.json()["token"]:
                self.log.error(f"Token is not present")
                flag = False
            else:
                self.log.info(f"Token is present")
        except Exception as e:
            self.log.error("Exception occurred: {e}")
            flag = False
        return flag

    def test_login_api_with_incorrect_cred(self):
        flag = True
        r = requests.post('https://reqres.in/api/login', data=test_data.invalid_credentials)
        status_code = r.status_code
        print(status_code)
        if status_code != 400:
            flag = False
        return flag