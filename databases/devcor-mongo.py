#!/usr/bin/env python

import pymongo

#setup db connection and creaete a collection called customers
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#insert a single document into the db
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

print(x.inserted_id)

#insert multiple documents into the database
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"},
  { "name": "Bob", "address": ["Oak Grove St","12th Avenue"]}
]

x = mycol.insert_many(mylist)

#print entire collection
print("-"*25)
print("print entire collection")
for x in mycol.find():
    print(x)

#search the collection
print("-"*25)
print("excluding object id from our search")
for x in mycol.find({}, { "_id": 0, "name": 1, "address":1 }):
    print(x)

#search for a single entry in collection
myquery = { "name": "Chuck" }
mydoc = mycol.find(myquery)
print("-"*25)
print("searching for the name 'Chuck'")
for x in mydoc:
    print(x)

#create a query
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
print("-"*25)
print("searching for all address entries greater than 'S'")
for x in mydoc:
    print(x)

#delete a document
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)
print("-"*25)
print("deleting 'Mountain 21'")

#update a document
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address" : "Canyon 123" } }
mycol.update_one(myquery, newvalues)
print("-"*25)
print("updating the value 'Valley 345' for 'Canyon 123'") 
for x in mycol.find():   
    print(x)

#update multiple documents
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print("-"*25)
print("updating all documents with address greater than 'S' with the name 'Minnie'")
print(x.modified_count, "documents updated.")
for x in mycol.find():
    print(x)


# to query by object id, you must import the bson.objectid
#from bson.objectid import ObjectId
#myquery = {'_id': ObjectId('5e8b76259e7a6076019c2078')}

#add items to list
myquery = {"name": "Bob"}
newvalues = { "$push": { "address": "4322 Humboldt Ave" }}
mycol.update_one(myquery, newvalues)
print("-"*25)
print("adding a value to an array within a document")
for x in mycol.find():
    print(x)

#delete an entire collection
#mycol.drop()


