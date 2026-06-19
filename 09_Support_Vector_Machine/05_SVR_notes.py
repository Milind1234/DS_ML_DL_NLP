# =============================================================================
#                    SUPPORT VECTOR REGRESSOR (SVR)
# =============================================================================
#
# Author : ChatGPT
# Topic  : Support Vector Machine - Regression
#
# Prerequisite:
# 1. Linear Regression
# 2. Support Vector Classifier (SVC)
# 3. Hyperplanes
# 4. Cost Functions
# 5. Optimization
#
# =============================================================================
# TABLE OF CONTENTS
# =============================================================================
#
# 1. Introduction
# 2. Why SVR?
# 3. Linear Regression vs SVR
# 4. Best Fit Line
# 5. Epsilon Margin
# 6. Epsilon Tube
# 7. Support Vectors in SVR
# 8. Cost Function
# 9. Slack Variables
# 10. Hyperparameter C
# 11. Epsilon-Insensitive Loss
# 12. Optimization Objective
# 13. Prediction Process
# 14. Advantages
# 15. Disadvantages
# 16. Scikit-Learn Implementation
# 17. Interview Questions
# 18. Exam Questions
# 19. Formula Sheet
# 20. One-Minute Revision
#
# =============================================================================



# =============================================================================
# 1. INTRODUCTION
# =============================================================================

"""
Support Vector Regression (SVR) is the regression version
of Support Vector Machine (SVM).

SVC:
----
Classification

SVR:
----
Regression

SVR is used when the output variable is continuous.

Examples:

House Price Prediction

Stock Price Prediction

Temperature Forecasting

Sales Prediction
"""


# =============================================================================
# 2. WHY SVR?
# =============================================================================

"""
Suppose we want to predict house prices.

Price
  ↑

50|
45|      *
40|
35|   *
30|
25| *
20|
   +----------------→ Size

A regression line can be fitted.

Question:
---------

Should every point be fitted perfectly?

SVR Answer:
-----------

NO

Allow small errors.

Penalize only large errors.

This is the main idea behind SVR.
"""


# =============================================================================
# 3. LINEAR REGRESSION VS SVR
# =============================================================================

"""
LINEAR REGRESSION

Goal:
-----
Minimize total error.

Every point contributes to loss.

Uses:

MSE

------------------------------------------------

SVR

Goal:
-----
Ignore small errors.

Penalize only large errors.

Uses:

Epsilon-Insensitive Loss

------------------------------------------------

Linear Regression:

Every error matters.

SVR:

Errors inside epsilon tube are ignored.
"""


# =============================================================================
# 4. BEST FIT LINE
# =============================================================================

"""
SVR creates a best fit line.

Equation:

f(x) = wᵀx + b

where

w = Weight Vector

b = Bias

This is the prediction function.

Goal:

Find optimal values of w and b.
"""


# =============================================================================
# 5. EPSILON MARGIN
# =============================================================================

"""
SVR introduces a new concept:

ε (Epsilon)

Definition:
-----------

Allowed prediction error.

Example:

Actual Price = 50

Predicted Price = 52

Error = 2

If ε = 5

Then:

Error < ε

No penalty.

This makes SVR robust.
"""


# =============================================================================
# 6. EPSILON TUBE
# =============================================================================

"""
SVR creates a tube around the best fit line.

Upper Tube:

f(x) + ε

Best Fit Line:

f(x)

Lower Tube:

f(x) - ε


Graph:

====================
Upper Tube
====================

--------------------
Best Fit Line
--------------------

====================
Lower Tube
====================


Goal:

Keep maximum points inside the tube.
"""


# =============================================================================
# 7. SUPPORT VECTORS IN SVR
# =============================================================================

"""
In SVC:

Support Vectors =
Nearest points to hyperplane.

------------------------------------------------

In SVR:

Support Vectors =
Points on boundary of epsilon tube
or outside epsilon tube.

These points determine the final regression line.

Hence:

Support Vectors = Backbone of SVR
"""


# =============================================================================
# 8. COST FUNCTION
# =============================================================================

"""
Like SVC,

SVR also tries to maximize margin.

Basic Objective:

          1
Minimize --- ||w||²
          2

This keeps the regression function flat.
"""


# =============================================================================
# 9. SLACK VARIABLES
# =============================================================================

"""
Symbol:

ξi

Purpose:
--------

Allow points outside epsilon tube.

Case 1:

Inside Tube

ξi = 0

------------------------------------------------

Case 2:

Outside Tube

ξi > 0

------------------------------------------------

Slack variables measure:

Distance beyond epsilon boundary.
"""


# =============================================================================
# 10. HYPERPARAMETER C
# =============================================================================

"""
C controls penalty.

Large C:

Model dislikes errors.

Result:

✓ Lower training error
✓ Risk of overfitting

------------------------------------------------

Small C:

Model tolerates errors.

Result:

✓ Better generalization
✓ Risk of underfitting
"""
# =============================================================================
# 11. EPSILON-INSENSITIVE LOSS
# =============================================================================

"""
SVR uses a special loss function called:

Epsilon-Insensitive Loss

------------------------------------------------

Definition:
-----------

Errors inside epsilon tube are ignored.

Errors outside epsilon tube are penalized.

------------------------------------------------

Formula:

Loss = max(0, |y - f(x)| - ε)

where:

y     = Actual Value

f(x)  = Predicted Value

ε     = Epsilon Margin

------------------------------------------------

Case 1:

|y - f(x)| ≤ ε

Loss = 0

No penalty.

------------------------------------------------

Case 2:

|y - f(x)| > ε

Loss > 0

Penalty applied.

------------------------------------------------

Example:

Actual Value:

50

Predicted Value:

53

ε = 5

Error = 3

Loss = 0

------------------------------------------------

Example:

Actual Value:

50

Predicted Value:

60

ε = 5

Error = 10

Loss = 10 - 5

Loss = 5
"""


