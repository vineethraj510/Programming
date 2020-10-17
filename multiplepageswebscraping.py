import requests
from bs4 import BeautifulSoup

for each in range(1,11):
	site = 'http://quotes.toscrape.com/page/'+str(each)+'/'

	request = requests.get(site).content

	soup = BeautifulSoup(request,'html.parser')

	quotations = soup.find_all('span', class_ = 'text')

	authors = soup.find_all('small', class_ = 'author')

	tags = soup.find_all('a', class_ = 'tag')

	for quote, author, tag in zip(quotations,authors,tags):
		print("Quotes:",quote.text)
		print("Author:",author.text)
		print("Tags:",tag.text)
		print()
	print('...........................Page Complete............................','\n')
	print('PAGE',each+1)




