class Teacher(object):

	Teachers = {1:"HEllo"};

	def __init__(self, regNum, name, age, email, ContactNum, address, yearsOfService, salary):
		self.name = name;
		self.email = email;
		self.regNum = regNum;
		self.age = age;
		self.ContactNum = ContactNum;
		self.address = address;
		self.yearsOfService = yearsOfService;
		self.salary = salary;


	def DisplayTeacherDetails(self):
		print("Register Number: " + str(self.regNum));
		print("Name: " + self.name);
		print("Age: " + str(self.age));
		print("Address: " + self.address);
		print("Contect Number: " + str(self.ContactNum));
		print("Email: " + self.email);
		print("Years Of Service: " + str(self.yearsOfService));
		print("Salary: " + str(self.salary));
		