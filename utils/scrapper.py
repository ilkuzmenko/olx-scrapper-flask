import time
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup

base_url = 'https://www.olx.ua'
category_url = 'https://www.olx.ua/d/uk/transport/legkovye-avtomobili/?page='
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def get_urls(url: str) -> list:
	all_urls = []
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	for s in soup.select("a.css-1bbgabe"):
		href = s.get('href')
		all_urls.append('https://www.olx.ua' + href)
	return all_urls


def scrape(url: str) -> dict:
	try:
		response = requests.get(url)
		if response.status_code == 200:
			soup = BeautifulSoup(response.content, 'html.parser')
			name = soup.select_one("h1.css-r9zjja-Text").text
			price = soup.select_one("h3.css-okktvh-Text").text
			image = soup.select_one("div.swiper-zoom-container img[src]").get('src')
			return {'name': name, 'price': price, 'image': image}
	except Exception as ex:
		print(f"{ex} in {url}")


def get_items() -> list:
	urls: list = get_urls(category_url + '1') + get_urls(category_url + '2')

	try:
		with Pool(processes=20) as p:
			result = p.map(scrape, urls)
	except Exception as ex:
		print(ex)
	finally:
		p.join()
		return result


if __name__ == '__main__':
	start = time.time()

	res = get_items()
	print(res)

	end = time.time()
	print('It took', (end - start), 'seconds')
