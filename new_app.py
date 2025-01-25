import requests

API_KEY = "858298fd7c164e29ba6c61a50ee21887"

def get_news(query):

    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return None
    
def display_news(articles):
    if articles:
        for i, article in enumerate(articles, start = 1):
            print(f"\nNews {i}: ")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"Source: {article['source'] ['name']}")
            print(f"URL: {article['url']}")

    else:
        print("No news articles found.")

def main():
    query = input("Enter a topic to search for news (e.g, technology, sports): ")

    articles = get_news(query)

    if articles:
        display_news(articles)
    else:
        print("Could not fetch news. Please check your query or try again later")

if __name__ == "__main__":
    main()