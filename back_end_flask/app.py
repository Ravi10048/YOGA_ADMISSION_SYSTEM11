from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from flask_cors import CORS
# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://yogaadmission-d92d1-default-rtdb.asia-southeast1.firebasedatabase.app/"})

# Create Flask app
app = Flask(__name__)
CORS(app, resources={r"/add_data": {"origins": "http://localhost:8501"}})  # Allow requests from the Streamlit app
"""CORS stands for Cross-Origin Resource Sharing. It is a security feature implemented by web browsers to restrict web pages from making requests to a different domain than the one that served the web page"""




@app.route('/')
def index():
    return "Welcome to the Yoga Classes API!"

# API endpoint to add data
@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()
        name = data.get('Name')
        age=data.get('Age')
        prev_age=data.get('prev_age')
        batch = data.get('Batch')
        new_batch=data.get('new_batch')
        new_payment = data.get('new_payment')
        payment_month=data.get('Payment')
        prev_month=data.get('prev_month')
        print(prev_month,payment_month)
        print(prev_age,age)
        
        if age<=17 or age>66:
            return jsonify({"success": False, "message": "Age Citeria Not satisfied!"}), 500
        if new_payment==0:
            return jsonify({"success": False, "message": "Make Payment First"}), 500
        if prev_age==age:
            if new_batch !="" and prev_month==payment_month:
                return jsonify({"success": False, "message": "Can't change batch during the month"}), 500
            if prev_month==payment_month:
                return jsonify({"success": False, "message": "Make Payment for next month First"}), 500
            else :
                if new_batch=="":
                    new_batch=batch
                ref = db.reference("yoga_classes")
                data = {'Name': name, 'Age': age, 'Batch': new_batch, 'Payment': payment_month}
                ref.push(data)
                ref_batch=db.reference("Batch:"+new_batch)
                data1={'Name': name, 'Age': age,'Payment': payment_month}
                ref_batch.push(data1)
                ref_year=db.reference(payment_month+"_data")
                data2={'Name': name, 'Age': age,'Batch':new_batch}
                ref_year.push(data2)
                ref_part=db.reference("Participants")
                data3={'Name': name, 'Age': age}
                ref_part.push(data3)
                return jsonify({"success": True, "message": "Data added successfully!"}), 200 # suceesful
            
        else:
            ref = db.reference("yoga_classes")
            data = {'Name': name, 'Age': age, 'Batch': batch, 'Payment': payment_month}
            ref.push(data)
            ref_batch=db.reference("Batch:"+batch)
            data1={'Name': name, 'Age': age,'Payment': payment_month}
            ref_batch.push(data1)
            ref_year=db.reference(payment_month+"_data")
            data2={'Name': name, 'Age': age,'Batch':batch}
            ref_year.push(data2)
            ref_part=db.reference("Participants")
            data3={'Name': name, 'Age': age}
            ref_part.push(data3)
            return jsonify({"success": True, "message": "Data added successfully!"}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500   # Internal Server Error

# @app.route('/get_data', methods=['GET'])
# def get_data():
#     ref = db.reference("yoga_classes")
#     data = ref.get()
#     # print("back",data)
#     return jsonify(data)  

# API endpoint to get data
@app.route('/get_data', methods=['GET'])
def get_data():
    ref = db.reference("yoga_classes")
    whole = ref.get()
    ref=db.reference("Participants")
    part=ref.get()
    ref = db.reference("Batch:5-6AM")
    b1 = ref.get()
    ref = db.reference("Batch:6-7AM")
    b2 = ref.get()
    ref = db.reference("Batch:7-8AM")
    b3 = ref.get()
    ref = db.reference("Batch:8-9AM")
    b4 = ref.get()
    ref = db.reference("January_data")
    jan = ref.get()
    ref = db.reference("February_data")
    feb = ref.get()
    ref = db.reference("March_data")
    march = ref.get()
    ref = db.reference("April_data")
    april = ref.get()
    ref = db.reference("May_data")
    may = ref.get()
    ref = db.reference("June_data")
    jun = ref.get()
    ref = db.reference("July_data")
    july = ref.get()
    ref = db.reference("August_data")
    aug = ref.get()
    ref = db.reference("September_data")
    sep = ref.get()
    ref = db.reference("October_data")
    oct = ref.get()
    ref = db.reference("November_data")
    nov = ref.get()
    ref = db.reference("December_data")
    dec = ref.get()
    # print("back",data)
    return jsonify(whole,part,b1,b2,b3,b4,jan,feb,march,april,may,jun,july,aug,sep,oct,nov,dec)  

# if __name__ == '__main__':
#     app.run(debug=True)
