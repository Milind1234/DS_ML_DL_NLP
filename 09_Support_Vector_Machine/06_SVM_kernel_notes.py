# =============================================================================
#                    SVM KERNELS NOTES
# =============================================================================
#
# Author : ChatGPT
# Topic  : Support Vector Machine Kernels
#
# Prerequisite:
# 1. Support Vector Classifier (SVC)
# 2. Support Vector Regression (SVR)
# 3. Hyperplanes
# 4. Margins
# 5. Linear Algebra Basics
#
# =============================================================================
# TABLE OF CONTENTS
# =============================================================================
#
# 1. Introduction
# 2. Why Kernels?
# 3. Linear SVM Problem
# 4. What is a Kernel?
# 5. Kernel Trick
# 6. Feature Space Transformation
# 7. Types of Kernels
# 8. Linear Kernel
# 9. Polynomial Kernel
# 10. RBF Kernel
# 11. Sigmoid Kernel
# 12. Gamma Hyperparameter
# 13. Degree Hyperparameter
# 14. Choosing the Right Kernel
# 15. Advantages
# 16. Disadvantages
# 17. Scikit-Learn Implementation
# 18. Interview Questions
# 19. Exam Questions
# 20. Formula Sheet
# 21. One-Minute Revision
#
# =============================================================================



# =============================================================================
# 1. INTRODUCTION
# =============================================================================

"""
SVM works extremely well when classes are linearly separable.

Example:

      + + + +

-------------------

      x x x x

A straight line can separate them.

------------------------------------------------

But real-world datasets are rarely like this.

Many datasets contain:

✓ Overlapping Classes

✓ Curved Boundaries

✓ Complex Relationships

In such situations:

Linear SVM fails.

To solve this problem,

we use:

SVM Kernels
"""


# =============================================================================
# 2. WHY KERNELS?
# =============================================================================

"""
Consider this dataset.

      x x x

    x       x

        +

    x       x

      x x x

------------------------------------------------

Can a straight line separate them?

NO.

------------------------------------------------

Linear SVM:

Accuracy ↓

Error ↑

------------------------------------------------

Question:

How can we separate them?

Answer:

Transform the dataset into a higher dimension.

This is the main idea behind kernels.
"""


# =============================================================================
# 3. LINEAR SVM PROBLEM
# =============================================================================

"""
Linear SVM creates:

Decision Boundary

+

Margin Planes

using straight lines.

------------------------------------------------

Works Well:

✓ Linearly Separable Data

------------------------------------------------

Fails:

✗ Non-Linear Data

Example:

    + + +

  +       +

      x

  +       +

    + + +

------------------------------------------------

No straight line can separate this efficiently.

Need:

Kernel Transformation
"""


# =============================================================================
# 4. WHAT IS A KERNEL?
# =============================================================================

"""
Definition:
-----------

A Kernel is a mathematical function that transforms
data from a lower-dimensional space to a higher-dimensional space.

------------------------------------------------

Purpose:

Make data linearly separable.

------------------------------------------------

Input Space:

2D

↓

Kernel Function

↓

Higher Dimensional Space

↓

Linear Separation Possible

------------------------------------------------

Simple Definition:

Kernel = Transformation Function
"""


# =============================================================================
# 5. KERNEL TRICK
# =============================================================================

"""
Kernel Trick is one of the most famous concepts in ML.

------------------------------------------------

Normally:

2D → 3D → 4D → 100D

Transformation is computationally expensive.

------------------------------------------------

Kernel Trick:

Compute similarity directly in higher dimensions
without explicitly transforming the data.

------------------------------------------------

Benefits:

✓ Faster

✓ Memory Efficient

✓ Handles Complex Data

------------------------------------------------

Interview Definition:

Kernel Trick allows SVM to operate in a high-dimensional
feature space without explicitly computing coordinates
in that space.
"""


# =============================================================================
# 6. FEATURE SPACE TRANSFORMATION
# =============================================================================

"""
Original Data:

1D

x-axis

● ● ● ○ ○ ○ ● ● ●

------------------------------------------------

Apply Transformation:

y = x²

------------------------------------------------

Now Data becomes:

2D

      ●
    ●   ●

○ ○       ○ ○

------------------------------------------------

Now a straight line can separate classes.

------------------------------------------------

This transformation is performed using kernels.
"""


