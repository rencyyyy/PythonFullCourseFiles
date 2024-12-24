import sys
import requests
from PyQt5. QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit,
                              QWidget, QVBoxLayout, QHBoxLayout)
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
        self.setWindowTitle("Weather Application")
        self.setWindowIcon(QIcon("Images/img.png"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.emoji_label)
        hbox.addWidget(self.description_label)
        vbox.addLayout(hbox)

        self.city_label.setAlignment(Qt.AlignLeft)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 20px;
            }
            QLineEdit#city_input{
                font-size: 30px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton#get_weather_button{
                color: #495057;
                font-size: 20px;
                background-color: #ade8f4;
                border-radius: 3px;
                padding: 5px
            }
            QPushButton#get_weather_button:hover{
                color: #343a40;
                font-size: 20px;
                background-color: #caf0f8;
                border-radius: 3px;
                padding: 5px
            }
            QLabel#temperature_label{
                font-size: 50px;
                padding: 15px;
            }
            QLabel#emoji_label{
                font-size: 50px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 30px;
                font-weight: bold;
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
                    print("Bad requests\nPlease check your input")
                case 401:
                    print("Unauthorized requests\nInvalid API key")
                case 403:
                    print("Forbidden\nAccess is denied")
                case 404:
                    print("Not Found\nCity not found")
                case 500:
                    print("Internal Server Error\nPlease try again later")
                case 502:
                    print("Bad Gateway\nInvalid response from the server")
                case 503:
                    print("Unavailable Service\nServer is down")
                case 504:
                    print("Gateway Timeout\nNo response from the server")
                case _:
                    print(f"HTTP Error Occured\n{http_error}")

        except requests.exceptions.ConnectionError:
            print("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            print("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            print("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            print(f"Request Error:\n{req_error}")


    def display_error(self, message):
        pass

    def display_weather(self, data):
        print(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())