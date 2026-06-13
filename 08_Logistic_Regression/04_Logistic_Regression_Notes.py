# =============================================================================
# LOGISTIC REGRESSION - COMPLETE NOTES
# =============================================================================

# =============================================================================
# 1. WHAT IS LOGISTIC REGRESSION?
# =============================================================================

# Logistic Regression is a Supervised Machine Learning algorithm used for
# Classification problems.

# Despite the name "Regression", it is used for Classification.

# Example:
#
# Study Hours      Result
# -----------      ------
#     2             Fail (0)
#     3             Fail (0)
#     4             Fail (0)
#     5             Pass (1)
#     6             Pass (1)
#     7             Pass (1)
#
# Goal:
# Given study hours, predict whether student will Pass or Fail.

# Output classes:
#
# Pass = 1
# Fail = 0
#
# This is Binary Classification because only two classes exist.


# =============================================================================
# 2. WHY NOT USE LINEAR REGRESSION FOR CLASSIFICATION?
# =============================================================================

# Linear Regression prediction:
#
# h(x) = θ0 + θ1x
#
# Problem:
#
# Linear Regression can produce:
#
# h(x) > 1
# h(x) < 0
#
# But probabilities must lie between:
#
# 0 ≤ P ≤ 1
#
# Therefore Linear Regression is not suitable for classification.


# Example:
#
# Prediction = 1.8
#
# Can probability be 180%?
#
# No.

# Another issue:
#
# Linear Regression is highly sensitive to outliers.
#
# A single outlier can shift the best fit line significantly.

# Therefore:
#
# Linear Regression ❌
# Logistic Regression ✅


# =============================================================================
# 3. IDEA BEHIND LOGISTIC REGRESSION
# =============================================================================

# Step 1:
#
# Create linear equation

# z = θ0 + θ1x

# Step 2:
#
# Pass z through Sigmoid Function.

# This converts any real value into range (0,1)

# Logistic Regression output:

# hθ(x) = σ(z)

# where

# z = θ0 + θ1x


# =============================================================================
# 4. SIGMOID FUNCTION
# =============================================================================

# Formula:

#            1
# σ(z) = ----------
#         1 + e^(-z)

# Important Property:
#
# Input Range:
# (-∞ , +∞)

# Output Range:
# (0 , 1)

# Therefore:
#
# Any large positive value approaches 1.
#
# Any large negative value approaches 0.


# Example:

# z = 10

# σ(10)
# ≈ 0.99995

# z = -10

# σ(-10)
# ≈ 0.000045


# =============================================================================
# 5. WHY SIGMOID?
# =============================================================================

# We need probabilities.

# Probability must always lie between:

# 0 and 1

# Sigmoid naturally satisfies this condition.

# Therefore:

# Logistic Regression Prediction

# hθ(x) = P(y=1 | x)


# =============================================================================
# 6. DECISION BOUNDARY
# =============================================================================

# Classification Rule:

# If hθ(x) >= 0.5
# Predict Class 1

# If hθ(x) < 0.5
# Predict Class 0


# Example:

# Probability = 0.75

# Since:
#
# 0.75 > 0.5
#
# Predict = 1


# Example:

# Probability = 0.2

# Since:
#
# 0.2 < 0.5
#
# Predict = 0


# =============================================================================
# 7. HYPOTHESIS FUNCTION
# =============================================================================

# Linear Regression:

# h(x) = θ0 + θ1x

# Logistic Regression:

# h(x) = σ(θ0 + θ1x)

# Expanding Sigmoid:

#                     1
# h(x) = -----------------------------
#        1 + e^-(θ0 + θ1x)

# This is called Logistic Hypothesis.


# =============================================================================
# 8. WHY MSE COST FUNCTION FAILS?
# =============================================================================

# Linear Regression Cost:

#               m
# J(θ) = 1/2m Σ (h(x)-y)^2
#              i=1

# Works because Linear Regression is linear.

# If we use same cost in Logistic Regression:

# h(x) contains Sigmoid.

# Sigmoid introduces non-linearity.

# Result:
#
# Cost function becomes Non-Convex.

# Non-convex function:
#
# Multiple local minima.

# Gradient Descent may get stuck.

# Therefore MSE is avoided.


# =============================================================================
# 9. LOG LOSS / CROSS ENTROPY LOSS
# =============================================================================

# Logistic Regression uses Log Loss.

# For one training example:

# If y = 1

# Cost = -log(h(x))

# If y = 0

# Cost = -log(1-h(x))


# =============================================================================
# 10. WHY THIS COST FUNCTION?
# =============================================================================

