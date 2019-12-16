class Node:

	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:

	def __init__(self):
		self.head=None


	def insertb(self,data):

		newnode=Node(data)
		newnode.next=self.head
		self.head=newnode

	def insertafternode(self,previousnode,data):

		newnode = Node(data)
		newnode.next=previousnode.next
		previousnode.next=newnode



	def insertatlast(self,data):

		newnode=Node(data)
		temp=self.head
		while (temp.next):
			temp=temp.next
		temp.next=newnode

	def deletefirstoccnode(self,key):
		temp=self.head
		if temp.data==key:
			self.head=temp.next
			temp=None
			return

		while(temp is not None):
			if temp.data==key:
				brek
			prev=temp
			temp=temp.next

		if temp==None:
			return

		prev.next=temp.next
		temp=None

	def deleteatgivenposition(self,pos):

		temp=self.head
		if pos==0:
			self.head=temp.next
			temp=None
			return

		for i in range(pos-1):
			if 



	def printlist(self):

		temp=self.head
		while (temp):
			print temp.data,
			temp=temp.next

		
if __name__=='__main__':
	llist=LinkedList()
	# llist.head=Node(1)
	
	llist.insertb(10)
	llist.insertb(9)
	llist.insertb(8)
	llist.insertatlast(11)
	llist.insertafternode(llist.head.next,1)

	llist.printlist()