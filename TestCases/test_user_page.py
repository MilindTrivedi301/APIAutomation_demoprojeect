import pytest

from Methods.UserPage import UserPageMethods


class TestUserPage(UserPageMethods):

    @pytest.mark.parametrize("page_number", [2, 7])
    @pytest.mark.UserPage
    def test_get_list_of_user_api(self, page_number):
        """USER PAGE: test get list of user API - Page No. - """
        self.parameterize_param = page_number
        status = self.check_list_of_user_api(page_number)
        assert status

    @pytest.mark.UserPage
    def test_create_new_user_api(self):
        """USER PAGE: test create new user API with incomplete data """
        status = self.check_create_new_user_with_incomplete_data_api()
        #assert status