import requests
from bs4 import BeautifulSoup
import json
from time import sleep
from random import randrange
from fake_useragent import UserAgent


def get_html(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        print(f'|status_code={response.status_code}|')
        return response
    except(requests.RequestException, ValueError):
        print(f'Error during requests to {url}')
        return False


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    # go to one of links in persons_links.txt, check how to get needed data
    person = soup.find('div', class_='bt-biografie-name').find('h3').text.strip()
    print(person)  # <h3> Sanae Abdi, SPD</h3> (without .text.strip())
    person_name_company = person.split(',')
    person_name = person_name_company[0]
    person_company = person_name_company[1].strip()

    # <a title="Homepage" href="https://sanae-abdi.spd.de/" class="bt-link-extern">Homepage</a>
    social_networks = soup.find_all(class_='bt-link-extern')
    social_networks_links = []
    for item in social_networks:
        social_networks_links.append(item['href'])

    data = {
        'person_name': person_name,
        'company_name': person_company,
        'social_networks': social_networks_links
    }

    return data


def main():
    ua = {'user-agent': UserAgent().random}

    with open('persons_links.txt') as file:  # save links in new list and strip them to be sure
        links = [link.strip() for link in file.readlines()]

    data_dict = []
    count = 0

    for link in links:
        html = get_html(url=link, headers=ua)
        if html:
            data_dict.append(parse_html(html.content))

            count += 1
            print(f'#{count}: {link} is done.')

            if count % 30 == 0:
                sleep(randrange(5, 8))

    # create json file for write all parsed data
    with open('name-company-socials.json', 'w') as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
