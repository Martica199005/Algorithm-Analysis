import re
import sys
import time

re_path="\d+"

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val



def simplify_expresion(expression):
    new_clauses=[]
    expression = str(expression)
    expression=(expression.replace("(","")).replace(")","")
    
    clauses = expression.split("^")
    if "False" in clauses:
        return "False"
    for i in range(0,len(clauses)):
      if "False" in clauses[i]:
        clauses[i]=clauses[i].replace("False","")
      if "True" in clauses[i]:
        clauses[i]=""
      sub_clause=clauses[i].split("V")
      sub_clause = list(filter(None,sub_clause))
      separator1="V"
      clauses[i]=separator1.join(sub_clause)
      new_clauses.append(clauses[i])
    
    new_clauses = list(filter(None,new_clauses))
    if len(new_clauses) == 0:
      return "True"
    new_clauses = [i for i in new_clauses if i != "True"]
    separator = "^"
    return separator.join(new_clauses)


def build_tree(expr, literals):
    queue = []

    root = Node(expr)
    queue.append((root, 0))
    while True:
        curr_tuple = queue.pop(0)
        curr_node = curr_tuple[0]
        level = curr_tuple[1]
        # reached a leaf node, tree is complete
        if level == len(literals):
            queue.insert(0, curr_tuple)
            break

        # built left child for negative case
        expression_left = str(curr_node.value)
        expression_left = expression_left.replace(literals[level], "False")
        expression_left = expression_left.replace("~False", "True")
        expression_left = simplify_expresion(expression_left)


        # built right child for negative case
        expression_right = str(curr_node.value)
        expression_right = expression_right.replace(literals[level], "True")
        expression_right = expression_right.replace("~True", "False")
        expression_right = simplify_expresion(expression_right)

        # create left and right nodes
        node_l = Node(expression_left)
        node_r = Node(expression_right)
        # add left and right child
        curr_node.left = node_l
        curr_node.right = node_r
        # adding nodes to queue
        queue.append((node_l, level + 1))
        queue.append((node_r, level + 1))

    for x in queue:
      if x[0].value=="True":
        return 1

    return 0


def write_out(filename,word):
  # The 'a' flag tells Python to keep the file contents
  # and append (add line) at the end of the file.
  myfile = open(filename, 'a')

  # Add the line
  myfile.write(word+"\n")

  # Close the file
  myfile.close()


#for line in sys.stdin:
# expression=line
filename="input09.txt"

f = open(filename, "r")
expression =f.read()
m = re.findall(re_path, expression)
list_variables=list(set(m))
number_variables=len(list_variables)
list_variables=[int(i) for i in list_variables]
list_variables.sort(reverse=True)
literals ={ i : str(list_variables[i]) for i in range(0, len(list_variables) ) }
#print(literals)
t1= time.process_time()
print(build_tree(expression, literals))
elapsed_time1 = time.process_time() - t1
#time in seconds
word1=filename+" "+"number of variables "+str(number_variables)+", time "+str(elapsed_time1)+" s"
print(word1)
write_out('output.txt',word1)


