import Teacher;
import School;
import Students;


while (1):
	try:
		print("press 1 to add School");
		print("press 2 to add Teacher");
		print("press 3 to add Student");
		print("press 0 Exist");
		
		print("Enter the number");
		p = int(input());

		if(p == 1):
			name = raw_input("Name: ");
			yr = raw_input("Year: ");
			Address = raw_input("Address: ");
			num = raw_input("num: ");
			email = raw_input("email: ");

			s2 = School.School(name, yr, Address , num, email);
			s2.DisplaySchoolDetails(); 

		elif(p == 2):
			regNum = raw_input("Register number: ");
			name = raw_input("name: ");
			age = raw_input("age: ");
			Address = raw_input("Address: ");
			num = raw_input("num: ");
			email = raw_input("email: ");
			yrofservice = raw_input("Years of Service: ");
			salary = raw_input("Salary: ");

			t2 = Teacher.Teacher(regNum, name, age, email, num, Address, yrofservice, salary);
			t2.DisplayTeacherDetails();

		elif(p == 3):
			regNum = raw_input("Register number: ");
			name = raw_input("name: ");
			grade = raw_input("grade: ");
			Address = raw_input("Address: ");
			num = raw_input("TelNumber: ");
			email = raw_input("email: ");
			Fname = raw_input("Father Name: ");
			Mname = raw_input("Mother name: ");

			stu1 = Students.Students(regNum, name, grade, Address, num, email, Fname, Mname);
			stu1.DisplayStudentDetails();

		elif(p == 0):
			print("Thank you for using....\nBYE......");
			break;
		break;

	except Exception as e:
		print("\n");
		print(e)
		# print("This is not a Valid Number!!!!!!\nPlease enter only the numbers provided below!!!!!!!!");
		print("\n");


# s2.DisplaySchoolDetails();
# t2.DisplayTeacherDetails();
# stu1.DisplayStudentDetails();
# print("\n");
# t1.DisplayTeacherDetails();