#Exercise 4
# Create tree: http://ironcreek.net/phpsyntaxtree/

import math as m
import random as r

class node():
	def __init__(self, data):
		self.data = data
		self.children = {}

	#def print_tree()


def read_from_file(name):
	liste = []
	fil = open("Git/TDT4171/Exercise4/data/"+name+".txt", 'r')
	for line in fil.readlines():
		liste.append(line.rstrip("\n").split("\t"))
	#print_list(liste)
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
		if n[-1] != classification:
			return False
	return True

def B(q):
	if q = 0: 
		return q
	else:
		return -( ( q*m.log(q, 2) ) + ( (1.0-q)*m.log((1.0-q), 2) ) )

def importance(data, attributes):
	attribute_entropy = [None]*len(attributes)

	for attribute in attributes:
		count = 0
		for liste in data:
			if liste[attribute] == data[0][attribute]:
				count += 1
		attribute_entropy[attribute] = B(count/len(data))
	return min(attribute_entropy)


def decision_tree_learinng(examples, attributes, parent_examples):
	if not examples:
		return Plurality(parent_examples)
	elif same_classification(examples):
		return examples[0][-1]
	elif not attributes:
		return Plurality(examples)
	else:
		A = importance(examples, attributes)
		tree = node(A)
		attributes.remove(A)
		for n in xrange(1,3):
			liste = []
			for e in examples:
				if int(e[A]) == n:
					liste.append(e)
			sub_tree = decision_tree_learinng(liste, list(attributes), examples)
			tree.children += {n: sub_tree}







def main():
	test = read_from_file("test")
	print_list(test)
	training = read_from_file("training")
	#print "\n"+"\n"
	#print_list(training)


main()