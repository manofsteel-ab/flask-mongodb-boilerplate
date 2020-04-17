# flask-mongodb-boilerplate
A boilerplate using flask and mongodb

## Prerequisites
1) Understanding of flask, uWSGI
2) Understanding of docker
3) Understanding of mongodb
4) Understanding of flask-mongoengine (A document mapper library)


## Local setup instruction
1) install  and start docker
2) clone this repo
3) goto root directory of repo
4) run this > docker-compose up

this will create two container >

1. app container
`flask-mongodb-boilerplate_web_1`

2. mongodb container
`flask-mongodb-boilerplate_mongo_1`

If you check the docker-compose file you will see, that I have mentioned MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD.
So this is a username and password for admin(default) database.
Now you have to create a new database for your application.
For example in this boilerplate I am using `sample` database.
Now follow these steps to create user for sample database(ex.sample)(You have to do this only once)

1. docker exec -it flask-mongodb-boilerplate_mongo_1 bash (Goto mongo container shell)
2. mongo (open mongo shell)
3. use admin (switch to admin database, need authentication to create new db)
4. db.auth(username, password); > use username and password that you have mentioned in docker-compose file
5. use sample (now switch to new database> sample)
6. db.createUser(
   {
     user: "username for sample db",
     pwd: 'password for sample db'(),
     roles: [ "readWrite", "dbAdmin" ]
   }
)  Use this command to create user for you sample db

Now update app/settings/configs.py file and update MONGODB_SETTINGS with your new db, username and password


Now you can access api `http://localhost:5000/`

Sample link - `http://localhost:5000/api/sample/health/`


### For production you just need to update configs.py file settings

## Useful links
http://docs.mongoengine.org/guide/defining-documents.html

https://docs.mongodb.com/manual/mongo/


## TODO's
1. Add TESTING ENV and sample TESTING
2. Add Documentation link about boilerplate structure
