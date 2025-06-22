from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests

app = FastAPI()

# Allow CORS from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/outline")
def get_outline(country: str = Query(..., description="Country name")):
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"Could not fetch Wikipedia page for {country}"}

    soup = BeautifulSoup(response.text, 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    markdown = ["## Contents"]
    for tag in headings:
        level = int(tag.name[1])
        title = tag.get_text().strip()
        markdown.append(f"{'#' * level} {title}")

    return {"outline": "\n\n".join(markdown)}
