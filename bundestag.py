import requests
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    with open('scrape learning/bundestag.de/persons_links.txt') as file:  # save links in new list and strip them to be sure
        links = [link.strip() for link in file.readlines()]

        data_dict = {}

        # creating counter
        count = 0
        for link in links:
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'lxml')
            # go to one of links in persons_links.txt, check how to get needed data
            person = soup.select('.bt-biografie-name h3').text  # col-xs-8 col-md-9 bt-biografie-name
            person_name_company = person.strip().split(',')  # example: Sanae Abdi, SPD
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

            count += 1
            print(f'#{count}: {link} is done.')

            data_dict.append(data)

            # create json file for write all parsed data 
            with open('data.json', 'w') as f:
                json.dump(data_dict, f, indent=4)