### This is based on lista_spolek.py but with additional data from Newconnect and also adding missing parameter extracted from url ###

import requests
from bs4 import BeautifulSoup

# Function to fetch company names and URLs from a given URL
def fetch_companies_and_urls(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing the companies
        table = soup.find('table', {'class': 'table table--accent-header table--accent-first table--even table--nowrap table--sticky-first-col table--sticky-header'})  # Adjust this class as needed

        if table is None:
            print("Table not found.")
            return []
        else:
            # Initialize a list to store company names and URLs
            companies = []

            # Iterate through the rows of the table
            for row in table.find_all('tr')[1:]:  # Skip the header row
                columns = row.find_all('td')
                if columns:
                    company_name = columns[0].text.strip()  # Adjust the index based on the column structure
                    # Assuming the company name is inside an <a> tag
                    link_tag = columns[0].find('a', href=True)  # Find the <a> tag with href attribute
                    if link_tag:
                        company_url = link_tag['href']  # Get the URL from the href attribute
                        # Extract only the part after "/notowania/"
                        company_url = company_url.split('/notowania/')[1] if '/notowania/' in company_url else None
                        companies.append((company_name, company_url))
                    else:
                        companies.append((company_name, None))  # In case there's no link

            return companies
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

# URLs of the webpages
url_1 = "https://www.biznesradar.pl/gielda/akcje_gpw"
url_2 = "https://www.biznesradar.pl/gielda/newconnect"  # Added newconnect data

# Fetch companies and their URLs from both URLs
companies_1 = fetch_companies_and_urls(url_1)
companies_2 = fetch_companies_and_urls(url_2)

# Combine the lists
all_companies = companies_1 + companies_2

# Print the combined list of companies and their URLs
for company_name, company_url in all_companies:
    print(f"{company_name},{company_url}")