import uvicorn
from fastapi import FastAPI, Query
import pickle
import pandas as pd
import warnings
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Create a FastAPI app instance
app = FastAPI()

# Load the pickled model using a relative file path
with open('model.pkl', "rb") as model_file:
    model = pickle.load(model_file)

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html>
<style>
    body {
        background-image: url(https://images.pexels.com/photos/2026324/pexels-photo-2026324.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
        background-size: cover;
        text-align: center; /* Center-align text within the body */
    }
    
    form {
        text-align: left;
    }
    
    select {
    font-size: 16px; 
    width: 102.4%; 
    box-sizing: border-box; 
    padding: 8px; 
    }
    h1 {
        font-size: 28px; /* Change the font size for the heading */
        color: #333; /* Change the text color for the heading */
        font-family: "Verdana", sans-serif;
    }

    label {
        font-size: 18px; /* Change the font size for labels */
        color: #555; /* Change the text color for labels */
    }

    input {
        font-size: 16px; /* Change the font size for input fields */
        padding: 5px; /* Add padding to input fields */
        margin: 5px 0; /* Add margin to input fields */
        width: 100%; /* Make input fields 100% width of their container */
        font-family: "Verdana", sans-serif;
    }

    input[type="submit"] {
        background-color: #007BFF; /* Change the background color for the submit button */
        color: #fff; /* Change the text color for the submit button */
        font-size: 18px; /* Change the font size for the submit button */
        padding: 10px 20px; /* Add padding to the submit button */
        cursor: pointer;
        font-family: "Verdana", sans-serif;
    }

    input[type="submit"]:hover {
        background-color: #0056b3; /* Change the background color on hover */
    }


    .header {
        background-color: rgba(255, 255, 255, 0.5);
        padding: 2px;
        border: 10px solid rgba(255, 255, 255, 0.5);
    }

    .form-container {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        margin: 20px auto; /* Add margin to create space */
        width: 50%;
        border-radius: 10px;
    }
    .header h1 
    {
        color: black; /* Set text color to white */
        font-size: 30px;
        font-family: "Verdana", sans-serif;
    }

    h2 {
        font-size: 20px; /* Change the font size for the result heading */
        color: #333; /* Change the text color for the result heading */
        font-family: "Verdana", sans-serif;
    }

    p {
        font-size: 18px; /* Change the font size for the result text */
        color: #333; /* Change the text color for the result text */
        font-family: "Verdana", sans-serif;
    }
</style>
<head>
    <title>Airport Customer Satisfaction Prediction</title>
</head>
<body>
    <div class="header">
        <img src="https://cavid0.files.wordpress.com/2016/11/adnsu-logo-1.png?w=1200" alt="University Logo" style="width: 130px; height: 130px; margin-top: 25px;">
        <h1>ASOIU University Diploma Work</h1>
    </div>
    <div class="form-container">
    <h1>Airport Satisfaction Predict</h1>
      <form id="prediction-form">
       
            <label for="age">Name:</label>
            <input type="string" id="name" name="name" required><br>
           
            <label for="gender">Gender:</label>
            <select id="gender" name="gender" required>
                <option value="Female">Female</option>
                <option value="Male">Male</option>
            </select><br>

            <label for="customer_type">Customer Type:</label>
            <select id="customer_type" name="customer_type" required>
                <option value="Disloyal Customer">Disloyal Customer</option>
                <option value="Loyal Customer">Loyal Customer</option>
            </select><br>

            
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required><br>

            <label for="type_of_travel">Type of Travel:</label>
            <select id="type_of_travel" name="type_of_travel" required>
                <option value="Personal Travel">Personal Travel</option>
                <option value="Business travel">Business travel</option>
            </select><br>

            <label for="classe">Class:</label>
            <select id="classe" name="classe" required>
                <option value="Eco">Eco</option>
                <option value="Eco Plus">Eco Plus</option>
                <option value="Business">Business</option>
            </select><br>

            <label for="flight_distance">Flight Distance:</label>
            <input type="number" id="flight_distance" name="flight_distance" required><br>

            <label for="seat_comfort">Seat comfort:</label>
            <input type="number" id="seat_comfort" name="seat_comfort" required><br>

            <label for="departure_arrival_time_convenient">Departure/Arrival time convenient:</label>
            <input type="number" id="departure_arrival_time_convenient" name="departure_arrival_time_convenient" required><br>

            <label for="food_and_drink">Food and drink:</label>
            <input type="number" id="food_and_drink" name="food_and_drink" required><br>

            <label for="gate_location">Gate location:</label>
            <input type="number" id="gate_location" name="gate_location" required><br>

            <label for="inflight_wifi_service">Inflight wifi service:</label>
            <input type="number" id="inflight_wifi_service" name="inflight_wifi_service" required><br>

            <label for="inflight_entertainment">Inflight entertainment:</label>
            <input type="number" id="inflight_entertainment" name="inflight_entertainment" required><br>

            <label for="online_support">Online support:</label>
            <input type="number" id="online_support" name="online_support" required><br>

            <label for="ease_of_online_booking">Ease of Online booking:</label>
            <input type="number" id="ease_of_online_booking" name="ease_of_online_booking" required><br>

            <label for="on_board_service">On-board service:</label>
            <input type="number" id="on_board_service" name="on_board_service" required><br>

            <label for="leg_room_service">Leg room service:</label>
            <input type="number" id="leg_room_service" name="leg_room_service" required><br>

            <label for="baggage_handling">Baggage handling:</label>
            <input type="number" id="baggage_handling" name="baggage_handling" required><br>

            <label for="checkin_service">Checkin service:</label>
            <input type="number" id="checkin_service" name="checkin_service" required><br>

            <label for="cleanliness">Cleanliness:</label>
            <input type="number" id="cleanliness" name="cleanliness" required><br>

            <label for="online_boarding">Online boarding:</label>
            <input type="number" id="online_boarding" name="online_boarding" required><br>

            <label for="departure_delay">Departure Delay in Minutes:</label>
            <input type="number" id="departure_delay" name="departure_delay" required><br>

            <label for="arrival_delay">Arrival Delay in Minutes:</label>
            <input type="number" id="arrival_delay" name="arrival_delay" required><br>

        <input type="submit" value="Predict Satisfaction">
    </form>
    <h2>Prediction Result:</h2>
    <p id="prediction_result"></p>
    </div>
    <script>
        const form = document.querySelector('form');
        const predictionResult = document.getElementById('prediction_result');
        
        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const formData = new FormData(form);
            
            const response = await fetch('/predict/?' + new URLSearchParams(formData).toString());
            const data = await response.json();
            
            predictionResult.textContent = data['prediction'];
        });
    </script>
