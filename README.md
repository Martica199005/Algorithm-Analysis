# Algorithm-Analysis
Two algorithms have been implemented for solving the SAT (Satisfiability) problem, determining the execution times for them and creating simple graphs to illustrate the complexity of the algorithms.

The FNC-SAT algorithm uses the matrix form to represent a formula. In the matrix, the rows correspond to the clauses in the formula, and the columns - variables. Each variable can be: (i) not appear in a clause and it will be labeled with 0, (ii) appear without negation and labeled with 1, (iii) to appear negated and labeled with -1. To find an interpretation, the algorithm will use a “exhaustive search” approach over all possible interpretations.
The function find_expression returns the matrix and the number of the clauses in the input string recived.
fcn_find_interpretation is a function which has as arguments the matrix and the number of variables. A list of lists is created and each list inside has its lenght equal to the number of varibles and filled with all the possible permutations of 1 and -1. These lists are multplied for all the rows of the matrix and if for each row the result contains at least a 1 , it means that an interpretation exists and the function returns 1. If for all the lists in the list doesn't exists a list which is multplied for all the rows of the matrix and for each row the results haven't at least a 1, it means that an interpretation doesn't exists.

BDD-SAT Algorithm (Binary Decision Diagram SAT) The BDD-SAT algorithm is a variant that involves the use of diagrams Binary Decision Diagrams to represent Boolean formulas - or functions. For this purpose the function build_tree creates the unreduced diagrams. The convention for these trees is this: the left edge of a node will represents the assignment of the false value (0) to the variable corresponding to the respective node, and right edge, true value assignment (1).

Requirements

In this topic, we intend to write an implementation for FNC-SAT, respectively BDD-SAT. Both algorithms determine if there is at least one interpretation (assignment of variables), for each of the Boolean expressions received as input, so that the formula is evaluated to true. The only difference among the algorithms is the representation of the Boolean formula. Besides this, it is also required to measure the execution time of the solvents and their plotting. What we want to observe through these graphs is how time necessary to find an interpretation increases (exponentially) as the number of variables and clauses increases.



input The encoding of a formula will be done as a string in which: ● Variables will be encoded as integers (Attention, integers can have several digits) ● Negation will be encoded using the ‘’ character ● The disjunction will be encoded using the ‘V’ character (uppercase V) ● The conjunction will be encoded using the character ‘^’ An example of an input string would be the following: (11V2V-30) ^ (2V30V11) ^ (11V30) ^ ( 2V11) It contains 4 clauses: the first two clauses have 3 literals, and the last two clauses have two literals. The variables present in the formula are 11,2,30.

output For each test, the program will need to calculate the value of satisfaction of the expression, “sat_val” (‘1’ denoting that it is satisfactory and ‘0’ otherwise), and determine the execution times of the SAT solving algorithms - “Sat_time”, respectively BDD-SAT - “bdd_sat_time”. All this will be written in the output file in the format “sat_val sat_time bdd_sat_time”, which the checker will use to validate solutions. The name of the output file will be given as a parameter of the “main.py” program. Also, at the end you will have to generate a graph with the size Ox on the axis tests (calculated as the product of the number of variables and the number of clauses), and on Oy axis, the associated execution time (determined by the program). The chart will not be checked by the checker. Useful functions and programs We recommend using functions to measure execution time from the Python time module, and for plotting them, the gnuplot utility. You have more many details both in exercise 3 of laboratory 6 and in the linked resources. 






