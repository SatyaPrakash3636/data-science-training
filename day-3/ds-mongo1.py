#import the driver module
import pymongo

#create a client object
clientobj=pymongo.MongoClient("mongodb://localhost:27017")

#database object
dbobj=clientobj["ds"]

#collection object
collobj=dbobj["dstable"]

#take one document
s={'name':'prasad','country':'india'}

#insert into the collection
p=collobj.insert_one(s)

#display the document
q=collobj.find_one({},{'_id':0})
print (q)

#displaying the databases
print (clientobj.list_database_names())

#displaying the table names
print (dbobj.list_collection_names())

#close the connection
clientobj.close()
