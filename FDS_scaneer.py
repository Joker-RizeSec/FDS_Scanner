from bs4 import BeautifulSoup
import requests
import os
import sys

class color():
	color1 = "\033[1;37m"
	color2 = "\033[30m"
	color3 = "\033[1;36m"
	end = "\033[1;m"
os.system("reset")
print(color.color1 + '''
			
			.########..####.########.########..######..########..######.
			.##.....##..##.......##..##.......##....##.##.......##....##
			.##.....##..##......##...##.......##.......##.......##......
			.########...##.....##....######....######..######...##......
			.##...##....##....##.....##.............##.##.......##......
			.##....##...##...##......##.......##....##.##.......##....##
			.##.....##.####.########.########..######..########..######.            
          	          				Codado por : Joker && Fyk1ll && SNM  
          	          	Fast Directory Scan		             
                                                   '''+color.end)
                                                   
  

url = raw_input(color.color1+"Digite a url do alvo: "+color.color2)
print(color.color3)
proxy = {'http': 'http://97.77.104.22:80'}

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

req = requests.get(url, headers=header)

html = req.text

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
cont = 0
for link in links:
    cont += 1
    print(color.color1+"====================== " +str(cont)+ " ======================"+color.end)
    print link.get('href')
print(color.color3+"====================== TERMINOU ======================"+color.end)
