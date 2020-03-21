
class School():

	def __init__(self, name, year, address, num, email):
		self.name = name;
		self.startedyr = year;
		self.address = address;
		self.telnum = num;
		self.email = email;

	def DisplaySchoolDetails(self):
		print("Name: " + self.name);
		print("Address: " + self.address);
		print("Telephone Number: " + str(self.telnum));
		print("Email: " + self.email);
		print("startedYr: " + str(self.startedyr));
