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

