# Ridge Regression, Lasso Regression & ElasticNet Regression Notes

# ------------------------------------------------------------------------
# REGULARIZATION IN MACHINE LEARNING
# ------------------------------------------------------------------------

# Problem in Linear Regression:
# --------------------------------
# Linear Regression may sometimes OVERFIT the training data.

# Overfitting means:
# - Model performs extremely well on training data
# - But performs poorly on unseen/test data

# Example:
# Training Accuracy = 99% or 100%
# Testing Accuracy  = Low

# This indicates:
# - LOW BIAS
# - HIGH VARIANCE

# To reduce overfitting, we use:
# 1. Ridge Regression
# 2. Lasso Regression
# 3. ElasticNet Regression

# These are called REGULARIZATION techniques.


# ------------------------------------------------------------------------
# LINEAR REGRESSION COST FUNCTION
# ------------------------------------------------------------------------

# Hypothesis Equation:
# y = θ0 + θ1x

# Cost Function:

#              m
# J(θ) = 1/2m  Σ  (hθ(xᶦ) - yᶦ)²
#             i=1

# This is called:
# Mean Squared Error (MSE)

# Where:
# - hθ(xᶦ) = Predicted value
# - yᶦ     = Actual value

# Goal:
# Minimize Cost Function

# Gradient Descent helps us reach:
# GLOBAL MINIMA


# ------------------------------------------------------------------------
# PROBLEM OF OVERFITTING
# ------------------------------------------------------------------------

# Suppose we have only 2 training points.

# Linear Regression may create a line
# that perfectly passes through all points.

# In this case:
# Error = 0

# Sounds good?
# NO.

# Because model memorized training data.

# When new test data comes:
# Prediction error increases.

# This is called:
# OVERFITTING

# Important:
# If training accuracy is 100%,
# suspect overfitting.


# =========================================================================
# 1. RIDGE REGRESSION
# =========================================================================

# Ridge Regression is also called:
# L2 Regularization

# Main Purpose:
# Reduce Overfitting

# ------------------------------------------------------------------------
# RIDGE REGRESSION COST FUNCTION
# ------------------------------------------------------------------------

# Original Cost Function:

#             m
# J(θ) = 1/2m Σ (hθ(xᶦ) - yᶦ)²
#            i=1

# Ridge adds penalty term:

#            m                     m
# J(θ) = 1/2m Σ (hθ(xᶦ) - yᶦ)² + λ Σ (slope²)
#           i=1                   i=1             

# OR

# J(θ) = MSE + λ(θ1² + θ2² + θ3² + ...)

# ------------------------------------------------------------------------
# WHAT IS λ (LAMBDA)?
# ------------------------------------------------------------------------

# Lambda is called:
# HYPERPARAMETER

# It controls:
# - strength of regularization
# - amount of penalty added

# ------------------------------------------------------------------------
# RELATIONSHIP BETWEEN LAMBDA & SLOPE
# ------------------------------------------------------------------------

# When:
# λ increases

# Then:
# slope/coefficient decreases

# Important:
# Coefficients become SMALLER
# BUT NEVER become ZERO.

# This reduces:
# - model complexity
# - overfitting

# ------------------------------------------------------------------------
# WHY DOES RIDGE REDUCE OVERFITTING?
# ------------------------------------------------------------------------

# In Linear Regression:
# Best fit line may perfectly pass through all points.

# Ridge adds penalty:
# λ(slope²)

# Because of this:
# model avoids extremely steep slopes.

# Therefore:
# - model becomes smoother
# - less sensitive to noise
# - overfitting reduces

# ------------------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------------------

# Before Ridge:

# hθ(x) = 0.34 + 0.52x1 + 0.48x2 + 0.24x3

# After Ridge:

# hθ(x) = 0.34 + 0.40x1 + 0.38x2 + 0.14x3

# Observation:
# All coefficients reduced.

# But:
# none became zero.

# Important:
# Ridge keeps all features.


# ------------------------------------------------------------------------
# INTERVIEW QUESTION
# ------------------------------------------------------------------------

# Q) What is the relation between lambda and slope in Ridge?

# Answer:
# When lambda increases,
# slope/coefficient decreases,
# but never becomes zero.


# =========================================================================
# 2. LASSO REGRESSION
# =========================================================================

# Lasso Regression is also called:
# L1 Regularization

# Main Purpose:
# FEATURE SELECTION

# ------------------------------------------------------------------------
# LASSO COST FUNCTION
# ------------------------------------------------------------------------

#            m
# J(θ) = 1/2m Σ (hθ(xᶦ) - yᶦ)² + λ Σ |slope|
#           i=1

# OR

# J(θ) = MSE + λ(|θ1| + |θ2| + |θ3| + ...)

