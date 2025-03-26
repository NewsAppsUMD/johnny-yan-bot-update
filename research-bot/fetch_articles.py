import requests
from bs4 import BeautifulSoup

def fetch_articles():
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=alzheimer"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    # Find and collect titles, links, and abstracts
    for article in soup.find_all("article", class_="full-docsum"):
        title = article.find("a", class_="docsum-title").text.strip()
        link = "https://pubmed.ncbi.nlm.nih.gov" + article.find("a")["href"]
        
        # Visit each article's page to get the abstract
        article_page = requests.get(link)
        article_soup = BeautifulSoup(article_page.text, "html.parser")
        abstract_tag = article_soup.find("div", class_="abstract-content")
        abstract = abstract_tag.text.strip() if abstract_tag else "No abstract available"
        
        articles.append({
            "title": title,
            "link": link,
            "abstract": abstract  # Include the abstract in the article dictionary
        })
    
    # Print each article's title and abstract
    for article in articles:
        print(f"Title: {article['title']}\nAbstract: {article['abstract']}\nLink: {article['link']}\n")
    
    return articles

if __name__ == "__main__":
    fetch_articles()
