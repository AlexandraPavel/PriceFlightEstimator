import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions

# Set up Edge options
edge_options = EdgeOptions()
edge_options.add_argument('--disable-notifications')
edge_options.use_chromium = True  # Use the Chromium version of Edge
edge_options.add_argument('--headless')  # Run Edge in headless mode (no GUI)

# Path to your Microsoft Edge WebDriver executable
edge_driver_path = 'C:/Users/Mircea Timpuriu/Desktop/Facultate/MA1S1/DS/msedgedriver.exe'

# Initialize the Edge driver
driver = Edge(executable_path=edge_driver_path, options=edge_options)

# List location
locations = ["Bucuresti", "Cluj", "Iasi", "Timisoara", "Sibiu", "Istanbul", "Londra", "Paris", "Amsterdam", "Madrid", "Frankfurt", "Barcelona", "Munich", "Roma", "Lisabona", "Dublin", "Viena", "Manchester", "Atena", "Zurich", "Oslo", "Copenhaga", "Milano", "Berlin", "Bruxelles", "Malaga", "Stockholm", "Varsovia", "Geneva", "Alicante", "Helsinki", "Porto", "Budapesta", "Nisa", "Hamburg"]
locations_abbr = ["BUH", "CLJ", "IAS", "TSR", "SBZ", "IST", "LON", "PAR", "AMS", "MAD", "FRA", "BCN", "MUC", "ROM", "LIS", "DUB", "VIE", "MAN", "ATH", "ZRH", "OSL", "CPH", "MIL", "BER", "BRU", "AGP", "STO", "WAW", "GVA", "ALC", "HEL", "OPO", "BUD", "NCE", "HAM"]

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from datetime import date, timedelta, datetime
import time
import pandas as pd
import functools
print("flights_" + str(date.today().strftime('%d_%m_%Y')) + ".csv")
def create_date_list(y1, m1, d1, y2, m2, d2):
    start_dt = date(y1, m1, d1)
    end_dt = date(y2, m2, d2)
    delta = timedelta(days=1)
    dates = []

    while start_dt <= end_dt:
        dates.append(start_dt.isoformat())
        start_dt += delta

    return dates

def time_of_day(time):
    time_object = datetime.strptime(time, '%H:%M').time()
    if time_object.hour < 5 or time_object.hour >= 22:
        return "Noaptea"
    elif time_object.hour >= 5 and time_object.hour < 10:
        return "Dimineata"
    elif time_object.hour >= 10 and time_object.hour < 16:
        return "Ziua"
    else:
        return "Seara"
    
# List of dates
dates = []
dl1 = list(create_date_list(2023, 12, 20, 2023, 12, 23))
dl2 = list(create_date_list(2023, 12, 26, 2023, 12, 30))
dl3 = list(create_date_list(2024, 1, 2, 2024, 1, 5))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

# Database structure
flight_db = pd.DataFrame(columns = ['date_of_enquiry', 'departure', 'destination', 'flight_date', 'flight_time', 'arrival_time', 'airline', 'layovers', 'flight_duration', 'price'])

