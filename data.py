"""
The file "data.py" was made to manage the dataBase.
"""

from pymongo import MongoClient
import utils

client = MongoClient(utils.variables.mongodB.token())
db = client[utils.variables.mongodB.dBname]
posts = db.posts
debugMode = utils.variables.debugMode.status()

def dBposts():
    return posts

def fetch(id_, field):
    
    item = db.posts.find_one({"title": id_}, {field: 1})
    for key, item in item.items(): pass

    if debugMode: utils.logs.dB.fetch(id_, field, item)

    return item

def update(id_, field, item):
    
    doc = posts.find_one_and_update(
		{"title": id_},
			{"$set":
				{field: item}
			}, upsert=True
		)
    
    if debugMode: utils.logs.dB.update(id_, field, item)

def isIndB(id_):
    
    if posts.count_documents({"title": id_}) == 0: bool = False
    else: bool = True
    
    if debugMode: utils.logs.dB.check(id_, bool)

    return bool

def delete(id_):

    posts.delete_one({"title": id_})

    if debugMode: utils.logs.dB.delete(id_)

def addUserTodB(userWebSiteName, userMail, userPassword, userSurname, userName, userAge):
    
    dataToUpload = {
        'title': userWebSiteName,
        'mail': userMail,
        'password': userPassword,
        'surname' : userSurname,
        'name' : userName,
        'age' : userAge
        }
    posts.insert_one(dataToUpload)
    
    if debugMode: utils.logs.dB.creation(userWebSiteName)