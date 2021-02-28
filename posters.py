import pymysql
import keys as k
#---------------------------------------------------------------------- Data base conection script
def db():
    db = pymysql.connect(host=k.Host, user=k.User, password=k.Pass, database=k.Dbname)
    return db 