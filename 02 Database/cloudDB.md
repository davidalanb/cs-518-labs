
### Connect to MongoDB Atlas

Login to mongoDB Atlas in your browser:
* Database > Clusters > Create / Connect > Drivers
    - Copy URI (starts with mongodb+srv)
* Security > DB Access > Users
    - Get username and password
    - update <password> in your URI

### Configure Atlas for access from Functions App

* Sign into MongoDB Atlas
* Security > Network Access > Add IP Address
* Add this Entry: 0.0.0.0/0