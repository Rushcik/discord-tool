import pystyle
from pystyle import Colors, Colorate

def afficher_informations():
    auteur = "!Anto"
    discord = "@rushcik"
    youtube = "https://www.youtube.com/rushcik"
    version = "1.0.0"
    tool    = "rushcik"

    info = f"""
    Auteur     : {auteur}
    Discord    : {discord}
    YouTube    : {youtube}
    Version    : {version}
    Tool       : {tool}
    Site       : Soon
    """

    print(Colorate.Horizontal(Colors.white_to_black, info))

if __name__ == "__main__":
    afficher_informations()

input("Enter to exit")
