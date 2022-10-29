import requests
from bs4 import BeautifulSoup
import webbrowser

def searchArticle():
    while True:
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(url.content, "html.parser")
        title = soup.find(class_="firstHeading").text

        print(f"{title}\nDo you want to read this article? (Y/N)")
        choice = input("Y or N: ")

        if choice == "y":
            url = "https://en.wikipedia.org/wiki/%s" %title
            webbrowser.open(url).lower()
            break
        elif choice == "n":
            print("\nTry another one...")
            searchArticle()
        else:
            print("\nWrong choice")
            searchArticle()


if __name__ == "__main__":
    searchArticle()