# Internet Speed Testing Application

## Overview

This application is a simple tool to measure your internet download speed using a test file download. It is built using Python's `tkinter` for the graphical user interface and `requests` for handling HTTP requests. The application displays the download speed in megabits per second (Mbps) after performing a download test.

## Features

- **Download Speed Measurement**: Calculates and displays the download speed in Mbps.
- **User-Friendly Interface**: Provides a clean and straightforward GUI using `tkinter`.
- **Asynchronous Processing**: Uses threading to keep the GUI responsive during the speed test.

## Installation

To run this application, you need Python and some Python packages. Follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. **Install Python**: Ensure you have Python 3.x installed on your system. You can download it from python.org.
3. **Install Required Packages**: Install the requests package using pip:
    ```bash
    pip install requests

## Usage

1. **Run the Application**:
   Save the provided code into a file named `speed_test.py` and run it using Python:
   ```bash
   python speed_test.py
2. **Perform a Speed Test** :
- Launch the application.
- Click the "Check Speed" button to start the download speed test.
- The application will disable the button during the test and update the download speed in the label once the test is complete.


## Code Explanation
- **calculate_download_speed Function**: Measures the download speed by downloading a test file in chunks and calculating the time taken.
- **run_speed_test Function**: Handles button state changes and updates the GUI with the calculated download speed using threading to ensure the GUI remains responsive.
- **GUI Layout**: Uses tkinter to create a window with a centered label displaying the download speed and a button to start the test.

## Acknowledgements
- **Requests Library**: For handling HTTP requests.
- **tkinter**: For creating the graphical user interface.