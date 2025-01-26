import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.biznesradar.pl/gielda/akcje_gpw"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the companies
    table = soup.find('table', {'class': 'table table--accent-header table--accent-first table--even table--nowrap table--sticky-first-col table--sticky-header'})  # Replace with the actual class name of the table

    if table is None:
        print("Table not found.")
    else:
        # Initialize a list to store company names
        companies = []

        # Iterate through the rows of the table
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if columns:
                company_name = columns[0].text.strip()  # Adjust the index based on the column structure
                companies.append(company_name)

        # Print the list of companies
        for company in companies:
            print(company)

else:
    print(f"Failed to retrieve data: {response.status_code}")