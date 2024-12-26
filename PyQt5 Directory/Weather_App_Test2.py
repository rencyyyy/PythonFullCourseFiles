import sys
import requests
from PyQt5. QtWidgets import (QApplication, QPushButton, QLabel, QLineEdit,
                              QWidget, QVBoxLayout)
from PyQt5. QtCore import Qt
from PyQt5. QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Check weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App Test")
        self.setWindowIcon(QIcon("Images/img.png"))

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 50px;
            }
            QLineEdit#city_input{
                font-size: 70px;
                font-weight: bold;
                border-radius: 10px;
                padding: 5px;
            }
            QPushButton#get_weather_button{
                font-size: 40px;
                color: #f5ebe0;
                background-color: #023047;
                border-radius: 10px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton#get_weather_button:hover{
                color: #fdf0d5;
                background-color: #335c67;
            }
            QLabel#temperature_label{
                font-size: 80px;
                padding: 20px;
                font-weight: bold;
            }
            QLabel#emoji_label{
                font-size: 80px;
                padding: 10px;
            }
            QLabel#description_label{
                font-size: 60px;
                padding: 10px;
            }
        """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key = "751ee4b0321835ac5b40d533da1519ea"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Requests:\nClient Error")
                case 401:
                    self.display_error("Unauthorized Access:\nClient must authenticate itself")
                case 403:
                    self.display_error("Forbidden:\nThe client does not have access rights to the content")
                case 404:
                    self.display_error("Not Found:\nThe server cannot find the requested resource.")
                case 500:
                    self.display_error("Internal Server Error:\nServer Error")
                case 502:
                    self.display_error("Bad Gateway:\nServer error")
                case 503:
                    self.display_error("Service Unavailable:\nServer is not ready to handle the request.")
                case 505:
                    self.display_error("Service HTTP Version Not Supported:\nVersion is not supported by the server.")

        except requests.exceptions.ConnectionError:
            self.display_error(f"Connection Error:\nCheck your internet connection")
        except requests.exceptions.TooManyRedirects:
            self.display_error(f"The URL is stuck in a redirection loop:\nPlease check and try again.")
        except requests.exceptions.Timeout:
            self.display_error("Request Timed Out:\nPlease try again later")
        except requests.exceptions.RequestException:
            self.display_error("An error occurred while processing your request:\nPlease try again.")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.temperature_label.clear()
        self.description_label.clear()
        self.emoji_label.clear()

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.display_emoji(weather_id))
        self.description_label.setText(f"'{weather_description.capitalize()}'")
    @staticmethod
    def display_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌧️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

