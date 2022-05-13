from bs4 import BeautifulSoup
import requests

def randomWord():
    word_generator = requests.get('https://www.coolgenerator.com/5-letter-word-generator').text.encode("utf-8")
    soup = BeautifulSoup(word_generator, 'lxml')
    word_box = soup.find('li', class_='col-sm-4 col-xs-6')
    word = word_box.find('p', class_='text-center font-18')
    return str(word.find('span'))[6:11]

