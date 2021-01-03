#  Read input from STDIN. Print output to STDOUT
import sys
import math
import re
import operator
import time
import itertools
from itertools import combinations



re_path="\d+"
re_path1='\((.*?)\)'






def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
 
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0)
 
    return M


def find_expression(formula):
    '''returns the matrix with values -1,1,0 : -1 means ~ var, 1 var, 0 
    var not appears in clause'''
    clause= formula.split("^")
    length_clause= len(clause)
    #print(length_clause)
    dict_literals={} # dictionary with literals
    literal_index = 0  # every literal has a index associated, unique
    matrix_l = zeros_matrix(length_clause, number_variables)
    # iterate over clause
    for index_cl in range(0, length_clause):  # for every clause
      sub_clause = clause[index_cl]
      sub_clause = re.findall(re_path1,sub_clause)
      literals=sub_clause[0].split("V")
      for index_lit in range(0, len(literals)):  # for every literal in sub clause
        literal = literals[index_lit] #single literal in each sub clause
        if literal[0] == '~':
          if literal[1:] not in dict_literals:
            #matrix_l= np.hstack((matrix_l, np.zeros((length_clause, 1))))
            dict_literals[literal[1:]] = literal_index #key literal, value index
            literal_index+=1
          matrix_l[int(index_cl)][int(dict_literals.get(literal[1:]))] = -1
        else:
          if literal not in dict_literals:
            #matrix_l= np.hstack((matrix_l, np.zeros((length_clause, 1))))
            dict_literals[literal] = literal_index #key literal, value index
            literal_index+=1
          matrix_l[int(index_cl)][int(dict_literals.get(literal))] = 1
   
    return matrix_l, length_clause

def fcn_find_interpretation(matrix_lit,number_variables):
  '''I find the first combination that gives me all True but as soon as I find only one False I stop and go to the next combination'''
  values=[-1,1]
  a=iter([list(p) for p in itertools.product(values, repeat=number_variables)])
  for a_item in a:
    count=0
    for line in range(0,len(matrix_lit)):
      count+=1
      result_clause = list(map(operator.mul,a_item,list(matrix_lit[line])))
      if 1 not in result_clause:
        break
    if count==len(matrix_lit) and 1 in result_clause:
      return 1, a_item
  return 0, None






def write_out(filename,word):
  # The 'a' flag tells Python to keep the file contents
  # and append (add line) at the end of the file.
  myfile = open(filename, 'a')

  # Add the line
  myfile.write(word+"\n")

  # Close the file
  myfile.close()


#for line in sys.stdin
#   expression=line

filename="input09.txt"

f = open(filename, "r")
expression =f.read()
m = re.findall(re_path, expression)
list_variables=list(set(m))
#print(list_variables)
number_variables=len(list_variables)
#print(number_variables)
t1= time.process_time()
matrix_input, length_formula = find_expression(expression)
#print(len(matrix_input))
#print(matrix_input)
result,interpretation=fcn_find_interpretation(matrix_input,number_variables)
elapsed_time = time.process_time() - t1
#time in seconds
word1=str(number_variables)+" "+str(elapsed_time)+" s"
print(word1)
write_out('output.txt',word1)
print(result)
print(interpretation)



















