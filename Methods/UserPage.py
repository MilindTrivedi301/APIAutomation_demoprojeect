import requests
from TestData import test_data
from Logs import log_file


class UserPageMethods:

    log = log_file.log_fuc()
    def check_list_of_user_api(self, page_number):
        """
        this method checks the status of get list of users API
        :param page_number
        :return status
        """
        flag = True
        try:
            self.log.info(f"API is: {test_data.user_page_create_user_url.format(page_number)}")
            r = requests.get(test_data.user_page_create_user_url.format(page_number))
            if r.status_code == 200:
                self.log.info(f"Status code of API is: {r.status_code}")
            else:
                self.log.error(f"Status code of API is: {r.status_code}, Expected Status code: 200")
                flag = False
            if r.json()['page'] == page_number:
                self.log.info(f"Response is correct")
            else:
                self.log.error(f"Response is not correct")
                self.log.error(f"Expected 'Page' value: {page_number}, Actual 'Page' value: {r.json()['page']}")
                flag = False
        except Exception as e:
            self.log.error(f"Exception {e} occurred")
            flag = False
        return flag

    def check_create_new_user_with_incomplete_data_api(self):
        """
        this method checks the status of create new user API with incomplete data
        :return: status
        """
        flag = True
        try:
            self.log.info(f"API is: {test_data.user_page_create_user_url}")
            self.log.info(f"Input Data is: {test_data.user_details_empty_job_field}")
            r = requests.post(test_data.user_page_create_user_url, data=test_data.user_details_empty_job_field)
            if r.status_code == 400:
                self.log.info(f"Status code of API is: {r.status_code}")
            else:
                self.log.error(f"Status code of API is: {r.status_code}, Expected Status code: 400")
                flag = False
        except Exception as e:
            flag = False
            self.log.error(f"Exception {e} occurred")
        return flag
