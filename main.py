import requests
from time import sleep
from pystyle import *
import platform
import os

def clear_screen():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")

def get_input_from_console():
    token = Write.Input('Enter your token: ', Colors.red_to_black, interval=0.0000)
    recipients = Write.Input('Enter recipients (comma separated, 2 minimum): ', Colors.red_to_black, interval=0.0000).split(',')
    group_name = Write.Input('Enter group name: ', Colors.red_to_black, interval=0.0000)
    return token, recipients, group_name

def create_group(recipients, group_name, token):
    try:
        headers = {
            'Authorization': token,
        }
        data = {
            'recipients': recipients,
            'name': group_name,
        }
        response = requests.post('https://discord.com/api/v9/users/@me/channels', json=data, headers=headers)
        print(response.json())
    except Exception as error:
        handle_error(error)

def handle_error(error):
    print(f'Error creating group: {error}')
    if hasattr(error, 'response'):
        print(f'Status Code: {error.response.status_code}')
        print(f'Error Response: {error.response.text}')

def main():
    token, recipients, group_name = get_input_from_console()
    while True:
        create_group(recipients, group_name, token)
        sleep(5)

if __name__ == "__main__":
    main()