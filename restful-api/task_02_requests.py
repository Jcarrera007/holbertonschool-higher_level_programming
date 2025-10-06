import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get(URL)
    
    if response.status_code == 200:
        posts = response.json()
        post_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        with open("posts.csv", mode="w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(post_data)
