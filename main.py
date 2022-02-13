from bs4 import BeautifulSoup
import requests

chatId = '1046931046'
tokenBot = '5273819559:AAF9caGBe-Cl5sqvgZH7D18vIx0T7RW16gk'

jobsList = []
first = True

def send_msg(text, parse_mode='HTML'):
    requests.post(f"https://api.telegram.org/bot{tokenBot}/sendMessage?chat_id={chatId}&text={text}&parse_mode={parse_mode}&disable_web_page_preview=true")

while True:
    kwork = requests.get('https://kwork.ru/projects?c=41')
    bsUse = BeautifulSoup(kwork.text, 'html.parser')
    blocks = bsUse.find_all('div', class_='card')
    for block in blocks:
        infoBlock = BeautifulSoup(str(block), 'html.parser')

        kwork = infoBlock.find_all('div', class_='wants-card__header-title')[0]
        kworkGetLink = BeautifulSoup(str(kwork), 'html.parser')
        kworkLink = kworkGetLink.find('a').attrs['href']

        price = infoBlock.find_all('div', class_='wants-card__header-price')[0]
        workInfo = infoBlock.find_all('div', class_='breakwords')[0]

        author = infoBlock.find_all('a', class_='v-align-t')[0]
        authorLink = author.attrs['href']
        
        if not kwork in jobsList: 
            jobsList.append(kwork)
            if first: pass
            else: send_msg(f'<b>Новый кворк от {author.text}!</b>\n{authorLink}\n\n{kwork.text}\n{kworkLink}\n{price.text}\n{workInfo.text}')
        
    first = False

        