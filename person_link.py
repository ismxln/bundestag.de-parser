import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    persons_links = []

    for i in range(0, 740, 20):
        link = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'

        response = requests.get(url=link)

        soup = BeautifulSoup(response.content, 'lxml')
        persons = soup.find_all('a')

        for person in persons:
            persons_links.append(person['href'])

    # .txt file with person links
    with open('scrape learning/bundestag.de/persons_links.txt', 'a') as file:
        for line in persons_links:
            file.write(f'{line}\n')
