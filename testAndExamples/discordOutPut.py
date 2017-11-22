import discord
import asyncio 
from xml.etree import ElementTree


class brain:
	def __init__(self):
		self.xs = 1
		#print('I should build xml here but ehhhhh')
	def checkCommand(self, userInput):
		with open('data.xml', 'rt') as f:
			tree = ElementTree.parse(f)


		for node in tree.iter('command'):	
			xmlInput = node.attrib.get('input')
			if(userInput==xmlInput):
				self.check = 't'
				return "True"
			else:
				self.check = 'f'
		if(self.check=='f'): #Doing this whole thing because IDK what the loop does once a return occurs... I suppose I could break but idk 
			return "False"

	def fetchCommand(self, userInput):
		with open('data.xml', 'rt') as f:
			tree = ElementTree.parse(f)
			print(userInput)
		for node in tree.iter('command'):	
			xmlInput = node.attrib.get('input')
			if(userInput==xmlInput):
				self.check = 't'
				output = node.attrib.get('comm')
				locals()[output]() #executes the function
			else:
				self.check = 'f'
		if(self.check=='f'):
			return "False"
				
						
	def fetchResp(self, userInput):
		with open('data.xml', 'rt') as f:
			tree = ElementTree.parse(f)
			print(userInput)
		for node in tree.iter('resp'):	
			xmlInput = node.attrib.get('input')
			if(userInput==xmlInput):
				self.check = 't'
				output = node.attrib.get('resps')
				return output
			else:
				self.check = 'f'
		if(self.check=='f'):
			return "False"
				
	def test(self):
		print('test')
				
client = discord.Client()
token = #your token goes here
@client.event	
async def on_message(message):
	if(message.author==client.user):
		return
	if(message.author!=client.user):
		userMessage = str(message.content)
		brainC = brain()
		x = brainC.checkCommand(userMessage)
		if(x=='True'):
			#input is a command
			command = brainC.fetchCommand(userMessage)
			print('exeCommand: '+ userMessage)
			#toss the command into a command execution script? or maybe execute a file with said name 
		if(x=='False'):
			# is just a word
			resp = brainC.fetchResp(userMessage)
			if(resp!='False'):
				await client.send_message(message.channel, resp)
			else:
				pass #its not here
@client.event
async def on_ready():
	print('User is: '+str(client.user))
client.run(token)
