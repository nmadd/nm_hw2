3_1a Tests:
# there's a full cascade when q is less than .5 (1/2)
Infection Rate: 100.0% X: 4 Y: 0 Q: 0.45 K: set([1, 2]) Num of Tests: 1
Infection Rate: 100.0% X: 4 Y: 0 Q: 0.46 K: set([1, 2]) Num of Tests: 1
Infection Rate: 100.0% X: 4 Y: 0 Q: 0.47 K: set([1, 2]) Num of Tests: 1
Infection Rate: 100.0% X: 4 Y: 0 Q: 0.48 K: set([1, 2]) Num of Tests: 1
Infection Rate: 100.0% X: 4 Y: 0 Q: 0.49 K: set([1, 2]) Num of Tests: 1
# but when q reaches .5, there's an equilibria
Infection Rate: 50.0% X: 2 Y: 2 Q: 0.5 K: set([1, 2]) Num of Tests: 1
Infection Rate: 50.0% X: 2 Y: 2 Q: 0.51 K: set([1, 2]) Num of Tests: 1
Infection Rate: 50.0% X: 2 Y: 2 Q: 0.52 K: set([1, 2]) Num of Tests: 1
Infection Rate: 50.0% X: 2 Y: 2 Q: 0.53 K: set([1, 2]) Num of Tests: 1
Infection Rate: 50.0% X: 2 Y: 2 Q: 0.54 K: set([1, 2]) Num of Tests: 1


3_1b Tests:
# there's a full cascade when q is less than .33 (1/3)
X: 7 Y: 0 Q: 0.3 K: set([1, 2, 3]) Num of Tests: 1
X: 7 Y: 0 Q: 0.31 K: set([1, 2, 3]) Num of Tests: 1
X: 7 Y: 0 Q: 0.32 K: set([1, 2, 3]) Num of Tests: 1
X: 7 Y: 0 Q: 0.33 K: set([1, 2, 3]) Num of Tests: 1
# however above .33, there's equilibria
X: 3 Y: 4 Q: 0.34 K: set([1, 2, 3]) Num of Tests: 1
X: 3 Y: 4 Q: 0.35 K: set([1, 2, 3]) Num of Tests: 1
X: 3 Y: 4 Q: 0.36 K: set([1, 2, 3]) Num of Tests: 1
X: 3 Y: 4 Q: 0.37 K: set([1, 2, 3]) Num of Tests: 1
X: 3 Y: 4 Q: 0.38 K: set([1, 2, 3]) Num of Tests: 1
X: 3 Y: 4 Q: 0.39 K: set([1, 2, 3]) Num of Tests: 1
