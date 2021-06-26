import pymongo

def connection_to_mongodb():
    connection_string = "mongodb+srv://dbUser:admin@cluster0.ruqz5.mongodb.net/sample_restaurants?retryWrites=true&w=majority"
    myclient = pymongo.MongoClient(connection_string)
    db = myclient.sample_restaurants
    cRestaurants = db["restaurants"]
    print(myclient)

    #Insert Record
    connection_customer = db["customers"]
    mydict = {"name": "Payal Desai", "address": "65 Yorkland Blvd., Toronto"}
    x = connection_customer.insert_one(mydict)
    print(x)

if __name__ == '__main__':
    connection_to_mongodb()