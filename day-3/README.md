## FILE HANDLING  (part-1):
    
    What is a file?
    A file is a collection of information

    What are the types of files?
    Two types: 1. text and 2. binary (non-text)

    How do you work with files?
    1. create the file object
    2. read/write on the file object
    3. close the file object

    a.  Creating the file object:
            fo=open('abc.txt','w')
        Here fo is the fileobj, open() is the method, 'abc.txt' is the
        actual file name, 'w' is the mode

                r               read              see the content
                w               write             create the content
                a               append            add to the existing content
                r+              read,write        modify
                w+              write, read       first create and then read
                a+              append, read      first append and then read

        If we are dealing with files other than .txt, then we need to attach
        'b' to the mode
            fo=open('abc.html','rb')

    b. read/write on the file object:
       read and write can be done on the file object via string or list
       string:  read(), write()
       list:    readlines(), writelines()

    c. closing the file object:
        fo.close()

## FILE HANDLING - (part-2): json, csv, Excel file handling

## WORKING WITH NOSQL DATABASES: MONGODB

        1. download the mongodb server and start the service
        2. install the driver module
        3. stable version of Python

1. start the mongodb service:
    c:\program files\mongodb\server\4.4\bin>mongod
    
        clientobj
        dbobj
        collectobj
        documents
        

1. MongoDB (NoSQL):

    a. download the server file for windows:
        mongodb-win32-i386-3.2.22-signed

        Identify the location where MongoDB is installed on your system
          c:\program files (x86)\MongoDB

    b. created a folder "data" and a subfolder "db" under "data' in
          c:\program files (x86)\MongoDB\data
          c:\program files (x86)\MongoDB\data\db

        

    c. open the cmd.exe with run as administrator
       move to the folder:
           c:\program files (x86)\MongoDB\Server\3.2\bin

    d. run the database service from here
        
        c:\program files (x86)\MongoDB\Server\3.2\bin> mongod 

    e. install the driver module for python
            pymongo


    WORKING WITH PYMONGO:
        MongoClinet object
        database object
        collection object (table)
        document (record)

        # connecting to MongoDB service:
         import pymongo
         clientobj=pymongo.MongoClient("mongodb://localhost:27017")
         dbobj=clientobj["newdb"]
         collobj=dbobj["newtb"]

         #take a document (record)
         s={"name":"prasad","country":"india"}

         #insert the document into the table
         x=collobj.insert_one(s)


         #select one record
         a=collobj.find_one()

         s1=[{"name":"xyz","country" : "india"}, {"name":"alex","country":"us"}]
         z=collobj.insert_many(s1)

         #select all records
         b=collobj.find()

         for m in b:
             print (m)


        #suppressing certain fields:
        c=collobj.find({},{"_id":0})

        #filtering the result
        mq={"name":"raju"}
        z=collobj.find(mq)
        for m in z:
            print (m)


        z=collobj.find(mq,{"_id":0,"country":0})
        for m in z:
            print (m)


        # advanced querying
         amq={"name": {"$regex":"^r"}}
         z=collobj.find(amq)
         for m in z:
             print (m)

        amq1={"name":{"$gt":"r"}}

        #sorting the documents (records)
        z=collobj.find().sort("name",1)  => display in the ascending order
        z=collobj.find().sort("name",-1) => display in the descending ordr


        #delete a record
        mq={"name":"prasad"}
        z=collobj.delete_one(mq)
        print (z.deleted_count)

        #delete many records
        mq={"name":{"$regex":"^r"}}
        z=collobj.delete_many(mq)
        print (z.deleted_count)

        p=collobj.find({},{"_id":0})
        for m in p:
            print (m)
        

        #updating records
        mq={"name":"kumar"}
        newvalue={"$set":{"country":"india"}}
        z=collobj.update_one(mq,newvalue)

        #update many
        mq={"country":"india"}
        newvalue={"$set":{"country":"INDIA"}}
        z=collobj.update_many(mq,newvalue)
        
        
        clientobj.close()

         
## NETWORK PROGRAMMING IN PYTHON:
    Network programming in Python is done at two levels:
        1. low level thru socket programming
        2. high level using standard libraries such as ftplib, httplib,urllib
                                                            smtplib

        Socket programming:
            1. What is a socket?
                A socket is the end point of a bi-diectional communication
                channel.


                sockets communicate within a process, betweeen processes of a machine
                or between the processes of machines located at different places

            we have a libray known as socket library in python.
            import socket
            (to invoke this library)



            1. server side sockets:
                bind()
                listen()
                accept()


            2. client side sockets:
                connect()


            3. general socket methods:
                recv()
                send()
                recvfrom()
                sendto()
                gethostname()
                close

                
          Whenever we want to create sockets,
                  1. domain (family)
                  2. type   (connction, connectionless)
                  3. protocols (within the family if you have choice of protocols)
                     this is value is normally 0


            socket family: AF_INET (address form internet protocol) default
                           PF_INET (protocol form internet protocol
                           PF_UNIX
                           PF_X25

            type:           connection (SOCK_STREAM)
                            connectionless (SOCK_DGRAM)

            protocols       0


            2. creating sockets:
                import socket
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #s=socket.socket()


            server.py

            #import the socket module
            import socket

            #create a socket, if you give empty params, default value is taken
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            #get the host and port no
            host=socket.gethostname()
            port=12345

            #bind the socket to the host and port
            s.bind((host,port))

            #listen => no. of connections that can be made parallelly
            s.listen(5)

            #wait for the clients to connect
            while True:
                c, addr=s.accept()   # create a client object c, take its address
                print ('Connected from ', addr)
                c.send(b'Thanks for connecting ') #send message to client
                c.close()                       # close the client object
            
            
            
                
        #client.py

        import socket                          #import socket module
        s=socket.socket()                       # create a socket
        host=socket.gethostname()               #get hostname
        port=12345                              #put the port no. as 12345
        s.connect((host,port))                  #connect to the server using host/port
        x=s.recv(1024)                          #receive 1024 bytes from server
        print (x)                               #print that received
        s.close()                               #close the socket
        


       HIGH LEVEL MODULES THAT USE NETWORK PROTOCOLS
       ftplib
       urllib
       smtplib

       1. FTP:
           import ftplib
           x=ftplib.FTP('ftp.sunet.se','anonymous','anonymous@sunet.se')
           x.welcome

           to see the directory entries of the remote machine,
           x.dir()


           if you want to save a local list,
           data=[]
           x.dir(data.append)


           for transeferring files,
           there are two categories

           text / binary

           Text files :-> storlines, retrlines
           Binary files:-> storbinary, retrbinary


           Retrieving a text from remote machine to local machine and display the content
            #text file retrieval
               x.retrlines('RETR ' +'robots.txt',sys.stdout.write)
            (displaying on the screen)

            fo=open('xyz.txt','w')
            x.retrlines('RETR '+'robots.txt',fo.write)
            fo.close()
            (for storing into a text file)

            #binary file retrieval
            fo=open('myfile.html','wb')
            x.retrbinary('RETR '+'HEADER.html',fo.write)
