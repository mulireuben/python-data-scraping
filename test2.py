import requests
from bs4 import BeautifulSoup
import openpyxl

# URL of the webpage containing the table
url = 'https://kmpdc.go.ke/Registers/General_Practitioners.php'

#define the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests":"1",
}

# Send a GET request to the webpage
response = requests.get(url,headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element
table = soup.find('table')

# prepare the workbook for the excel
workbook=openpyxl.Workbook()
sheet=workbook.active

# Extract table rows
for row in table.find_all('tr'):
    cells=row.find_all(['th' ,'td'])
    sheet.append([cell.get_text(strip=True) for cell in cells])

    workbook.save("scrapped_data.xlsx")

print("Data saved")