</body>
</html>
"""

# Define the endpoint to serve the HTML content
@app.get("/", response_class=HTMLResponse)
async def serve_html():
    return HTMLResponse(content=html_content)

# Define the endpoint to make predictions
@app.get("/predict/")
async def predict(
    name: str = Query(...),
    gender: str = Query(...),
    customer_type: str = Query(...),
    age: int = Query(...),
    type_of_travel: str = Query(...),
    classe : str = Query(...),
    flight_distance: int = Query(...),
    seat_comfort: int = Query(...),
    departure_arrival_time_convenient: int = Query(...),
    food_and_drink: int = Query(...),
    gate_location: int = Query(...),
    inflight_wifi_service: int = Query(...),
    inflight_entertainment: int = Query(...),
    online_support: int = Query(...),
    ease_of_online_booking: int = Query(...),
    on_board_service: int = Query(...),
    leg_room_service: int = Query(...),
    baggage_handling: int = Query(...),
    checkin_service: int = Query(...),
    cleanliness: int = Query(...),
    online_boarding: int = Query(...),
    departure_delay: int = Query(...),
    arrival_delay: int = Query(...)
    ):
    # Create a DataFrame from the input data
    data = pd.DataFrame({'Name':[name],
        'Gender': [gender],  # replace with the actual value
        'Customer Type': [customer_type],  # replace with the actual value
        'Age': [age],  # replace with the actual value
        'Type of Travel': [type_of_travel],  # replace with the actual value
        'Class': [classe],  # replace with the actual value
        'Flight Distance': [flight_distance],  # replace with the actual value
        'Seat comfort': [seat_comfort],  # replace with the actual value
        'Departure/Arrival time convenient': [departure_arrival_time_convenient],  # replace with the actual value
        'Food and drink': [food_and_drink],  # replace with the actual value
        'Gate location': [gate_location],  # replace with the actual value
        'Inflight wifi service': [inflight_wifi_service],  # replace with the actual value
        'Inflight entertainment': [inflight_entertainment],  # replace with the actual value
        'Online support': [online_support],  # replace with the actual value
        'Ease of Online booking': [ease_of_online_booking],  # replace with the actual value
        'On-board service': [on_board_service],  # replace with the actual value
        'Leg room service': [leg_room_service],  # replace with the actual value
        'Baggage handling': [baggage_handling],  # replace with the actual value
        'Checkin service': [checkin_service],  # replace with the actual value
        'Cleanliness': [cleanliness],  # replace with the actual value
        'Online boarding': [online_boarding],  # replace with the actual value
        'Departure Delay in Minutes': [departure_delay],  # replace with the actual value
        'Arrival Delay in Minutes': [arrival_delay],  # replace with the actual value
    })
    data['Gender'] = data['Gender'].map({'Female':0,'Male':1})
    data['Customer Type'] = data['Customer Type'].map({'Disloyal Customer':0,'Loyal Customer':1})
    data['Type of Travel'] = data['Type of Travel'].map({'Personal Travel':0,'Business travel':1})
    data['Class'] = data['Class'].map({'Eco':0,'Eco Plus':1,'Business':2})
    # Make predictions using the pre-trained model
    predictions = model.predict(data.drop(['Name'], axis = 1))
    columns_of_interest = data[['Seat comfort', 'Food and drink', 'Gate location',
       'Inflight wifi service', 'Inflight entertainment', 'Online support',
       'Ease of Online booking', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Cleanliness', 'Online boarding']]

    min_column = min(columns_of_interest, key=lambda col: data[col].values[0])
    max_column = max(columns_of_interest, key=lambda col: data[col].values[0])

    min_value = data[min_column].values[0]
    min_columns = [col for col in columns_of_interest if data[col].values[0] == min_value]

    if predictions[0] == 0:
        if len(min_columns) == 1:
            prediction_result = f"{name}'s satisfaction level is Unsatisfied. It is {min_columns[0]} that does not satisfy {name}. We value your feedback and apologize for any inconvenience."
        else:
            services_str = ', '.join(min_columns[:-1]) + f", and {min_columns[-1]}"
            prediction_result = f"{name}'s satisfaction level is Unsatisfied. The services {services_str} do not satisfy {name}. We value your feedback and apologize for any inconvenience."
    else:
        max_value = data[max_column].values[0]
        max_columns = [col for col in columns_of_interest if data[col].values[0] == max_value]
        if len(max_columns) == 1:
            prediction_result = f"{name}'s satisfaction level is Satisfied. {max_columns[0]} is very satisfying to {name}. We appreciate your positive experience and thank you for choosing our services."
        else:
            services_str = ', '.join(max_columns[:-1]) + f", and {max_columns[-1]}"
            prediction_result = f"{name}'s satisfaction level is Satisfied. The services {services_str} are very satisfying to {name}. We appreciate your positive experience and thank you for choosing our services."

    return {"prediction": prediction_result}


# Run the FastAPI app using Uvicorn
if __name__ == '__main__':
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5002,
        log_level="debug",
    )
