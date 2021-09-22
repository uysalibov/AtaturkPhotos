import requests
from bs4 import BeautifulSoup
import random

class AtaturkPhotos:
    def __init__(self):
        self.images = []
        self.urls = [
            'https://www.ktb.gov.tr/TR-96577/ataturk-portreleri.html',
            'https://www.ktb.gov.tr/TR-96579/siyah-beyaz-fotograflarla-ataturk-galerisi-1.html',
            'https://www.ktb.gov.tr/TR-96580/siyah-beyaz-fotograflarla-ataturk-galerisi--2.html',
            'https://www.ktb.gov.tr/TR-96581/siyah-beyaz-fotograflarla-ataturk-galerisi--3.html',
            'https://www.ktb.gov.tr/TR-96582/siyah-beyaz-fotograflarla-ataturk-galerisi--4.html',
            'https://www.ktb.gov.tr/TR-96583/siyah-beyaz-fotograflarla-ataturk-galerisi--5.html',
            'https://www.ktb.gov.tr/TR-96584/siyah-beyaz-fotograflarla-ataturk-galerisi--6.html',
            'https://www.ktb.gov.tr/TR-96585/siyah-beyaz-fotograflarla-ataturk-galerisi--7.html'
        ]
    
    def start_scrape(self):
        with requests.Session() as session:
            for url in self.urls:
                r = session.get(url)
                soup = BeautifulSoup(r.content)
                images = soup.findAll('a')
                for image in images:
                    if image.has_attr('rel'):
                        self.images.append(image.find('img')['src'][:-2])
                    
    def save_to_txt(self, filename = 'AtaturkPhotos'):
        with open(f'{filename}.txt', 'w') as fp:
            for image in self.images:
                fp.write(f'https://www.ktb.gov.tr{image}\n')
                
    def random_image(self, amount = 1):
        if self.images != []:
            return random.choices(self.images, k=amount)
        else:
            raise ValueError('List already empty. Please use start_scrape func.')
    
if __name__ == '__main__':
    ata = AtaturkPhotos()
    ata.start_scrape()
    ata.save_to_txt()