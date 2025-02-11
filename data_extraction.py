import re
import json

def extract_data_from_text(text):
    # Example regex patterns for extracting data
    
    patient_name_pattern = r"Patient Name:\s*(.*)"
    dob_pattern = r"DOB:\s*(\d{2}/\d{2}/\d{4})"
    date_pattern = r"Date:\s*(\d{2}/\d{2}/\d{4})"
    injection_pattern = r"Injection:\s*(Yes|No)"
    exercise_therapy_pattern = r"Exercise Therapy:\s*(Yes|No)"
    
    # Difficulty ratings for various activities
    difficulty_patterns = {
        'bending': r"Bending:\s*(\d)",
        'putting_on_shoes': r"Putting on Shoes:\s*(\d)",
        'sleeping': r"Sleeping:\s*(\d)"
    }
    
    # Pain symptoms
    pain_patterns = {
        'pain': r"Pain:\s*(\d)",
        'numbness': r"Numbness:\s*(\d)",
        'tingling': r"Tingling:\s*(\d)",
        'burning': r"Burning:\s*(\d)",
        'tightness': r"Tightness:\s*(\d)"
    }
    
    # Example extraction process
    patient_name = re.search(patient_name_pattern, text).group(1)
    dob = re.search(dob_pattern, text).group(1)
    date = re.search(date_pattern, text).group(1)
    injection = re.search(injection_pattern, text).group(1)
    exercise_therapy = re.search(exercise_therapy_pattern, text).group(1)
    
    difficulty_ratings = {key: int(re.search(pattern, text).group(1)) for key, pattern in difficulty_patterns.items()}
    pain_symptoms = {key: int(re.search(pattern, text).group(1)) for key, pattern in pain_patterns.items()}
    
    # Create JSON structure
    data = {
        "patient_name": patient_name,
        "dob": dob,
        "date": date,
        "injection": injection,
        "exercise_therapy": exercise_therapy,
        "difficulty_ratings": difficulty_ratings,
        "pain_symptoms": pain_symptoms
    }
    
    return json.dumps(data, indent=4)

# Sample extracted text
text = """Patient Name: John Doe
DOB: 01/05/1988
Date: 02/06/2025
Injection: Yes
Exercise Therapy: No
Bending: 3
Putting on Shoes: 1
Sleeping: 2
Pain: 2
Numbness: 5
Tingling: 6
Burning: 7
Tightness: 5"""

# Extract data
extracted_data_json = extract_data_from_text(text)
print(extracted_data_json)
