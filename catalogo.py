# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mayra\OneDrive\Escritorio\Facu\5to Semestre\Visualizacion\catalogo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mysql
from mysql.connector.errors import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from agregar_reseña import Ui_MainWindow as agregar_reseña
from Eliminar_actualizar_reseña import Ui_MainWindow as editar_reseña

class Ui_catalogo(object):
        V_IdUsuario = ""
        lstDatos = []
        mtzDatos =[]

        def set_values(self, value1, value2):
                self.value1 = value1
                self.value2 = value2
        def init(self, P_nombre, P_Usuario):
                self.V_IdUsuario = P_nombre

        def setupUi(self, catalogo):
                catalogo.setObjectName("catalogo")
                catalogo.resize(805, 687)
                catalogo.setStyleSheet("background-color:rgb(85, 0, 255)")
                self.centralwidget = QtWidgets.QWidget(catalogo)
                self.centralwidget.setObjectName("centralwidget")
                self.netflix = QtWidgets.QLabel(self.centralwidget)
                self.netflix.setGeometry(QtCore.QRect(170, 20, 281, 71))
                self.netflix.setStyleSheet("")
                self.netflix.setObjectName("netflix")
                self.titulo_catalogo = QtWidgets.QLabel(self.centralwidget)
                self.titulo_catalogo.setGeometry(QtCore.QRect(260, 100, 111, 31))
                self.titulo_catalogo.setObjectName("titulo_catalogo")
                self.agregar_resena = QtWidgets.QPushButton(self.centralwidget)
                self.agregar_resena.setGeometry(QtCore.QRect(580, 420, 121, 31))
                font = QtGui.QFont()
                font.setFamily("Calibri")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.agregar_resena.setFont(font)
                self.agregar_resena.setStyleSheet("QPushButton{\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(111, 118, 255);\n"
        "border-radius: 10px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "color: rgb(255, 255, 0);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "background-color:rgb(121, 139, 255);\n"
        "}")
                self.agregar_resena.setObjectName("agregar_resena")
                self.error = QtWidgets.QLabel(self.centralwidget)
                self.error.setGeometry(QtCore.QRect(370, 460, 211, 16))
                self.error.setStyleSheet("font: 10pt \"Gill Sans MT\";color:red;")
                self.error.setText("")
                self.error.setObjectName("error")
                self.editar_resena = QtWidgets.QPushButton(self.centralwidget)
                self.editar_resena.setGeometry(QtCore.QRect(580, 480, 121, 31))
                font = QtGui.QFont()
                font.setFamily("Calibri")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.editar_resena.setFont(font)
                self.editar_resena.setStyleSheet("QPushButton{\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(111, 118, 255);\n"
        "border-radius: 10px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "color: rgb(255, 255, 0);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "background-color:rgb(121, 139, 255);\n"
        "}")
                self.editar_resena.setObjectName("editar_resena")
                self.salir_catalogo = QtWidgets.QPushButton(self.centralwidget)
                self.salir_catalogo.setGeometry(QtCore.QRect(570, 530, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Calibri")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.salir_catalogo.setFont(font)
                self.salir_catalogo.setStyleSheet("QPushButton{\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(111, 118, 255);\n"
        "border-radius: 10px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "color: rgb(255, 255, 0);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "background-color:rgb(121, 139, 255);\n"
        "}")
                self.salir_catalogo.setObjectName("salir_catalogo")
                self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
                self.tableWidget.setGeometry(QtCore.QRect(190, 410, 301, 161))
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(3)
                self.tableWidget.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
                self.tableWidget_2.setGeometry(QtCore.QRect(130, 150, 401, 191))
                self.tableWidget_2.setObjectName("tableWidget_2")
                self.tableWidget_2.setColumnCount(4)
                self.tableWidget_2.setRowCount(5)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setVerticalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setVerticalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setVerticalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setVerticalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setVerticalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(3, item)
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(140, 360, 381, 31))
                self.widget.setObjectName("widget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label_3 = QtWidgets.QLabel(self.widget)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.horizontalLayout.addWidget(self.label_3)
                self.campopassword = QtWidgets.QLineEdit(self.widget)
                self.campopassword.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.campopassword.setText("")
                self.campopassword.setObjectName("campopassword")
                self.horizontalLayout.addWidget(self.campopassword)
                self.buscar_id = QtWidgets.QPushButton(self.widget)
                font = QtGui.QFont()
                font.setFamily("Calibri")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.buscar_id.setFont(font)
                self.buscar_id.setStyleSheet("QPushButton{\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: rgb(111, 118, 255);\n"
        "border-radius: 10px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "color: rgb(255, 255, 0);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "background-color:rgb(121, 139, 255);\n"
        "}")
                self.buscar_id.setObjectName("buscar_id")
                self.horizontalLayout.addWidget(self.buscar_id)
                
                self.buscar_id.clicked.connect(self.buscar_id_clicked)
                self.agregar_resena.clicked.connect(self.agregar_resena_clicked)
                self.editar_resena.clicked.connect(self.editar_resena_clicked)
                self.salir_catalogo.clicked.connect(self.salir_catalogo_clicked)
                
                catalogo.setCentralWidget(self.centralwidget)
                self.retranslateUi(catalogo)
                QtCore.QMetaObject.connectSlotsByName(catalogo)

        def retranslateUi(self, catalogo):
                _translate = QtCore.QCoreApplication.translate
                catalogo.setWindowTitle(_translate("catalogo", "catalogo"))
                self.netflix.setText(_translate("catalogo", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">HBO</span></p></body></html>"))
                self.titulo_catalogo.setText(_translate("catalogo", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Cátalogo</span></p><p><br/></p></body></html>"))
                self.agregar_resena.setText(_translate("catalogo", "Agregar reseña"))
                self.editar_resena.setText(_translate("catalogo", "Editar reseña"))
                self.salir_catalogo.setText(_translate("catalogo", "Salir"))
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("catalogo", "ID"))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("catalogo", "Comentario"))
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText(_translate("catalogo", "Calificacion"))
                item = self.tableWidget_2.verticalHeaderItem(0)
                item.setText(_translate("catalogo", "1"))
                item = self.tableWidget_2.verticalHeaderItem(1)
                item.setText(_translate("catalogo", "2"))
                item = self.tableWidget_2.verticalHeaderItem(2)
                item.setText(_translate("catalogo", "3"))
                item = self.tableWidget_2.verticalHeaderItem(3)
                item.setText(_translate("catalogo", "4"))
                item = self.tableWidget_2.verticalHeaderItem(4)
                item.setText(_translate("catalogo", "5"))
                item = self.tableWidget_2.horizontalHeaderItem(0)
                item.setText(_translate("catalogo", "id"))
                item = self.tableWidget_2.horizontalHeaderItem(1)
                item.setText(_translate("catalogo", "Nombre"))
                item = self.tableWidget_2.horizontalHeaderItem(2)
                item.setText(_translate("catalogo", "Tipo"))
                item = self.tableWidget_2.horizontalHeaderItem(3)
                item.setText(_translate("catalogo", "Género"))
                self.label_3.setText(_translate("catalogo", "<html><head/><body><p>Ingresa el ID deseado</p></body></html>"))
                self.buscar_id.setText(_translate("catalogo", "buscar"))

        def salir_catalogo_clicked(self):
                catalogo.close()

        def buscar_id_clicked(self):
                id_Pelicula = self.campopassword.text()
                
                result_pelicula = self.ConexionDB_pelicula(id_Pelicula)
                result_reseña = self.ConexionDB_reseña(id_Pelicula)

                if result_pelicula:
                        self.muestra_informacion(result_pelicula, result_reseña)
                else:
                        self.mostrar_error("ID no encontrado")
        
        def agregar_resena_clicked(self):
                print("La función agregar_resena_clicked se ha llamado")
                self.window = QtWidgets.QMainWindow()
                self.ui = agregar_reseña()
                self.ui.setupUi(self.window)
                self.window.show()
        
        def editar_resena_clicked(self):
                print("La función editar_resena_clicked se ha llamado")
                self.window = QtWidgets.QMainWindow()
                self.ui = editar_reseña()
                self.ui.setupUi(self.window)
                self.window.show()

        def muestra_informacion(self, result_pelicula, result_reseña):
                self.limpiar_tablas()

                if result_pelicula and isinstance(result_pelicula[0], (list, tuple)):
                        id_Pelicula, nombre, tipo, Genero_id_Genero = result_pelicula[0]
                
                rowPosition = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(rowPosition)

                self.tableWidget_2.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(id_Pelicula)))
                self.tableWidget_2.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(nombre)))
                self.tableWidget_2.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(tipo)))
                self.tableWidget_2.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(Genero_id_Genero)))


                if result_reseña:
                        for result in result_reseña:
                                if isinstance(result, (list, tuple)):
                                        id_Reseña, comentario, calificacion = result

                                rowPosition = self.tableWidget.rowCount()
                                self.tableWidget.insertRow(rowPosition)

                                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(id_Reseña)))
                                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(comentario)))
                                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(calificacion)))

        def limpiar_tablas(self):
                self.tableWidget_2.setRowCount(0)
                self.tableWidget.setRowCount(0)

        def ConexionDB_pelicula(self, id_Pelicula):
                try:
                        dbConn = mysql.connect(user="root", password="Pedraza26", host="localhost", database="mydb")
                        dbCommand = dbConn.cursor()

                        sql_query = "SELECT id_Pelicula, nombre, tipo, Genero_id_Genero FROM pelicula WHERE id_Pelicula = %s"
                        dbCommand.execute(sql_query, (id_Pelicula,))

                        result = dbCommand.fetchall()

                        return result

                except mysql.Error as e:
                        print(e.msg)
                        return None

                finally:
                        dbCommand.close()
                        dbConn.close()

        def ConexionDB_reseña(self, id_Pelicula):
                try:
                        dbConn = mysql.connect(user="root", password="Pedraza26", host="localhost", database="mydb")
                        dbCommand = dbConn.cursor()

                        sql_query = "SELECT id_Reseña, comentario, calificacion FROM reseña WHERE Pelicula_id_Pelicula = %s"
                        dbCommand.execute(sql_query, (id_Pelicula,))

                        result = dbCommand.fetchall()

                        return result

                except mysql.Error as e:
                        print(e.msg)
                        return None

                finally:
                        dbCommand.close()
                        dbConn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    catalogo = QtWidgets.QMainWindow()
    ui = Ui_catalogo()
    ui.setupUi(catalogo)
    catalogo.show()
    sys.exit(app.exec_())