# Case 1:
#
# Actual = 1
#
# Predicted = 1
#
# Cost ≈ 0

# Good prediction.

# Case 2:
#
# Actual = 1
#
# Predicted = 0
#
# Cost → ∞

# Huge penalty.

# Thus wrong confident predictions get heavily punished.


# =============================================================================
# 11. COMBINED COST FUNCTION DERIVATION
# =============================================================================

# Two cases:

# y=1
#
# Cost = -log(h)

# y=0
#
# Cost = -log(1-h)

# Combine both into one equation:

# Cost(h,y)
#
# = -y log(h)
#   -(1-y)log(1-h)

# This is Binary Cross Entropy.


# =============================================================================
# 12. FINAL COST FUNCTION
# =============================================================================

#              m
# J(θ) = -1/m  Σ  [ y(i)log(h(i)) + (1-y(i)) log(1-h(i)) ]
#             i=1
# 
#  m = Number of training examples
#  y(i) = Actual label (0 or 1)
#  hθ(x(i)) = Predicted probability that the example belongs to class 1
#  log = Natural logarithm
# 
# Important:
#
# This cost function is Convex.
#
# Therefore:
#
# Global Minimum exists.


# =============================================================================
# 13. GRADIENT DESCENT
# =============================================================================

# Goal:
#
# Minimize Cost Function.

# Update Rule:

# θj = θj - α(∂J/∂θj)

# where:

# α = Learning Rate

# j = 0,1,2,...n

# Repeat until convergence.


# =============================================================================
# 14. LOG ODDS DERIVATION (IMPORTANT INTERVIEW QUESTION)
# =============================================================================

# Logistic Equation:

#           1
# h = ------------
#      1+e^(-z)

# Rearranging:

# 1/h = 1+e^(-z)

# 1/h -1 = e^(-z)

# (1-h)/h = e^(-z)

# Taking log:

# log(h/(1-h)) = z

# Since:

# z = θ0 + θ1x

# Therefore:

# log(h/(1-h))
#
# = θ0 + θ1x

# This is called Log-Odds or Logit.


# =============================================================================
# 15. ADVANTAGES OF LOGISTIC REGRESSION
# =============================================================================

# 1. Simple
# 2. Fast
# 3. Interpretable
# 4. Produces probabilities
# 5. Works well on linearly separable data
# 6. Easy to implement


# =============================================================================
# 16. DISADVANTAGES
# =============================================================================

# 1. Cannot capture complex non-linear boundaries
# 2. Sensitive to multicollinearity
# 3. Underperforms on highly complex datasets
# 4. Assumes linear relation in log-odds space


# =============================================================================
# PERFORMANCE METRICS
# =============================================================================


# =============================================================================
# 17. CONFUSION MATRIX
# =============================================================================

#                Actual
#
#               1      0
#
# Pred 1       TP     FP
#
# Pred 0       FN     TN


# TP = True Positive
#
# Actually Positive
# Predicted Positive

# TN = True Negative
#
# Actually Negative
# Predicted Negative

# FP = False Positive
#
# Actually Negative
# Predicted Positive

# FN = False Negative
#
# Actually Positive
# Predicted Negative


# =============================================================================
# 18. ACCURACY
# =============================================================================

# Formula:

# Accuracy
#
# = (TP + TN)
#   -------------------
#   TP+TN+FP+FN

# Measures overall correctness.


# =============================================================================
# 19. PROBLEM WITH ACCURACY
# =============================================================================

# Example:

# 1000 samples

# 900 class = 1
# 100 class = 0

# Model predicts every sample as class 1.

# Accuracy:

# 900/1000

# = 90%

# Looks good.

# But model never learned minority class.

# Therefore:
#
# Accuracy fails on Imbalanced Dataset.


# =============================================================================
# 20. PRECISION
# =============================================================================

# Formula:

# Precision
#
# = TP
#   -------
#   TP + FP

# Meaning:
#
# Out of all predicted positives,
# how many were actually positive?


# Spam Example:

# Email predicted as Spam.

# Precision asks:

# Among emails predicted Spam,
# how many truly were Spam?


# High Precision:
#
# Low False Positives


# =============================================================================
# 21. RECALL
# =============================================================================

# Formula:

# Recall
#
# = TP
#   -------
#   TP + FN

# Meaning:
#
# Out of all actual positives,
# how many did model detect?


# Disease Detection Example:

# Actual Disease = Positive

# Recall asks:
#
# How many patients were correctly detected?


# High Recall:
#
# Low False Negatives


