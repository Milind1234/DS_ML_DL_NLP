# =============================================================================
#                    SUPPORT VECTOR CLASSIFIER (SVC)
# =============================================================================
#
# Author : ChatGPT
# Topic  : Support Vector Machine - Classification
#
# Prerequisite:
# 1. Linear Algebra
# 2. Vectors
# 3. Dot Product
# 4. Logistic Regression
# 5. Distance of Point from Plane
#
# =============================================================================
# TABLE OF CONTENTS
# =============================================================================
#
# 1. Introduction
# 2. Why SVM?
# 3. Logistic Regression vs SVM
# 4. Hyperplane
# 5. Support Vectors
# 6. Margin
# 7. Maximum Margin Classifier
# 8. Hard Margin
# 9. Soft Margin
# 10. Mathematical Intuition
# 11. Hyperplane Equation
# 12. Support Vector Equations
# 13. Margin Derivation
# 14. Optimization Objective
# 15. Constraints
# 16. Hinge Loss
# 17. Slack Variables
# 18. Hyperparameter C
# 19. Cost Function
# 20. Prediction Process
# 21. Advantages
# 22. Disadvantages
# 23. Scikit-Learn Implementation
# 24. Interview Questions
# 25. Formula Sheet
#
# =============================================================================



# =============================================================================
# 1. INTRODUCTION
# =============================================================================

"""
Support Vector Machine (SVM) is a supervised machine learning algorithm.

It can solve:

1. Classification Problems
2. Regression Problems

Classification Version:
-----------------------
Support Vector Classifier (SVC)

Regression Version:
-------------------
Support Vector Regressor (SVR)

In this file we will discuss only SVC.
"""


# =============================================================================
# 2. WHY SVM?
# =============================================================================

"""
Suppose we have two classes:

Class A = Red Points
Class B = Yellow Points

            + + + + +
            + + + + +

--------------------------------

            x x x x x
            x x x x x

Can we separate them?

YES.

Many lines can separate them.

Question:
---------
Which line should we choose?

SVM Answer:
-----------
Choose the line that maximizes the margin.

This is the main nerve of SVM.
"""


# =============================================================================
# 3. LOGISTIC REGRESSION VS SVM
# =============================================================================

"""
LOGISTIC REGRESSION

Goal:
-----
Find a decision boundary.

Example:

    + + + +
    + + + +

--------------
Boundary

    x x x x
    x x x x


SVM

Goal:
-----
Find a decision boundary
+
Find maximum margin


    + + + +
    + + + +

=============
Upper Margin

--------------
Boundary

=============
Lower Margin

    x x x x
    x x x x


SVM cares about:
----------------
1. Classification
2. Confidence of classification
3. Margin maximization

This makes SVM more robust.
"""


# =============================================================================
# 4. HYPERPLANE
# =============================================================================

"""
A hyperplane is a decision boundary.

Dimensions         Hyperplane

2D                 Line

3D                 Plane

nD                 Hyperplane


2D Example

      y
      |
      |
  +   |    +
      |
---------------> x
      |
  x   |    x

The line separating them is called hyperplane.
"""


# =============================================================================
# 5. SUPPORT VECTORS
# =============================================================================

"""
Definition:
-----------
Nearest points to the hyperplane.

Example:

      +     +
   +     +

=================
Upper Margin

-----------------
Hyperplane

=================
Lower Margin

   x     x
      x


These two nearest points are support vectors.

IMPORTANT:
----------
Support vectors control the hyperplane.

Move support vectors
→ Hyperplane changes

Move other points
→ Hyperplane may not change

Hence:

Support Vectors = Backbone of SVM
"""


# =============================================================================
# 6. MARGIN
# =============================================================================

"""
Margin:
-------
Distance between support vectors and hyperplane.

SVM creates:

1. Decision Boundary
2. Upper Margin Plane
3. Lower Margin Plane


         + + +

=================

-----------------

=================

         x x x


Goal:
-----
Maximum Margin
"""


# =============================================================================
# 7. MAXIMUM MARGIN CLASSIFIER
# =============================================================================

"""
Consider two possible separators.

Case 1:

 + + + +
 + + + +

========
Boundary
========

 x x x x
 x x x x

Margin = Large


Case 2:

 + + + +
 + + + +

====
Boundary
====

 x x x x
 x x x x

Margin = Small


SVM chooses Case 1.

Reason:
-------
Better Generalization
"""


