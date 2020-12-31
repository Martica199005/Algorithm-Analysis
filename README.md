# Algorithm-Analysis
Theme objectives The objectives of the theme are the implementation in Python of two algorithms for solving the SAT (Satisfiability) problem, determining the execution times for them and creating simple graphs to illustrate the complexity of the algorithms.

algorithms

The FNC-SAT algorithm The FNC-SAT algorithm uses the matrix form to represent a formula. In the matrix, the rows correspond to the clauses in the formula, and the columns - variables. Each variable can be: (i) not appear in a clause, (ii) appear without negation, (iii) to appear negated. To find an interpretation, the algorithm will have a “exhaustive search” (or brute force search which consists of systematically enumerating all possible candidates for the solution and checking whether each candidate satisfies the problem's statement) approach over all possible interpretations. You can identify and add local optimizations to remove some interpretations (e.g. for situations where a variable does not appear in a clause).

BDD-SAT Algorithm (Binary Decision Diagram SAT) The BDD-SAT algorithm is a variant that involves the use of diagrams Binary Decision Diagrams, presented in the course, to represent Boolean formulas - or functions. For the purpose of this topic we will considered satisfactory the unreduced version of these diagrams, namely the trees decision tracks. The convention for these trees is this: the left edge of a node will represents the assignment of the false value (0) to the variable corresponding to the respective node, and right edge, true value assignment (1).

To find the result of the evaluation of the function f under the interpretation {x3} for example, we go through the tree starting from the initial node x1, in the order of the edges left-left-right (x1 = 0, x2 = 0, x3 = 1), reaching the value of truth 0.

Requirements

In this topic, we intend to write an implementation for FNC-SAT, respectively BDD-SAT. Both algorithms determine if there is at least one interpretation (assignment of variables), for each of the Boolean expressions received as input, so that the formula is evaluated to true. The only difference among the algorithms is the representation of the Boolean formula. Besides this, it is also required to measure the execution time of the solvents and their plotting. What we want to observe through these graphs is how time necessary to find an interpretation increases (exponentially) as the number of variables and clauses increases.

Importance SAT was the first problem discovered to be NP-complete, thanks to the theorem Cook-Levin. As a result, it was studied for a long time, discovering many heuristic algorithms that can find (most of the time) valid configurations in time polynomial, despite the fact that it is not yet known whether or not there is an exact algorithm to solve SAT in polynomial time. These solvents are very useful in the case many other problems for which, in the same way, that no effective solutions have been formulated - by usually also NP-complete problems - because we can reduce them polynomially to SAT.

Specifications The main program, which will be run by the checker, will have to have the name "Main.py". It can include as many other modules as you need. The only restriction is the file name and the fact that all the secondary modules, written by you, must be find out in the same directory with him.

input The encoding of a formula will be done as a string in which: ● Variables will be encoded as integers (Attention, integers can have several digits) ● Negation will be encoded using the ‘’ character ● The disjunction will be encoded using the ‘V’ character (uppercase V) ● The conjunction will be encoded using the character ‘^’ An example of an input string would be the following: (11V2V-30) ^ (2V30V11) ^ (11V30) ^ ( 2V11) It contains 4 clauses: the first two clauses have 3 literals, and the last two clauses have two literals. The variables present in the formula are 11,2,30.

output For each test, the program will need to calculate the value of satisfaction of the expression, “sat_val” (‘1’ denoting that it is satisfactory and ‘0’ otherwise), and determine the execution times of the SAT solving algorithms - “Sat_time”, respectively BDD-SAT - “bdd_sat_time”. All this will be written in the output file in the format “sat_val sat_time bdd_sat_time”, which the checker will use to validate solutions. The name of the output file will be given as a parameter of the “main.py” program. Also, at the end you will have to generate a graph with the size Ox on the axis tests (calculated as the product of the number of variables and the number of clauses), and on Oy axis, the associated execution time (determined by the program). The chart will not be checked by the checker. Useful functions and programs We recommend using functions to measure execution time from the Python time module, and for plotting them, the gnuplot utility. You have more many details both in exercise 3 of laboratory 6 and in the linked resources. restriţii The execution time of the solvents must not exceed 30 seconds.






