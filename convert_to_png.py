### Convert TIF, TIFF, WEBP and WDP to png
### By scanning all the files in files directory
### Save them with the same file name
### as PNG

# Imports
import os
from PIL import Image
import imagecodecs
import numpy as np

def convert_webp_to_png(input_path, output_path):
    """
    Converts a WebP image to PNG format.
    Args:
        input_path (str): The path to the input WebP file.
        output_path (str): The desired path for the output PNG file.
    """
    try:
        # Open the WebP image
        img = Image.open(input_path)
        # Convert to RGB or RGBA mode if necessary to handle transparency
        # 'RGB' for images without transparency, 'RGBA' for images with transparency
        if img.mode == 'P' or img.mode == 'L' or img.mode == '1': # Handle palette-based or grayscale images
            img = img.convert('RGBA') # Convert to RGBA for potential transparency in PNG
        elif img.mode != 'RGBA' and img.mode != 'RGB':
            img = img.convert('RGBA') # Ensure a compatible mode for PNG
        # Save the image as PNG
        img.save(output_path, 'png')
        print(f"Successfully converted '{input_path}' to '{output_path}'")
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def convert_tiff_to_png(input_tiff_path, output_png_path):
    try:
        # Open the TIFF image
        with Image.open(input_tiff_path) as img:
            # Save it as a PNG
            img.save(output_png_path, "PNG")
        print(f"Successfully converted '{input_tiff_path}' to '{output_png_path}'")
    except FileNotFoundError:
        print(f"Error: Input TIFF file not found at '{input_tiff_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_wdp_to_png(input_wdp_path, output_png_path):
    """
    Converts a WDP (JPEG XR) image to PNG format.

    Args:
        input_wdp_path (str): The path to the input WDP file.
        output_png_path (str): The path to save the output PNG file.
    """
    try:
        # Read the WDP image data
        wdp_data = imagecodecs.imread(input_wdp_path)

        # Create a Pillow Image object from the decoded data
        # The mode might need adjustment depending on the WDP's color depth (e.g., 'RGB', 'RGBA', 'L')
        # If the WDP has an alpha channel, use 'RGBA'. Otherwise, 'RGB' or 'L' (grayscale).
        # You might need to inspect the 'wdp_data.shape' to determine the correct mode.
        if wdp_data.ndim == 3 and wdp_data.shape[2] == 4: # Assuming RGBA
            img = Image.fromarray(wdp_data, 'RGBA')
        elif wdp_data.ndim == 3 and wdp_data.shape[2] == 3: # Assuming RGB
            img = Image.fromarray(wdp_data, 'RGB')
        elif wdp_data.ndim == 2: # Assuming Grayscale
            img = Image.fromarray(wdp_data, 'L')
        else:
            raise ValueError("Unsupported WDP image format or dimensions.")

        # Save the image as PNG
        img.save(output_png_path, format='PNG')
        print(f"Successfully converted '{input_wdp_path}' to '{output_png_path}'")

    except Exception as e:
        print(f"Error converting WDP to PNG: {e}")

def convert_avif_to_png(input_avif_path, output_png_path):
        ##
        """
        Converts an AVIF image to PNG format.

        Args:
            input_avif_path (str): The path to the input AVIF file.
            output_png_path (str): The path where the output PNG file will be saved.
        """
        try:
            img = Image.open(input_avif_path)
            img.save(output_png_path, format='PNG')
            print(f"Successfully converted '{input_avif_path}' to '{output_png_path}'")
        except Exception as e:
            print(f"Error converting AVIF to PNG: {e}")

# how to call these functions samples

input_file = "example.webp"  # Replace with your WebP file path
output_file = "output.png"    # Replace with your desired PNG output path

# Function Calls
## convert_webp_to_png(input_file, output_file)
## convert_tiff_to_png(input_file, output_file)
## convert_wdp_to_png(input_file, output_file)

# directory path to scan through
## directory_path = "files"  # Replace with your directory path
directory_path = "files"  # Replace with your directory path

# create list of files in directory
## var_files = os.listdir(directory_path)
var_files = os.listdir()

for item in var_files:
    ## print(item)
    file_info = item.split('.')

    # get file name
    file_name = file_info[0]

    # test if file_info after split is bigger than 1
    # incase there is a file with no extension 
    if(len(file_info)>1):
        file_type = file_info[1]
    else:
        file_type = "None"



    if(file_type.lower() == "webp"):
        output_file = file_name + '.' + 'png'
        convert_webp_to_png(item, output_file)
    elif(file_type.lower() == "wdp"):
        output_file = file_name + '.' + 'png'
        convert_wdp_to_png(item, output_file)
    elif(file_type.lower() == "tif" or file_type.lower() == "tiff"):
        output_file = file_name + '.' + 'png'
        convert_tiff_to_png(item, output_file)
    elif(file_type.lower() == "avif"):
        output_file = file_name + '.' + 'png'
        convert_avif_to_png(item, output_file)


    print(f"file_info\n {file_info}")
    print(f"file_name\n {file_name}")
    print(f"file_type\n {file_type}")

