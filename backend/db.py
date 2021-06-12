import mysql.connector
from mysql.connector import errorcode


def insertAlgo(duneId, name):
    try:
        mydb = mysql.connector.connect(user="root", password="root", host="localhost", database="project_d")
        cursor = mydb.cursor()

        Insert_Img = "INSERT INTO algorithmimage (Name, DuneLocation) VALUES(%s,%s)"

        cursor.execute(Insert_Img, (name, duneId))
        mydb.commit()

        Id_Inserted = cursor.lastrowid

        # Close contections
        cursor.close()
        mydb.close()

        return Id_Inserted

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
        else:
            return err

def updateAlgo(link, top, bottom, imageId):
    try:
        mydb = mysql.connector.connect(user="root", password="root", host="localhost", database="project_d")
        cursor = mydb.cursor()
        Update_Img = "UPDATE algorithmimage SET Link = %s,  TopCoordinate = %s, BottomCoordinate = %s WHERE Id = %s"

        cursor.execute(Update_Img, (link, top, bottom, imageId))

        mydb.commit()

        # Close contections
        cursor.close()
        mydb.close()
        return "oke"

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
        else:
            return err

def getData():
    try:
        mydb = mysql.connector.connect(user="root", password="root", host="localhost", database="project_d")
        cursor = mydb.cursor()

        Select_Dunes = "SELECT * FROM dunes"

        cursor.execute(Select_Dunes)

        data = cursor.fetchall()

        # Close contections
        cursor.close()
        mydb.close()
        return data

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
        else:
            return err

def getHistory(duneId):
    try:
        mydb = mysql.connector.connect(user="root", password="root", host="localhost", database="project_d")
        cursor = mydb.cursor()

        Select_History = "SELECT * FROM algorithmimage WHERE DuneLocation = %s"

        cursor.execute(Select_History % (duneId))

        data = cursor.fetchall()

        # Close contections
        cursor.close()
        mydb.close()
        return data

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
        else:
            return err

def getOneCal(imgId):
    try:
        mydb = mysql.connector.connect(user="root", password="root", host="localhost", database="project_d")
        cursor = mydb.cursor()

        Select_Image = "SELECT * FROM algorithmimage WHERE Id = %s"

        cursor.execute(Select_Image % (imgId))

        data = cursor.fetchall()

        # Close contections
        cursor.close()
        mydb.close()
        return data

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
        else:
            return err
