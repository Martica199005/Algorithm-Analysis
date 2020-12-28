import numpy as np
import re

#NOT  ~
#OR v
#AND ^

# BOSS TE ROG EU MULT NU COPIA DE LA MINE SA ITI TRAIASCA SPIRITU CRACIUNULUI IN TINE
# DACA SCHIMBI NUMELE LA NISTE VARIABILE TOT COPIAT SE NUMESTE SI NE LUAM AMANDOI PE TEMA :\

str1="(11V2V~30)^(2V30V11)^(11V30)^(~2V11)"
re_path="\D"
re_path1='\((.*?)\)'
#print('---')
#m = re.search(re_path1, str1)
#print(m)
#print('---')
# first and second clause 3 literals?
#third and forth clause 2 literals?

#a = np.matrix('11 2 30; 1 1 0; 1 0 1;0 0 0')
#print(a)

def find_expression(formula):
    '''returns the matrix with values -1,1,0 : -1 means ~ var, 1 var, 0 
    var not appears in clause'''
    clause= formula.split("^")
    length_clause= len(clause)
    print(clause)
    print(length_clause)
    dict_literals={} # dictionary with literals
    literal_index = 0  # every literal has a index associated, unique
    s =(length_clause, 0) #rows,columns
    matrix_l = np.zeros(s)
    # iterate over clause
    for index_cl in range(0, length_clause):  # for every clause
      sub_clause = clause[index_cl]
      print('---')
      sub_clause = re.findall(re_path1,sub_clause)
      print(sub_clause[0])
      literals=sub_clause[0].split("V")
      print(literals)
      for index_lit in range(0, len(literals)):  # for every literal in sub clause
        literal = literals[index_lit] #single literal in each sub clause
        if literal[0] == '~':
          print(literal)
          
          if literal[1:] not in dict_literals:
            print(literal[1:])
            matrix_l= np.hstack((matrix_l, np.zeros((length_clause, 1))))
            print(matrix_l)
            dict_literals[literal[1:]] = literal_index #key literal, value index
            literal_index+=1
            print(dict_literals)
          matrix_l[index_cl, dict_literals[literal[1:]]] = -1
          #print(matrix_l)
        else:
          print('no tilde')
          if literal not in dict_literals:
            print(literal)
            matrix_l= np.hstack((matrix_l, np.zeros((length_clause, 1))))
            print(matrix_l)
            dict_literals[literal] = literal_index #key literal, value index
            literal_index+=1
            print(dict_literals)
          matrix_l[index_cl, dict_literals[literal]] = 1
          #print(matrix_l)
      print('---')
    inv_dict_literals= {v: k for k, v in dict_literals.items()}
    return matrix_l, inv_dict_literals
      


#matrix [0]
print(find_expression(str1)[0])
#inv dict [1]
#print(find_expression(str1)[1])