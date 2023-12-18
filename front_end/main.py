
import streamlit as st
import requests,time
import pandas as pd
from PIL import Image
from json.decoder import JSONDecodeError
from streamlit_option_menu import option_menu

st.markdown(
    f"""
    <style>
        body {{
            background-color: {"#FFFFFF"};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Yoga Classes',
                          
                          ['Admission Form',
                           'Records'], # multiple pages 
                          icons=['activity','map'],
                          default_index=0)
if (selected == 'Admission Form'):
    col1, col2, col3 = st.columns([1, 1, 1])
    st.title('Yoga Classes Admission Form')

    image1=Image.open("D:/python/solar secure/flexi/yoga1.png")
    image1=image1.resize((150,200))
    # st.image(image1)
    col2.image(image1)

    def send_data_to_flask(participant_data):
        flask_api_url = "http://localhost:5000/add_data"
        try:
            response = requests.post(flask_api_url, json=participant_data)
            response_json = response.json()  # Try to parse the response as JSON

            # Check if the response is a valid JSON
            if response_json:
                return response_json
            else:
                print(f"Invalid JSON response: {response.text}")
                return {"success": False, "message": "Invalid JSON response from the server."}

        except requests.exceptions.RequestException as e:
            print(f"Failed to send data to Flask. Error: {e}")
            return {"success": False, "message": f"Failed to send data to Flask. Error: {e}"}
        except requests.exceptions.JSONDecodeError as e:
            print(f"Failed to decode JSON response. Error: {e}")
            return {"success": False, "message": f"Failed to decode JSON response. Error: {e}"}


    def fetch_previous_details(name):
        try:
            response = requests.get("http://localhost:5000/get_data")
            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                data,part,b1,b2,b3,b4,jan,feb,march,april,may,jun,july,aug,sep,oct,nov,dec = response.json()
                
                # print(data)
                keys_list = list(data.keys())[::-1]
                for participant_key in keys_list:
                    participant_data = data[participant_key]
                    if participant_data.get('Name') == name:
                        prev_month = participant_data.get('Payment')
                        prev_age=participant_data.get('Age')
                        return prev_month,prev_age
                # If no matching participant is found
                return "NA",0
            else:
                print(f"Error: Received status code {response.status_code} from the server.")
                return "NA",0
        except:
            st.write("error")    

    def yoga_admission_form():
        # Get user inputs
        name = st.text_input('Full Name')
        name=name.upper()
        age = st.number_input('Age',step=1)
        selected_batch = st.selectbox('Select Batch', ['6-7AM', '7-8AM', '8-9AM', '5-6PM'], key='unique_key_for_batch_selection')

        # Input field for the new batch for update
        # new_batch = st.selectbox('New Batch (if updating)', ['6-7AM', '7-8AM', '8-9AM', '5-6PM'], key='unique_key_for_new_selection')
        new_batch=st.text_input('New Batch (if updating)')

        # Dropdown for payment month
        payment_month = st.selectbox('Select Month for Payment', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

        # Input field for the new payment amount
        # new_payment = st.number_input(f"Enter Payment Amount for {payment_month}:",value=500, key='new_payment')
        new_payment = st.selectbox('Make Payment', [0,500])
        if st.button('Enroll'):
            prev_month,prev_age=fetch_previous_details(name)
            participant_data = {'Name': name, 'Age': age, 'Batch': selected_batch, 'Payment': payment_month,"new_payment":new_payment,'new_batch':new_batch,'prev_month':prev_month,'prev_age':prev_age}
            response = send_data_to_flask(participant_data)
    
            if response.get("success"):
                if new_payment!=0:
                    st.success("Payment Succesfull")
                else:
                    st.error("Make Payment First")    
                # st.success("Data sent to Flask successfully!")

                # Wait for a short time before making the GET request
            else:
                st.error(f"Failed Transaction : {response.get('message')}")
            
            time.sleep(1)  # You can adjust the delay as needed
                
            try:
                data,part,b1,b2,b3,b4,jan,feb,march,april,may,jun,july,aug,sep,oct,nov,dec= requests.get("http://localhost:5000/get_data").json()
                # print("output data:", data)
                    
                # Display each entry individually
                st.subheader("Yoga Classes Data:")
                # Convert the dictionary to a Pandas DataFrame
                col=['Name','Age','Batch','Payment']
                # df = pd.DataFrame(list(data.values()), index=data.keys(), columns=data[list(data.keys())[0]].keys())
                df = pd.DataFrame(list(data.values()),columns=col)
                # df.drop('index',inplace=True)
                st.table(df.tail())
            except JSONDecodeError:
                    st.error("Invalid JSON data received from the server.")
    yoga_admission_form()
elif (selected == 'Records'):
    try:
        whole,part,b1,b2,b3,b4,jan,feb,march,april,may,jun,july,aug,sep,oct,nov,dec = requests.get("http://localhost:5000/get_data").json()   
        # Display each entry individually
        st.subheader("Yoga Classes Table:")
        # Convert the dictionary to a Pandas DataFrame
        col=['Name','Age','Batch','Payment']
        # df.drop('index',inplace=True)
        st.table(pd.DataFrame(list(whole.values()),columns=col).tail())
        if part is not None:
            col=['Name','Age']
            st.subheader('Participants_Table:')
            st.table(pd.DataFrame(list(part.values()),columns=col).tail())
        col=['Name','Age','Payment']
        if b1 is not None:
            st.subheader('BATCH 5-6AM:')
            st.table(pd.DataFrame(list(b1.values()),columns=col).tail())
        if b2 is not None:
            st.subheader('BATCH 6-7AM:')
            st.table(pd.DataFrame(list(b2.values()),columns=col).tail())
        if b3 is not None:
            st.subheader('BATCH 7-8AM:')
            st.table(pd.DataFrame(list(b3.values()),columns=col).tail())
        if b4 is not None:
            st.subheader('BATCH 8-9AM:')
            st.table(pd.DataFrame(list(b4.values()),columns=col).tail())
        col=['Name','Age','Batch']    
        if jan is not None:
            st.subheader('January_data:')
            st.table(pd.DataFrame(list(jan.values()),columns=col).tail())
        if feb is not None:
            st.subheader('February_data:')
            st.table(pd.DataFrame(list(feb.values()),columns=col).tail())
        if march is not None:
            st.subheader('March_data:')
            st.table(pd.DataFrame(list(march.values()),columns=col).tail())
        if april is not None:
            st.subheader('April_data:')
            st.table(pd.DataFrame(list(april.values()),columns=col).tail())
        if may is not None:
            st.subheader('May_data:')
            st.table(pd.DataFrame(list(may.values()),columns=col).tail())
        if jun is not None:
            st.subheader('June_data:')
            st.table(pd.DataFrame(list(jun.values()),columns=col).tail())
        if july is not None:
            st.subheader('July_data:')
            st.table(pd.DataFrame(list(july.values()),columns=col).tail())
        if aug is not None:
            st.subheader('August_data:')
            st.table(pd.DataFrame(list(aug.values()),columns=col).tail()) 
        if sep is not None:
            st.subheader('September_data:')
            st.table(pd.DataFrame(list(sep.values()),columns=col).tail())
        if oct is not None:
            st.subheader('October_data:')
            st.table(pd.DataFrame(list(oct.values()),columns=col).tail())
        if nov is not None:
            st.subheader('November_data:')
            st.table(pd.DataFrame(list(nov.values()),columns=col).tail())
        if dec is not None:
            st.subheader('December_data:')
            st.table(pd.DataFrame(list(dec.values()),columns=col).tail())           


    except JSONDecodeError:
                    st.error("Invalid JSON data received from the server.")




