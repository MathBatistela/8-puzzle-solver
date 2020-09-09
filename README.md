# 8-puzzle-solver

A.I - Implemented A* to solve the 8-puzzle problem.

### Usage
```
python3 main.py [initial state] [args]

args:	--terminal (print the result on terminal)
	--file (export the result in a file named "output.txt"
        --all (executes the above two commands together)
  
example: python3 main.py 1,0,3,4,2,5,7,8,6 --terminal
```
### Representation
```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 |   | 5 |
+---+---+---+
| 7 | 8 | 6 |
+---+---+---+
|   order   |
+-----------+
|depth |cost|
+-----------+
```

### Example
```
python3 main.py 1,0,3,4,2,5,7,8,6 --terminal
```
