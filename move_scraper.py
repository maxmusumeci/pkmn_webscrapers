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
indexURL = rootURL + '/wiki/List_of_moves' 
currentPath = os.getcwd() # get current write directory
csv_file = currentPath + "/../mon_data/csvs/moves.csv"


def getMoves():
    listOfURLs = requests.get(indexURL)
    soup = bs4.BeautifulSoup(listOfURLs.text, "html.parser")
    move_table = soup.select_one('table.sortable')
    #print(move_table)

    moves = []
    for row in move_table.find_all('tr')[2:]:
        columns = row.find_all('td')
        name = columns[1].get_text(strip=True)
        typ = columns[2].get_text(strip=True)
        category = columns[3].get_text(strip=True)
        pp = columns[4].get_text(strip=True)
        bp = columns[5].get_text(strip=True)
        acc = columns[6].get_text(strip=True)

        moves.append({
            'Name': name,
            'Type': typ,
            'Category': category,
            'PP': pp,
            'Power': bp,
            'Accuracy': acc
        })

    return moves


def write_csv(to_write):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Type', 'Category', 'PP', 'Power', 'Accuracy'])

        for i in to_write:
            writer.writerow([i['Name'], i['Type'], i['Category'], i['PP'], i['Power'], i['Accuracy']])


#abilities = getAbilities()
moves = getMoves()
write_csv(moves)

print("Done")

