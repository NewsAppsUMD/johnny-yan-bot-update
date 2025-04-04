import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json  # Importing the json module for pretty-printing

def fetch_articles():
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=alzheimer"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    # Find and collect titles, links, authors, and publication dates
    for article in soup.find_all("article", class_="full-docsum"):
        if len(articles) >= 10:
            break
        
        title = article.find("a", class_="docsum-title").text.strip()
        link = "https://pubmed.ncbi.nlm.nih.gov" + article.find("a")["href"]
        
        # Visit each article's page to get the author(s) and publication date
        article_page = requests.get(link)
        article_soup = BeautifulSoup(article_page.text, "html.parser")
        
        pub_date_tag = article_soup.find("span", class_="cit")
        pub_date_raw = pub_date_tag.text.strip() if pub_date_tag else None
        
        # Extract and format publication date
        pub_date = None
        if pub_date_raw:
            date_match = re.search(r'(\d{4} \w{3} \d{1,2})', pub_date_raw)  # Match YYYY Mon DD format
            if date_match:
                pub_date_obj = datetime.strptime(date_match.group(0), '%Y %b %d')
                pub_date = pub_date_obj.strftime('%B %d, %Y')
        
        # Extract author(s) and clean up the formatting
        authors_tag = article_soup.find("div", class_="authors-list")
        if authors_tag:
            authors = authors_tag.text.strip()
            # Remove unwanted characters and numbers
            authors = re.sub(r'\s*\d+\s*', '', authors)  # Remove numbers
            authors = authors.replace('\xa0', '').replace('\n', '').strip()
            authors = ','.join(authors.split(', '))  # Ensure authors are separated by commas
        else:
            authors = "No authors listed"
        
        if pub_date:  # Only add articles with a valid publication date
            articles.append({
                "title": title,
                "link": link,
                "authors": authors,
                "publication_date": pub_date
            })
    
    return articles

if __name__ == "__main__":
    articles = fetch_articles()
    # Use json.dumps to pretty-print the list of dictionaries
    print(json.dumps(articles, indent=4))