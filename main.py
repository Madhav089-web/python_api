import fastapi
import sqlite3
import pydantic
def main():
    # print(fastapi.FastAPI)
    # print("Hello from python-api!")
    ...
app=fastapi.FastAPI()
db=sqlite3.connect("./main.db")
cursor=db.cursor()
"""
cursor.execute("drop TABLE EMPLOYEES;")
db.commit()
cursor.execute(CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);)
db.commit()
cursor.execute( INSERT INTO employees (id,first_name, last_name, email, position, salary) VALUES
(1,'John', 'Anderson', 'john.anderson@example.com', 'Software Engineer', 85000.00),
(2,'Emily', 'Clark', 'emily.clark@example.com', 'HR Manager', 75000.00),
(3,'Michael', 'Smith', 'michael.smith@example.com', 'Project Manager', 90000.00),
(4,'Jessica', 'Taylor', 'jessica.taylor@example.com', 'Marketing Specialist', 68000.00),
(5,'William', 'Brown', 'william.brown@example.com', 'Data Analyst', 72000.00),
(6,'Ashley', 'Davis', 'ashley.davis@example.com', 'UI/UX Designer', 70000.00),
(7,'David', 'Wilson', 'david.wilson@example.com', 'System Administrator', 78000.00),
(8,'Sarah', 'Moore', 'sarah.moore@example.com', 'Accountant', 69000.00),
(9,'James', 'Lee', 'james.lee@example.com', 'Technical Lead', 95000.00),
(10,'Olivia', 'Martin', 'olivia.martin@example.com', 'Content Writer', 60000.00);
)
db.commit()
"""
cursor.execute("Select * from employees;")
data=cursor.fetchall()
showing_data=[]
# x=0
print(showing_data)
def initializer():
    global showing_data
    showing_data=[]
    db=sqlite3.connect("./main.db")
    cursor=db.cursor()
    cursor.execute("Select * from employees;")
    data=cursor.fetchall()

    db.commit()
    db.close()
    
    for i in range(len(data)):
    # print(i)
    # showing_data[i]={}
        element={}
        element['id']=data[i][0]
        element['firstName']=data[i][1]
        element['lastName']=data[i][2]
        element['email']=data[i][3]
        element['position']=data[i][4]
        element['salary']=data[i][5]
        showing_data.append(element)
   

    # print(i)
# print(showing_data)
app.put
initializer()
print(showing_data)

@app.get("/")
async def index():
    initializer()
    return {"result":showing_data}
@app.get("/Id/{id}")
async def idFunction(id:int):
    ...
    for x in showing_data:
        if(id==x['id']):
            return {"result":x}
    initializer()
    return {"result":f"Cannot find the employee with id:{id}"}
@app.post("/Id/")
async def addNewEntry(data:dict):
    try:
        print(data)
        for y in showing_data:
            if(data['id']==y['id']):
                return{"result":"cannot add two entries with same id "}
        db=sqlite3.connect("./main.db")
        cursor=db.cursor()
        cursor.execute(f"Insert into employees values({data['id']},'{data['firstName']}','{data['lastName']}','{data['email']}','{data['position']}',{data['salary']});")
        db=sqlite3.connect("./main.db")
        cursor=db.cursor()
        initializer()
        return{"result":"data inserted successfully"}
        
    except Exception as e:
        return{"result":"failed to add a new entry ! since error ocurred !"}

@app.patch('/Id')
async def updateEntry(data:dict):
    try:
        print(data)
        initializer()
        field=data["field"]
        print(field)
        match field:
            case "salary":
                db=sqlite3.connect("./main.db")
                cursor=db.cursor()
                cursor.execute(f"Update  employees set salary = {data["salary"]} where id= {data["id"]};")
                db.commit()
                db.close()
            case "firstName":
                db=sqlite3.connect("./main.db")
                cursor=db.cursor()
                cursor.execute(f"Update  employees set first_name = '{data["firstName"]}' where id= {data["id"]};")
                db.commit()
                db.close()
            case "lastName":
                db=sqlite3.connect("./main.db")
                cursor=db.cursor()
                cursor.execute(f"Update  employees set last_name = '{data["lastName"]}' where id= {data["id"]};")
                db.commit()
                db.close()
            case "position":
                db=sqlite3.connect("./main.db")
                cursor=db.cursor()
                cursor.execute(f"Update  employees set position = '{data["position"]}' where id= {data["id"]};")
                db.commit()
                db.close()
            case "email":
                db=sqlite3.connect("./main.db")
                cursor=db.cursor()
                print(f"Update  employees set email = {data["email"]} where id = {data["id"]};")
                cursor.execute(f"Update  employees set email = '{data["email"]}' where id = {data["id"]};")
                db.commit()
                db.close()
            
        return {"result":"Updated Successfully"}
    except Exception as e:
        # print(e.__str__)
        return {"result":"An error ocurred !"}
@app.delete("/DeleteEntry/{id}")
async def deleteEntry(id:int):
    try:
        ...
        db=sqlite3.connect("./main.db")
        cursor=db.cursor()
        
        cursor.execute(f"DELETE FROM employees where id ={id}")
        db.commit()
        db.close()
        initializer()

        return {"result":"Deleted Successfully !"}
    except Exception as e:
        return {"result":" Failed to delete since an error occured! "}
db.close()
# if __name__ == "__main__":
#     main()
