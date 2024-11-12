import requests
from bs4 import BeautifulSoup

# формируем запрос с помощью http-запроса
st_accept = "text/html"
# имитируем подключение UserAgent через браузеры
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

req = requests.get("https://selectel.ru/blog/courses/", headers)
# считываем текст HTML-документа
src = req.text
print(src)

# выборка данных из полученного материала  с помощью конвертера Beautiful Soup
# инициализируем html-код страницы
with open("index.html") as fp:
   soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>веб-страница</html>", 'html.parser')





# использованы материалы https://habr.com/ru/companies/selectel/articles/754674/
# https://selectel.ru/blog/http-request/
# и https://www.crummy.com/software/BeautifulSoup/bs4/doc/
