from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# op = webdriver.ChromeOptions()
# service = Service(executable_path=r"C:\Users\灿灿灿\Downloads\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=service,options=op)
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.get("https://www.guazi.com")

# Get all the vehicle elements
vehicles = driver.find_element(By.XPATH,"//div[@class='list-infoBox']")

# Write the vehicle and price data to a text file
with open("vehicle_data.txt", "w") as f:
    for vehicle in vehicles:
        name = vehicle.find_element(By.XPATH,".//h2").text
        price = vehicle.find_element(By.XPATH,".//p").text
        f.write(f"{name} - {price}\n")