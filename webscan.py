import requests
from bs4 import BeautifulSoup

def main():
    print("""

 █     █░▓█████  ▄▄▄▄     ██████  ▄████▄   ▄▄▄       ███▄    █ 
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀    ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
░░██▒██▓ ░▒████▒░▓█  ▀█▓▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
  ▒ ░ ░   ░ ░  ░▒░▒   ░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
  ░   ░     ░    ░    ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
    ░       ░  ░ ░            ░  ░ ░            ░  ░         ░ 
                      ░          ░                             
                                               by schizophrenic
          """)
    
    url = input("Veuillez entrer l'url d'un site: ")
    website = requests.get(f"{url}/sitemap.xml")
    soup = BeautifulSoup(website.content, "xml")
    loc = soup.find_all("loc")
    i = 0
    if loc:
        for num in loc:
            results = soup.find_all("loc")[i].text.strip()
            print(f"[{i}] {results}")
            i += 1
    else:
        print("Aucun liens trouvés")
main()