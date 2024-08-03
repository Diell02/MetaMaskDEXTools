import time
import json
import os
import sys
import cv2
import numpy as np
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import pygetwindow as gw

# Set up Firefox options to use the existing profile
profile_path = '' #Place your profile path C:/Users/NameOfUser/AppData/Roaming/Mozzila/Firefox/Profiles/YourDefaultProfile
firefox_options = Options()
firefox_options.add_argument(f"-profile {profile_path}")
firefox_options.add_argument("--start-maximized")

# Initialize the WebDriver using GeckoDriverManager
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

# Paths to the button images
metamask_button_image_path = './buttonPics/metamask.png'
next_button_image_path = './buttonPics/next.png'
confirm_button_image_path = './buttonPics/confirm.png'
sign_button_image_path = './buttonPics/sign.png'
accprofile_button_image_path = './buttonPics/accprofile.png'
disconnect_button_image_path = './buttonPics/disconnectwallet.png'

# Function to click a button by image recognition
def click_button_by_image(button_image_path):
    try:
        # Take a screenshot of the current screen
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Load the button image
        button_image = cv2.imread(button_image_path, cv2.IMREAD_GRAYSCALE)

        # Find the button in the screenshot
        result = cv2.matchTemplate(screenshot_gray, button_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Define the threshold for matching
        threshold = 0.8
        if max_val >= threshold:
            button_x, button_y = max_loc
            button_center_x = button_x + button_image.shape[1] // 2
            button_center_y = button_y + button_image.shape[0] // 2

            # Move the mouse to the button and click it
            pyautogui.moveTo(button_center_x, button_center_y)
            pyautogui.click()
        else:
            print("Button not found on the screen")
    except pyautogui.PyAutoGUIException as e:
        print(f"PyAutoGUIException: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# MetaMask extension URL
metamask_url = ""  # Update this with your MetaMask extension ID

# Open MetaMask
print(f"Opening MetaMask at {metamask_url}")
driver.get(metamask_url)

# Wait for MetaMask to load
time.sleep(10)  # Adjust based on your internet speed and MetaMask loading time

# Function to unlock MetaMask
def unlock_metamask(password):
    wait = WebDriverWait(driver, 10)
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password_input.send_keys(password)
    unlock_button = driver.find_element(By.XPATH, "//button[text()='Unlock']")
    unlock_button.click()
    time.sleep(10)  # Adjust based on your internet speed and MetaMask processing time

# Function to import a wallet using its private key
def import_wallet(private_key):
    wait = WebDriverWait(driver, 10)
    
    # Click the account button
    account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'multichain-account-picker__label') and starts-with(text(), 'Account')]")))
    account_button.click()
    time.sleep(3)

    # Click "+ Add account or hardware wallet"
    add_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'mm-button-secondary') and contains(text(), 'Add account or hardware wallet')]")))
    add_account_button.click()
    time.sleep(3)
    
    # Click "Import account"
    import_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'mm-button-link') and contains(text(), 'Import account')]")))
    import_account_button.click()
    time.sleep(3)

    # Enter the private key
    private_key_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='private-key-box']")))
    private_key_input.send_keys(private_key)
    
    # Click the import button
    import_confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='import-account-confirm-button']")))
    import_confirm_button.click()
    time.sleep(5)  # Adjust based on your internet speed and MetaMask processing time

# Function to connect to DEXTools and handle MetaMask popup
def connect_to_dextools():
    wait = WebDriverWait(driver, 10)
    
    # Go to DEXTools account page
    dextools_account_url = "https://www.dextools.io/app/en/user/account"
    driver.get(dextools_account_url)
    time.sleep(10)  # Adjust based on website loading time
    
    # Click the Connect button
    connect_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-process-id='connectWallet']")))
    driver.execute_script("arguments[0].click();", connect_button)
    time.sleep(10)
    
    # Click the MetaMask button using the image
    click_button_by_image(metamask_button_image_path)
    time.sleep(30)  # Wait for the new MetaMask window to open

    # Bring the new MetaMask window to the foreground
    metamask_window = None
    for window in gw.getAllTitles():
        if "MetaMask" in window:
            metamask_window = gw.getWindowsWithTitle(window)[0]
            metamask_window.activate()
            break

    time.sleep(30)  # Give time for the window to come to the foreground

    # Click the "Next" button in the new MetaMask window using the image
    click_button_by_image(next_button_image_path)
    time.sleep(10)
    
    click_button_by_image(confirm_button_image_path)
    time.sleep(10)
	
	# Locate and click the button with specific data-process-id and text
    verify_wallet_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-process-id='connectWallet' and contains(text(),'Verify wallet')]")))
    driver.execute_script("arguments[0].click();", verify_wallet_button)
    time.sleep(30)
	
    click_button_by_image(sign_button_image_path)
    time.sleep(10)
	
	# Go to DEXTools vote page -----------------------------------ADD URL--------------------------------ADD URL----------------------------------
    dextools_vote_url = ""
    driver.get(dextools_vote_url)
    time.sleep(15)
	
    # Locate the thumbs-up icon element
    thumbs_up_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//fa-icon[@class='ng-fa-icon hand is-not-vote ng-star-inserted']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", thumbs_up_icon)
    time.sleep(10)
		
    thumbs_up_icon.click()
    time.sleep(5)

    # Scroll back up to the top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(5)
	
    click_button_by_image(accprofile_button_image_path)
    time.sleep(10)
	
    click_button_by_image(disconnect_button_image_path)
    time.sleep(20)


# Unlock MetaMask
password = "Test1234!"  #Place the password of MetaMask account
unlock_metamask(password)

# Get the wallet index from the command line arguments
wallet_index = int(sys.argv[1])

# Path to the directory containing wallet JSON files
wallets_dir = ''

# Import a wallet by index
wallet_file = os.listdir(wallets_dir)[wallet_index]  # Get the wallet file by index
wallet_path = os.path.join(wallets_dir, wallet_file)

with open(wallet_path, 'r') as f:
    wallet_info = json.load(f)
    private_key = wallet_info['private_key']
    import_wallet(private_key)

# Connect to DEXTools and handle MetaMask popup
connect_to_dextools()

# Close the WebDriver
driver.quit()

print(f'Successfully imported wallet {wallet_index} and connected to DEXTools.')
