# Import necessary modules for Flask application
from flask import Flask, render_template, request
import requests

# Initialize the Flask app
app = Flask(__name__)

# Function to fetch the IP details using an external API
def get_fetch_ip_details(user_ip):
    try:
        # Making a GET request to fetch the IP details in JSON format
        response = requests.get(f"http://ip-api.com/json/{user_ip}")
        json_data = response.json()

        # Check if the status of the request is 'fail', return None in that case
        if json_data['status'] == 'fail':
            return None
        
        else:
            # Prepare a dictionary with the IP details to send to the frontend
            ip_deatils = {
            'ip': json_data['query'],
            'city': json_data['city'],
            'region': json_data['regionName'],
            'country': json_data['country'],
            'isp': json_data['isp'],
            'latitude': json_data['lat'],
            'longitude': json_data['lon'],
            'timezone': json_data['timezone'],
            }
            
            return ip_deatils
    
    except:
        # Return None in case of any error during the API call
        return None

# Route to handle the homepage request
@app.route("/")
def index():
    # Fetch the IP details of the user's IP address
    ipdata = get_fetch_ip_details(request.remote_addr)
    # Render the HTML template and pass the IP details to the template
    return render_template("index.html", ipdata=ipdata)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
