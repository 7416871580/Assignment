import cv2
import pytesseract
from PIL import Image

# Path to Tesseract executable (adjust according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust for your Tesseract installation path

def extract_text_from_image(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Preprocessing: Convert to grayscale and threshold to improve accuracy
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Run OCR on the preprocessed image
    text = pytesseract.image_to_string(thresh)
    
    return text

# Test the function with an image path
image_path = 'patient-assessment-template.jpg'  # Replace with your image path
extracted_text = extract_text_from_image(image_path)
print(extracted_text)
