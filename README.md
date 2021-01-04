# Algorithm-Analysis
Two algorithms have been implemented for solving the SAT (Satisfiability) problem, determining the execution times for them and creating simple graphs to illustrate the complexity of the algorithms.

The FNC-SAT algorithm uses the matrix form to represent a formula. In the matrix, the rows correspond to the clauses in the formula, and the columns - variables. 
Each variable can be: (i) not appear in a clause and it will be labeled with 0, (ii) appear without negation and labeled with 1, (iii) to appear negated and labeled with -1. To find an interpretation, the algorithm will use a “exhaustive search” approach over all possible interpretations.
The function find_expression returns the matrix and the number of the clauses in the input string recived.
fnc_find_interpretation is a function which has as arguments the matrix and the number of variables. A list of lists is created and each list inside has its lenght equal to the number of varibles and filled with all the possible permutations of 1 and -1. These lists are multplied for all the rows of the matrix and if for each row the result contains at least a 1 , it means that an interpretation exists and the function returns 1. If for all the lists in the list doesn't exists a list which is multplied for all the rows of the matrix and for each row the results haven't at least a 1, it means that an interpretation doesn't exists.

BDD-SAT Algorithm (Binary Decision Diagram SAT) The BDD-SAT algorithm is a variant that involves the use of diagrams Binary Decision Diagrams to represent Boolean formulas - or functions. For this purpose the function build_tree creates the unreduced diagrams. The convention for these trees is this: the left edge of a node will represents the assignment of the false value (0) to the variable corresponding to the respective node, and right edge, true value assignment (1).
Also for this algorithm, if at least an interpretation exists for the given formula the function build_tree returns 1 else 0 if the formula isn't satisfiable.

 The only difference among the algorithms is the representation of the Boolean formula. 
 
The encoding of a formula is done as a string in which: 
● Variables are encoded as integers (integers can have several digits) 
● Negation is encoded using the '~' character 
● The disjunction (OR) is encoded using the 'V' character 
● The conjunction (AND) is encoded using the character '^' 


 Ox on the axis tests (calculated as the product of the number of variables and the number of clauses), and on Oy axis, the associated execution time (determined by the program). The chart will not be checked by the checker. 
 Besides this, it is also required to measure the execution time of the solvents and their plotting. 
 What we want to observe through these graphs is how time necessary to find an interpretation increases (exponentially) as the number of variables and clauses increases.






