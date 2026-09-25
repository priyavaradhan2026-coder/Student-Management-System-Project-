from colorama import Fore, Style, init
init(autoreset=True)
class Student():
    def __init__(self,student_id,name,age,marks):
       self.student_id=student_id
       self.name=name
       self.age=age
       self.marks=marks
 
    def display(self):
        print("\nstudent_ID:",self.student_id)
        print("name        :",self.name)
        print("age         :",self.age)
        print("marks       :",self.marks)
 
 
class StudentManagementSystem():
    def __init__(self):
        self.students=[]
 
    def get_valid_int(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                 print(Fore.RED + "Invalid input! Please enter a number.")
 
    def add_student(self):
        n = self.get_valid_int("how many student do you want to add ?:")
 
        for i in range(n):
            print(f"\nEnter the details of the student{i+1}")
 
            student_id = self.get_valid_int("Enter student_id:")
            name = input("Enter student name:")
            age = self.get_valid_int("Enter student age:")
            marks = float(input("Enter student marks:"))
 
            student=Student(student_id,name,age,marks)
            self.students.append(student)
 
        print(Fore.GREEN+f"\n{n} Student added successfully!")
 
    def view_student(self):
        if len(self.students)==0:
            print("No students found")
        else:
            print("\n----------student Details----------")
            for student in self.students:
                student.display()
 
    def search_student(self):
        student_id = self.get_valid_int("Enter student ID to search:")
 
        for student in self.students:
            if student.student_id==student_id:
                print("\n student Found!")
                student.display()
                return
        print("\n student Not Found!")
 
    def update_marks(self):
        student_id = self.get_valid_int("Enter student Id:")
        for student in self.students:
            if student.student_id==student_id:
                new_marks=float(input("Enter new mark:"))
                student.marks=new_marks
                print(Fore.GREEN+"Marks updated successfully")
                return
        print("Student Not Found")
 
    def delete_student(self):
        student_id = self.get_valid_int("Enter student ID:")
        for student in self.students:
            if student.student_id==student_id:
                self.students.remove(student)
                print(Fore.GREEN+"\n Student deleted successfully!")
                return
        print("Student Not Found")
 
    def display_topper(self):
        if len(self.students)==0:
            print("No students available")
        else:
            topper=self.students[0]
            for student in self.students:
                if student.marks > topper.marks:
                    topper=student
            print(Fore.GREEN+"\n--Topper Details----")
            topper.display()
 
 
sms=StudentManagementSystem()
 
while True:
    print("\n=======STUDENT MANAGEMENT SYSTEM=====")
    print("1. Add student:")
    print("2. View student:")
    print("3. Search student:")
    print("4. Update student:")
    print("5. Delete student:")
    print("6. Display Topper:")
    print("7. Exit")
 
    choice = sms.get_valid_int("Enter your choice:")
 
    if choice==1:
        sms.add_student()
    elif choice==2:
        sms.view_student()
    elif choice==3:
        sms.search_student()
    elif choice==4:
        sms.update_marks()
    elif choice==5:
        sms.delete_student()
    elif choice==6:
        sms.display_topper()
    elif choice==7:
        print("======THANK YOU======")
        break
    else:
        print("Invalid choice")
