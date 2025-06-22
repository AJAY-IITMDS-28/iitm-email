import requests
from bs4 import BeautifulSoup
import json

def fetch_imdb_titles(min_rating=4.0, max_rating=8.0, max_results=25):
    url = (
        "https://www.imdb.com/search/title/"
        f"?title_type=feature&user_rating={min_rating},{max_rating}"
        "&sort=user_rating,asc"
    )
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.select(".lister-item.mode-advanced")[:max_results]

    result = []
    for item in items:
        header = item.select_one(".lister-item-header a")
        href = header["href"]
        imdb_id = href.split("/")[2]
        title = header.text.strip()

        year_tag = item.select_one(".lister-item-year")
        year = year_tag.text.strip("()") if year_tag else ""

        rating_tag = item.select_one(".ratings-imdb-rating strong")
        rating = rating_tag.text if rating_tag else ""

        result.append({
            "id": imdb_id,
            "title": title,
            "year": year,
            "rating": rating
        })
    return result

# Run the program
data = fetch_imdb_titles()
print(json.dumps(data, indent=2))
