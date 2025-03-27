import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def fetch_articles():
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=alzheimer"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    # Find and collect titles, links, abstracts, authors, and publication dates
    for article in soup.find_all("article", class_="full-docsum"):
        if len(articles) >= 10:
            break
        
        title = article.find("a", class_="docsum-title").text.strip()
        link = "https://pubmed.ncbi.nlm.nih.gov" + article.find("a")["href"]
        
        # Visit each article's page to get the abstract, author(s), and publication date
        article_page = requests.get(link)
        article_soup = BeautifulSoup(article_page.text, "html.parser")
        
        abstract_tag = article_soup.find("div", class_="abstract-content")
        abstract = abstract_tag.text.strip() if abstract_tag else "No abstract available"
        
        pub_date_tag = article_soup.find("span", class_="cit")
        pub_date_raw = pub_date_tag.text.strip() if pub_date_tag else None
        
        # Extract and format publication date
        pub_date = None
        if pub_date_raw:
            date_match = re.search(r'(\d{4} \w{3} \d{1,2})', pub_date_raw)  # Match YYYY Mon DD format
            if date_match:
                pub_date_obj = datetime.strptime(date_match.group(0), '%Y %b %d')
                pub_date = pub_date_obj.strftime('%B %d, %Y')
        
        # Extract author(s)
        authors_tag = article_soup.find("div", class_="authors-list")
        authors = authors_tag.text.strip() if authors_tag else "No authors listed"
        
        if pub_date:  # Only add articles with a valid publication date
            articles.append({
                "title": title,
                "link": link,
                "authors": authors,
                "abstract": abstract,
                "publication_date": pub_date
            })
    
    # Print each article's details
    for article in articles:
        print(f"Title: {article['title']}\nPublication Date: {article['publication_date']}\nAuthors: {article['authors']}\nLink: {article['link']}\n")
    
    return articles

if __name__ == "__main__":
    fetch_articles()
