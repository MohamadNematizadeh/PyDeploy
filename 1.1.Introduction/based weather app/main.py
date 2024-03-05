import json
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from requests import get as getWeather

app = QApplication([])

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        self.ui1 = loader.load("ui/Home.ui")
        self.ui2 = loader.load("ui/main.ui")
        self.error = loader.load("ui/error.ui")
        self.ui1.show()
        self.ui1.result_board.setIcon(QIcon("icon/app.png"))
        self.ui1.pushButton_select.clicked.connect(self.City)

    def City(self):
        cityName = self.ui1.lineEdit_cityName.text()
        self.cityName(cityName)
       
    def cityName(self,cityName):
        print(cityName)
        response = getWeather("http://goweather.herokuapp.com/weather/"+cityName)
        print(response.status_code)
        if response.status_code == 200:
            weather = json.loads(response.text)
            self.ui2.label_14.setText(cityName)
            print(response.text)
            self.ui2.show()
            self.ui1.close() 
            description = weather["description"]
            if description == "Sunny":
                    self.ui2.result_board_2.setIcon(QIcon("icon/sune.png"))

            elif description == "Clear":
                    self.ui2.result_board_2.setIcon(QIcon("icon/Cloudy.png"))

            elif description == "Partly cloudy":
                    self.ui2.result_board_2.setIcon(QIcon("icon/app.png"))

            elif description == "Rainny":
                    self.ui2.result_board_2.setIcon(QIcon("icon/Rainny.png"))

            elif description == "Light rain, mist":
                    self.ui2.result_board_2.setIcon(QIcon("icon/Layer3.png"))
            else:
                    self.ui2.result_board_2.setIcon(QIcon("icon/sune.png"))

            #Forecasts Next 3 days
            self.ui2.label_2.setText(weather["wind"])
            self.ui2.result_board_3.setIcon(QIcon("icon/Layer2.png"))
            self.ui2.result_board_4.setIcon(QIcon("icon/Layer4.png"))
            self.ui2.label_3.setText(weather["temperature"])
            temp = weather.get("forecast")
            weather1 = temp[0]
            weather2 = temp[1]
            weather3 = temp[2]
            self.ui2.label_8.setText("temperature :"+weather1.get("temperature"))
            self.ui2.label_9.setText("wind :"+weather1.get("wind"))
            self.ui2.label_10.setText("temperature :"+weather2.get("temperature"))
            self.ui2.label_11.setText("wind :"+weather2.get("wind"))
            self.ui2.label_12.setText("temperature :"+weather3.get("temperature"))
            self.ui2.label_13.setText("wind :"+weather3.get("wind"))
            self.ui2.change_city.clicked.connect(self.ui)
            self.ui2.exit.clicked.connect(self.exit)
        else :
                self.error.show()
                self.ui1.close() 
                self.error.pushButton.clicked.connect(self.ui1.show())

            
    def ui(self):
            self.ui1.show()
            self.ui2.close() 
    def exit(self):
            self.ui2.close() 




if __name__ == "__main__":
    main_window = MainWindow()
    app.exec()