"""
This module Convert TIF, TIFF, WEBP, WDP, AVIF to png.
"""

# Imports
import os
from typing import Dict
from PIL import Image
import imagecodecs

# var list of supported files
var_file_types: list[str] = ["webp", "wdp", "tif", "tiff", "avif"]

def output_path_func(input_path) -> str:
    """Create new name for png file as output path"""
    # Get output file name
    output_data = get_name_type(input_path)
    output_path = output_data["file_name"] + ".png"

    return output_path

def get_name_type(file_name: str = "") -> Dict[str, str]:
    """split file name at the dot and return a list with file name and type"""
    # declare return value
    return_dictionary = {}

    ## print(file_naam)
    file_info = file_name.split(".")

    # get file name
    file_name = file_info[0]

    # test if file_info after split is bigger than 1
    # incase there is a file with no extension
    if len(file_info) > 1:
        file_type = file_info[1]
    else:
        file_type = "None"

    # make sure file type is lowercase
    file_type = file_type.lower()

    return_dictionary["file_name"] = file_name
    return_dictionary["file_type"] = file_type

    return return_dictionary


# file type is in list
def supported_file(file_naam) -> bool:
    """Check file_name if it is in my supported list"""
    # Set default return value
    return_value: bool = False

    file_type_dict = get_name_type(file_naam)
    file_type = file_type_dict["file_type"]

    # over kill IF, but is a good example
    if file_type in var_file_types:
        return_value = True
    elif file_type not in var_file_types:
        return_value = False

    return return_value


def convert_wdp_to_png(input_path) -> None:
    """Converts a WDP (JPEG XR) image to PNG format."""
    # Read the WDP image data
    wdp_data = imagecodecs.imread(input_path)

    # Create a Pillow Image object from the decoded data
    # The mode might need adjustment depending on the WDP's color depth (e.g., 'RGB', 'RGBA', 'L')
    # If the WDP has an alpha channel, use 'RGBA'. Otherwise, 'RGB' or 'L' (grayscale).
    # You might need to inspect the 'wdp_data.shape' to determine the correct mode.
    if wdp_data.ndim == 3 and wdp_data.shape[2] == 4:  # Assuming RGBA
        img = Image.fromarray(wdp_data, "RGBA")
    elif wdp_data.ndim == 3 and wdp_data.shape[2] == 3:  # Assuming RGB
        img = Image.fromarray(wdp_data, "RGB")
    elif wdp_data.ndim == 2:  # Assuming Grayscale
        img = Image.fromarray(wdp_data, "L")
    else:
        raise ValueError("Unsupported WDP image format or dimensions.")

    # Get output file name
    output_path = output_path_func(input_path)

    # Save the image as PNG
    img.save(output_path, format="PNG")
    print(f"Successfully converted '{input_path}' to '{output_path}'")


def convert_webp_to_png(input_path):
    """Converts a WebP image to PNG format."""
    # Open the WebP image
    img = Image.open(input_path)
    # Convert to RGB or RGBA mode if necessary to handle transparency
    # 'RGB' for images without transparency, 'RGBA' for images with transparency

    if img.mode in ("P", "L", "1"):  # Handle palette-based or grayscale images
        img = img.convert("RGBA")  # Convert to RGBA for potential transparency in PNG

    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")  # Ensure a compatible mode for PNG

    # Get output file name
    output_path = output_path_func(input_path)

    # Save the image as PNG
    img.save(output_path, "png")
    print(f"Successfully converted '{input_path}' to '{output_path}'")


def convert_tiff_to_png(input_path) -> None:
    """converts TIFF to PNG"""
    # Open the TIFF image
    with Image.open(input_path) as img:
        # Save it as a PNG
        # Get output file name
        output_path = output_path_func(input_path)
        # save image
        img.save(output_path, "PNG")

    print(f"Successfully converted '{input_path}' to '{output_path}'")


def convert_avif_to_png(input_avif_path):
    """Converts an AVIF image to PNG format."""
    try:
        img = Image.open(input_avif_path)

        # Get output file name
        output_path = get_name_type(input_avif_path)
        output_path = output_path["file_name"] + ".png"

        img.save(output_path, format="PNG")
        print(f"Successfully converted '{input_avif_path}' to '{output_path}'")
    except ValueError as e:
        print(f"Error converting AVIF to PNG: {e}")


def ___main___() -> None:
    # create list of files in directory
    ## var_files = os.listdir(directory_path)
    var_files = os.listdir()

    # loop list
    for item in var_files:
        ## print(f"item\n {item}")
        ## print(f"item\n {item}")

        item_dict = get_name_type(item)
        ## item_name = item_dict["file_name"]
        item_type = item_dict["file_type"]

        if supported_file(item):
            match item_type:
                case "wdp":
                    convert_wdp_to_png(item)
                case "webp":
                    convert_webp_to_png(item)
                case "tif" | "tiff":
                    convert_tiff_to_png(item)
                case "avif":
                    convert_avif_to_png(item)

        ## item_type = item_dict["file_type"]

        ## print(f"file_info\n {file_info}")
        ## print(f"file_name\n {file_name}")
        ## print(f"file_type\n {file_type}")


___main___()
