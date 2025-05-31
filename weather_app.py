from flask import Flask, render_template, request
import requests

# Constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

app = Flask(__name__)

def get_weather(city):
    """
    Fetches the current weather data for a given city.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)
    return render_template("index.html", weather=weather_data)

@app.route("/details/<city>")
def details(city):
    weather_data = get_weather(city)
    return render_template("details.html", weather = weather_data)
    @app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(404)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)

