import requests
from bs4 import BeautifulSoup
import sys

# Get soup
url = "https://www.imf.org/en/publications/weo/weo-database/2024/october/download-entire-database"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# def function for safe link extraction
def get_link(soup, css_selector, label):
    try:
        element = soup.select_one(css_selector)
        if element is None:
            raise ValueError("href does not exist, please check the 'file_elements' list against the source html")
        return element['href']
    except Exception as e:
        print(f"Error in extracting in {label} as {e}")
        sys.exit()

# def function for user input
def file_selector():
    while True:
        try:
            user_input = int(input("Please pick a file with the numerical designation: "))
            if user_input in range(1, 5):
                return user_input
            print("That isn't a valid answer, please pick a number between 1 and 4.\n")
        except ValueError:
            print("That isn't a valid answer, please pick a number between 1 and 4.\n")

# User_loop
def file_extractor():
    user_choice = file_selector()
    chosen_href = get_link(file_elements[user_choice-1][0], file_elements[user_choice-1][1], file_elements[user_choice-1][2])
    filename = chosen_href.rsplit("/", 1)[-1]
    response2 = requests.get(chosen_href)
    with open(f"{filename}", 'wb') as f:
        f.write(response2.content)
    print(f"{filename} saved to local dir\n")


# Set up nested list for possible choices
file_elements = [
    [soup, 'a[href="https://www.imf.org/-/media/files/publications/weo/weo-database/2024/october/weooct2024all.xls"]', "By Countries"],
    [soup, 'a[href="https://www.imf.org/-/media/files/publications/weo/weo-database/2024/october/weooct2024alla.xls"]', "By Country Groups"],
    [soup, 'a[href="https://www.imf.org/-/media/files/publications/weo/weo-database/2024/october/weooct2024-sdmxdata.zip"]', "SDMX Data"],
    [soup, 'a[href="https://www.imf.org/-/media/files/publications/weo/weo-database/2024/october/weopub-dsd-oct2024.xlsx"]', "SDMX DSD"]]

# Print options and initiate script.
print("1. By Countries\n2. By Country Group\n3. SDMX Data\n4. SDMX Data Definitions\n")
file_extractor()
while True:
    loop = (input("Would you like to download another file?")).lower()
    if loop == 'yes':
        file_extractor()
    elif loop == 'no':
        print("Ending script.")
        break
    else:
        print("That isn't a valid answer, please enter either yes or no.\n")
