
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.select('td.titleColumn')
ratings = soup.select('td.imdbRating strong')

movie_list = []

for i in range(10):  # Top 10 for demo
    title = movies[i].a.text
    year = movies[i].span.text.strip('()')
    rating = ratings[i].text
    link = "https://www.imdb.com" + movies[i].a['href']
    movie_list.append([title, year, rating, link])

df = pd.DataFrame(movie_list, columns=["Title", "Year", "Rating", "Link"])
df.to_csv("imdb_top_movies.csv", index=False)
print("Data saved to imdb_top_movies.csv")
