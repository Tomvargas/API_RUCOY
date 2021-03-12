import pymysql
import keys as k
#---------------------------------------------------------------------- Data base conection script
def db():
    db = pymysql.connect(host=k.Host, user=k.User, password=k.Pass, database=k.Dbname)
    return db 


#---------------------------------------------------------------------- POST npc
def postnpc(itemsid, name, srcimg, idd):

    try:
        DB = db()
        query="INSERT INTO npc (id, name, sell, srcimg) VALUES( "+str(idd)+", '"+name+"', '"+itemsid+"', '"+srcimg+"' );"
        cursor = DB.cursor()
        cursor.execute(query)
        DB.commit()
        cursor.close()
                
        return True

    except pymysql.connect.Error:
        return False

#---------------------------------------------------------------------- POST boss
def postboss(idd, name, mingold, maxgold, itemdrop, area, srcimg):

    try:
        DB = db()
        query="INSERT INTO boss (id, name, minGold, maxGold, itemDrop, area, srcimg) VALUES( "+str(idd)+", '"+name+"', '"+mingold+"', '"+maxgold+"', '"+itemdrop+"', '"+area+"', '"+srcimg+"' );"
        cursor = DB.cursor()
        cursor.execute(query)
        DB.commit()
        cursor.close()
                
        return True

    except pymysql.connect.Error:
        return False

#---------------------------------------------------------------------- POST bossevent
def postbossevent(idd, name, mingold, maxgold, itemdrop, area, srcimg):

    try:
        DB = db()
        query="INSERT INTO bossevent (id, name, minGold, maxGold, itemDrop, area, srcimg) VALUES( "+str(idd)+", '"+name+"', '"+str(mingold)+"', '"+str(maxgold)+"', '"+itemdrop+"', '"+area+"', '"+srcimg+"' );"
        cursor = DB.cursor()
        cursor.execute(query)
        DB.commit()
        cursor.close()
                
        return True

    except pymysql.connect.Error:
        return False

#---------------------------------------------------------------------- POST monster
def postmonster(idd, name, lvl, mingold, maxgold, dropid, area, srcimg):

    try:
        DB = db()
        query="INSERT INTO monsters (id, name, lvl, minGold, maxGold, dropid, area, srcimg) VALUES( "+str(idd)+", '"+name+"', '"+str(lvl)+"', '"+str(mingold)+"', '"+str(maxgold)+"', '"+dropid+"', '"+area+"', '"+srcimg+"' );"
        cursor = DB.cursor()
        cursor.execute(query)
        DB.commit()
        cursor.close()
                
        return True

    except pymysql.connect.Error:
        return False

#---------------------------------------------------------------------- POST item
def postitem(idd, category, name,lvlr, pricer, finditem, srcimg):

    try:
        DB = db()
        query="INSERT INTO items (id, category, name, levelR, priceR, finditem, srcimg) VALUES( "+str(idd)+", '"+category+"', '"+name+"', '"+str(lvlr)+"', '"+str(pricer)+"', '"+finditem+"', '"+srcimg+"' );"
        cursor = DB.cursor()
        cursor.execute(query)
        DB.commit()
        cursor.close()
                
        return True

    except pymysql.connect.Error:
        return False

