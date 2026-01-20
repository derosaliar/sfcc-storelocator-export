import os, glob
import xml.etree.ElementTree as ET
import csv
from datetime import datetime

# Retrieve all .XML files in folder
for filename in glob.glob('*.xml'):
    # Loading .XML file...
    tree = ET.parse(filename)
    root = tree.getroot()

    # SFCC namespace
    namespace = {'ns': 'http://www.demandware.com/xml/impex/store/2007-04-30'}

    # Proceed to extract requested data
    rows = []
    storeServicesArray = []
    for store in root:
        if(store.attrib and store.tag == '{http://www.demandware.com/xml/impex/store/2007-04-30}store'):
            storeID = store.attrib['store-id']
            for node in store:
                if(node.tag.find('name') != -1):
                    storeName = node.text
                if(node.tag.find('address1') != -1):
                    storeAddress1 = node.text
                if(node.tag.find('address2') != -1):
                    storeAddress2 = node.text
                if(node.tag.find('city') != -1):
                    storeCity = node.text
                if(node.tag.find('postal-code') != -1):
                    storePostalCode = node.text
                if(node.tag.find('state-code') != -1):
                    storeStateCode = node.text
                if(node.tag.find('country-code') != -1):
                    storeCountryCode = node.text
                # Proceed to extract requested data from custom attributes
                if(node.tag.find('custom-attributes')) != -1:
                    for customattribute in node:
                        if(customattribute.attrib['attribute-id'].find('customAttributeTest')) != -1:
                            customAttributeTestArray = []                                
                            customAttributeTestArray = '|'.join(customAttributeTestArray)
                            rows.append([storeID, storeName, storeAddress1, storeAddress2, storeCity, storePostalCode, storeStateCode, storeCountryCode,customAttributeTestArray])
    # Write requested data in .CSV file
    with open(filename.replace('.xml','.csv'), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Store ID", "Store Name", "Address1", "Address2", "City", "Postal Code", "State Code", "Country Code", "Custom Attribute Test Array"])
        writer.writerows(rows)

    print("CSV file " + filename + " has been generated successfully.")