# =============================================================================
# 7. TYPES OF KERNELS
# =============================================================================

"""
Most Common Kernels:

1. Linear Kernel

2. Polynomial Kernel

3. RBF Kernel

4. Sigmoid Kernel

------------------------------------------------

Most Used In Industry:

RBF Kernel
"""


# =============================================================================
# 8. LINEAR KERNEL
# =============================================================================

"""
Simplest Kernel.

------------------------------------------------

Formula:

K(x,z) = xᵀz

------------------------------------------------

Dot Product between two vectors.

------------------------------------------------

Used When:

Data is already linearly separable.

------------------------------------------------

Advantages:

✓ Fast

✓ Simple

✓ Less Computation

------------------------------------------------

Disadvantages:

✗ Cannot handle complex boundaries

------------------------------------------------

Scikit-Learn:

kernel='linear'
"""


# =============================================================================
# 9. POLYNOMIAL KERNEL
# =============================================================================

"""
Polynomial Kernel introduces polynomial features.

------------------------------------------------

Formula:

K(x,z) = (xᵀz + c)^d

where:

c = Constant

d = Degree

------------------------------------------------

Example:

Degree = 2

Features:

x²

xy

y²

------------------------------------------------

Can create curved decision boundaries.

------------------------------------------------

Advantages:

✓ Captures interactions

✓ Handles moderate complexity

------------------------------------------------

Disadvantages:

✗ Slow for high degree

✗ Overfitting risk

------------------------------------------------

Scikit-Learn:

kernel='poly'
"""


# =============================================================================
# 10. RBF KERNEL
# =============================================================================

"""
RBF = Radial Basis Function

Most Popular Kernel.

------------------------------------------------

Formula:

K(x,z)

= exp(-γ||x-z||²)

------------------------------------------------

Also called:

Gaussian Kernel

------------------------------------------------

Idea:

Nearby points

→ High Similarity

Far points

→ Low Similarity

------------------------------------------------

Advantages:

✓ Handles highly non-linear data

✓ Excellent accuracy

✓ Industry Standard

✓ Default Choice

------------------------------------------------

Disadvantages:

✗ Hyperparameter tuning needed

------------------------------------------------

Scikit-Learn:

kernel='rbf'
"""


# =============================================================================
# 11. SIGMOID KERNEL
# =============================================================================

"""
Inspired by Neural Networks.

------------------------------------------------

Formula:

K(x,z)

= tanh(γxᵀz + r)

------------------------------------------------

Looks similar to:

Activation Function

used in Neural Networks.

------------------------------------------------

Advantages:

✓ Neural Network-like behavior

------------------------------------------------

Disadvantages:

✗ Rarely used

✗ Often underperforms RBF

------------------------------------------------

Scikit-Learn:

kernel='sigmoid'
"""


# =============================================================================
# 12. GAMMA HYPERPARAMETER
# =============================================================================

"""
Gamma is used in:

RBF Kernel

Polynomial Kernel

Sigmoid Kernel

------------------------------------------------

Controls:

Influence of a single training point.

------------------------------------------------

Large Gamma:

Nearby points only.

Decision boundary becomes complex.

Overfitting Risk ↑

------------------------------------------------

Small Gamma:

Far points also influence.

Decision boundary smoother.

Underfitting Risk ↑

------------------------------------------------

Interview Question:

What happens when gamma increases?

Answer:

Decision boundary becomes more complex.
"""

# =============================================================================
# 13. DEGREE HYPERPARAMETER
# =============================================================================

"""
Used only in:

Polynomial Kernel

------------------------------------------------

Formula:

K(x,z)=(xᵀz+c)^d

------------------------------------------------

d = Degree

------------------------------------------------

Degree = 1

Linear Boundary

------------------------------------------------

Degree = 2

Quadratic Boundary

------------------------------------------------

Degree = 3

Cubic Boundary

------------------------------------------------

Higher Degree:

More Flexible Model

More Overfitting Risk
"""


# =============================================================================
# 14. CHOOSING THE RIGHT KERNEL
# =============================================================================

