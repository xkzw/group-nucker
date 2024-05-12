import requests
from time import sleep
import platform
import os
from pystyle import *
from datetime import datetime, timedelta
import socket

hostname = socket.gethostname()

def clear_screen():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")

def main():
    try:
        clear_screen()
        Write.Print("""
 $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$\         $$$$$$\  $$$$$$$\   $$$$$$\  $$\      $$\ $$\      $$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |$$$\    $$$ |$$  _____|$$  __$$\ 
$$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |      $$ /  \__|$$ |  $$ |$$ /  $$ |$$$$\  $$$$ |$$$$\  $$$$ |$$ |      $$ |  $$ |
$$ |$$$$\ $$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$$  |      \$$$$$$\  $$$$$$$  |$$$$$$$$ |$$\$$\$$ $$ |$$\$$\$$ $$ |$$$$$\    $$$$$$$  |
$$ |\_$$ |$$  __$$< $$ |  $$ |$$ |  $$ |$$  ____/        \____$$\ $$  ____/ $$  __$$ |$$ \$$$  $$ |$$ \$$$  $$ |$$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |            $$\   $$ |$$ |      $$ |  $$ |$$ |\$  /$$ |$$ |\$  /$$ |$$ |      $$ |  $$ |
\$$$$$$  |$$ |  $$ | $$$$$$  |\$$$$$$  |$$ |            \$$$$$$  |$$ |      $$ |  $$ |$$ | \_/ $$ |$$ | \_/ $$ |$$$$$$$$\ $$ |  $$ |
 \______/ \__|  \__| \______/  \______/ \__|             \______/ \__|      \__|  \__|\__|     \__|\__|     \__|\________|\__|  \__|\n
""", Colors.red_to_black, interval=0.0000)
 
        Write.Print("                                                      Created by lv8\n                                          Follow my github: github.com/nosztalgia\n", Colors.red_to_black, interval=0.0001)

        Write.Print("[1] Group spammer\n[2] Infos\n\n", Colors.red_to_black, interval=0.000)

        selection = Write.Input("(" + "lv8" + "@" + hostname + ")-[~]$> ", Colors.red_to_black, interval=0.000)

        if selection == "1":
            create_group()
        elif selection == "2":
            infos()
        else:
            Write.Print("\nInvalid selection, press ENTER to go back to selection menu", Colors.red, interval=0.000)
            input()
            main()
    except Exception as e:
        Write.Print(f"\nAn error occurred: {e}\nPress ENTER to go back to menu", Colors.red, interval=0.000)
        input()
        main()

def infos():
    Write.Print("""
Welcome to this group spammer tool, this will create multiple groups in the account of your choice (every 5 seconds but you can modify the delay line 78)
Your token will be asked because this is considered as a selfbot.
I recommend to keep 5 seconds to prevent rate limit.""", Colors.red_to_black, interval=0.000)
    input()
    main()

def unauthorized(error_message):
    if "401: Unauthorized" in str(error_message):
        print(Colors.red, "Invalid token!")
    else:
        print(Colors.red, f"[ERROR] Error creating group: {error_message}")

def create_group():
    token = Write.Input("(" + "lv8" + "@" + hostname + ")-[~/group-spammer/your_token]$> ", Colors.red_to_black, interval=0.000)
    recipients_input = Write.Input("(" + "lv8" + "@" + hostname + ")-[~/group-spammer/recipients_id_comma_separed]$> ", Colors.red_to_black, interval=0.000)
    
    recipients = recipients_input.split(',')
    
    while True:
        try:
            headers = {
                'Authorization': token,
            }
            data = {
                'recipients': recipients,
            }
            response = requests.post('https://discord.com/api/v9/users/@me/channels', json=data, headers=headers)
            if response.status_code == 200:
                print(Colors.red_to_black, "[LOGS] Group created, next group in 5 seconds")
                for i in range(5, 0, -1):
                    print(Colors.red_to_black, f"[LOGS] Next group in {i - 1} seconds", end='\r')
                    sleep(1)
            else:
                print(Colors.red, f"[ERROR] Error creating group: {response.text}")
        except requests.exceptions.RequestException as e:
            handle_error(e)
        sleep(0)

def handle_error(error):
    print(f'Error creating group: {error}')
    input()
    if hasattr(error, 'response'):
        print(f'Status Code: {error.response.status_code}')
        print(f'Error Response: {error.response.text}')
        input()

main()
