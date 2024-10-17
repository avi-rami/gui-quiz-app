import requests
import html

response = requests.get("https://opentdb.com/api.php?amount=10&category=12&difficulty=medium&type=boolean")
response.raise_for_status()
data = response.json()["results"]
data = html.unescape(data)
question_data = data