"""
Linear Kernel

When:

Data is linearly separable.

------------------------------------------------

Polynomial Kernel

When:

Feature interactions exist.

------------------------------------------------

RBF Kernel

When:

Unsure which kernel to use.

Best default choice.

------------------------------------------------

Sigmoid Kernel

Rarely used.

------------------------------------------------

Practical Rule:

Start with RBF.
"""


# =============================================================================
# 15. ADVANTAGES OF KERNELS
# =============================================================================

"""
✓ Handle Nonlinear Data

✓ Improve Accuracy

✓ Powerful Transformations

✓ Work in High Dimensions

✓ Flexible Decision Boundaries

✓ Kernel Trick saves computation
"""


# =============================================================================
# 16. DISADVANTAGES OF KERNELS
# =============================================================================

"""
✗ Hyperparameter tuning required

✗ Computationally expensive

✗ Difficult interpretation

✗ Training becomes slow on huge datasets

✗ Wrong kernel reduces performance
"""


# =============================================================================
# 17. SCIKIT-LEARN IMPLEMENTATION
# =============================================================================

from sklearn.svm import SVC

# Linear Kernel

model1 = SVC(kernel='linear')

# Polynomial Kernel

model2 = SVC(kernel='poly', degree=3)

# RBF Kernel

model3 = SVC(kernel='rbf', gamma='scale')

# Sigmoid Kernel

model4 = SVC(kernel='sigmoid')

model3.fit(X_train, y_train)

y_pred = model3.predict(X_test)


"""
Most Commonly Used:

kernel='rbf'
"""


# =============================================================================
# 18. INTERVIEW QUESTIONS
# =============================================================================

"""
Q1. Why do we need kernels?

Ans:
To handle non-linearly separable data.

------------------------------------------------

Q2. What is Kernel Trick?

Ans:
Computing similarity in higher dimensions
without explicit transformation.

------------------------------------------------

Q3. Most popular kernel?

Ans:
RBF Kernel.

------------------------------------------------

Q4. Formula of Linear Kernel?

Ans:
K(x,z)=xᵀz

------------------------------------------------

Q5. Formula of Polynomial Kernel?

Ans:
K(x,z)=(xᵀz+c)^d

------------------------------------------------

Q6. Formula of RBF Kernel?

Ans:
exp(-γ||x-z||²)

------------------------------------------------

Q7. What does Gamma control?

Ans:
Influence of training points.

------------------------------------------------

Q8. What happens if Gamma increases?

Ans:
Decision boundary becomes complex.

------------------------------------------------

Q9. Best kernel to start with?

Ans:
RBF Kernel.

------------------------------------------------

Q10. Which kernel is rarely used?

Ans:
Sigmoid Kernel.
"""


# =============================================================================
# 19. EXAM QUESTIONS
# =============================================================================

"""
1. What is Kernel Trick?

2. Explain Linear Kernel.

3. Explain Polynomial Kernel.

4. Explain RBF Kernel.

5. Explain Sigmoid Kernel.

6. What is Gamma?

7. Difference between Linear and RBF Kernel.

8. Why do we need kernels?

9. Explain Feature Space Transformation.

10. Advantages of Kernel Trick.
"""


# =============================================================================
# 20. FORMULA SHEET
# =============================================================================

"""
Linear Kernel:

K(x,z)=xᵀz

------------------------------------------------

Polynomial Kernel:

K(x,z)=(xᵀz+c)^d

------------------------------------------------

RBF Kernel:

K(x,z)=exp(-γ||x-z||²)

------------------------------------------------

Sigmoid Kernel:

K(x,z)=tanh(γxᵀz+r)

------------------------------------------------

Gamma:

Controls influence of training points.

------------------------------------------------

Degree:

Controls polynomial complexity.
"""


# =============================================================================
# 21. ONE-MINUTE REVISION
# =============================================================================

"""
Kernel = Transformation Function

Kernel Trick =
High-dimensional computation without explicit transformation

Linear Kernel =
Simple Data

Polynomial Kernel =
Feature Interactions

RBF Kernel =
Most Popular

Sigmoid Kernel =
Neural Network Inspired

Gamma =
Controls Influence Radius

Degree =
Polynomial Complexity

Best Default Kernel =
RBF

Use Kernels When?
→ Data is not linearly separable
"""

# =============================================================================
# END OF SVM KERNELS NOTES
# =============================================================================