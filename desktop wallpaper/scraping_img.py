import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# import os


string = 1
link = 'https://zastavok.net/'
user = UserAgent(verify_ssl=False).random
headers = {
    'user-agent': user
}

# выборка картинки
for str in range(2):
    response = requests.get(f'{link}/{string}', headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    # print(response)
    # вариант  через SV
    # block = sv.select('div.block-photo div div.short div.short_prev a', soup)
    # for img in block:
    #     link_img = img.get('href')
    #     print(link_img)
    block = soup.find('div', class_='block-photo')
    all_img = block.find_all('div', class_='short_full')

    # итерация и скачивание кокретной картинки
    for img in all_img:
        link_img = img.find('a').get('href')
        download = requests.get(f'{link}{link_img}').text
        download_soup = BeautifulSoup(download, 'lxml')
        download_blok = download_soup.find('div', class_='block_down').find().find('a').get('href')
        name = download_soup.find('div', id='main_image').find('img').get('alt')
    #     скачиваем
        img_link = requests.get(f'{link}{download_blok}').content

        path = '/image'  # сюда качаем  фото
        with open(f"{path}/{name}.jpg", 'wb') as file:
            # os.chdir('/Users/magickubik/Documents/КОТ/pythonProject1/image')
            # вариант 2 куда качать фото
            file.write(img_link)
            print('--downloade')
    # инкреминтация чтобы перейти на НЕКСТ страницу
    string += 1

