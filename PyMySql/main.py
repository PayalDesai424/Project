# Week_8

import requests

def fetch_rest_api():
    print("rest api call")
    response=requests.get("https://reqres.in/api/users?page=1")
    user_data=response.json()
    print(user_data)

    total=user_data["total"]
    print(total)

    data=user_data['data']
    for record in data:
        print(record["id"],record["email"],record["first_name"],record["last_name"])


# working with file
if __name__ == '__main__':
    print('working with file')
    fetch_rest_api();
    try:
        f1 = open("student1.txt", "r")
        # print(f1.read())
        print(f1.read(10))
        print(f1.readline())
        f1.close()

    except:
        print("File not found")
    else:
        print(f1.read(10))
        print(f1.readline())
        f1.close()
    finally:
        print("All is well...")




    #f1=open("student.txt","w")
    #f1.write("Hello")

    f1=open("student.txt","a")
    #f1.write("\nHello")

    id = input("Enter your student id: ")
    f1.write(id)
    f1.write(",")
    first_name=input("Enter your first name: ")
    f1.write(first_name)
    f1.write(",")
    last_name=input("Enter your last name: ")
    f1.write(last_name)
    f1.write(",")
    city=input("Enter your city: ")
    f1.write(city)
    f1.write("\n")


    #for row in f1:
        #print(row)
        #print(row.split(","))

    f1.close()


    

