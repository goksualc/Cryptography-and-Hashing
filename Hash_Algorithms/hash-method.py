class Emp:
	def __init__(self, emp_name, id):
		self.emp_name = emp_name
		self.id = id

	def __eq__(self, other):
	
		return self.emp_name == other.emp_name and self.id == other.id

	def __hash__(self):
	
		return hash((self.emp_name, self.id))

emp = Emp('Ragav', 12)
print("The hash is: %d" % hash(emp))

emp_copy = Emp('Ragav', 12)
print("The hash is: %d" % hash(emp_copy))
