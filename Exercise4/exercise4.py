#Exercise 4
# Create tree: http://ironcreek.net/phpsyntaxtree/
from __future__ import division
import math as m
import random as r

class node():
	def __init__(self, data):
		self.data = data
		self.children = {}

	def getTreeStructure(self):
		print 'len', len(self.children)
		if len(self.children) == 0:
			return "[" + str(self.data) + "]"
		else:
			print 'self.data', str(self.data)
			temp = "[" + str(self.data) + " "
		
		for k, v in self.children.items():
			print "k", k
			print "v", v
			print "taest", self.children[k]
			temp += self.children[k].getTreeStructure()
		
		return temp + "]"

def read_from_file(name):
	liste = []
	fil = open(name, 'r')
	for line in fil.readlines():
		liste.append(line.rstrip("\n").split("\t"))
	return liste

def print_list(l):
	for line in l:
		print line

def Plurality(examples):
	ones_count = 0
	twos_count = 0

	for n in xrange(0, len(examples)):
		if examples[-1] == '1': 
			ones_count += 1
		else: 
			twos_count += 1

	if ones_count > twos_count: 
		return 1
	elif twos_count > ones_count: 
		return 2
	else:
		return r.randint(1,2)

def same_classification(examples):
	classification = examples[0][-1]
	for n in xrange(1, len(examples)):
		if examples[n][-1] != classification:
			return False
	return True

def B(q):
	#print "q", q
	if q == 0.0: 
		return q
	else:
		return -( ( q*m.log(q, 2) ) + ( (1.0-q)*m.log((1.0-q), 2) ) )

def importance(data, attributes):
	print "attributelistavitarinn", attributes
	attribute_entropy = {}
	print "attribute list", attribute_entropy

	for attribute in attributes:
		count = 0
		for liste in data:
			if liste[attribute] == data[0][attribute]:
				count += 1
		print "attribute", attribute
		print "B", float( count/len(data)), count
		attribute_entropy[attribute] = B(float( count/len(data) ) )
	
	print attribute_entropy
	
	
	minimum = 1.1
	index = None
	for n in attribute_entropy:
		if attribute_entropy[n] < minimum:
			minimum = attribute_entropy[n]
			index = n
	print "N", index
	print '--------------------------------------------------------------------------------'
	return index

def decision_tree_learinng(examples, attributes, parent_examples, random_importance):
	if not examples:
		return Plurality(parent_examples)
	elif same_classification(examples):
		return examples[0][-1]
	elif not attributes:
		return Plurality(examples)
	else:
		if random_importance:
			A = attributes[ r.randint(0, len(attributes)-1) ]
		else:
			A = importance(examples, attributes)
		
		tree = node(A)
		attributes.remove(A)
		print "after remove", attributes
		
		for n in xrange(1,3):
			liste = []
			for e in examples:
				if int(e[A]) == n:
					liste.append(e)
			sub_tree = decision_tree_learinng(liste, list(attributes), examples, random_importance)
			tree.children[n] = sub_tree
	return tree


def main():
	test = read_from_file("Git/TDT4171/Exercise4/data/test.txt")
	training = read_from_file("Git/TDT4171/Exercise4/data/training.txt")
	#print_list(test)
	#print "\n"+"\n"
	#print_list(training)
	tree = decision_tree_learinng(training, range( len(training[0])-1 ), [], False)
	print "************************************************************************"
	print tree.getTreeStructure()

main()