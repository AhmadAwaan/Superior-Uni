import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }

counter = 1
max_counter = 500

titlelist = []
locationList =[]
modelList = []
kmList = []
spexlist = []
fuelTypelist = []
ccList = []
pricelist = []
allConte = []
for i in range(counter,max_counter+1):
    page_url = f'https://www.pakwheels.com/used-cars/search/-/?page={i}'
    counter += 1
    print(page_url)
    response = requests.get(page_url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    main_content = soup.find('div', class_="col-md-9 search-listing pull-right")
    content = main_content.find_all('div', 'col-md-9 grid-style')
    print(len(content))
    allConte.extend(content)
    time.sleep(3)


for i in  allConte:
    title = i.find('a', class_='car-name ad-detail-path')
    a = title.text.split()
    res = ' '.join(a)
    titlelist.append(res)

    location = i.find('ul', class_='list-unstyled search-vehicle-info fs13')
    mainLocation = location.text.split()[0]
    locationList.append(mainLocation)

    price = i.find('div', class_='price-details generic-dark-grey')
    Price = price.text.split()
    if price:
        if len(Price) >1:
            firstValue = Price[1]
            secondValue = Price[2]
            addValyues = firstValue + secondValue
            pricelist.append(addValyues)
        else:
            pricelist.append(None)
    else:
        pricelist.append(None)

    metaData = i.find('ul', class_='list-unstyled search-vehicle-info-2 fs13')

    model = metaData.text.split()[0]
    modelList.append(model)

    usedInKm = metaData.text.split()[1]
    kmList.append(usedInKm)

    FuelType = metaData.text.split()[3]
    fuelTypelist.append(FuelType)

    cc = metaData.text.split()[4]
    ccList.append(cc)

    spex = metaData.text.split()[6]
    spexlist.append(spex)


data= pd.DataFrame({
            'Title': titlelist,
            'Location': locationList,
            'Model ': modelList,
            'KM': kmList,
            'Fuel Type': fuelTypelist,
            'CC': ccList,
            'Specs':spexlist,
            "Price" : pricelist
        })
        
data.to_csv('CarData From PakWheels.csv', index=False)
print(f"Data saved ")