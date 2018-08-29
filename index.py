
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path

import mysql.connector
from mysql.connector import errorcode



form_class,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))


class MainApp(QMainWindow,form_class):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handel_buttons()
        self.Handel_DataBase_Connection()


    def InitUI(self):
        self.setWindowTitle("برنامج إدارة السيارات")
        self.tabWidget.tabBar().setVisible(False)


    def Handel_DataBase_Connection(self):

        try:
            self.cnx = mysql.connector.connect(user='root', password='01234',
                                      host='127.0.0.1',
                                      database='mydb')
            self.cursor = self.cnx.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        #else:
         #   cnx.close()






    def Handel_buttons(self):
        self.btn_Add_Car_Info.clicked.connect(self.Add_Car_Info)
        self.btn_Update_Car_Info.clicked.connect(self.Update_Car_Info)
        self.btn_Delete_Car_Info.clicked.connect(self.Delete_Car_Info)

        self.btn_Add_Fuel_Info.clicked.connect(self.Add_Fuel_Info)
        self.btn_Update_Fuel_Info.clicked.connect(self.Update_Fuel_Info)

        self.btn_Add_Maintenance_Info.clicked.connect(self.Add_Maintenance_Info)
        self.btn_Update_Maintenance_Info.clicked.connect(self.Update_Maintenance_Info)

        self.btn_Add_Licence_Info.clicked.connect(self.Add_Licence_Info)
        self.btn_Update_Licence_Info.clicked.connect(self.Update_Licence_Info)

        self.btn_Add_Revenu_Info.clicked.connect(self.Add_Revenu_Info)
        self.btn_Update_Revenu_Info.clicked.connect(self.Update_Revenu_Info)

        self.btn_Add_Rent_Info.clicked.connect(self.Add_Rent_Info)
        self.btn_Update_Rent_Info.clicked.connect(self.Update_Rent_Info)

        self.btn_Add_ElectricityWater_Info.clicked.connect(self.Add_ele_water_Info)
        self.btn_Update_ElectricityWater_Info.clicked.connect(self.Update_ele_water_Info)




    ###############################################################
    ############## Car Info  ##############

    #Add Car

    def Add_Car_Info(self):
        car_number = self.txt_Car_Car_Number.text()
        owner_company = self.txt_Car_Owner_Company.text()
        branch = self.txt_Car_Branch.text()
        service_mode = self.cbo_Car_Service_Mode.currentIndex()
        shaceh_number = self.txt_Car_Shaceh_Number.text()
        motor_number = self.txt_Car_Motor_Number.text()
        fuel_type = self.cbo_Car_Fuel_Type.currentIndex()
        car_type = self.txt_Car_Car_Type.text()
        car_model = self.txt_Car_Car_Model.text()
        car_load = self.txt_Car_Car_Load.text()
        car_weight = self.txt_Car_Car_Wieght.text()
        car_shape = self.txt_Car_Car_Shape.text()
        car_color = self.txt_Car_Car_Color.text()

        # Execute the SQL command
        self.cursor.execute("""INSERT INTO car_info(car_number,owner_company,branch,service_mode,shaceh_number,motor_number,fuel_type,car_type,car_model,car_load,car_weight,car_shape,car_color)
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            car_number, owner_company, branch, service_mode, shaceh_number, motor_number, fuel_type, car_type,
            car_model, car_load, car_weight, car_shape, car_color))

        self.cnx.commit()
          
        print("Insertion Data Into DataBase Is Done")




    #Update Car

    def Update_Car_Info(self):
        pass

    #Delete Car

    def Delete_Car_Info(self):
        pass


    ###############################################################
    ###############################################################
    ############## Fuel Info  ##############

    # Add Fuel

    def Add_Fuel_Info(self):
        pass

    # Update Fuel

    def Update_Fuel_Info(self):
        pass

    ###############################################################
    ############## Maintenance Info  ##############

    def Add_Maintenance_Info(self):
        pass


    def Update_Maintenance_Info(self):
        pass


    ###############################################################
    ############## Licence Info  ##############

    def Add_Licence_Info(self):
        pass

    def Update_Licence_Info(self):
        pass


    ###############################################################
    ############## Revenu Info  ##############

    def Add_Revenu_Info(self):
        pass

    def Update_Revenu_Info(self):
        pass


    ###############################################################
    ############## Rent Info  ##############

    def Add_Rent_Info(self):
        pass

    def Update_Rent_Info(self):
        pass


    ###############################################################
    ############## Electricity & Water Info  ##############

    def Add_ele_water_Info(self):
        pass

    def Update_ele_water_Info(self):
        pass


    ###############################################################





def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()




