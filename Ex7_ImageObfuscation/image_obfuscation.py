import os
from PIL import Image, ImageDraw, ImageFilter

def create_dummy_image(path):
    """
    Creates a dummy image with some 'sensitive' text to demonstrate obfuscation.
    """
    img = Image.new('RGB', (400, 200), color=(240, 240, 240))
    d = ImageDraw.Draw(img)
    # Draw simple background patterns
    d.rectangle([20, 20, 380, 180], outline=(100, 100, 100), width=3)
    
    # Draw simulated sensitive data text
    d.text((50, 60), "CONFIDENTIAL DATA", fill=(200, 0, 0))
    d.text((50, 90), "Employee ID: EMP987654", fill=(0, 0, 0))
    d.text((50, 120), "SSN: 999-12-3456", fill=(0, 0, 255))
    
    img.save(path)
    print(f"[Prep] Created dummy image with sensitive data at '{path}'")

def obfuscate_by_blur(image_path, output_path, radius=10):
    """
    Applies Gaussian Blur to the entire image to obfuscate its content.
    """
    with Image.open(image_path) as img:
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius))
        blurred_img.save(output_path, 'JPEG')
        print(f"[Obfuscation] Blurred image saved to '{output_path}'")

def obfuscate_region_pixelate(image_path, output_path, box, pixel_size=10):
    """
    Obfuscates only a specific bounding box (region) using pixelation.
    Box format: (left, upper, right, lower)
    """
    with Image.open(image_path) as img:
        # Crop the sensitive region
        region = img.crop(box)
        
        # Downsample and upsample to create pixelation effect
        small = region.resize((max(1, region.width // pixel_size), max(1, region.height // pixel_size)), Image.NEAREST)
        pixelated = small.resize(region.size, Image.NEAREST)
        
        # Paste the pixelated region back onto the original image
        obfuscated_img = img.copy()
        obfuscated_img.paste(pixelated, box)
        obfuscated_img.save(output_path, 'JPEG')
        print(f"[Obfuscation] Region-pixelated image saved to '{output_path}'")

def main():
    input_image = 'original_image.jpg'
    blurred_output = 'obfuscated_image.jpg'
    pixelated_output = 'obfuscated_region_image.jpg'

    # Ensure source image exists
    create_dummy_image(input_image)

    # 1. Full Image Blurring Obfuscation
    obfuscate_by_blur(input_image, blurred_output, radius=8)

    # 2. Region-specific Pixelation (e.g. hiding only the SSN section: from y=110 to y=150)
    # Bounding box covering the SSN text: left=40, top=110, right=300, bottom=150
    ssn_box = (40, 110, 300, 150)
    obfuscate_region_pixelate(input_image, pixelated_output, ssn_box, pixel_size=8)

    print("\n--- Image Obfuscation Completed ---")
    print(f"Original image path: {os.path.abspath(input_image)}")
    print(f"Obfuscated image path: {os.path.abspath(blurred_output)}")
    print(f"Obfuscated region image path: {os.path.abspath(pixelated_output)}")

if __name__ == '__main__':
    main()

"""
EXPECTED OUTPUT:
[Prep] Created dummy image with sensitive data at 'original_image.jpg'
[Obfuscation] Blurred image saved to 'obfuscated_image.jpg'
[Obfuscation] Region-pixelated image saved to 'obfuscated_region_image.jpg'

--- Image Obfuscation Completed ---
Original image path: <absolute_path>/original_image.jpg
Obfuscated image path: <absolute_path>/obfuscated_image.jpg
Obfuscated region image path: <absolute_path>/obfuscated_region_image.jpg
"""
