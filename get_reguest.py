import requests
import configuration as conf

# def get_docs():
#     return requests.get(conf.BASE_URL + conf.DOC_PATH)
#
# response = get_docs()
#
# print("//DOCS запрос//")
# print(f'Статус код = {response.status_code}')
# print(f'Заголовки: {response.headers}')
# # print(f'Текст: {response.text}')
#
# def get_logs():
#     return requests.get(conf.BASE_URL + conf.LOGS_PATH,
#                          params={"count":20})
#
# response_logs = get_logs()
#
# print("//LOGS запрос//")
# print(f'Статус код = {response_logs.status_code}')
# print(f'Заголовки: {response_logs.headers}')
# print(f'Текст = {response_logs.text}')

def get_users_table():
    return requests.get(conf.BASE_URL + conf.USER_TABLE)

response_user = get_users_table()

print(f'Статус код = {response_user.status_code}')
print(response_user.text)
