import requests
from bs4 import BeautifulSoup

# with open('scrape learning/bundestag.de/persons_links.txt') as file:  # save links in new list and strip them to be sure
#     lines = [line.strip() for line in file.readlines()]

#     for line in lines:
#         response = requests.get(line)
#         soup = BeautifulSoup(response.content, 'lxml')
#         # go to one of links in persons_links.txt, check how to get needed data
#         person = soup.select('.bt-biografie-name h3').text  # col-xs-8 col-md-9 bt-biografie-name
#         person_name_company = person.strip().split(',')  # example: Sanae Abdi, SPD
#         person_name = person_name_company[0]
#         person_company = person_name_company[1]


response = requests.get('https://www.bundestag.de/en/members/abdi_sanae-861028')
soup = BeautifulSoup(response.content, 'lxml')
# go to one of links in persons_links.txt, check how to get needed data
person = soup.find(class_='bt-biografie-name').find('h3').text  # col-xs-8 col-md-9 bt-biografie-name
person_name_company = person.strip().split(',')  # example: Sanae Abdi, SPD
person_name = person_name_company[0]
person_company = person_name_company[1]

print(person_name, person_company)