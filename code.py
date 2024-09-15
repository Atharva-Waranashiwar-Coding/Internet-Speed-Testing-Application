import time
import requests
import threading
from tkinter import *

# URL to download a test file (you can change this to a URL of your choice)
TEST_URL = "https://cachefly.cachefly.net/100mb.test"

# Function to calculate download speed
def calculate_download_speed():
    start_time = time.time()
    response = requests.get(TEST_URL, stream=True)
    total_bytes = 0

    # Download the file in chunks to simulate real-world downloading
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            total_bytes += len(chunk)

    end_time = time.time()

    download_time = end_time - start_time
    download_speed = (total_bytes / download_time) / (10**6)  # Convert to Mbps

    return download_speed

# Function to run the download speed test in a separate thread
def run_speed_test():
    button.config(state=DISABLED)  # Disable the button while the test is running
    download_speed = calculate_download_speed()
    down_label.config(text=f"{download_speed:.2f} Mbps")
    button.config(state=NORMAL)  # Re-enable the button after the test is complete

# Creation of GUI
window = Tk()
window.title("Internet Speed Testing")
window.geometry('500x300')  # Adjusted size for better layout

# Creating a frame to center the content
frame = Frame(window)
frame.pack(expand=True)

# Adding a label for download speed in big bold letters
down_label = Label(frame, text="0.00 MBps", font=("Helvetica", 36, "bold"))
down_label.pack(pady=20)

# Adding a button for starting the speed test
button = Button(frame, text="Check Speed", font=("Helvetica", 16), command=lambda: threading.Thread(target=run_speed_test).start(), background='#49A', width=20)
button.pack(pady=20)

# Closing of GUI
window.mainloop()
