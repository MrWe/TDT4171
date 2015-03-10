#Exercise 4

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


def decision_tree_learinng(examples, attributes, parent_examples):
	if not examples:
		return Plurality(parent_examples)
	elif same_classification(examples):
		return examples[0][-1]
	elif not attributes:
		return Plurality(examples)
	else:
		A = importance(a, examples)
		tree = 
		for n in 






def main():
	read_from_file("test")
	print "\n"+"\n"
	read_from_file("training")


main()