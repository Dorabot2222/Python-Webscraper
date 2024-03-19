import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all elements with a specific class or tag containing article titles
        articles = soup.find_all('h2', class_='article-title')  # Adjust according to the structure of the website
        
        # Extract the text of each article title and print it
        for article in articles:
            print(article.text.strip())
    else:
        print("Failed to retrieve webpage")

# URL of the website to scrape
url = 'https://www.example.com/news'

# Call the function to scrape articles from the specified URL
scrape_articles(url)
