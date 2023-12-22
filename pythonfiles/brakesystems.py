import time
from telnetlib import EC
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.onlinecarparts.co.uk/spare-parts/brakes-group.html')
driver.maximize_window()
brake_subcategory = []
row = driver.find_element(By.CLASS_NAME, 'catalog-grid')
print(row.accessible_name)
items = row.find_elements(By.CLASS_NAME, 'row')
for item in items:
    images = item.find_elements(By.CLASS_NAME, 'lazyloaded')
    div = item.find_elements(By.CLASS_NAME, 'catalog-grid-item__link')
    name = item.find_elements(By.CLASS_NAME, 'catalog-grid-item__name')

    for sparee in div:
        image_div = sparee.find_element(By.CLASS_NAME, 'catalog-grid-item__image')
        image = image_div.find_element(By.TAG_NAME, 'img')
        name = sparee.find_element(By.CLASS_NAME, 'catalog-grid-item__name')
        brake_subcategory.append({'name': name.text, 'image': image.get_attribute('src')})



        # brake_subcategory.append({'name': item.text ,'image': image.get_attribute('src')})
print(brake_subcategory)
print(len(brake_subcategory))
workbook = xlsxwriter.Workbook('Brake SubCategoryParts.xlsx')
worksheet = workbook.add_worksheet("Subcategories")

# Write the header row
worksheet.write(0, 0, 'Name')
worksheet.write(0, 1, 'Image')

# Iterate over the list of dictionaries and write the data to the worksheet
for i, item in enumerate(brake_subcategory, start=1):
    worksheet.write(i, 0, item['name'])
    worksheet.write(i, 1, item['image'])

# Save the workbook
workbook.close()