# =============================================================================
# 12. OPTIMIZATION OBJECTIVE
# =============================================================================

"""
SVR tries to:

1. Keep Regression Line Flat

2. Keep Points Inside Epsilon Tube

3. Minimize Errors Outside Tube

------------------------------------------------

Final Optimization Objective:


          1
Minimize --- ||w||²
          2

          n
+ C Σ ξi
     i=1


where

C = Hyperparameter

ξi = Slack Variable

------------------------------------------------

Interpretation

First Term:

          1
          - ||w||²
          2

Controls Flatness.

------------------------------------------------

Second Term:

      n
C Σ ξi
    i=1

Penalizes errors.

------------------------------------------------

Goal:

Flat Function

+

Small Error
"""


# =============================================================================
# 13. PREDICTION PROCESS
# =============================================================================

"""
Training Complete.

Best Fit Line Found.

------------------------------------------------

Prediction Formula:

f(x) = wᵀx + b

------------------------------------------------

Example:

Suppose

w = 3

b = 10

Input:

x = 5

Prediction:

f(x)

= 3(5)+10

= 25

------------------------------------------------

Output:

25

This becomes the final predicted value.
"""


# =============================================================================
# 14. ADVANTAGES
# =============================================================================

"""
✓ Works well for nonlinear regression

✓ Handles high-dimensional data

✓ Robust due to epsilon margin

✓ Good generalization

✓ Kernel support available

✓ Effective on small datasets

✓ Can model complex relationships
"""


# =============================================================================
# 15. DISADVANTAGES
# =============================================================================

"""
✗ Slow on large datasets

✗ Sensitive to hyperparameters

✗ Kernel selection can be difficult

✗ Training cost is high

✗ Harder to interpret than Linear Regression

✗ Not ideal for millions of samples
"""


# =============================================================================
# 16. SCIKIT-LEARN IMPLEMENTATION
# =============================================================================

from sklearn.svm import SVR

model = SVR(
    kernel='rbf',
    C=1.0,
    epsilon=0.1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


"""
Important Parameters:

kernel

C

epsilon

gamma

------------------------------------------------

Common Kernels:

kernel='linear'

kernel='poly'

kernel='rbf'

kernel='sigmoid'
"""


# =============================================================================
# 17. INTERVIEW QUESTIONS
# =============================================================================

"""
Q1. What is SVR?

Ans:
Regression version of SVM.

------------------------------------------------

Q2. Difference between SVC and SVR?

Ans:

SVC:
Classification

SVR:
Regression

------------------------------------------------

Q3. What is Epsilon in SVR?

Ans:

Allowed prediction error.

------------------------------------------------

Q4. What is Epsilon Tube?

Ans:

Region around regression line where
errors are ignored.

------------------------------------------------

Q5. What is Epsilon-Insensitive Loss?

Ans:

Loss function that ignores errors
inside epsilon tube.

------------------------------------------------

Q6. What are Support Vectors in SVR?

Ans:

Points lying on or outside
epsilon tube.

------------------------------------------------

Q7. What is Hyperparameter C?

Ans:

Penalty parameter controlling
tradeoff between flatness and error.

------------------------------------------------

Q8. What happens if C increases?

Ans:

Model becomes stricter and
overfitting risk increases.

------------------------------------------------

Q9. What happens if Epsilon increases?

Ans:

More errors ignored.

Model becomes simpler.

------------------------------------------------

Q10. Why is SVR robust?

Ans:

Because small errors are ignored.
"""


# =============================================================================
# 18. EXAM QUESTIONS
# =============================================================================

"""
1. Define Support Vector Regression.

2. Explain Epsilon Margin.

3. Explain Epsilon Tube.

4. What is Epsilon-Insensitive Loss?

5. Explain Support Vectors in SVR.

6. Explain Hyperparameter C.

7. Derive SVR Cost Function.

8. Linear Regression vs SVR.

9. Explain Slack Variables.

10. Explain Prediction Function:

    f(x)=wᵀx+b
"""


# =============================================================================
# 19. FORMULA SHEET
# =============================================================================

"""
Prediction Function:

f(x)=wᵀx+b

------------------------------------------------

Upper Tube:

f(x)+ε

------------------------------------------------

Lower Tube:

f(x)-ε

------------------------------------------------

Constraint:

|y-f(x)| ≤ ε

------------------------------------------------

Epsilon-Insensitive Loss:

max(0, |y-f(x)| - ε)

------------------------------------------------

Optimization Objective:

          1
Minimize --- ||w||²
          2

          n
+ C Σ ξi
     i=1

------------------------------------------------

Prediction:

f(x)=wᵀx+b
"""


# =============================================================================
# 20. ONE-MINUTE REVISION
# =============================================================================

"""
SVR = Regression Version of SVM

Best Fit Line:

f(x)=wᵀx+b

Epsilon = Allowed Error

Epsilon Tube = Error Tolerance Region

Inside Tube = No Loss

Outside Tube = Loss

Support Vectors =
Points on/outside Tube

Loss Function =
Epsilon-Insensitive Loss

Hyperparameter =
C

Large C =
Strict Model

Small C =
Flexible Model

Prediction =
wᵀx+b

Kernel Needed?

→ For Nonlinear Regression
"""

# =============================================================================
# END OF SVR NOTES
# =============================================================================
