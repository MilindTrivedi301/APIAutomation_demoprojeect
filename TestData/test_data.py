#from Helper import helper

#server = helper.get_server_value_from_parameter_file()

###########################LOGIN_PAGE################################################

#login_base_url = f'https://{server}/api/login'

valid_credentials = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

invalid_credentials = {
    "email": "peter@klaven"
}


###########################USER_PAGE################################################

#user_page_get_list_user_url = "https://"+server+"/api/users?page={}"
user_page_create_user_url = "https://reqres.in/api/users?page={}"
#user_page_create_user_url = f"https://{server}/api/users"

user_details_empty_job_field = {
    "name": "morpheus",
    "job": ""
}