# =============================================================================
# 22. PRECISION VS RECALL
# =============================================================================

# Precision Focus:
#
# Reduce False Positives

# Recall Focus:
#
# Reduce False Negatives


# Example:

# Spam Detection

# False Positive is dangerous.
#
# Important email marked Spam.

# Therefore:
#
# Precision important.


# Example:

# Cancer Detection

# False Negative dangerous.
#
# Cancer patient missed.

# Therefore:
#
# Recall important.


# =============================================================================
# 23. F-BETA SCORE
# =============================================================================

# General Formula:

# Fβ

# = (1+β²)
#
#   Precision × Recall
#
# -------------------------
#
# β²Precision + Recall


# Purpose:
#
# Balance Precision and Recall.


# =============================================================================
# 24. F1 SCORE
# =============================================================================

# β = 1

# F1

# = 2PR
#   ------
#   P + R

# Harmonic Mean of
# Precision and Recall.


# Used when:
#
# Precision and Recall
# are equally important.


# =============================================================================
# 25. F0.5 SCORE
# =============================================================================

# β = 0.5

# Precision gets more importance.

# Used when:

# FP is costly.


# =============================================================================
# 26. F2 SCORE
# =============================================================================

# β = 2

# Recall gets more importance.

# Used when:

# FN is costly.


# =============================================================================
# MULTICLASS LOGISTIC REGRESSION
# ONE VS REST (OVR)
# =============================================================================


# =============================================================================
# 27. PROBLEM
# =============================================================================

# Logistic Regression naturally supports:

# Binary Classification only.

# Example:

# Class A vs Class B


# But what if:

# Class1
# Class2
# Class3

# Three classes exist?

# Need Multiclass Classification.


# =============================================================================
# 28. ONE VS REST (OVR)
# =============================================================================

# Also called:

# One-vs-All (OVA)

# Idea:

# Train one binary classifier
# for each class.


# Example:

# Classes:

# O1
# O2
# O3

# Train:

# M1:
#
# O1 vs Rest

# M2:
#
# O2 vs Rest

# M3:
#
# O3 vs Rest


# =============================================================================
# 29. TARGET TRANSFORMATION
# =============================================================================

# Original labels:

# O1
# O2
# O3

# For Model M1:

# O1 → 1
# O2 → 0
# O3 → 0

# For Model M2:

# O1 → 0
# O2 → 1
# O3 → 0

# For Model M3:

# O1 → 0
# O2 → 0
# O3 → 1


# =============================================================================
# 30. PREDICTION IN OVR
# =============================================================================

# New Sample

# M1 probability = 0.25

# M2 probability = 0.20

# M3 probability = 0.55

# Highest probability:

# 0.55

# Therefore:

# Predict Class O3


# =============================================================================
# 31. TIME COMPLEXITY OF OVR
# =============================================================================

# If K classes exist:

# Need K Logistic Regression models.

# Total Models:

# K


# =============================================================================
# 32. IMPORTANT INTERVIEW QUESTIONS
# =============================================================================

# Q1. Why Logistic Regression is called Regression?
#
# Because underlying model predicts continuous probability.

# Q2. Why Sigmoid?
#
# Maps output into (0,1).

# Q3. Why not MSE?
#
# Produces non-convex cost function.

# Q4. What is Decision Boundary?
#
# Boundary separating classes.

# Q5. Why Cross Entropy?
#
# Convex optimization and better gradients.

# Q6. Accuracy vs Precision?
#
# Accuracy = Overall correctness
# Precision = Quality of positive predictions

# Q7. Precision vs Recall?
#
# Precision focuses FP.
# Recall focuses FN.

# Q8. Why F1 Score?
#
# Balances Precision and Recall.

# Q9. What is OVR?
#
# Converts multiclass problem into multiple binary problems.

# Q10. How many models for K classes?
#
# K models.


# =============================================================================
# QUICK REVISION SHEET
# =============================================================================

# Sigmoid:
#
# σ(z)=1/(1+e^-z)

# Logistic Hypothesis:
#
# h(x)=σ(θTx)

# Decision Boundary:
#
# h(x)>=0.5 => 1
# h(x)<0.5 => 0

# Accuracy:
#
# (TP+TN)/(TP+TN+FP+FN)

# Precision:
#
# TP/(TP+FP)

# Recall:
#
# TP/(TP+FN)

# F1:
#
# 2PR/(P+R)

# Cross Entropy:
#
# -[ylog(h)+(1-y)log(1-h)]

# OVR:
#
# K classes => K binary classifiers
#
# Predict class with maximum probability.
# =============================================================================