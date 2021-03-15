# API RUCOY
Rest API of Rucoy online, Android Game with basics information
this API will have information about creatures, npc, areas and items within the game in order to promote and increase the fun of the game.

This API provide data of the following objects:
* Monsters
* NPC
* Boss
* Boss Event
* Items

> ¡Alert this API is not online and data base works localy, please wait for release date!

## HOW TO USE METHODS
### GET
You can see data with ```http://host/name/parameter```

The routes for each object are ```/NPC```, ```/BOSS```, ```/BOSSEVENT```, ```/MONSTERS```, ```/ITEMS```

For specific searches you can use te parameter like ```http://host/NPC/Gear Merchant```

### POST
For use POST method you can use any software like Postman or Insomnia.

First you must write a json in your software using POST method, and write following structs:

#### ITEMS STRUCT
```json
{
    "id": int,
    "category": "Armor",
    "name": "Armor Name",
    "lvlr": int,
    "pricer": int,
    "finditem": "Where can find the item",
    "srcimg": "img route"
}
```

#### NPC STRUCT
```json
{
    "idd": int,
    "itemsid": "Armor",
    "name": "Armor Name",
    "srcimg": "img route"
}
```

#### BOSS AND BOSS EVENT STRUCT
```json
{
    "id": int,
    "name": "Boss Name",
    "mingold": int,
    "maxgold": int,
    "itemdrop": "id of items drop",
    "area": "Area",
    "srcimg": "img route"
}
```

#### MONSTERS STRUCT
```json
{
    "id": int,
    "name": "Monster Name",
    "lvl": int,
    "mingold": int,
    "maxgold": int,
    "dropid": "id of items drop",
    "area": "Area",
    "srcimg": "img route"
}
```