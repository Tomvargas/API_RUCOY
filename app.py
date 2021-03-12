from flask import Flask, jsonify, request
from getters import npc, boss, bossevent, monsters, items
from posters import postboss, postbossevent, postitem, postmonster, postnpc

app = Flask(__name__) #cinit flask and store in object app

#-------------------------------------------------------- GET METHODS

@app.route('/NPC') #create route
#get function for NPC route
def _npc():
    data = npc() #list with dictionary data
    return jsonify(data) #return list in json format

@app.route('/BOSS')
def _boss():
    data = boss()
    return jsonify(data)

@app.route('/BOSSEVENT')
def _bossevent():
    data = bossevent()
    return jsonify(data)

@app.route('/MONSTERS')
def _monsters():
    data = monsters()
    return jsonify(data)  

@app.route('/ITEMS')
def _items():
    data = items()
    return jsonify(data)  

#------------------------------------------------- END OF GET METHODS


#------------------------------------------------- POST METHODS

@app.route('/NPC', methods=['POST'])
def _postnpc():
    data = postnpc(request.json['itemsid'], request.json['name'], request.json['srcimg'], request.json['idd'])
    
    if data:
        get = npc()
        return jsonify({"NPC INSERTADO CON ÉXITO - NUEVA LISTA": get})
        
    return ('NO SE PUDO INGRESAR EL OBJETO') 

@app.route('/BOSS', methods=['POST'])
def _postboss():
    data = postboss(request.json['id'], request.json['name'], request.json['mingold'], request.json['maxgold'] , request.json['itemdrop'] , request.json['area'],  request.json['srcimg'])
    
    if data:
        get = boss()
        return jsonify({"BOSS INSERTADO CON ÉXITO - NUEVA LISTA": get})
        
    return ('NO SE PUDO INGRESAR EL OBJETO') 

@app.route('/BOSSEVENT', methods=['POST'])
def _postbossevnt():
    data = postbossevent(request.json['id'], request.json['name'], request.json['mingold'], request.json['maxgold'] , request.json['itemdrop'] , request.json['area'],  request.json['srcimg'])
    
    if data:
        get = bossevent()
        return jsonify({"BOSS EVENT INSERTADO CON ÉXITO - NUEVA LISTA": get})
        
    return ('NO SE PUDO INGRESAR EL OBJETO') 

@app.route('/ITEMS', methods=['POST'])
def _postitem():
    data = postitem(request.json['id'], request.json['category'], request.json['name'], request.json['lvlr'], request.json['pricer'] , request.json['finditem'],  request.json['srcimg'])
    
    if data:
        get = items()
        return jsonify({"ITEM INSERTADO CON ÉXITO - NUEVA LISTA": get})
        
    return ('NO SE PUDO INGRESAR EL OBJETO') 

@app.route('/MONSTERS', methods=['POST'])
def _postmonster():
    data = postmonster(request.json['id'], request.json['name'], request.json['lvl'], request.json['mingold'] , request.json['maxgold'],  request.json['dropid'],  request.json['area'],  request.json['srcimg'])
    
    if data:
        get = items()
        return jsonify({"ITEM INSERTADO CON ÉXITO - NUEVA LISTA": get})
        
    return ('NO SE PUDO INGRESAR EL OBJETO') 

#------------------------------------------------- END OF POST METHODS

#if name is executing as principal file
if __name__ == '__main__':
    app.run(debug=True, port=3000)