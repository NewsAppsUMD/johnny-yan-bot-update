import csv
from fetch_articles import fetch_articles

def save_to_csv():
    articles = fetch_articles()  # Now this will return the list of articles
    
    with open("research_articles.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        
        for article in articles:
            writer.writerow([article["title"], article["link"]])

if __name__ == "__main__":
    save_to_csv()
