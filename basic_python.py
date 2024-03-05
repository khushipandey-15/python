#DAY 10
# X=int(input("enter the value:"))
# y=int(input("enter y value:"))
# print("addition:",X+y)
# print("subtraction:",X-y)
# print("multiple:",X*y)
# print("precent:",X%y)
# print("divide:",X/y)
#DAY 11
# a="chural"
# for character in a:
#  print(character)
#DAY 12
# name="harry"
# print(name[0:9:3])
# print(name[:10])
# print(name[1:14])
# print(name[:-1])
# print(name[-4:-2])

#DAY 13

# a="vaibhav33"
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.rstrip('3'))
# print(a.replace('vaibhav','khushi'))
# print(a.lstrip('v'))

# str="everything!!! is awosome"
# print(str.endswith("!!!"))
# print(str.endswith("!!",6,13))
# print(str.startswith("nve"))
# print(str.startswith("eve"))
# print(str.split(" "))
# print(str.capitalize())
# #print(str.find("isa"))
# #print(str.index("!!is"))
# print(str.find("is"))
# print(str.index("awo"))
# a="charbottewotka"
# print(a.isalnum())
# print(a.isalpha())
# print(a.isprintable())
# a="    "
# print(a.isspace())
#DAY 14

# a=int(input("enter you age:"))
# if a<18:
#     print("you can drive")
# elif a==18:
#     print("you have to make you driving licence")   
# elif a>18:
#     print("you can not drive")     

# DAY 15
# a=int(input("the time is" ))
# if (a>=6 and a<=12) :
#     print("good morning re baba")
# elif  (a>12 and a<=16):
#     print("good afternoon")
# elif (a>16 and a<=20):
#     print("good evening")
# elif(a>20 and a<=24):
#     print("good night")    
# else:
#     print("vaibhav mota hai")     
# # a={1,2,3,}
# # b={4,5,6}

# # import time
# # timestamp=time.strftime('%H:%M:%S')
# # print(timestamp)
# # timestamp=time.strftime('%H')
# # print(timestamp)
# # timestamp=time.strftime('%M')
# # print(timestamp)
# # timestamp=time.strftime('%S')
# # print(timestamp)
# #DAY 16
# # x=int("khushi")

# # match x:
# #     case 0:
# #         print("thora sa takla")
# #     case 1:
# #         print("thora jada takla" )  
# #     case _:
# #         print("pura takla") 

# #DAY 17
# # x=("khushi")

# # for i in x:
# #     print(i)
# # for x in x:
# #     print(x,end =",")    


# # abhi=("aloo","bindi","began")

# # for abhi in abhi:
# #     print(abhi)
# #     for abhi in abhi:
# #         print(abhi)

# # for i in range(5):
# #     print(i)
# # for i in range(1,12,2):
# #     print(i)    
# #DAY 18
# # i=0
# # while(i<3):
# #     print("pagal")
# #     i=i+1
# #DAY 19
# # for i in range(12):
# #     print("5 X",i,"=",i*5)
# #     if(i==10):
# #         break
# # for i in range(12):

# #     if(i==10):
# #         continue
# #     print("5 X",i,"=",i*5)

#  # DAY20
# # def isgreater(a,b):
# #     if a>b:
# #         print("a is greater than b")

# #     else:
# #         print("b is greater than a")  

# # isgreater(12,14)  

# # def issmaller(a,b):
# #     if a<b:
# #         print("a is smaller than b")
# #     else:
# #         print("b is smaller than a")
# # issmaller(12,19)

# #DAY 21    

# # def average(a,b,c,d):
# #     i=(a+b+c+d)//2
# #     print(i,"is average value")
# # average(2,3,5,6)  

# # def table(c):
# #     for i in range(c):
# #         print("5 X",i+1,"=",5*(i+1))
# #         i=i+1
# # table(10)
# # def name(fname,mname,lname="ghose"):
# #     print("hello ",fname,mname,lname)
# # name("adi","suman")    

# #DAY 22(list)
# marks=[23,45,56,67,98,78,90,87,"andry",True]
# print(marks)
# print(marks[:])
# print(marks[1:9:2])
# print(marks[-1])
# if 23 in marks:
#     print("pagal")
# else:
#     print("seee")

#DAY 23(list)
# l=[1,7,3,5,9]
# l.append(4)
# print(l.count(1))
# l.sort()
# l.sort(reverse=True)
# l.insert(3,67)
# n=[12,13,14,15,19]
#l.extend(n)
# l.copy(n)
# print(l.index(7))


# DAY 24(tuple)

# tup=(1,5,2,7)
# print(type(tup),tup)
# print(len(tup))
# print(tup[1:4])

# DAY 25(TUPLE methods)
# tup=(1,2,34,5,6,3,3)
# print(tup.count(3))


# DAY 25(TUPLE methods)
countries=("india","austrlia","finland","russia")
temp=list(countries)
temp.append("usa")
temp.pop(3)

temp.insert(2,"america")
countries=tuple(temp)
print(countries)
countries_2=("pakistan","bangladesh","china")
world=countries+countries_2
print(world)
tup1=(10,2,3,4,3,2,1,1,3,4,3,3)
res=tup1.count(3)
print(res)
res=tup1.index(3,4,8)
put=len(tup1)
print("3 comes in first index between 4 to 8 index :",res)
print(put)


# DAY 26
import time

t=time.strftime("%H:%M:%S")
print(t)
hour=time.strftime('%H')
print(hour)

if(hour>0 and hour<12):
    print("Good Morning")

elif(hour>=12 and hour<18):
    print("Good  Afternoon")

elif(hour>=18 and hour<=24):
    print("Good night")


#COLLAGE CODE

from flask import Flask,render template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///user.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)

class student(db.model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    subject=db.Column(db.String(50))
    roll=db.Column(db.String(50))
    contact=db.Column(db.String(50))

    def __init__(self,name,subject,roll,contact):
        self.name=name
        self.subject=subject
        self.roll=roll
        self.contact=contact

with app.app_context():
    db.create_all()

@app.route("/upload")
def dataLoad():

    data=[
        {
            'name':"goku",
            'subject':"martialart",
            'roll':'1',
            'contact':'48421834'
        },
        {
            'name':"gohan",
            'subject':"physics",
            'roll':'2',
            'contact':'48432834'
        },
        {
            'name':"vikratn",
            'subject':"math",
            'roll':'3',
            'contact':'23484234'
        }
    ] 
    for i in data:
        stud=student(i['name'],i['subject'],i['roll'],i['contact'])
        db.session.add(stud)
    db.session.commit()

    return "success"
@app.route('/')
def home():
    data=student.query.all
    print(data)

    return render_template('home.html',data=data)
#html
<html>
    <head>
        <title>home page</title>
    </head>
    <body>
        <style>
            table,th,td{
                border:1px solid black;
            }
        </style>
        <h1>Student table</h1>
        <table style="width:100%"
        <tr>
            <th>Id</th>
            <th>Name</th>
            <th>subject</th>
            <th>contact</th>
        </tr>

        {%for i in data%}
        <tr>
            <td>{{i.id}}</td>
            <td>{{i.name}}</td>
            <td>{{i.subject}}</td>
            <td>{{i.contact}}</td>
        </tr>
        {% endfor %}
    </body>
</html>












