import csv
from fetch_articles import fetch_articles

def save_to_csv():
    articles = fetch_articles()  # Get articles as a list of dictionaries

    with open("research_articles.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link", "Authors", "Publication Date", "Abstract"])
        
        for article in articles:
            writer.writerow([
                article["title"],
                article["link"],
                article["authors"],
                article["publication_date"],
                article["abstract"]
            ])

if __name__ == "__main__":
    save_to_csv()
    print("CSV file saved successfully!")
