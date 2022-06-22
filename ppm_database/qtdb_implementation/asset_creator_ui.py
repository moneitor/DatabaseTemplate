from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2 import QtCore

from asset_creator_compiled import Ui_Dlg_AssetCreation
from new_asset_compiled import Ui_NewAsset

import sys
import os

DATABASE_TEMP = "assets"
DATABASE_PROJECT = "projects"



def connect_to_db(db_name):
    """Connects to the database given as a parameter"""
    _db = QSqlDatabase.addDatabase("QSQLITE")
    _db.setDatabaseName("./{}.db".format(db_name))       
        
    if _db.open():
        print(_db.tables())
        if ("projects" in _db.tables()):                
            print("Projects database exist")
                
        return _db
        


class PPM_Asset_creator(QDialog, Ui_Dlg_AssetCreation):
    def __init__(self):
        super(PPM_Asset_creator, self).__init__()
        
        self.current_db = DATABASE_TEMP
        
        self.setupUi(self)
        self.setLayout(self.lyt_main)
        
        self.setMinimumWidth(1000)
        
        self.lyt_main.setStretch(0, 2)
        self.lyt_main.setStretch(1, 8)
        self.lyt_main.setContentsMargins(30, 30, 30, 30)
        
        self.tbl_assets.setColumnWidth(0, 50)
        self.tbl_assets.setColumnWidth(1, 150)
        self.tbl_assets.setColumnWidth(2, 150)
        self.tbl_assets.setColumnWidth(3, 90)
        self.tbl_assets.setColumnWidth(4, 600)
        
        
        self.populate_projects()
        self.connections()        
        
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("./{}.db".format(self.current_db))
        
        if db.open():
            print(db.tables())             
            if "self.current_db" not in db.tables():       
                print("Creating Table")         
                #self.temp_create_assets_table()
            else:
                print("Table Exists")  
            self.populate_table()
        else:
            print("Table exists")
            QMessageBox.critical(self, "Database Error", "Could not open '{}.db' database".format(self.current_db))
            
            
            
    def connections(self):
        self.bnt_search.clicked.connect(self._get_columns_amount)
        self.btn_addAsset.clicked.connect(self.add_asset)
        
        
        
    def populate_projects(self):
        """Populates the projects combobox"""
        
        self.cmb_project.clear()
        self.cmb_project.addItem("Global")
        
        _db = connect_to_db(DATABASE_PROJECT)

        query = QSqlQuery()
        bOk = query.exec_("SELECT name FROM {}".format(DATABASE_PROJECT))
        
        if bOk:
            while query.next():
                project_name = query.value("name")
                self.cmb_project.addItem(project_name)
        else:            
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))
        
            
            
    def _get_columns_amount(self):
        query = QSqlQuery()
        bOk = query.exec_("SELECT * FROM {} ORDER BY name".format(self.current_db))
        
        count = 1            
        if bOk:            
            while query.next():                
                count += 1                
        return count
    
            
            
    def populate_table(self):
        
        self.lst_description.clear()
        self.tbl_assets.clearContents()
        self.tbl_assets.setRowCount(0)
        
        
        query = QSqlQuery()
        bOk = query.exec_("SELECT * FROM {} ORDER BY name".format(self.current_db))
            
        if bOk:
            
            while query.next():
                
                row = self.tbl_assets.rowCount()
                self.tbl_assets.insertRow(row)
                for column in range(self._get_columns_amount()):
                    
                    table_widget = QTableWidgetItem(str(query.value(column)))
                    if column == 0:
                        table_widget.setTextAlignment(QtCore.Qt.AlignRight)
                    else:
                        table_widget.setTextAlignment(QtCore.Qt.AlignLeft)
                    
                    self.tbl_assets.setItem(row, column, table_widget)
            print ("Table was puplated.")
        else:
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))            
            
            
            
    def return_asset_name(self, id):
        query = QSqlQuery()
        sSql = "SELECT name, project, type, description FROM assets WHERE id = {}".format(id)
        bOk = query.exec(sSql)
        
        if bOk:
            query.next()
            if query.isValid():
                return "{}, {} : {}".format(query.value("name"),  query.value("project"), query.value("type"))
            else:
                return ""
        else:
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))       
            
            
    def add_asset(self):
        new_asset_ui = New_Asset()
        new_asset_ui.show()
        new_asset_ui.exec_() 
        
        self.populate_table()
            
            
            
    def temp_create_assets_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            project TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL                
        )
        """.format(self.current_db)
        query = QSqlQuery()
        query.exec_(sql)
        query.exec_("INSERT INTO {} VALUES (101, 'spaceship', 'VehiclesRBD', 'abc', 'Spacheship model for destruction')".format(self.current_db))
        query.exec_("INSERT INTO {} VALUES (102, 'statue', 'bloodTutorial', 'abc', 'Statue asset to put blood into')".format(self.current_db))
        query.exec_("INSERT INTO {} VALUES (103, 'biped', 'General', 'abc', 'Biped for RnD')".format(self.current_db))
        query.exec_("INSERT INTO {} VALUES (104, 'roof', 'RoofDynamics', 'abc', 'Roof for Destruction')".format(self.current_db))
        
        print("Table {} created".format(self.current_db))
        
        
        
        
class New_Asset(QDialog, Ui_NewAsset):
    def __init__(self):
        super(New_Asset, self).__init__()
        self.setupUi(self)
        self.setLayout(self.lyt_main)
        
        self.connections()
        self.populate_projects()
        
        self._add_additional_items()
        
        
    def _add_additional_items(self):
        self.cb_type.addItem("Texture")
        self.cb_type.addItem("HDRi")
        
        
    def connections(self):
        self.btn_cancel.clicked.connect(self.close)
        self.btn_create.clicked.connect(self.add_asset)       
    

        
    def populate_projects(self):
        
        self.cb_project.clear()
        self.cb_project.addItem("Global")
        
        _db = connect_to_db(DATABASE_PROJECT)

        query = QSqlQuery()
        bOk = query.exec_("SELECT name FROM {}".format(DATABASE_PROJECT))
        
        if bOk:
            while query.next():
                project_name = query.value("name")
                self.cb_project.addItem(project_name)
        else:            
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))
            
            
            
    def return_project_info(self, info="path", database=DATABASE_PROJECT):      

        query = QSqlQuery()
        bOk = query.exec_("SELECT * FROM {} WHERE name = 'PersonalOtls'".format(database))
        if bOk:
            query.next()
            if query.isValid():
                print(query.value(info))
            
        
        
    
    def add_asset(self):
        connect_to_db(DATABASE_TEMP)
        query = QSqlQuery()
        query.prepare("INSERT INTO {} (name, project, type, description) VALUES (:n, :p, :t, :d)".format(DATABASE_TEMP))
        query.bindValue(":n", self.ln_name.text())
        query.bindValue(":p", self.cb_project.currentText())
        query.bindValue(":t", self.cb_type.currentText())
        query.bindValue(":d", self.txt_description.toPlainText())
        
        bOk = query.exec_()
        if bOk:
            QMessageBox.information(self, "Successfull!", "Asset added to the Database. ")
            self.close()
        else:
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))
        
            
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = PPM_Asset_creator()
    #w = New_Asset()
    
    w.show()
    
    sys.exit(app.exec_())

