import requests
import bs4
import csv
import os
from multiprocessing import Pool

# Steps:

# Get al the URLS
# Scrape the correct ones using certain keywords
# for each ability
# Make a row with 4 columns number, name, description, gen
# Go through each column and get relevant info
# make into csv format



rootURL = 'https://bulbapedia.bulbagarden.net'
indexURL = rootURL + '/wiki/Ability#List_of_Abilities' ##List_of_Abilities'
allAbilities = []
currentPath = os.getcwd() # get current write directory
csv_file = currentPath + "/../mon_data/csvs/abilities.csv"


csv_columns = ['id', 'name', 'description', 'gen']



def getAbilities():

    listOfURLs = requests.get(indexURL)
    print(listOfURLs)
    soup = bs4.BeautifulSoup(listOfURLs.text, "html.parser")
    #print(soup)
    abilities_table = soup.select_one('table.sortable:not(.roundtable)')
    #print(abilities_table)

    abilities = []

    for row in abilities_table.find_all('tr')[1:]:

        columns = row.find_all('td')

        name = columns[1].get_text(strip=True)
        description = columns[2].get_text(strip=True)

        abilities.append({
            'Name': name,
            'Description': description

        })
    #[print(a, end='\n') for a in abilities]

    return abilities


def write_csv(abilities):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Description'])

        for a in abilities:
            writer.writerow([a['Name'], a['Description']])


abilities = getAbilities()
write_csv(abilities)

print("Done")
