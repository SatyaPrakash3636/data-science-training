#inserting many documents
import pymongo
clientobj=pymongo.MongoClient("mongodb://localhost:27017")
dbobj=clientobj["ds"]
collobj=dbobj["dstable1"]

#take bulk documents in a list
data=[{'name':'AAA', 'country':'UK'},{'name':'BBB','country':"US"},{'name':'CCC','country':'USSR'}]

#insert the list into the collection
p=collobj.insert_many(data)

#display the records
q=collobj.find({},{'_id':0})

#iterate thru q to display
for m in q:
    print (m)

#close the connection
clientobj.close()
