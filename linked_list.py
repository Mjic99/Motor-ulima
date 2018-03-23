class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class List:

	def __init__(self):
		self.head = None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp