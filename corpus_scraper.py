from bs4 import BeautifulSoup
import requests

page_link = "http://www.simpsonsarchive.com/episodes/AABF21.txt"

page_response = requests.get(page_link, timeout = 5)

page_content = BeautifulSoup(page_response.content, "html.parser")

for word in page_content:
	print(word)