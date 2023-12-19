
# Yoga Admission System

## Overview
The Yoga Admission System is a web application built with Flask, Streamlit, and Firebase. It allows users to enroll in yoga classes, make payments, and view class records.

Public web app link -  https://yogaadmissionsystem11-raxcxtb9op3mhrbrexqgwi.streamlit.app/

Backend server link - https://yoga-admission-form11.onrender.com


## Features
- **Admission Form:** Fill out a form to enroll in yoga classes.
- **Records:** View records for yoga classes, participants, and monthly data.

## Screenshot  Admission Form

![s1](https://github.com/Ravi10048/YOGA_ADMISSION_SYSTEM11/assets/116975230/629b63ad-7e24-4661-988a-4e613ae4a58f)

## Screenshot  Participants enrolled in Classes

![s1](https://github.com/Ravi10048/YOGA_ADMISSION_SYSTEM11/assets/116975230/629b63ad-7e24-4661-988a-4e613ae4a58f)


## Terms and Condition regarding Enrollement
- **Age Limit:** Participants must be within the age range of 18 to 65 years to enroll for the monthly yoga classes.

- **Monthly Fee:** The monthly fee for the yoga classes is 500/- Rs INR.

- **Enrollment Procedure:**
  - Participants can enroll at any time during the month.
  - Enrollment is for the entire month, and participants are required to pay the monthly fee.

- **Payment Details:**
  - Participants have the flexibility to pay their fees at any time during the month.
  - Monthly fees are due on a month-to-month basis.

- **Batch Selection:**
  - There are four batches available each day:
    - 6-7AM
    - 7-8AM
    - 8-9AM
    - 5-6PM
  - Participants can choose any batch for a given month.
  - Batch selection can be changed from one month to another.

- **Batch Shifts:**
  - Participants are allowed to move from one batch to another between different months.
  - However, participants need to remain in the same batch throughout a given month.



## Technologies Used
- Flask: Backend API
- Streamlit: Frontend UI
- Firebase: Database


## Getting Started
1. Clone the repository: `https://github.com/Ravi10048/YOGA_ADMISSION_SYSTEM11`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Firebase: Replace the `serviceAccountKey.json` file with your Firebase credentials.
4. Run the Flask app: `gunicorn app:app`
5. Open the Streamlit app: Visit `https://your-streamlit-app-url`


## Project Structure
- `app.py`: Flask backend code
- `main.py`: Streamlit frontend code
- `serviceAccountKey.json`: Firebase credentials


## API Endpoints
- `/add_data`: Add participant data (POST request)
- `/get_data`: Get yoga class data (GET request)

## Contributing
Contributions are welcome! If you find any issues or have improvements, feel free to create a pull request.


## Screenshots Yoga Class Table and Participant Table

![s3](https://github.com/Ravi10048/YOGA_ADMISSION_SYSTEM11/assets/116975230/78add70d-4c9a-44a5-92ff-d34a40ab6331)

## Screenshots Batch wise Table 

![s4](https://github.com/Ravi10048/YOGA_ADMISSION_SYSTEM11/assets/116975230/207f3441-7d22-4d7d-bfb5-daf3f02f593d)

