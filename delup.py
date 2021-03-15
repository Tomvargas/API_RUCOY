import pymysql
import keys as k
#---------------------------------------------------------------------- Data base conection script
def db():
    db = pymysql.connect(host=k.Host, user=k.User, password=k.Pass, database=k.Dbname)
    return db


def objdelete(subname, name):
    
    DB = db()
        
    cursor = DB.cursor()

    sql = "DELETE FROM "+subname.lower()+" WHERE name = '"+name+"'"

    print( subname.lower() + " -- "+name+" ------ "+sql)

    try:
       cursor.execute(sql)
       DB.commit()

       cursor.close()
       DB.close()
       return ('el objeto '+name+' fué eliminado')

    except pymysql.connect.Error:
        return ('No se encontró este objeto')


def objupdate(key, value, subname, idd):
    
    DB = db()
    List = []
    dic={}
        
    cursor = DB.cursor()

    if value.isnumeric():
        sql = "UPDATE "+subname.lower()+" SET "+key+" = "+value+" WHERE id = "+idd+";"
    else:
        sql = "UPDATE "+subname.lower()+" SET "+key+" = '"+value+"' WHERE id = "+idd+";"    

    try:
       cursor.execute(sql)
       DB.commit()

       cursor.close()
       DB.close()
       return ('El objeto se actualizó')

    except pymysql.connect.Error:
        return ('No se encontró este objeto')

