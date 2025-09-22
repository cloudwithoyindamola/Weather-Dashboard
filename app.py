from flask import Flask, jsonify
import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.s3_client = boto3.client('s3')

    def create_bucket_if_not_exists(self):
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
        except:
            try:
                self.s3_client.create_bucket(Bucket=self.bucket_name)
            except Exception as e:
                print(f"Error creating bucket: {e}")

    def fetch_weather(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def save_to_s3(self, weather_data, city):
        if not weather_data:
            return False
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"
        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            return True
        except Exception as e:
            return False

dashboard = WeatherDashboard()

@app.route("/")
def home():
    return "<h1>Weather Dashboard is now Running ✅</h1><p>Visit /weather to fetch data</p>"

@app.route("/weather")
def get_weather():
    dashboard.create_bucket_if_not_exists()
    cities = ["Abuja, NG", "Lagos, NG", "Ibadan, NG"]
    results = []
    for city in cities:
        weather_data = dashboard.fetch_weather(city)
        if "error" not in weather_data:
            dashboard.save_to_s3(weather_data, city)
        results.append({city: weather_data})
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