# Set the number and range of departure locations
for i in range(3):
    # Set the number and range of destinations
    for j in range(5, 25):
        try:
            if i != j:
                print(locations[i] + " -> " + locations[j])
                counter = 0
                # Extract all URLs for a way
                url_list = []
                for dat in dl1:
                    url = "http://vola.ro/flight_search/from/" + locations[i] + "/to/" + locations[j] + "/from_code/" + locations_abbr[i] + "/to_code/" + locations_abbr[j] + "/dd/" + str(dat) + "/rd/2023-12-08/ad/1/ow/1"
                    url_list.append((url, dat, 0))
                for dat in dl2:
                    url = "http://vola.ro/flight_search/from/" + locations[i] + "/to/" + locations[j] + "/from_code/" + locations_abbr[i] + "/to_code/" + locations_abbr[j] + "/dd/" + str(dat) + "/rd/2023-12-08/ad/1/ow/1"
                    url2 = "http://vola.ro/flight_search/from/" + locations[j] + "/to/" + locations[i] + "/from_code/" + locations_abbr[j] + "/to_code/" + locations_abbr[i] + "/dd/" + str(dat) + "/rd/2023-12-08/ad/1/ow/1"
                    url_list.append((url, dat, 0))
                    url_list.append((url2, dat, 1))
                for dat in dl3:
                    url = "http://vola.ro/flight_search/from/" + locations[j] + "/to/" + locations[i] + "/from_code/" + locations_abbr[j] + "/to_code/" + locations_abbr[i] + "/dd/" + str(dat) + "/rd/2023-12-08/ad/1/ow/1"
                    url_list.append((url, dat, 1))
                for elem in url_list:
                    counter += 1
                    print(counter)
                    (url, dat, return_flight) = elem    
                    driver.get(url)
                    full_price_list = []
                    full_stop_list = []
                    full_hour_list = []
                    # Wait until all dynamic elements are shown in this page
                    while True:
                        try:
                            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ith-filter-categories[contains(@filters, '$ctrl.filters')]")))
                            if i == 0 and j == 5 and elem == url_list[0]:
                                button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
                                button.click();
                            break
                        except TimeoutException as e:
                            driver.refresh()
                    for k in range(1):
                        try:
                            # Find all the relevant details
                            imgResults = driver.find_elements(By.XPATH,"//img[contains(@ng-repeat, 'airlineCode in ::$ctrl.airlines | limitTo: $ctrl.getLimit() track by airlineCode')]")
                            res = functools.reduce(lambda x,y : x+y, [char for char in imgResults[0].get_attribute('src') if char.isupper()])
                            pr = driver.find_elements(By.CLASS_NAME, 'price')
                            prices = [price.text for price in pr if len(price.text) > 3]
                            st = driver.find_elements(By.CLASS_NAME, 'stops')
                            stops = [stop.text for stop in st if len(stop.text) > 15]
                            h = driver.find_elements(By.CLASS_NAME, 'checkpoint__hour')
                            hours = [ho.text for ho in h if len(ho.text) > 1]
                            full_price_list.extend(prices)
                            full_stop_list.extend(stops)
                            full_hour_list.extend(hours)
                        except StaleElementReferenceException as e:
                            print(e)
                            pass
                    # Set the number of flights to be extracted for a way in at a specific date (max 30)
                    for l in range(20):
                        try:
                            # Calculate the total flight time
                            tmp = full_stop_list[l].split(",")[0]
                            total_time = int(tmp.split(" ")[0][:-1]) * 60 + int(tmp.split(" ")[1][:-1])

                            # Calculate the number of layovers
                            total_esc = 0
                            esc1 = full_stop_list[l].split(",")[1]
                            if esc1 != " Zbor direct":
                                total_esc += int(esc1[1]) 
                            
                            if return_flight == 0:
                                dep = locations[i]
                                des = locations[j]
                            else:
                                dep = locations[j]
                                des = locations[i]

                            # Create the new row for flight database
                            new_row = {'date_of_enquiry': date.today(),
                                    'departure': dep ,
                                    'destination': des,
                                    'flight_date': dat,
                                    'flight_time': full_hour_list[2 * l],
                                    'arrival_time': full_hour_list[2 * l + 1],
                                    'airline': functools.reduce(lambda x,y : x+y, [char for char in imgResults[l].get_attribute('src') if char.isupper()]),
                                    'layovers': total_esc,
                                    'flight_duration': total_time,
                                    'price': full_price_list[l].split(" ")[0]}
                            flight_db.loc[len(flight_db)] = new_row
                        except ValueError as e:
                            print("Iar nu e bine")
                        except IndexError as f:
                            print("Nu e bine")
        except StaleElementReferenceException as e:
            print("Aia e")  
            pass
driver.quit()
# Drop eventual duplicates and export to csv (name of the file is based on the date of the extraction)
# If you try to scrape more than once in a day, it WILL be overwritten
flight_db_2 = flight_db.drop_duplicates()
flight_db_2.to_csv("flights_" + str(date.today().strftime('%d_%m_%Y')) + ".csv")
