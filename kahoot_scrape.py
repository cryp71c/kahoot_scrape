import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for Progressbar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  # Import Options to configure headless mode
import time

def get_kahoot_data():
    # Get the URL(s) entered by the user
    urls = url_text.get("1.0", "end-1c").strip().splitlines()  # Get all lines from the text area
    filename = filename_entry.get().strip()  # Get the filename

    # Validate the input
    if not urls or not filename:
        messagebox.showerror("Input Error", "Please enter valid URLs and a file name.")
        return

    try:
        # Set up the progress bar to show the progress
        progress_bar["maximum"] = len(urls)
        progress_bar["value"] = 0

        with open(filename, 'w') as file:
            for idx, url in enumerate(urls, 1):
                # Setup the Chrome WebDriver with headless option
                chrome_options = Options()
                chrome_options.add_argument("--headless")  # Enable headless mode
                chrome_options.add_argument("--no-sandbox")  # Useful for some environments
                chrome_options.add_argument("--disable-dev-shm-usage")  # To avoid certain errors on Linux

                # Initialize the WebDriver with headless options
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
                
                # Open the Kahoot page
                driver.get(url)
                
                # Wait for the page to load (you can adjust the time as needed)
                time.sleep(5)  # Sleep for 5 seconds to ensure the content loads

                # Scrape the quiz name from the page title
                quiz_name = driver.title.strip()  # Get the page title (usually the quiz name)

                # Find the elements you're interested in (example: all elements with a specific class)
                elements = driver.find_elements(By.CLASS_NAME, 'styles__Question-sc-19vxqaz-6')  # Adjust based on the actual class name

                # Write the quiz name to the file
                file.write(f"Quiz Name: {quiz_name}\n")
                file.write(f"Data from URL: {url}\n")
                
                q = 1
                # Extract and write the data for each URL to the file
                for element in elements:
                    file.write(f"{q}) {element.text}\n")  # Prints the text content of each element
                    q += 1
                file.write("\n" + "="*50 + "\n\n")

                # Update the progress bar after processing each URL
                progress_bar["value"] = idx
                window.update_idletasks()  # This updates the UI during the process

        # Display success message
        messagebox.showinfo("Success", f"Data extraction successful. Data saved in '{filename}'.")
        
    except Exception as e:
        # Handle errors and display them in a message box
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    finally:
        # Close the browser after extracting the data
        driver.quit()

# Create the main window
window = tk.Tk()
window.title("Kahoot Data Extractor")

# Create and place the URL label and text box (for multiple URLs)
url_label = tk.Label(window, text="Enter Kahoot URLs (one per line):")
url_label.pack(pady=10)

url_text = tk.Text(window, height=10, width=50)
url_text.pack(pady=10)

# Create and place the filename label and text entry box
filename_label = tk.Label(window, text="Enter output filename:")
filename_label.pack(pady=10)

filename_entry = tk.Entry(window, width=50)
filename_entry.pack(pady=10)

# Create and place the progress bar
progress_bar = ttk.Progressbar(window, length=400, orient="horizontal", mode="determinate")
progress_bar.pack(pady=10)

# Create and place the 'Extract Data' button
extract_button = tk.Button(window, text="Extract Data", command=get_kahoot_data)
extract_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()