# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 03:34:30 2023

@author: anees
"""

import qrcode
import subprocess
import webbrowser
import socket


def get_local_ip():
    # Get the local IP address of the machine
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to a known external server
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None


if __name__ == "__main__":
    # Fetch the local IP address
    local_ip = get_local_ip()

    if local_ip:
        # Construct the URL using the local IP address
        port = 3000  # Replace with the actual port your server is running on
        url = f"http://{local_ip}:{port}"

        # Generate the QR code with the URL
        qr_code_data = url
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_data)
        
        # Create an image from the QR code data
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image to a file or display it
        img.show()
    else:
        print("Unable to fetch local IP address.")


    