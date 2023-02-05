import mysql.connector
# mysql.install_as_MySQLdb()
import MySQLdb
import xlrd

database = mysql.connector.connect(host="localhost", user="root", password="1234", db="excel")
cursor = database.cursor()

car_table = ("CREATE TABLE IF NOT EXISTS car(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,company_name VARCHAR(45),model_name VARCHAR(45),year INT NOT NULL,km INT)")
cursor.execute(car_table)

# read excel sheet

data_sheet = xlrd.open_workbook('car.xlsx')
data_sheet

sheet_name = data_sheet.sheet_names()
sheet_name


sql = "INSERT INTO car(id,company_name,model_name,year,km) VALUES (%s,%s,%s,%s,%s)"

for sh in range(0,len(sheet_name)):
    sheet= data_sheet.sheet_by_index(sh)

for r in range(1,sheet.nrows):
        id = sheet.cell(r,0).value
        company_name = sheet.cell(r,1).value
        model_name = sheet.cell(r,2).value
        year = sheet.cell(r,3).value
        km = sheet.cell(r,4).value
      
        car_value = (id,company_name,model_name,year,km)
        cursor.execute(sql, car_value)
        database.commit()