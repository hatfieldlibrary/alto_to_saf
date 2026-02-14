from PIL import Image
import os

def convert_jp2_to_jpg_thumbnail(input_path, output_path, size=(128, 128)):
    """
    Converts a JP2 image to a JPG thumbnail using Pillow.

    Args:
        input_path (str): Path to the input .jp2 file.
        output_path (str): Path for the output .jpg thumbnail file.
        size (tuple): Desired size of the thumbnail (width, height).
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Convert to RGB mode if necessary for JPEG compatibility (JP2 can be different modes)
            if img.mode in ('RGBA', 'P', 'LA', 'CMYK'):
                img = img.convert('RGB')

            # Create the thumbnail (modifies the image in-place to fit the size while maintaining aspect ratio)
            img.thumbnail(size, Image.Resampling.LANCZOS)

            # Save the image in JPG format
            img.save(output_path, 'JPEG')
            print(f"Successfully converted and saved thumbnail to {output_path}")

    except IOError as e:
        print(f"Error converting image: {e}")

# Example usage:
# Ensure you have a 'source.jp2' file and want to save as 'thumbnail.jpg'
# convert_jp2_to_jpg_thumbnail('source.jp2', 'thumbnail.jpg', size=(150, 150))
