from flask import Flask, jsonify
from db import npc, boss, bossevent, monsters, items

app = Flask(__name__) #cinit flask and store in object app

@app.route('/NPC')
def _npc():
    data = npc()
    return jsonify(data)


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


#if name is executing as principal file
if __name__ == '__main__':
    app.run(debug=True, port=3000)