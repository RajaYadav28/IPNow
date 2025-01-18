from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_fetch_ip_details(user_ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{user_ip}")
        json_data = response.json()

        if json_data['status'] == 'fail':
            return None
        
        else:
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
        return None


@app.route("/")
def index():
    ipdata = get_fetch_ip_details(request.remote_addr)
    return render_template("index.html", ipdata=ipdata)


if __name__ == "__main__":
    app.run(debug=True)