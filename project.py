
class Student:

    def __init__(self, First, Last, Age, Email, ID):
        self.First = First
        self.Last = Last
        self.Age = Age
        self.Email = Email
        self.ID = ID
        self.courses = []

    def Add_student(self,First ,Last , Age, Email, ID):
        obj = Student(First, Last, Age, Email, ID)
        list_of_student.append(obj)

    def Search_st(self,no):
        for i in range(list_of_student.__len__()):
            if list_of_student[i].ID == no :
                return i
    def Remove_student(self, no):
        i = st.Search_st(no)
        del list_of_student[i]
        print("-----------------------------------------removed----------------------------------------------")

    def Update_student(self,ID,First,Last,Age,Email):
        i = st.Search_st(ID)
        list_of_student[i].First = First
        list_of_student[i].Last = Last
        list_of_student[i].Age = Age
        list_of_student[i].Email = Email

    def display(self, obj):
            print("ID : ", obj.ID)
            print("First Name   : ", obj.First)
            print("Last Name : ", obj.Last)
            print("Age : ", obj.Age)
            print("Email : ", obj.Email)
            print("\n")

class Professor:

    def __init__(self, First, Last, Age, Email,pro_ID,payment):
        self.First = First
        self.Last =Last
        self.Age=Age
        self.Email=Email
        self.pro_ID=pro_ID
        self.payment=payment

    def Add_professor(self,First,Last,Age,Email,pro_ID,payment ):
        obj = Professor(First,Last,Age,Email,pro_ID ,payment)
        list_of_professor.append(obj)

    def Search_professor(self, num):
        for i in range(list_of_professor.__len__()):
            if list_of_professor[i].pro_ID == num:
                return i

    def Remove_professor(self, no):
        i = pro.Search_professor(no)
        del list_of_professor[i]
        print("-----------------------------------------removed----------------------------------------------")

    def display(self, obj):
            print("ID : ", obj.pro_ID)
            print("First Name   : ", obj.First)
            print("Last Name : ", obj.Last)
            print("Age : ", obj.Age)
            print("Email : ", obj.Email)
            print("payment  : ", obj.payment)
            print("\n")
class Course :
    def __init__(self,code,name,unit,capacity,professor,time,location):
        self.name = name
        self.unit =unit
        self.capacity = capacity
        self.time=time
        self.location=location
        self.professor = professor
        self.code=code

    def Add_course(self,code,name,unit,capacity,professor,time,location):
        obj = Course(code,name,unit,capacity,professor,time,location)
        list_of_course.append(obj)

    def Search_course(self, num):
        for i in range(list_of_course.__len__()):
            if (list_of_course[i].code == num):
                return i

    def Remove_course(self, no):
        i = co.Search_course(no)
        del list_of_course[i]
        print("-----------------------------------------removed----------------------------------------------")

    def display(self, obj):
            print("course code : ", obj.code)
            print("course Name  : ", obj.name)
            print("professor : ", obj.professor)
            print("capacity : ", obj.capacity)
            print("unit : ", obj.unit)
            print("course time : ", obj.time)
            print("location : ", obj.location)
            print("\n")


list_of_professor = []
list_of_student = []
list_of_course = []

def menu():
    print("1.Student Management" )
    print("2.Professor  Management")
    print("3.Course  Management")
    print("4.Course  Selection")
    print("5.show courses you have selected")
def sudent_menu():
    print("1.Add Student ")
    print("2.Show Student ")
    print("3.Edit Student ")
    print("4.Delete Student ")
    print("0.Exit ")
def professor_menu():
    print("1.Add professor ")
    print("2.Search professor ")
    print("3.Delete professor ")
    print("0.Exit ")
def course_menu():
    print("1.Add course ")
    print("2.Search course ")
    print("3.Delete course ")
    print("0.Exit ")

def course_selection():
    id=int(input("Enter your id :  "))
    for i in range (list_of_student.__len__()):
        if id == list_of_student[i].ID :
            print("course name   course code")
            for i in range(list_of_course.__len__()):
                print(list_of_course[i].name, end='       ')
                print(list_of_course[i].code)
                print("\n")
            code = int(input("choose a course code :  "))
            for i in range(list_of_course.__len__()):
                if code == list_of_course[i].code:
                    list_of_course[i].capacity -= 1
                    list_of_student[i].courses.append(list_of_course[i])
                else:
                    print("there is no course with this code")
        else:
            print("there is no student  with this id")

def show(obj):
    for i in range(obj.courses.__len__()):
        print("course Name  : ", obj.courses[i].name,end='  ')
        print("professor : ", obj.courses[i].professor,end='   ')
        print("course time : ", obj.courses[i].time,end='   ')
        print("location : ", obj.courses[i].location,end='   ')
        print("\n")
while True:
    menu()
    try:
        choice1=int(input("please enter a number : "))
        st = Student("","",0,"",0)
        pro = Professor("","",0,"",0,0)
        co = Course(0,"",0,0,"",0,"")
        if choice1==1:
            choice2=-1
            while choice2:
                sudent_menu()
                choice2 = int(input("please enter a number : "))
                if choice2==1:
                    first=input("first name : ")
                    last = input("last name : ")
                    age = int(input("age : "))
                    email = input("email : ")
                    id = int(input("id : "))
                    st.Add_student(first,last,age,email,id)
                elif choice2==2:
                    iid=int(input("Enter id : "))
                    d=st.Search_st(iid)
                    st.display(list_of_student [d])
                elif choice2 == 3:
                    iid=int(input("Enter id : "))
                    d=st.Search_st(iid)
                    first=input("first name : ")
                    last = input("last name : ")
                    age = int(input("age : "))
                    email = input("email : ")
                    st.Update_student(iid,first,last,age,email)
                    st.display(list_of_student[d])
                elif choice2 == 4:
                    iid=int(input("Enter id : "))
                    st.Remove_student(iid)
        elif choice1==2:
             choice2 = -1
             while choice2:
               professor_menu()
               choice2 = int(input("please enter a number : "))
               if choice2 == 1:
                    first = input("first name : ")
                    last = input("last name : ")
                    age = int(input("age : "))
                    email = input("email : ")
                    id = int(input("id : "))
                    payment  = int(input("payment : "))
                    pro.Add_professor(first, last, age, email, id,payment)
               elif choice2 == 2:
                   iid = int(input("Enter id : "))
                   d = pro.Search_professor(iid)
                   pro.display(list_of_professor[d])

               elif choice2 == 3:
                   iid = int(input("Enter id : "))
                   pro.Remove_professor(iid)
        elif choice1==3:
            choice2 = -1
            while choice2:
               course_menu()
               choice2 = int(input("please enter a number : "))
               if choice2 == 1:
                 code =int( input("course code : "))
                 name = input("course name  : ")
                 unit = int(input("course unit : "))
                 professor  = input(" course professor : ")
                 capacity = int(input(" course capacity : "))
                 time = int(input(" course time : "))
                 location=input(" course location :")
                 co.Add_course(code,name,unit,capacity,professor,time,location)
               elif choice2 == 2:
                 iid = int(input("Enter course code  : "))
                 s=co.Search_course(iid)
                 co.display(list_of_course[s])
               elif choice2 == 3:
                 iid = int(input("Enter course code  : "))
                 co.Remove_course(iid)
        elif choice1== 4:
            course_selection()
        elif choice1== 5:
            id = int(input("Enter your id : "))
            d = st.Search_st(id)
            show(list_of_student[d])

    except Exception as e:
        print(e)