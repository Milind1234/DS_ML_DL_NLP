# ======================================================
# NOTES: SAMPLE VARIANCE AND WHY WE USE (n - 1)
# ======================================================

# ------------------------------------------------------
# 1. POPULATION VARIANCE
# ------------------------------------------------------
# When we have the ENTIRE population data, we calculate
# population variance using the following formula:
#
#   σ² = (1 / N) * Σ (xᵢ - μ)²
#
# where:
#   N  = total number of population data points
#   μ  = population mean
#
# Since μ is known and fixed, dividing by N is correct.


# ------------------------------------------------------
# 2. SAMPLE VARIANCE
# ------------------------------------------------------
# In real life, we usually do NOT have population data.
# So we take a SAMPLE from the population.
#
# Sample variance formula:
#
#   s² = (1 / (n - 1)) * Σ (xᵢ - x̄)²
#
# where:
#   n  = number of sample data points
#   x̄ = sample mean


# ------------------------------------------------------
# 3. WHY DO WE USE SAMPLE DATA?
# ------------------------------------------------------
# Sample data is used to:
# - Estimate population mean
# - Estimate population variance
#
# These estimates should be as close as possible to
# the true population values.


# ------------------------------------------------------
# 4. WHAT IF WE DIVIDE BY n INSTEAD OF (n - 1)?
# ------------------------------------------------------
# If we calculate sample variance as:
#
#   (1 / n) * Σ (xᵢ - x̄)²
#
# then the result is usually SMALLER than the true
# population variance.
#
# This means:
# → We UNDER-ESTIMATE the population variance


# ------------------------------------------------------
# 5. WHY DOES UNDER-ESTIMATION HAPPEN?
# ------------------------------------------------------
# Reason:
# The sample mean (x̄) is calculated from the SAME sample.
#
# Because of this:
# - Data points are closer to x̄ than to μ
# - Distances (xᵢ - x̄) become smaller
# - Squared distances become smaller
#
# As a result:
# Sample variance becomes biased (too small)


# ------------------------------------------------------
# 6. BASSEL'S CORRECTION
# ------------------------------------------------------
# To correct this under-estimation, we divide by (n - 1)
# instead of n.
#
# This correction is called:
# → BASSEL'S CORRECTION
#
# Since (n - 1) < n:
# Dividing by (n - 1) increases the variance value
# and compensates for the lost variability.


# ------------------------------------------------------
# 7. UNBIASED ESTIMATOR
# ------------------------------------------------------
# Using (n - 1) makes sample variance an:
# → UNBIASED estimator of population variance
#
# This means:
# On average, sample variance ≈ population variance


# ------------------------------------------------------
# 8. DEGREE OF FREEDOM (DOF)
# ------------------------------------------------------
# Degree of Freedom = number of independent values
#
# When calculating variance:
# - Sample mean x̄ is already fixed
# - One data point becomes dependent
#
# Therefore:
# Degree of Freedom = n - 1


# ------------------------------------------------------
# 9. INTERVIEW-FRIENDLY SUMMARY
# ------------------------------------------------------
# - Sample variance uses (n - 1) to avoid under-estimation
# - Dividing by n gives a biased (smaller) variance
# - (n - 1) corrects this bias
# - This correction is called Bessel's correction
# - (n - 1) represents degree of freedom


# ======================================================
# END OF NOTES
# ======================================================

"""
In statistics, Bessel's correction is the use of 
n − 1 instead of n in the formula for the sample variance 
and sample standard deviation,[1] where n is the number of
observations in a sample. This method corrects the bias in 
the estimation of the population variance. It also partially 
corrects the bias in the estimation of the population 
standard deviation.
"""