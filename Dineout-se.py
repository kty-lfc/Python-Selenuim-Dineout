# importing the modules
import os
import time
import pandas as pd
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get method() will navigate to a page given by the URL address
# driver.get(
#   "https://www.justdial.com/Delhi/Ceiling-Tile-Dealers-Armstrong/nct-11271379")

driver.get(
    "https://www.dineout.co.in/bangalore-restaurants/east-bangalore/indiranagar")

# the user-defined function


def strings_to_num(argument):

    switcher = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }
    return switcher.get(argument, "nothing")


# fetching all the store details
storeDetails = driver.find_elements_by_class_name('restnt-detail-wrap')

# instatiating empty lists
nameList = []
addressList = []
numbersList = []

# iterating the storeDetails
print('length=', len(storeDetails))
for i in range(len(storeDetails)):
    # for i in range(20):
    # restnt-card-wrap-new
    # fetching the name, address and contact for each entry
    try:
        name = storeDetails[i].find_element_by_class_name(
            'restnt-name ellipsis').text
        # print(name)
    except NoSuchElementException:
        name = "404 Error"
        pass

    try:
        address = storeDetails[i].find_element_by_class_name(
            'restnt-loc ellipsis').text

        # print(address)
    except NoSuchElementException:
        address = "Address Error"
        pass

    try:
        contactList = storeDetails[i].find_elements_by_class_name(
            'double-line-ellipsis')
        # print(contactList)
    except NoSuchElementException:
        contactList = "Detail Info Error"
        pass

    myList = []

    for j in range(len(contactList)):

        myString = contactList[j].get_attribute('class').split("-")[1]

        myList.append(strings_to_num(myString))

    nameList.append(name)
    addressList.append(address)
    numbersList.append("".join(myList))

# intialise data of lists.
data = {'Company Name': nameList,
        'Address': addressList,
        'Phone': numbersList}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Save Data as .csv
df.to_csv('Res_dineout-1.csv',  header=False)

#df.to_csv('Temple1.csv', mode='a', header=False)

driver.close
