from fetch_articles import fetch_articles

def generate_summary():
    articles = fetch_articles()  # Fetch articles including abstracts
    
    for article in articles:
        title = article["title"]
        abstract = article["abstract"]
        link = article["link"]
        
        # Create a summary using the abstract
        summary = (
            f"Article Title: {title}\n"
            f"Summary: {abstract}\n"
            f"Read more: {link}\n"
            f"-----------------------------------\n"
        )
        
        # Print the summary
        print(summary)

if __name__ == "__main__":
    generate_summary()