# Difference from Ridge:
# Ridge -> square of slope
# Lasso -> magnitude/absolute value of slope


# ------------------------------------------------------------------------
# RELATIONSHIP BETWEEN LAMBDA & SLOPE
# ------------------------------------------------------------------------

# When lambda increases:
# coefficients decrease

# BUT here:
# coefficients CAN become ZERO.

# ------------------------------------------------------------------------
# WHY IS THIS IMPORTANT?
# ------------------------------------------------------------------------

# If coefficient becomes zero:

# 0 × feature = 0

# That feature gets removed.

# Therefore:
# Lasso performs automatic FEATURE SELECTION.

# ------------------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------------------

# Before Lasso:

# hθ(x) = 0.52 + 0.65x1 + 0.72x2 + 0.34x3 + 0.12x4

# After Lasso:

# hθ(x) = 0.42 + 0.51x1 + 0.60x2 + 0.14x3 + 0x4

# Observation:
# x4 removed because coefficient became zero.

# Therefore:
# x4 was not important.

# ------------------------------------------------------------------------
# WHY USE LASSO?
# ------------------------------------------------------------------------

# Suppose dataset has:
# - hundreds of features

# Many features may be useless.

# Lasso automatically removes:
# - weakly correlated features

# Therefore:
# - simpler model
# - reduced complexity
# - improved interpretability


# ------------------------------------------------------------------------
# INTERVIEW QUESTION
# ------------------------------------------------------------------------

# Q) Why do we use Lasso Regression?

# Answer:
# Lasso Regression is used for:
# - Feature Selection
# - Removing unimportant features


# =========================================================================
# 3. ELASTICNET REGRESSION
# =========================================================================

# ElasticNet is combination of:
# - Ridge Regression
# - Lasso Regression

# Main Purposes:
# 1. Reduce Overfitting
# 2. Feature Selection

# ------------------------------------------------------------------------
# ELASTICNET COST FUNCTION
# ------------------------------------------------------------------------

#            m
# J(θ) = 1/2m Σ (hθ(xᶦ) - yᶦ)²
#           i=1

#        + λ1 Σ (slope²)
#        + λ2 Σ |slope|

# OR

# ElasticNet = Ridge + Lasso

# ------------------------------------------------------------------------
# WHAT DOES EACH PART DO?
# ------------------------------------------------------------------------

# λ1(slope²)
# -> Ridge Part
# -> Reduces overfitting

# λ2|slope|
# -> Lasso Part
# -> Performs feature selection


# ------------------------------------------------------------------------
# WHY USE ELASTICNET?
# ------------------------------------------------------------------------

# Use ElasticNet when:
# - model is overfitting
# - dataset contains many features

# ElasticNet solves both:
# - overfitting
# - irrelevant features


# =========================================================================
# IMPORTANT COMPARISON
# =========================================================================

# ------------------------------------------------------------------------
# Linear Regression
# ------------------------------------------------------------------------
# Purpose:
# Predict output using best-fit line

# Problem:
# May overfit


# ------------------------------------------------------------------------
# Ridge Regression (L2)
# ------------------------------------------------------------------------
# Purpose:
# Reduce Overfitting

# Penalty:
# Square of coefficients

# Coefficients:
# Become smaller
# Never become zero

# Feature Selection:
# NO


# ------------------------------------------------------------------------
# Lasso Regression (L1)
# ------------------------------------------------------------------------
# Purpose:
# Feature Selection

# Penalty:
# Absolute value of coefficients

# Coefficients:
# Can become zero

# Feature Selection:
# YES


# ------------------------------------------------------------------------
# ElasticNet
# ------------------------------------------------------------------------
# Purpose:
# Both Overfitting Reduction + Feature Selection

# Combination:
# Ridge + Lasso


# =========================================================================
# KEY INTERVIEW QUESTIONS
# =========================================================================

# Q1) Why do we use Ridge Regression?
# Ans:
# To reduce overfitting.

# Q2) Why do we use Lasso Regression?
# Ans:
# For feature selection.

# Q3) Why does Ridge reduce overfitting?
# Ans:
# Because it penalizes large coefficients.

# Q4) Why does Lasso perform feature selection?
# Ans:
# Because coefficients can become zero.

# Q5) What is Lambda?
# Ans:
# Hyperparameter controlling regularization strength.

# Q6) Relation between lambda and slope?
# Ans:
# As lambda increases:
# coefficients decrease.

# Ridge:
# coefficients never become zero.

# Lasso:
# coefficients may become zero.


# =========================================================================
# FINAL CONCLUSION
# =========================================================================

# Regularization techniques help improve Linear Regression.

# Ridge:
# - reduces overfitting

# Lasso:
# - removes unimportant features

# ElasticNet:
# - combines both advantages

# These methods are mainly used for:
# Hyperparameter tuning of Linear Regression.