# =============================================================================
# 8. HARD MARGIN
# =============================================================================

"""
Definition:
-----------
Perfectly separable data.

No errors allowed.

Example:


 + + + + +

================

---------------

================

 x x x x x


Characteristics:
----------------

✓ No misclassification

✓ Maximum margin

✓ Clean dataset

✓ Zero training error


Problems:
---------
Sensitive to outliers

Rarely used in real life
"""


# =============================================================================
# 9. SOFT MARGIN
# =============================================================================

"""
Real-world data:

 + + + +
 + x + +

================

---------------

================

 x x + x
 x x x x


Overlap exists.

Perfect separation impossible.

Hence:

Allow some mistakes.

This is called Soft Margin SVM.


Characteristics:
----------------

✓ Allows errors

✓ Better generalization

✓ Real-world friendly

✓ Most commonly used
"""


# =============================================================================
# 10. MATHEMATICAL INTUITION
# =============================================================================

"""
Equation of Line:

ax + by + c = 0

Vector Form:

w1x1 + w2x2 + b = 0

Matrix Form:

wᵀx + b = 0


This is the SVM hyperplane.
"""


# =============================================================================
# 11. HYPERPLANE EQUATION
# =============================================================================

"""
Main Hyperplane:

wᵀx + b = 0


Upper Margin Plane:

wᵀx + b = +1


Lower Margin Plane:

wᵀx + b = -1


Three important equations:

(1) wᵀx + b = +1

(2) wᵀx + b = 0

(3) wᵀx + b = -1
"""


# =============================================================================
# 12. UNDERSTANDING w VECTOR
# =============================================================================

"""
w is perpendicular to hyperplane.


          w
          ↑
          |
----------|-----------
 Hyperplane


Properties:

1. Normal Vector

2. 90° to hyperplane

3. Determines orientation
"""


# =============================================================================
# 13. POSITIVE SIDE & NEGATIVE SIDE
# =============================================================================

"""
For any point x:

If:

wᵀx+b > 0

Positive Side


If:

wᵀx+b < 0

Negative Side


Classification:

Positive Class = +1

Negative Class = -1
"""


# =============================================================================
# 14. MARGIN DERIVATION
# =============================================================================

"""
Upper Margin:

wᵀx₁+b = +1


Lower Margin:

wᵀx₂+b = -1


Subtract:

wᵀx₁+b - (wᵀx₂+b)

wᵀ(x₁-x₂) = 2


Divide by ||w||

Margin Width:

                2
Margin = --------------
             ||w||


VERY IMPORTANT FORMULA
"""


# =============================================================================
# 15. OPTIMIZATION OBJECTIVE
# =============================================================================

"""
Goal:

Maximize Margin

Margin:

      2
---------------
 ||w||


Therefore:

Maximize

      2
---------------
 ||w||


Equivalent Form:

Minimize ||w||


Standard Form:

          1
Minimize --- ||w||²
          2


This is the objective function.
"""


# =============================================================================
# 16. CLASS LABELS
# =============================================================================

"""
Unlike Logistic Regression

0
1

SVM Uses:

+1
-1


Reason:

Makes mathematics easier.
"""


# =============================================================================
# 17. CONSTRAINTS
# =============================================================================

"""
For positive class:

wᵀx+b ≥ +1


For negative class:

wᵀx+b ≤ -1


Combined:

yi(wᵀxi+b) ≥ 1


This is the most important SVM constraint.
"""


# =============================================================================
# 18. HINGE LOSS
# =============================================================================

"""
Logistic Regression:

Log Loss


SVM:

Hinge Loss


Formula:

Loss = max(0, 1 - yi*f(x))


where:

f(x)=wᵀx+b


Cases:

Correctly Classified:

yi*f(x) ≥ 1

Loss = 0


Misclassified:

yi*f(x) < 1

Loss > 0
"""


# =============================================================================
# 19. SLACK VARIABLES
# =============================================================================

"""
Symbol:

ξi


Purpose:
--------
Allow margin violations.

Hard Margin:

No ξi


Soft Margin:

ξi > 0


Interpretation:

ξi = 0

Correct Classification


0 < ξi < 1

Inside Margin


ξi > 1

Misclassified
"""


# =============================================================================
# 20. HYPERPARAMETER C
# =============================================================================

"""
C controls penalty.

Large C:

Model hates mistakes.

Result:

✓ Fewer errors
✓ Small margin
✓ Overfitting risk


Small C:

Model tolerates mistakes.

Result:

✓ Larger margin
✓ Better generalization
✓ Underfitting possible
"""


