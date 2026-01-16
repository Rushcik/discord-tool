import os
import json
import colorama
from pystyle import Colorate, Colors
import subprocess
import webbrowser
import sys

rushcik_logo = """
░▒▓███████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓▒░    ▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓      ▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░   ▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░▒▓█▓▒░      ░▒▓█▓      ▒▓████████▓░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓      ▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██      ▒▓█▓▒░░▒▓█▓▒░ 
"""

interface = f"""{rushcik_logo}
                                ┏━━━━━━━━━━━━━━━━━━━━━┓
                                ┃Github :  rushcik    ┃
                                ┃Discord: .gg/rushcik┃
                                ┗━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━    Discord Tools    ━━━━┓   ┏━━━━    Osint Tools    ━━━━┓
┃   (01) Token   Information  ┃   ┃   (11) Coming Soon    ┃
┃   (02) Token   Checker      ┃   ┃   (12) Coming Soon    ┃
    (03) Token   Dmall                (13) Coming Soon
    (04) Token   Raid                 (14) Coming Soon 
    (05) Token   Name                 (15) Coming Soon
    (06) Token   Hypesquad            (16) Coming Soon
    (07) Token   Bio                  (17) Coming Soon                      
    (08) Webhook Info                 (18) Coming Soon                    
┃   (09) Webhook Spammer      ┃   ┃   (19) Coming Soon    ┃
┃   (10) Tool info            ┃   ┃   (20) Coming Soon    ┃
┗━━━━                    ━━━━┛   ┗━━━━                    ━━━━┛
"""

colored_ascii_art = Colorate.Horizontal(Colors.cyan_to_blue, interface)

def open_discord_invite():
    invite_url = "https://discord.gg/rushcik" 
    webbrowser.open(invite_url)

def check_requirements():
    utils_folder = './utils'
    config_file = os.path.join(utils_folder, 'config.json')

    if not os.path.isdir(utils_folder):
        return 

    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            try:
                config = json.load(f)
            except:
                pass

def main():
    colorama.init()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored_ascii_art)
        
        choice = input("\033[94m┌──(user@rushcik)-[~/Home]\n└─$> \033[0m")
        
        if choice.isdigit():
            num = int(choice)
            if num == 1:
                subprocess.run(['python', 'plugins/Discord/Tokeninfo.py'])
            elif num == 10:
                subprocess.run(['python', 'plugins/Discord/info.py'])
            elif 1 < num < 10 or 10 < num <= 20:
                print("\033[93mThis module is not yet implemented.\033[0m")
                input("Press Enter to continue...")
            else:
                print("\033[91mInvalid selection!\033[0m")
                input("Press Enter to continue...")
        else:
            if choice.lower() == 'exit':
                sys.exit()
            print("\033[91mPlease enter a valid number!\033[0m")
            input("Press Enter to continue...")

if __name__ == "__main__":
    open_discord_invite()
    main()