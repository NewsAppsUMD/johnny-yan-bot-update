from fetch_articles import fetch_articles

def generate_summary():
    articles = fetch_articles()  # Fetch articles as dictionaries

    for article in articles:
        title = article["title"]
        abstract = article["abstract"]
        link = article["link"]

        summary = (
            f"📖 *{title}*\n"
            f"📝 Summary: {abstract}\n"
            f"🔗 Read more: {link}\n"
            f"-----------------------------------\n"
        )

        print(summary)

if __name__ == "__main__":
    generate_summary()