# =============================================================================
# 21. COST FUNCTION (SOFT MARGIN SVM)
# =============================================================================

"""
Optimization:

             1
Minimize    --- ||w||²
             2


Regularization
      +
Penalty


Final Objective:


          1
Minimize --- ||w||²
          2

          n
+ C Σ ξi
     i=1


where

C = Hyperparameter

ξi = Slack Variable
"""


# =============================================================================
# 22. GEOMETRIC INTERPRETATION OF C
# =============================================================================

"""
Large C:

Try to classify all points correctly.


Small C:

Allow few mistakes
for larger margin.


Interview Question:

What happens if C becomes huge?

Answer:

Margin shrinks
Model overfits
"""


# =============================================================================
# 23. PREDICTION PROCESS
# =============================================================================

"""
Training Complete.

Hyperplane Found.

Prediction:

Compute:

f(x)=wᵀx+b


If:

f(x) > 0

Class = +1


Else:

Class = -1
"""


# =============================================================================
# 24. ADVANTAGES
# =============================================================================

"""
✓ Works well on high-dimensional data

✓ Effective when features > samples

✓ Robust to overfitting

✓ Uses support vectors only

✓ Powerful with kernels

✓ Good generalization
"""


# =============================================================================
# 25. DISADVANTAGES
# =============================================================================

"""
✗ Slow on huge datasets

✗ Difficult tuning

✗ Sensitive to kernel choice

✗ Not easily interpretable

✗ Training complexity increases
"""
# =============================================================================
# 26. SCIKIT-LEARN IMPLEMENTATION
# =============================================================================

from sklearn.svm import SVC

model = SVC(
    kernel='rbf',
    C=1.0
)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)


"""
Common Kernels:

kernel='linear'

kernel='poly'

kernel='rbf'

kernel='sigmoid'
"""


# =============================================================================
# 27. INTERVIEW QUESTIONS
# =============================================================================

"""
Q1. Why is SVM called Support Vector Machine?

Ans:
Because support vectors determine
the hyperplane.


Q2. What is a support vector?

Ans:
Nearest point to hyperplane.


Q3. What is margin?

Ans:
Distance between support vectors
and hyperplane.


Q4. Why maximize margin?

Ans:
Better generalization.


Q5. Hard Margin vs Soft Margin?

Ans:

Hard:
No errors allowed

Soft:
Errors allowed


Q6. What is C?

Ans:
Penalty parameter.


Q7. What happens if C increases?

Ans:
Overfitting risk increases.


Q8. Why use -1 and +1 labels?

Ans:
Simplifies optimization.
"""


# =============================================================================
# 28. EXAM QUESTIONS
# =============================================================================

"""
1. Define Support Vector Machine.

2. What are Support Vectors?

3. Derive Margin Formula.

4. Explain Hard Margin.

5. Explain Soft Margin.

6. Explain Hyperparameter C.

7. Explain Hinge Loss.

8. Derive SVM Cost Function.

9. Explain Constraint:

   yi(wᵀxi+b) ≥ 1

10. Logistic Regression vs SVM.
"""


# =============================================================================
# 29. FORMULA SHEET
# =============================================================================

"""
Hyperplane:

wᵀx+b=0


Upper Margin:

wᵀx+b=+1


Lower Margin:

wᵀx+b=-1


Margin Width:

      2
-------------
 ||w||


Constraint:

yi(wᵀxi+b) ≥ 1


Hard Margin:

          1
Minimize --- ||w||²
          2


Soft Margin:

          1
Minimize --- ||w||²
          2

          n
+ C Σ ξi
     i=1


Hinge Loss:

max(0,1-yi*f(x))
"""


# =============================================================================
# 30. ONE-MINUTE REVISION
# =============================================================================

"""
Support Vector = Closest Point

Hyperplane = Decision Boundary

Margin = Distance Around Boundary

Goal = Maximum Margin

Hard Margin = No Errors

Soft Margin = Errors Allowed

C = Penalty Parameter

Large C = Small Margin

Small C = Large Margin

Constraint:

yi(wᵀxi+b) ≥ 1

Margin:

2/||w||

Loss:

Hinge Loss

Kernel Needed?

→ When Data is Not Linearly Separable
"""

# =============================================================================
# END OF SVC NOTES
# =============================================================================