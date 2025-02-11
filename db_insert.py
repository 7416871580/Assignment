import psycopg2
import json

# Database connection parameters
conn = psycopg2.connect(
    dbname="your_dbname", 
    user="your_user", 
    password="your_password", 
    host="localhost", 
    port="5432"
)

def insert_data_to_db(patient_data_json):
    cursor = conn.cursor()
    
    # Insert patient data into 'patients' table
    patient_name = patient_data_json["patient_name"]
    dob = patient_data_json["dob"]
    cursor.execute(
        "INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id", 
        (patient_name, dob)
    )
    patient_id = cursor.fetchone()[0]
    
    # Insert form data (JSON) into 'forms_data' table
    form_json = json.dumps(patient_data_json)  # Ensure data is in JSON format
    cursor.execute(
        "INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s)", 
        (patient_id, form_json)
    )
    
    conn.commit()
    cursor.close()

# Assuming extracted_data_json is your JSON data
extracted_data_json = json.loads('''{
    "patient_name": "John Doe",
    "dob": "01/05/1988",
    "date": "02/06/2025",
    "injection": "Yes",
    "exercise_therapy": "No",
    "difficulty_ratings": {
        "bending": 3,
        "putting_on_shoes": 1,
        "sleeping": 2
    },
    "pain_symptoms": {
        "pain": 2,
        "numbness": 5,
        "tingling": 6,
        "burning": 7,
        "tightness": 5
    }
}''')

insert_data_to_db(extracted_data_json)
