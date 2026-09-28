import requests

import post_request as pr
import get_reguest as gr
import data as d

def get_user_body(first_name):
    current_body = d.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = pr.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = gr.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = pr.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                             "Имя может содержать только русские или латинские буквы, " \
                                             "длина должна быть не менее 2 и не более 15 символов"

def negative_assert_no_first_name(user_body):
    response = pr.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# 1
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# 2
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Ааааааааааааааа")

# 3
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# 4
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")

# 5
def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")

# 6
def test_create_user_russian_letter_in_first_name_get_success_response():
    positive_assert("Мария")

# 7
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("Человек и КО")

# 8
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")

# 9
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# 10
def test_create_user_no_first_name_get_error_response():
    user_body = d.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)

# 11
def test_create_user_empty_first_name_get_error_response():
    user_body = d.user_body.copy()
    user_body["firstName"] = ""
    negative_assert_no_first_name(user_body)

# 12
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = pr.post_new_user(user_body)

    assert response.status_code == 400