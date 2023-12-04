# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 03:34:30 2023

@author: anees
"""

import qrcode
import subprocess
import webbrowser

if __name__ == "__main__":


    # Specify the path to the Python script you want to execute
    url = "http://192.168.1.52:3000" 
    
    # Generate the QR code with the url
    qr_code_data = url
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code data
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file or display it
    img.show()
    webbrowser.open(url)


    