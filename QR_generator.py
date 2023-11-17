# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 03:34:30 2023

@author: anees
"""

import qrcode
import subprocess

if __name__ == "__main__":


    # Specify the path to the Python script you want to execute
    script_path = "test.py"
    
    # Generate the QR code with the script path
    qr_code_data = f"python {script_path}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_code_data)
    qr.make(fit=True)
    
    # Create an image from the QR code data
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file or display it
    img.show()
    
    # Execute the Python script using subprocess
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")