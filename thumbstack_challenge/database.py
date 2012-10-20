#!/usr/local/bin/python

"""
you can find challenge description on:
http://www.thumbtack.com/challenges


SET [name] [value]: Set a variable [name] to the value [value]. 
	Neither variable names or values will ever contain spaces.

GET [name]: Print out the value stored under the variable [name]. 
	Print NULL if that variable name hasn't been set.

UNSET [name]: Unset the variable [name]

NUMEQUALTO [value]: Return the number of variables equal 
	to [value]. If no values are equal, this should output 0.

BEGIN: Open a transactional block

ROLLBACK: Rollback all of the commands from the most recent transaction block. 
	If no transactional block is open, print out INVALID ROLLBACK

COMMIT: Permanently store all of the operations from any presently open transactional blocks

END: Exit the program
"""
import sys


supported_statements = ['SET', 'GET', 'UNSET', 'END', 'NUMEQUALTO','BEGIN', 'ROLLBACK', 'COMMIT']
end_statement = 'END'



class Database(object):

	def __init__(self):
		""" initialize database"""
		self.db = {}
		self.equal_values = {} #keep the number of equal values (increase and decrease) O(1) - NUMEQUALTO
		self.transaction_log = [] # transaction log - cleared after commit		
		self.transaction_mode = False #are you in transaction mode

	def set(self, key, value):
		self.db[key] = value
		if self.equal_values.has_key(value):
			self.equal_values[value] += 1
		else:
			self.equal_values[value] = 1

		# add to transaction log if in transaction mode
		if self.transaction_mode:
			self.transaction_log.append(['SET', key, value ])

	def get(self, key):
		if self.db.has_key(key):
			return self.db[key]
		return False

	def unset(self, key):
		""" unset - if key does not exist - do nothing"""
		if self.db.has_key(key):
			value = self.db[key] #remove from values
			self.equal_values[value] -= 1
			del self.db[key]

		# add to transaction log if in transaction mode
		if self.transaction_mode:
			self.transaction_log.append(['UNSET', key, value])

	def numequalto(self, key):
		if self.equal_values.has_key(key):
			return self.equal_values[key]
		return 0

	def commit(self):
		""" commit clears transaction log - everything is in DB already """
		del self.transaction_log[:] 
		self.transaction_mode = False

	def	begin(self):
		""" begin transaction - set transaction mode and append to transaction log """
		self.transaction_mode = True
		self.transaction_log.append('BEGIN')

	def rollback(self):
		remove = True
		if len(self.transaction_log) < 1:
			print 'INVALID ROLLBACK'
		else:
			while remove:
				# turn of transaction mode while removing
				self.transaction_mode = False
				item = self.transaction_log.pop()
				if item == 'BEGIN' :
					remove = False
				elif item[0] == 'SET':
					self.call_statement(['UNSET', item[1]])
				elif item[0] == 'UNSET':
					self.call_statement(['SET', item[1], item[2]])

			i = len(self.transaction_log) - 1
			if i > 0:
				while self.transaction_log[i] != 'BEGIN':
					i -= 1

			self.transaction_mode = True
			for statement in self.transaction_log[i:]:
				self.call_statement(statement)
					

	def call_statement(self, statement):
		""" call statement """
		if statement[0] == 'GET':
			if len(statement) != 2:
				print 'syntax error - GET [name]'
			else:
				key = statement[1]
				value = self.get(key)
				if value:
					print value
				else:
					print 'NULL'

		elif statement[0] == 'SET':
			if len(statement) != 3:
				print 'syntax error - SET [name] [value]'
			else:
				key = statement[1]
				value = statement[2]
				self.set(key, value)

		elif statement[0] == 'UNSET':
			if len(statement) != 2:
				print 'syntax error - UNSET [name]'
			else:
				key = statement[1]
				self.unset(key)

		elif statement[0] == 'NUMEQUALTO':
			if len(statement) != 2:
				print 'syntax wrror - NUMEQUALTO [name]'
			else:
				key = statement[1]
				print self.numequalto(key)

		elif statement[0] == 'BEGIN':
			self.begin()
       
		elif statement[0] == 'ROLLBACK':
			self.rollback()	

		elif statement[0] == 'COMMIT':
			self.commit()
				
				 				

if __name__ == '__main__':
	statements_stack = []
	db = Database()
	print 'Simple DB v1.0.0'
	while True:
		statement = raw_input('>>').strip().split()
		if len(statement) < 1:
			print 'wrong statement'
		elif statement[0] == end_statement:
			print 'closing ...'
			sys.exit(0)
		elif statement[0] not in supported_statements:
			print 'unsupported statement'
		else:
			db.call_statement(statement)
				 
