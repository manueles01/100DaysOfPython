import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

all_movies = [h3.get_text() for h3 in soup.find_all("h3", class_="title")]
all_movies.reverse()

with open("movies.txt", "w") as f:
    for movie in all_movies:
        f.write(movie + "\n")
