# Implement Any Image Obfuscation Mechanism

## Aim
To implement an image obfuscation system in Python using image processing filters (Gaussian blurring and localized region-of-interest pixelation) to redact sensitive data fields.

## Theory
Image obfuscation is the process of modifying an image to make sensitive parts (such as faces, license plates, or confidential documents) unreadable or unidentifiable, while keeping the rest of the image intact or demonstrating full-image protection.
- **Gaussian Blur**: A filter that blends neighboring pixel values using a Gaussian mathematical function. The parameter `radius` controls the blur strength.
- **Pixelation**: Downsampling a specific region of an image to a very low resolution, then scaling it back up using nearest-neighbor interpolation. This maps blocks of pixels to single values, permanently destroying high-frequency features (fine text/faces) while preserving general shapes.
- **Bounding Boxes / Region-of-Interest (ROI)**: Identifying coordinates (Left, Top, Right, Bottom) to apply obfuscation selectively rather than degrading the entire image.

## Algorithm
1. **Load Target Image**: Read the target image file using the `Pillow` library.
2. **Apply Full-Image Obfuscation (Gaussian Blur)**:
   - Apply `ImageFilter.GaussianBlur` with a radius of $R$.
   - Save the fully blurred image to a file.
3. **Apply Selective Obfuscation (Pixelation)**:
   - Define a bounding box $(x_1, y_1, x_2, y_2)$ corresponding to the sensitive region (e.g., SSN text or face).
   - Crop the sub-image within the bounding box.
   - Resize the cropped region down by a scale factor $S$ (e.g., $10\times$ smaller).
   - Resize the tiny image back to its original size using Nearest Neighbor interpolation.
   - Paste the pixelated region back onto the original image.
   - Save the partially redacted image to a file.
4. **Output Paths**: Display the file paths of the processed images.

## Requirements
- Python 3.x
- Pillow (`pip install Pillow`)

## How to Run
1. Run the Python script:
   ```bash
   python image_obfuscation.py
   ```

## Sample Output
```
[Prep] Created dummy image with sensitive data at 'original_image.jpg'
[Obfuscation] Blurred image saved to 'obfuscated_image.jpg'
[Obfuscation] Region-pixelated image saved to 'obfuscated_region_image.jpg'

--- Image Obfuscation Completed ---
Original image path: C:\Users\Sivap\Documents\lab\SPC\Ex7_ImageObfuscation\original_image.jpg
Obfuscated image path: C:\Users\Sivap\Documents\lab\SPC\Ex7_ImageObfuscation\obfuscated_image.jpg
Obfuscated region image path: C:\Users\Sivap\Documents\lab\SPC\Ex7_ImageObfuscation\obfuscated_region_image.jpg
```

## Result
Image obfuscation was successfully implemented in Python. The script successfully demonstrated both full-image Gaussian blurring and region-of-interest pixelation to secure sensitive fields within an image.
