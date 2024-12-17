# QR Code Authorization

## Overview

This repository contains a Python script for QR code-based authorization using OpenCV and Pyzbar. The script scans QR codes from a live webcam feed, compares the decoded data against a predefined list of authorized entries, and displays whether the code is authorized or unauthorized in real-time.

## Features

1. Real-time QR code scanning using a webcam.

2. Authorization check against a list of pre-approved data.

3. Visual feedback with bounding boxes and status messages:

3. Green for authorized QR codes.

4. Red for unauthorized QR codes.

## Requirements

1. To run this script, ensure you have the following installed:

2. Python 3.x

3. OpenCV

4. NumPy

5. Pyzbar

You can install the required libraries using:

pip install opencv-python-headless numpy pyzbar

## How to Use

1. Clone the Repository:

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. Prepare Authorization Data:

Place your authorized data entries (one per line) in the myData.txt file located in the Resources directory.

Example content of myData.txt:

Entry1
Entry2
Entry3

3. Run the Script:

python qr_authorization.py

4. Scan QR Codes:

The webcam feed will open.

Position a QR code within the frame.

The script will display the authorization status ("Authorized" or "Unauthorized") on the video feed.

5. Exit:

Press 1 to stop the webcam feed and exit the script.

