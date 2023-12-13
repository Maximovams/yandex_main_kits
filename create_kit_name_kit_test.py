import sender_stand_request
import data


def get_new_user_token():
    user_body = data.user_body
    response_user = sender_stand_request.post_new_user(user_body)
    return response_user.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]



def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

def negative_assert_code_400(kit_body):
    resp = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp.status_code == 400


def test_create_client_kit_name_1_letter_get_success_response():
    positive_assert("а")


def test_create_client_kit_name_511_letter_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    negative_assert(kit_body)

def test_create_client_kit_name_empty_get_error_response():
    kit_body = get_kit_body("")
    negative_assert(kit_body)


def test_create_client_kit_name_512_letter_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)


def test_create_client_kit_name_english_letter_get_success_response():
    positive_assert("QWErty")


def test_create_client_kit_name_russian_letter_get_success_response():
    positive_assert("Мария")


def test_create_client_kit_name_special_simbol_get_success_response():
    positive_assert('"№%@",')


def test_create_client_kit_name_has_space_get_success_response():
    positive_assert("Человек и КО")


def test_create_client_kit_name_has_numbers_get_success_response():
    positive_assert("123")


def test_create_client_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)


def test_create_client_kit_name_number_type_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)