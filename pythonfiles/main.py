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

# locate category list by its ID
category_list = driver.find_element(By.CLASS_NAME,'catalog-grid')

# find all the list items
category_list_items = category_list.find_elements(By.TAG_NAME,'div')

# create a list to store the list item texts
list_item_texts = []

workbook = xlsxwriter.Workbook('Brake SubCategoryParts.xlsx')

#By default worksheet names in the spreadsheet will be
# Sheet1, Sheet2 etc., but we can also specify a name.
worksheet = workbook.add_worksheet("Subcategories")
row = 0
# iterate through the list items and get the text for each item
new_list = []
for item in category_list_items:

    new_list.append(item.text)

print(new_list)
print(len(category_list))

for spare in new_list:
    worksheet.write(row, 0, spare)
    row += 1
workbook.close()



done = input('Done? :')
if done.lower() == 'done':
    driver.quit()

