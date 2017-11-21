from xml.etree import ElementTree

class start:
	def __init__(self):
		self.xs = '0'
		
	def main(self):
		self.userInput = input('[WALTOR]: ')
		print('This is a test to see how the brain *could* work')
		print('importing the xml sheet')
		with open('data.xml', 'rt') as files:
			tree = ElementTree.parse(files)
		#Check if input is in command list
		brainC = brain()
	
		self.x = brainC.checkCommand(self.userInput)
		if(self.x=='True'):
			#input is a command
			self.command = brainC.fetchCommand(self.userInput)
			print('exeCommand: '+ userInput)
			#toss the command into a command execution script? or maybe execute a file with said name 
		if(self.x=='False'):
			# is just a word
			self.resp = brainC.fetchResp(self.userInput)
			if(self.resp!='False'):
				print(self.resp)
			else:
				
				print('Command and responses')
class brain:
	def __init__(self):
		self.xs = 1
		#print('I should build xml here but ehhhhh')
	def checkCommand(self, userInput):
		with open('data.xml', 'rt') as f:
			tree = ElementTree.parse(f)
		for path in[ './commands/resp' ]:	
			node = tree.find(path)
			if(userInput==node.text):
				self.check = 't'
				return "True"
			else:
				self.check = 'f'
		if(self.check=='f'): #Doing this whole thing because IDK what the loop does once a return occurs... I suppose I could break but idk 
			return "False"
			
			
	def fetchResp(self, userInput):
		with open('data.xml', 'rt') as f:
			tree = ElementTree.parse(f)
		for path in[ './responses/resp' ]:	
			node = tree.find(path)
			if(userInput==node.text):
				self.check = 't'
				return node.tail
			else:
				self.check = 'f'
			if(self.check=='f'):
				return "Not Found"
				
				
				
				
startC = start()
startC.main()
