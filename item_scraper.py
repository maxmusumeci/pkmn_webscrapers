import os
import requests
import csv
import bs4


rootURL = 'https://bulbapedia.bulbagarden.net'
indexURL = rootURL + '/wiki/List_of_items_by_name' 
currentPath = os.getcwd() # get current write directory
csv_file = currentPath + "/../mon_data/csvs/items.csv" # wherever you want this file to end up


def getItems():
    listOfURLs = requests.get(indexURL)
    soup = bs4.BeautifulSoup(listOfURLs.text, "html.parser")
    #print(soup)
    item_table = soup.select('table.roundy')
    #print(item_table)

    items = []
    for table in item_table:
        for row in table.find_all('tr')[1:-1]:
            columns = row.find_all('td')
            name = columns[1].get_text(strip=True)
            gen = columns[2].get_text(strip=True)
            description = columns[3].get_text(strip=True)

            items.append({
                'Name': name,
                'Gen': gen,
                'Description': description,
            })

    return items 


def write_csv(to_write):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Gen', 'Description'])

        for i in to_write:
            writer.writerow([i['Name'], i['Gen'], i['Description']])


#abilities = getAbilities()
items = getItems()
write_csv(items)

print("Done")

