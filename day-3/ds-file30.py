#deleting
import pymongo
clientobj=pymongo.MongoClient("mongodb://localhost:27017")
dbobj=clientobj["ds"]
collobj=dbobj["dstable1"]

z=collobj.find({},{'_id':0})
for m in z:
    print (m)
print ()
print ()

#query object
mq={'country':'UK'}
q=collobj.delete_many(mq)
r=collobj.find({},{'_id':0})
for m in r:
    print (m)
clientobj.close()



