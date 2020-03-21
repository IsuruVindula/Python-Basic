
class Students():
	def __init__(self, regnum, name, grade, address, num, email, Fname,Mname):
		self.name = name;
		self.regnum - regnum;
		self.grade = grade;
		self.address = address;
		self.telnum = num;
		self.email = email;
		self.fatherName = Fname;
		self.motherName = Mname;

	def DisplayStudentDetails(self):
		print("RegNumber: " + str(self.regnum));
		print("Name: " + self.name);
		print("Address: " + self.address);
		print("Telephone Number: " + str(self.telnum));
		print("Email: " + self.email);
		print("Grade: " + str(self.grade));
		print("Father's Name: " + self.fatherName);
		print("Mother's Name: " + self.motherName);

