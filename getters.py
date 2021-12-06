import pymysql
import keys as k
#---------------------------------------------------------------------- Data base conection script
def db():
    db = pymysql.connect(host=k.Host, user=k.User, password=k.Pass, database=k.Dbname)
    return db

#---------------------------------------------------------------------- Get npc json
def npc():
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM npc"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "ItemsID": row[2], "srcIMG": row[3]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List


#---------------------------------------------------------------------- Get boss json
def boss():
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM boss"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "minGold":row[2], "maxGold":row[3], "ItemsID": row[4], "area":row[5], "srcIMG": row[6]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List


#---------------------------------------------------------------------- Get bossevent json
def bossevent():
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM bossevent"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "minGold":row[2], "maxGold":row[3], "ItemsID": row[4], "area":row[5], "srcIMG": row[6]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List

#---------------------------------------------------------------------- Get monsters json
def monsters():
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM monsters"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "Level":row[2], "minGold":row[3], "maxGold": row[4], "dropid":row[5], "area": row[6], "srcImg": row[7]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List

#---------------------------------------------------------------------- Get items json
def items():
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM items"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"Category": row[1], "Name":row[2], "Level required":row[3], "Price recomended": row[4], "Find item":row[5], "srcImg":row[6]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List

#---------------------------------------------------------------------- Get item json
def item(name):
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM items where name = '"+name+"'"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"Category": row[1], "Name":row[2], "Level required":row[3], "Price recomended": row[4], "Find item":row[5], "srcImg":row[6]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List

#---------------------------------------------------------------------- Get one boss json
def bss(name):
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM boss where name = '"+name+"'"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "minGold":row[2], "maxGold":row[3], "ItemsID": row[4], "area":row[5], "srcIMG": row[6]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List


#---------------------------------------------------------------------- Get one bossevent json
def bevent(name):
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM bossevent where name = '"+name+"'"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "minGold":row[2], "maxGold":row[3], "ItemsID": row[4], "area":row[5], "srcIMG": row[6]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List

#---------------------------------------------------------------------- Get monster json
def monster(name):
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM monsters where name = '"+name+"'"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "Level":row[2], "minGold":row[3], "maxGold": row[4], "dropid":row[5], "area": row[6], "srcImg": row[7]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List

    #---------------------------------------------------------------------- Get an NPC json
def npc1(name):
    DB = db()
    List = []

    # prepare a cursor object using cursor() method
    cursor = DB.cursor()

    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM npc where name = '"+name+"'"

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        dic = {"name": row[1], "ItemsID": row[2], "srcIMG": row[3]}
        # Now add dic to list
        List.append(dic) 

    # disconnect from server
    DB.close()

    print(List)

    return List