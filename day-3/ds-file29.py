#querying
import pymongo
clientobj=pymongo.MongoClient("mongodb://localhost:27017")
dbobj=clientobj["ds"]
collobj=dbobj["dstable1"]

z=collobj.find({},{'_id':0})
for m in z:
    print (m)
    

#query object
mq={'country':'UK'}
mq1={'country': {"$regex" : "^US"}}
mq2={'name': {"$gt":"B"}}


#pass the query object to find
p=collobj.find(mq,{'_id':0})

#iterate
for m in p:
    print (m)

print ()
print ()

#using regex
q=collobj.find(mq1,{'_id':0})
for n in q:
    print (n)
    

#using relational operator
r=collobj.find(mq2,{'_id':0})
for d in r:
    print (d)
    
clientobj.close()



