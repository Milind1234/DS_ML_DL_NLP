# =============================================================================
#                    RNN, LSTM AND GRU - INTERVIEW NOTES
# =============================================================================
#
# Author: Milind Chavan
#
# Purpose:
#   Interview-ready notes for understanding:
#
#       1. RNN
#       2. Long-Term Dependency Problem
#       3. Vanishing Gradient Problem
#       4. LSTM
#       5. LSTM Architecture
#       6. Forget Gate
#       7. Input Gate
#       8. Candidate Memory
#       9. Cell State
#      10. Output Gate
#      11. Hidden State
#      12. LSTM Variants
#      13. GRU
#      14. RNN vs LSTM vs GRU
#      15. Interview Questions
#
# IMPORTANT:
#   These are primarily conceptual notes.
#   The uploaded handwritten notes are the primary reference.
#   The explanation is reorganized into an interview-friendly structure.
#
# =============================================================================


# =============================================================================
# 1. WHAT IS AN RNN?
# =============================================================================
#
# RNN = Recurrent Neural Network
#
# An RNN is a type of neural network designed to work with sequential data.
#
# Examples of sequential data:
#
#   - Text
#   - Speech
#   - Time-series data
#   - Sensor data
#   - Stock prices
#   - Weather data
#   - Music
#   - Machine translation
#
#
# The main idea behind RNN:
#
#   "The output from the previous time step is used as information
#    for the current time step."
#
#
# This gives the RNN a form of MEMORY.
#
#
# Example:
#
# Sentence:
#
#       "I love machine learning"
#
# The model reads:
#
#       I
#       ↓
#       love
#       ↓
#       machine
#       ↓
#       learning
#
# At every step, the RNN receives:
#
#       Current input
#       +
#       Previous hidden state
#
#
# So the RNN does NOT process every word completely independently.
#
# It carries information from previous time steps.
#
#
# ---------------------------------------------------------------------------
# INTERVIEW ANSWER
# ---------------------------------------------------------------------------
#
# Q: What is an RNN?
#
# A:
# "RNN stands for Recurrent Neural Network. It is a neural network
# architecture designed for sequential data. It maintains a hidden state
# that carries information from previous time steps, allowing the model
# to use previous context while processing the current input."
#
#
# ---------------------------------------------------------------------------
# SIMPLE EXPLANATION
# ---------------------------------------------------------------------------
#
# Think of an RNN like a person reading a sentence word by word.
#
# When reading:
#
#       "The movie was..."
#
# the person remembers:
#
#       "The movie"
#
# when processing the next word.
#
# That previous information is represented by the hidden state in an RNN.
#
# =============================================================================


# =============================================================================
# 2. BASIC RNN ARCHITECTURE
# =============================================================================
#
# At time t:
#
#       x_t  = current input
#       h_t  = current hidden state
#       h_(t-1) = previous hidden state
#
#
# Basic RNN equation:
#
#       h_t = tanh(W_hh * h_(t-1) + W_xh * x_t + b_h)
#
#
# Where:
#
#       x_t       -> current input
#       h_(t-1)   -> previous hidden state
#       W_xh      -> input-to-hidden weights
#       W_hh      -> hidden-to-hidden weights
#       b_h       -> bias
#       tanh      -> activation function
#       h_t       -> current hidden state
#
#
# The hidden state is the "memory" of the RNN.
#
#
# Output can be calculated using:
#
#       y_t = W_hy * h_t + b_y
#
#
# Depending on the task, an activation function may also be applied
# to obtain the final output.
#
#
# ---------------------------------------------------------------------------
# IMPORTANT INTERVIEW POINT
# ---------------------------------------------------------------------------
#
# The same weights are generally reused at every time step.
#
# Example:
#
#       t=1 -> same RNN parameters
#       t=2 -> same RNN parameters
#       t=3 -> same RNN parameters
#
# This makes RNNs parameter-efficient compared with using a separate
# neural network for every position in a sequence.
#
# =============================================================================


# =============================================================================
# 3. WHY DO WE NEED RNNs?
# =============================================================================
#
# Traditional feed-forward neural networks do not naturally maintain
# information about previous inputs.
#
# Suppose we have:
#
#       "I went to the restaurant because the food was excellent."
#
# The meaning of the sentence depends on the sequence of words.
#
# RNNs are designed to process this sequence.
#
#
# For example:
#
#       x1 = "I"
#       x2 = "went"
#       x3 = "to"
#       x4 = "the"
#       x5 = "restaurant"
#
# At each step:
#
#       h1 = information from "I"
#       h2 = information from "I went"
#       h3 = information from "I went to"
#       ...
#
#
# Therefore:
#
#       Current input + previous hidden state
#
# are used to understand the current context.
#
# =============================================================================


# =============================================================================
# 4. THE MAJOR PROBLEM WITH BASIC RNN
# =============================================================================
#
# Basic RNNs have difficulty learning LONG-TERM DEPENDENCIES.
#
#
# Long-term dependency means:
#
#       Information from an earlier part of a sequence
#       is needed much later.
#
#
# Example:
#
#       "I grew up in India and I speak ______."
#
# To correctly predict the answer:
#
#       "Hindi"
#
# the model may need information from "India".
#
# There may be many words between the important information and
# the final prediction.
#
#
# This creates a LONG-TERM DEPENDENCY problem.
#
#
# In the uploaded notes, the idea is illustrated with a context gap:
#
#       Earlier information
#              ↓
#          LARGE GAP
#              ↓
#       Current prediction
#
# As the gap increases, a basic RNN can struggle to preserve
# the earlier information.
#
# =============================================================================


# =============================================================================
# 5. VANISHING GRADIENT PROBLEM
# =============================================================================
#
# One of the major reasons basic RNNs struggle with long-term dependencies
# is the VANISHING GRADIENT PROBLEM.
#
#
# During training, neural networks use:
#
#       Backpropagation
#
# RNNs are trained through:
#
#       Backpropagation Through Time (BPTT)
#
#
# During BPTT, gradients are propagated backward through many time steps.
#
# If the gradients become smaller and smaller at every step:
#
#       gradient
#           ↓
#       smaller
#           ↓
#       smaller
#           ↓
#       smaller
#           ↓
#       almost zero
#
# then the early layers/time steps receive almost no useful learning signal.
#
#
# This is called:
#
#       VANISHING GRADIENT
#
#
# ---------------------------------------------------------------------------
# WHY DOES IT HAPPEN?
# ---------------------------------------------------------------------------
#
# The gradient can involve repeated multiplication of derivatives.
#
# Conceptually:
#
#       gradient ≈
#       derivative_1 × derivative_2 × derivative_3 × ...
#
#
# If the values being multiplied are smaller than 1:
#
#       0.5 × 0.5 × 0.5 × 0.5 × ...
#
# becomes extremely small.
#
#
# Therefore, information about the error signal from later time steps
# may not effectively reach earlier time steps.
#
#
# ---------------------------------------------------------------------------
# CONSEQUENCE
# ---------------------------------------------------------------------------
#
# The RNN learns recent information well,
# but may fail to learn information that occurred much earlier.
#
#
# ---------------------------------------------------------------------------
# INTERVIEW ANSWER
# ---------------------------------------------------------------------------
#
# Q: What is the vanishing gradient problem?
#
# A:
# "The vanishing gradient problem occurs when gradients become extremely
# small during backpropagation through many layers or time steps. In RNNs,
# repeated multiplication of small derivatives can make the gradient
# approach zero. As a result, earlier time steps receive very little
# learning signal, making it difficult for the network to learn
# long-term dependencies."
#
# =============================================================================


# =============================================================================
# 6. HOW DOES LSTM SOLVE THE PROBLEM?
# =============================================================================
#
# LSTM = Long Short-Term Memory
#
# LSTM is a special type of RNN architecture designed to handle
# long-term dependencies more effectively.
#
#
# The central idea:
#
#       LSTM introduces a CELL STATE
#
# and uses:
#
#       1. Forget Gate
#       2. Input Gate
#       3. Candidate Memory
#       4. Output Gate
#
#
# The LSTM can decide:
#
#       What should I forget?
#       What new information should I remember?
#       What information should I output?
#
#
# This controlled memory mechanism helps LSTM retain useful information
# over longer sequences.
#
# =============================================================================


# =============================================================================
# 7. LSTM HAS TWO IMPORTANT STATES
# =============================================================================
#
# LSTM maintains two major forms of information:
#
#       1. Cell State (C_t)
#       2. Hidden State (h_t)
#
#
# ---------------------------------------------------------------------------
# 1. CELL STATE
# ---------------------------------------------------------------------------
#
# Cell state is the long-term memory of the LSTM.
#
# Think of it as:
#
#       "What information should be carried forward?"
#
#
# It travels through the sequence and is modified using gates.
#
#
# ---------------------------------------------------------------------------
# 2. HIDDEN STATE
# ---------------------------------------------------------------------------
#
# Hidden state is the short-term/current representation.
#
# It represents information that is relevant for the current time step
# and can be passed to the next step or used for prediction.
#
#
# ---------------------------------------------------------------------------
# EASY INTERVIEW EXPLANATION
# ---------------------------------------------------------------------------
#
# Cell state:
#
#       Long-term memory
#
# Hidden state:
#
#       Short-term/current working memory
#
#
# A very simple way to remember:
#
#       C_t -> Long-term memory
#       h_t -> Short-term memory / current output representation
#
# =============================================================================


# =============================================================================
# 8. LSTM GATES
# =============================================================================
#
# LSTM uses gates to control information flow.
#
#
# Main gates:
#
#       1. Forget Gate
#       2. Input Gate
#       3. Output Gate
#
#
# Additionally:
#
#       Candidate Memory
#
# is calculated to determine what new information can potentially
# be added to the cell state.
#
#
# Easy way to remember:
#
#       FORGET  -> What should I remove?
#
#       INPUT   -> What should I add?
#
#       OUTPUT  -> What should I show?
#
# =============================================================================


# =============================================================================
# 9. SIGMOID FUNCTION
# =============================================================================
#
# LSTM gates commonly use the sigmoid activation function.
#
#
# Sigmoid:
#
#       sigmoid(x) = 1 / (1 + e^(-x))
#
#
# Output range:
#
#       0 to 1
#
#
# This makes sigmoid useful for gates.
#
#
# Interpretation:
#
#       0 -> completely block information
#       1 -> completely allow information
#
#
# Values between 0 and 1 represent partial control.
#
#
# Example:
#
#       gate = 0.0
#       -> almost nothing passes
#
#       gate = 0.5
#       -> partially passes
#
#       gate = 1.0
#       -> almost everything passes
#
# =============================================================================


# =============================================================================
# 10. FORGET GATE
# =============================================================================
#
# The forget gate decides:
#
#       "What information from the previous cell state should I keep?"
#
#
# Formula:
#
#       f_t = sigmoid(
#                 W_f * [h_(t-1), x_t] + b_f
#             )
#
#
# Where:
#
#       h_(t-1) -> previous hidden state
#       x_t     -> current input
#       W_f     -> forget gate weights
#       b_f     -> forget gate bias
#
#
# The output:
#
#       f_t
#
# lies between:
#
#       0 and 1
#
#
# It is then used with the previous cell state:
#
#       f_t * C_(t-1)
#
#
# ---------------------------------------------------------------------------
# INTERPRETATION
# ---------------------------------------------------------------------------
#
# Suppose:
#
#       previous cell state = [6, 8, 9]
#
# and:
#
#       forget gate = [0, 0, 0]
#
# then:
#
#       [6, 8, 9] * [0, 0, 0]
#
#       = [0, 0, 0]
#
# Meaning:
#
#       Forget the previous information.
#
#
# If:
#
#       forget gate = [1, 1, 1]
#
# then:
#
#       [6, 8, 9] * [1, 1, 1]
#
#       = [6, 8, 9]
#
# Meaning:
#
#       Keep the previous information.
#
#
# If:
#
#       forget gate = [0.5, 0.5, 0.5]
#
# then:
#
#       [6, 8, 9] * [0.5, 0.5, 0.5]
#
#       = [3, 4, 4.5]
#
# Meaning:
#
#       Keep only part of the information.
#
#
# ---------------------------------------------------------------------------
# INTERVIEW ANSWER
# ---------------------------------------------------------------------------
#
# Q: What does the forget gate do?
#
# A:
# "The forget gate determines which information from the previous cell
# state should be retained or discarded. It uses a sigmoid function,
# producing values between 0 and 1, which act as soft gates on the
# previous cell state."
#
# =============================================================================


# =============================================================================
# 11. INPUT GATE
# =============================================================================
#
# The input gate decides:
#
#       "What new information should be added to the memory?"
#
#
# Formula:
#
#       i_t = sigmoid(
#                 W_i * [h_(t-1), x_t] + b_i
#             )
#
#
# The input gate controls how much new information enters the memory.
#
#
# But LSTM also needs to determine:
#
#       WHAT new information should be stored?
#
# For that, we calculate:
#
#       Candidate Memory
#
# =============================================================================


# =============================================================================
# 12. CANDIDATE MEMORY
# =============================================================================
#
# Candidate memory represents new information that could potentially
# be added to the cell state.
#
#
# Formula:
#
#       C~_t = tanh(
#                 W_C * [h_(t-1), x_t] + b_C
#              )
#
#
# Important:
#
#       Input gate decides HOW MUCH to add.
#
#       Candidate memory decides WHAT information can be added.
#
#
# This distinction is extremely important in interviews.
#
#
# Example:
#
#       Candidate memory:
#
#           [0.2, 0.7, -0.4]
#
#       Input gate:
#
#           [0.8, 0.5, 0.1]
#
#
# Element-wise multiplication:
#
#       i_t * C~_t
#
# determines the amount of candidate information added to memory.
#
# =============================================================================


# =============================================================================
# 13. UPDATING THE CELL STATE
# =============================================================================
#
# The new cell state is calculated using:
#
#       1. Previous cell state
#       2. Forget gate
#       3. Input gate
#       4. Candidate memory
#
#
# Formula:
#
#       C_t =
#           f_t * C_(t-1)
#           +
#           i_t * C~_t
#
#
# This is one of the MOST IMPORTANT LSTM equations.
#
#
# ---------------------------------------------------------------------------
# BREAK IT DOWN
# ---------------------------------------------------------------------------
#
#       f_t * C_(t-1)
#
# means:
#
#       How much old memory should remain?
#
#
#       i_t * C~_t
#
# means:
#
#       How much new information should be added?
#
#
# Therefore:
#
#       NEW MEMORY
#       =
#       RETAINED OLD MEMORY
#       +
#       SELECTED NEW INFORMATION
#
#
# ---------------------------------------------------------------------------
# INTERVIEW ANSWER
# ---------------------------------------------------------------------------
#
# Q: How is the LSTM cell state updated?
#
# A:
# "First, the forget gate determines which part of the previous cell state
# should be retained. Then the input gate and candidate memory determine
# what new information should be added. The new cell state is the sum of
# these two components:
#
#       C_t = f_t * C_(t-1) + i_t * C~_t"
#
# =============================================================================


# =============================================================================
# 14. OUTPUT GATE
# =============================================================================
#
# The output gate determines:
#
#       "What information from the current cell state should be exposed
#        as the hidden state?"
#
#
# Formula:
#
#       o_t = sigmoid(
#                 W_o * [h_(t-1), x_t] + b_o
#             )
#
#
# Then hidden state is:
#
#       h_t = o_t * tanh(C_t)
#
#
# So:
#
#       Cell state
#           ↓
#       tanh(C_t)
#           ↓
#       Output gate
#           ↓
#       Hidden state
#
#
# ---------------------------------------------------------------------------
# INTERVIEW ANSWER
# ---------------------------------------------------------------------------
#
# Q: What does the output gate do?
#
# A:
# "The output gate determines which information from the current cell
# state should be exposed as the hidden state. The hidden state is
# calculated by multiplying the output gate with tanh of the cell state."
#
# =============================================================================


# =============================================================================
# 15. COMPLETE LSTM FLOW
# =============================================================================
#
# At every time step t:
#
#
# STEP 1:
#
#       Receive:
#
#           x_t
#           h_(t-1)
#           C_(t-1)
#
#
# STEP 2:
#
#       Calculate forget gate:
#
#           f_t = sigmoid(W_f [h_(t-1), x_t] + b_f)
#
#
# STEP 3:
#
#       Calculate input gate:
#
#           i_t = sigmoid(W_i [h_(t-1), x_t] + b_i)
#
#
# STEP 4:
#
#       Calculate candidate memory:
#
#           C~_t = tanh(W_C [h_(t-1), x_t] + b_C)
#
#
# STEP 5:
#
#       Update cell state:
#
#           C_t = f_t * C_(t-1) + i_t * C~_t
#
#
# STEP 6:
#
#       Calculate output gate:
#
#           o_t = sigmoid(W_o [h_(t-1), x_t] + b_o)
#
#
# STEP 7:
#
#       Calculate hidden state:
#
#           h_t = o_t * tanh(C_t)
#
#
# STEP 8:
#
#       Pass:
#
#           C_t -> next time step
#           h_t -> next time step
#
#
# This process is repeated for every time step.
#
# =============================================================================


# =============================================================================
# 16. COMPLETE LSTM FORMULAS - QUICK REVISION
# =============================================================================
#
# Forget Gate:
#
#       f_t = sigmoid(W_f [h_(t-1), x_t] + b_f)
#
#
# Input Gate:
#
#       i_t = sigmoid(W_i [h_(t-1), x_t] + b_i)
#
#
# Candidate Memory:
#
#       C~_t = tanh(W_C [h_(t-1), x_t] + b_C)
#
#
# Cell State:
#
#       C_t = f_t * C_(t-1) + i_t * C~_t
#
#
# Output Gate:
#
#       o_t = sigmoid(W_o [h_(t-1), x_t] + b_o)
#
#
# Hidden State:
#
#       h_t = o_t * tanh(C_t)
#
#
# ---------------------------------------------------------------------------
# ONE-LINE MEMORY TRICK
# ---------------------------------------------------------------------------
#
#       FORGET -> remove old information
#       INPUT  -> select new information
#       MEMORY -> update long-term memory
#       OUTPUT -> expose useful information
#
# =============================================================================


# =============================================================================
# 17. WHY DOES LSTM USE SIGMOID AND TANH?
# =============================================================================
#
# SIGMOID:
#
#       Range = 0 to 1
#
# It is useful for gates because we want a value that represents
# "how much information should pass."
#
#
# TANH:
#
#       Range = -1 to +1
#
# It is useful for representing candidate information and transforming
# the cell state before generating the hidden state.
#
#
# Easy interview answer:
#
#       Sigmoid -> controls information flow
#
#       Tanh    -> represents/transforms information
#
#
# =============================================================================


# =============================================================================
# 18. EXAMPLE: RESTAURANT REVIEW
# =============================================================================
#
# The uploaded notes use a text paragraph similar to:
#
#       "I went to restaurant and ordered burger.
#        The burger looked tasty and crispy.
#        But burger is not good for me.
#        It has lot of fat, cholesterol.
#        But this burger was made with many good
#        things and only vegetable were used,
#        so it was good."
#
#
# This example demonstrates why context and memory are important.
#
#
# A model may encounter words such as:
#
#       good
#       bad
#       tasty
#       fat
#       cholesterol
#       vegetable
#
#
# But the final meaning depends on context.
#
# LSTM can maintain relevant information through the sequence.
#
#
# Example:
#
#       "The burger was tasty"
#
# initially gives positive information.
#
# Later:
#
#       "But it has a lot of fat and cholesterol"
#
# gives negative information.
#
# Later:
#
#       "only vegetables were used, so it was good"
#
# changes the interpretation again.
#
#
# LSTM gates allow the network to decide what information should be
# retained and what information should be discarded.
#
# =============================================================================


# =============================================================================
# 19. SIMPLE REAL-LIFE ANALOGY FOR LSTM
# =============================================================================
#
# Imagine you are reading a long story.
#
#
# FORGET GATE:
#
#       "This information is no longer important.
#        I can forget it."
#
#
# INPUT GATE:
#
#       "This new information is important.
#        I should consider storing it."
#
#
# CANDIDATE MEMORY:
#
#       "Here is the new information that could be stored."
#
#
# CELL STATE:
#
#       "This is my long-term memory."
#
#
# OUTPUT GATE:
#
#       "From everything I remember, this is what I should reveal
#        right now."
#
#
# This is a very good analogy to use in an interview.
#
# =============================================================================


# =============================================================================
# 20. LSTM VS BASIC RNN
# =============================================================================
#
# RNN:
#
#       h_t = f(h_(t-1), x_t)
#
#       Simple recurrent memory
#
#       Can struggle with long-term dependencies
#
#       More vulnerable to vanishing gradients
#
#
# LSTM:
#
#       Uses gates and cell state
#
#       Better at maintaining long-term information
#
#       More complex
#
#       More parameters
#
#
# ---------------------------------------------------------------------------
# INTERVIEW ANSWER
# ---------------------------------------------------------------------------
#
# Q: Why would you choose LSTM instead of a simple RNN?
#
# A:
# "I would choose LSTM when the task contains dependencies over longer
# sequences. A basic RNN can struggle with vanishing gradients and may
# forget older information. LSTM introduces a cell state and gating
# mechanisms that provide controlled information flow and make learning
# long-term dependencies easier."
#
# =============================================================================


# =============================================================================
# 21. LSTM VARIANTS
# =============================================================================
#
# The uploaded notes also mention variants of LSTM.
#
# One important variant shown is:
#
#       PEEPHOLE CONNECTIONS
#
#
# ---------------------------------------------------------------------------
# PEEPHOLE CONNECTIONS
# ---------------------------------------------------------------------------
#
# In a standard LSTM, gates primarily receive information from:
#
#       previous hidden state
#       +
#       current input
#
#
# With peephole connections, gates can also receive information
# directly from the cell state.
#
#
# The idea is:
#
#       Cell State
#            ↓
#       Gate decision
#
#
# This allows gates to take the internal cell state into account
# when deciding whether to forget, add, or output information.
#
#
# ---------------------------------------------------------------------------
# INTERVIEW POINT
# ---------------------------------------------------------------------------
#
# Q: What are peephole connections in LSTM?
#
# A:
# "Peephole connections are an LSTM variant where the gates can directly
# access the cell state. This allows gate decisions to consider the
# internal memory state in addition to the hidden state and current input."
#
# =============================================================================


# =============================================================================
# 22. COUPLED FORGET AND INPUT GATE
# =============================================================================
#
# Another LSTM variant mentioned in the notes is coupling:
#
#       Forget Gate
#       +
#       Input Gate
#
#
# Instead of independently deciding:
#
#       what to forget
#       what to add
#
# the two decisions can be coupled.
#
#
# Conceptually:
#
#       if we forget more,
#       we may add more new information.
#
#
# One common conceptual form is:
#
#       i_t = 1 - f_t
#
#
# This reduces the number of independent gate decisions.
#
#
# IMPORTANT:
#
# The exact implementation can vary depending on the architecture.
#
# =============================================================================


# =============================================================================
# 23. GRU
# =============================================================================
#
# GRU = Gated Recurrent Unit
#
#
# GRU is another gated recurrent neural network architecture.
#
# It was introduced as a simpler alternative to LSTM.
#
#
# Main idea:
#
#       GRU tries to handle long-term dependencies
#       while using a simpler architecture than LSTM.
#
#
# ---------------------------------------------------------------------------
# IMPORTANT DIFFERENCE
# ---------------------------------------------------------------------------
#
# LSTM:
#
#       Separate cell state
#       +
#       hidden state
#
#
# GRU:
#
#       Does NOT maintain a separate cell state in the same way.
#
#       Its hidden state carries the recurrent information.
#
#
# GRU also uses fewer gates.
#
#
# Main GRU gates:
#
#       1. Update Gate
#       2. Reset Gate
#
#
# =============================================================================


# =============================================================================
# 24. GRU UPDATE GATE
# =============================================================================
#
# Update gate decides how much of the previous hidden state should
# be retained versus how much new information should be incorporated.
#
#
# Conceptually:
#
#       Update Gate
#            ↓
#       How much old information?
#       How much new information?
#
#
# A common formulation is:
#
#       z_t = sigmoid(W_z x_t + U_z h_(t-1) + b_z)
#
#
# The exact notation can differ between implementations.
#
#
# ---------------------------------------------------------------------------
# EASY EXPLANATION
# ---------------------------------------------------------------------------
#
# Update gate:
#
#       "Should I keep the old information,
#        or should I replace it with new information?"
#
# =============================================================================


# =============================================================================
# 25. GRU RESET GATE
# =============================================================================
#
# Reset gate determines how much of the previous hidden state should
# influence the candidate hidden state.
#
#
# A common formulation:
#
#       r_t = sigmoid(W_r x_t + U_r h_(t-1) + b_r)
#
#
# Easy explanation:
#
#       Reset gate:
#
#       "How much previous information should I ignore
#        when creating the new candidate?"
#
#
# =============================================================================


# =============================================================================
# 26. GRU CANDIDATE HIDDEN STATE
# =============================================================================
#
# A common formulation is:
#
#       h~_t =
#           tanh(
#               W_h x_t
#               +
#               U_h (r_t * h_(t-1))
#               +
#               b_h
#           )
#
#
# The reset gate controls how much previous hidden information
# contributes to the candidate.
#
# =============================================================================


# =============================================================================
# 27. GRU FINAL HIDDEN STATE
# =============================================================================
#
# A common formulation:
#
#       h_t =
#           (1 - z_t) * h_(t-1)
#           +
#           z_t * h~_t
#
#
# Depending on the notation used by a framework or textbook,
# the interpretation of z_t can be written in the opposite convention.
#
# Therefore, in interviews:
#
#       Focus on the concept,
#       not only the symbol names.
#
#
# Main idea:
#
#       Previous hidden state
#                    +
#       Candidate new information
#                    ↓
#       Update gate decides the mixture
#
# =============================================================================


# =============================================================================
# 28. LSTM VS GRU
# =============================================================================
#
#
#                 LSTM                    GRU
#       --------------------------------------------------
#       Cell state + hidden state     Hidden state
#
#       More gates                   Fewer gates
#
#       More parameters              Fewer parameters
#
#       More complex                 Simpler
#
#       Often useful for complex     Often useful when a
#       long-term dependencies       simpler recurrent model
#                                    is preferred
#
#
# ---------------------------------------------------------------------------
# IMPORTANT
# ---------------------------------------------------------------------------
#
# GRU is NOT automatically "better" than LSTM.
#
# The best choice depends on:
#
#       - Dataset
#       - Sequence length
#       - Amount of training data
#       - Computational resources
#       - Accuracy requirements
#       - Training time
#       - Model complexity
#
# =============================================================================


# =============================================================================
# 29. RNN VS LSTM VS GRU - QUICK TABLE
# =============================================================================
#
#       RNN
#       ---
#       Basic recurrent architecture
#       Simple
#       Fewer parameters
#       Can struggle with long-term dependencies
#       More vulnerable to vanishing gradients
#
#
#       LSTM
#       ----
#       Gated RNN
#       Cell state + hidden state
#       Forget + Input + Output gates
#       Handles long-term dependencies better
#       More computationally expensive
#
#
#       GRU
#       ---
#       Gated RNN
#       Uses hidden state without a separate cell state
#       Update + Reset gates
#       Simpler than LSTM
#       Usually fewer parameters than LSTM
#
# =============================================================================


# =============================================================================
# 30. HOW TO EXPLAIN LSTM IN 30 SECONDS
# =============================================================================
#
# INTERVIEW QUESTION:
#
#       "Explain LSTM."
#
#
# GOOD ANSWER:
#
# "LSTM stands for Long Short-Term Memory and is a type of recurrent
# neural network designed to handle long-term dependencies.
#
# A standard RNN can suffer from vanishing gradients, which makes it
# difficult to retain information over long sequences.
#
# LSTM solves this using a cell state and gating mechanisms.
# It has a forget gate that decides what to remove, an input gate that
# decides what new information to add, and an output gate that decides
# what information to expose as the hidden state.
#
# The cell state acts as long-term memory, while the hidden state
# represents the current output or short-term information."
#
# =============================================================================


# =============================================================================
# 31. HOW TO EXPLAIN RNN -> LSTM PROGRESSION
# =============================================================================
#
# INTERVIEW QUESTION:
#
#       "Why did LSTM come after RNN?"
#
#
# ANSWER:
#
# "RNNs were introduced to process sequential data by maintaining
# a hidden state. However, basic RNNs have difficulty learning
# long-term dependencies because of problems such as vanishing gradients
# during backpropagation through time.
#
# LSTM was introduced as a gated recurrent architecture that provides
# a more controlled memory mechanism using a cell state and gates.
#
# This allows the model to selectively forget old information,
# add new information, and expose relevant information."
#
# =============================================================================


# =============================================================================
# 32. BACKPROPAGATION THROUGH TIME - BPTT
# =============================================================================
#
# RNNs are trained using:
#
#       Backpropagation Through Time
#
# or:
#
#       BPTT
#
#
# Conceptually:
#
#       RNN sequence
#
#       t1 -> t2 -> t3 -> t4 -> t5
#
# During backpropagation, the error is propagated backward:
#
#       t5 -> t4 -> t3 -> t2 -> t1
#
#
# This is why RNNs can suffer from:
#
#       Vanishing gradients
#       Exploding gradients
#
#
# because gradients are repeatedly propagated through many time steps.
#
# =============================================================================


# =============================================================================
# 33. VANISHING VS EXPLODING GRADIENT
# =============================================================================
#
# VANISHING GRADIENT:
#
#       Gradient becomes extremely small.
#
#       Result:
#           Early time steps learn very slowly.
#
#
# EXPLODING GRADIENT:
#
#       Gradient becomes extremely large.
#
#       Result:
#           Training becomes unstable.
#
#
# Common techniques for exploding gradients:
#
#       Gradient clipping
#
#
# For long-term dependencies:
#
#       LSTM / GRU
#
# can help because they provide gated recurrent mechanisms.
#
# =============================================================================


# =============================================================================
# 34. WHY CELL STATE HELPS LSTM
# =============================================================================
#
# One of the key advantages of LSTM is its cell-state pathway.
#
# The cell state can carry information through many time steps while
# gates control how information is modified.
#
#
# Instead of forcing all information through repeated nonlinear
# transformations in exactly the same way as a basic RNN,
# LSTM provides a more controlled path for memory.
#
#
# This helps LSTM learn long-term relationships more effectively.
#
# =============================================================================


# =============================================================================
# 35. ELEMENT-WISE MULTIPLICATION IN LSTM
# =============================================================================
#
# LSTM frequently uses element-wise multiplication.
#
# Symbol:
#
#       *
#
# or sometimes:
#
#       ⊙
#
#
# Example:
#
#       C_(t-1) = [6, 8, 9]
#
#       f_t = [0.5, 0.5, 0.5]
#
#
# Then:
#
#       f_t ⊙ C_(t-1)
#
#       = [3, 4, 4.5]
#
#
# This is NOT matrix multiplication.
#
# It is element-by-element multiplication.
#
#
# This is important when explaining gate operations.
#
# =============================================================================


# =============================================================================
# 36. WHAT HAPPENS AT ONE LSTM TIME STEP?
# =============================================================================
#
# Suppose:
#
#       x_t = current word
#
#       h_(t-1) = previous hidden state
#
#       C_(t-1) = previous cell state
#
#
# LSTM asks three major questions:
#
#
#       QUESTION 1:
#       What old information should I forget?
#
#       -> Forget Gate
#
#
#       QUESTION 2:
#       What new information should I add?
#
#       -> Input Gate + Candidate Memory
#
#
#       QUESTION 3:
#       What information should I output?
#
#       -> Output Gate
#
#
# Then:
#
#       C_t -> updated long-term memory
#
#       h_t -> updated hidden/current representation
#
# =============================================================================


# =============================================================================
# 37. COMMON INTERVIEW QUESTION:
#     "WHAT IS THE DIFFERENCE BETWEEN CELL STATE AND HIDDEN STATE?"
# =============================================================================
#
# ANSWER:
#
# "The cell state represents the long-term memory of an LSTM and carries
# information across time steps. The hidden state represents the current
# output or short-term working representation and is also passed to the
# next time step."
#
#
# EASY VERSION:
#
#       Cell state  -> What I remember for the long term
#
#       Hidden state -> What I am currently using/outputting
#
# =============================================================================


# =============================================================================
# 38. COMMON INTERVIEW QUESTION:
#     "WHY DOES LSTM HAVE A FORGET GATE?"
# =============================================================================
#
# ANSWER:
#
# "The forget gate allows the LSTM to selectively remove irrelevant
# information from the previous cell state. Its sigmoid output ranges
# between 0 and 1, allowing the model to control how much previous
# memory should be retained."
#
# =============================================================================


# =============================================================================
# 39. COMMON INTERVIEW QUESTION:
#     "WHY IS SIGMOID USED FOR GATES?"
# =============================================================================
#
# ANSWER:
#
# "Sigmoid produces values between 0 and 1, which makes it suitable
# for controlling information flow. A value close to zero blocks
# information, while a value close to one allows it to pass."
#
# =============================================================================


# =============================================================================
# 40. COMMON INTERVIEW QUESTION:
#     "WHY IS TANH USED IN LSTM?"
# =============================================================================
#
# ANSWER:
#
# "Tanh maps values between -1 and 1 and is used to represent candidate
# information and to transform the cell state before producing the
# hidden state."
#
# =============================================================================


# =============================================================================
# 41. COMMON INTERVIEW QUESTION:
#     "IS LSTM STILL AN RNN?"
# =============================================================================
#
# YES.
#
# LSTM is a type/variant of recurrent neural network.
#
#
# Relationship:
#
#       RNN
#        |
#        +---- Basic RNN
#        |
#        +---- LSTM
#        |
#        +---- GRU
#
#
# LSTM and GRU are gated recurrent architectures.
#
# =============================================================================


# =============================================================================
# 42. COMMON INTERVIEW QUESTION:
#     "IS GRU BETTER THAN LSTM?"
# =============================================================================
#
# NOT ALWAYS.
#
# The correct answer is:
#
#       "It depends on the task."
#
#
# GRU:
#
#       - Simpler
#       - Fewer parameters
#       - Often faster to train
#
#
# LSTM:
#
#       - More complex
#       - Separate cell state
#       - More explicit memory control
#
#
# In practice:
#
#       Try both if the problem warrants it,
#       then compare validation performance,
#       training time, and resource usage.
#
# =============================================================================


# =============================================================================
# 43. COMMON INTERVIEW QUESTION:
#     "WHEN WOULD YOU USE RNN?"
# =============================================================================
#
# A basic RNN can be considered when:
#
#       - The sequence dependency is relatively short
#       - The problem is simple
#       - Computational simplicity is important
#       - A lightweight recurrent baseline is desired
#
#
# For more difficult long-term dependencies,
# LSTM or GRU may be more appropriate.
#
# =============================================================================


# =============================================================================
# 44. COMMON INTERVIEW QUESTION:
#     "WHEN WOULD YOU USE LSTM?"
# =============================================================================
#
# LSTM is useful when:
#
#       - Sequence data is involved
#       - Long-term dependencies matter
#       - Earlier context can influence later predictions
#       - A richer recurrent memory mechanism is useful
#
#
# Examples:
#
#       - Text classification
#       - Sentiment analysis
#       - Sequence prediction
#       - Time-series forecasting
#       - Speech-related tasks
#       - Machine translation
#
# =============================================================================


# =============================================================================
# 45. COMMON INTERVIEW QUESTION:
#     "WHEN WOULD YOU USE GRU?"
# =============================================================================
#
# GRU can be useful when:
#
#       - You need gated recurrent behavior
#       - You want fewer parameters than LSTM
#       - Training speed/model simplicity is important
#       - The task does not require the full complexity of an LSTM
#
# =============================================================================


# =============================================================================
# 46. COMMON MISTAKE #1
# =============================================================================
#
# WRONG:
#
#       "Forget gate completely deletes information."
#
#
# BETTER:
#
#       "Forget gate produces values between 0 and 1 that control
#        how much of the previous cell state is retained."
#
#
# It is generally a SOFT selection mechanism, not simply a hard
# delete operation.
#
# =============================================================================


# =============================================================================
# 47. COMMON MISTAKE #2
# =============================================================================
#
# WRONG:
#
#       "Cell state is the output."
#
#
# BETTER:
#
#       Cell state = long-term memory
#
#       Hidden state = current output representation
#
# =============================================================================


# =============================================================================
# 48. COMMON MISTAKE #3
# =============================================================================
#
# WRONG:
#
#       "LSTM completely eliminates vanishing gradients."
#
#
# BETTER:
#
#       "LSTM is designed to mitigate the difficulty of learning
#        long-term dependencies associated with basic RNNs."
#
#
# Avoid saying:
#
#       "LSTM guarantees no vanishing gradient."
#
# =============================================================================


# =============================================================================
# 49. COMMON MISTAKE #4
# =============================================================================
#
# WRONG:
#
#       "GRU has exactly the same architecture as LSTM."
#
#
# BETTER:
#
#       LSTM and GRU are both gated recurrent architectures,
#       but their internal memory mechanisms are different.
#
# =============================================================================


# =============================================================================
# 50. IMPORTANT DIMENSIONS IN LSTM
# =============================================================================
#
# Suppose:
#
#       Input size = 3
#
#       Hidden size = 4
#
#
# Then:
#
#       x_t shape = (3,)
#
#       h_(t-1) shape = (4,)
#
#
# Concatenation:
#
#       [h_(t-1), x_t]
#
# has:
#
#       4 + 3 = 7
#
# features.
#
#
# Each gate can therefore use a weight matrix of compatible dimensions.
#
#
# For example:
#
#       W_f shape = (4, 7)
#
# if:
#
#       hidden size = 4
#       concatenated input size = 7
#
#
# Then:
#
#       W_f @ [h_(t-1), x_t]
#
# produces 4 values.
#
# =============================================================================


# =============================================================================
# 51. WHY ARE THERE MANY PARAMETERS IN LSTM?
# =============================================================================
#
# LSTM has multiple transformations:
#
#       Forget gate
#       Input gate
#       Candidate memory
#       Output gate
#
#
# Each has its own parameters.
#
#
# Therefore, compared with a basic RNN:
#
#       LSTM -> more parameters
#
#
# More parameters can mean:
#
#       - Higher computational cost
#       - More memory usage
#       - Potentially longer training time
#
#
# But the benefit is better control over memory.
#
# =============================================================================


# =============================================================================
# 52. LSTM TRAINING FLOW
# =============================================================================
#
# Forward pass:
#
#       Input sequence
#            ↓
#       LSTM cells
#            ↓
#       Hidden states
#            ↓
#       Output
#            ↓
#       Loss
#
#
# Backward pass:
#
#       Loss
#        ↓
#       Gradients
#        ↓
#       Back through time
#        ↓
#       Update weights
#
#
# This is:
#
#       Backpropagation Through Time
#
#
# The trainable parameters such as:
#
#       W_f
#       W_i
#       W_C
#       W_o
#
# and corresponding biases are updated during training.
#
# =============================================================================


# =============================================================================
# 53. SIMPLE MEMORY DIAGRAM
# =============================================================================
#
#
#                    CURRENT INPUT
#                         x_t
#                          |
#                          |
#             +------------+------------+
#             |            |            |
#             ↓            ↓            ↓
#          FORGET        INPUT        OUTPUT
#           GATE          GATE          GATE
#             |            |
#             |        CANDIDATE
#             |         MEMORY
#             |            |
#             +-----+------+
#                   |
#                   ↓
#              CELL STATE
#                   |
#                   ↓
#               tanh(C_t)
#                   |
#                   ×
#                   |
#              OUTPUT GATE
#                   |
#                   ↓
#             HIDDEN STATE
#
#
# Previous:
#
#       C_(t-1)
#       h_(t-1)
#
# are also used during the computation.
#
# =============================================================================


# =============================================================================
# 54. THE MOST IMPORTANT LSTM FLOW TO MEMORIZE
# =============================================================================
#
#
#       Previous Memory
#             |
#             ↓
#       FORGET GATE
#             |
#             ↓
#       Keep / Remove
#
#
#       Current Input
#             |
#             ↓
#       INPUT GATE
#             +
#       CANDIDATE MEMORY
#             |
#             ↓
#       Add useful information
#
#
#       Previous Memory + New Information
#                    |
#                    ↓
#               CELL STATE
#
#
#       CELL STATE
#             |
#             ↓
#        OUTPUT GATE
#             |
#             ↓
#        HIDDEN STATE
#
#
# This is the entire LSTM concept in one diagram.
#
# =============================================================================


# =============================================================================
# 55. RNN / LSTM / GRU INTERVIEW COMPARISON
# =============================================================================
#
# Question:
#
#       "Compare RNN, LSTM and GRU."
#
#
# Answer:
#
# "A basic RNN maintains a hidden state and is simple, but it can struggle
# with long-term dependencies because of vanishing gradients.
#
# LSTM addresses this using a cell state and three main gates:
# forget, input and output gates.
#
# GRU is another gated RNN architecture that simplifies the LSTM design
# using update and reset gates and does not maintain a separate cell state
# in the same way.
#
# GRU generally has fewer parameters than LSTM, while LSTM provides a
# more explicit memory mechanism."
#
# =============================================================================


# =============================================================================
# 56. QUICK REVISION - ONE-LINERS
# =============================================================================
#
# RNN:
#       Neural network for sequential data.
#
# Hidden state:
#       Carries information from previous time steps.
#
# BPTT:
#       Backpropagation Through Time.
#
# Long-term dependency:
#       Earlier information is needed much later.
#
# Vanishing gradient:
#       Gradients become very small.
#
# LSTM:
#       Gated RNN designed to better learn long-term dependencies.
#
# Cell state:
#       Long-term memory.
#
# Hidden state:
#       Current/short-term representation.
#
# Forget gate:
#       Decides what old memory to retain.
#
# Input gate:
#       Controls how much new information is added.
#
# Candidate memory:
#       Represents potential new information.
#
# Output gate:
#       Controls what information is exposed.
#
# Sigmoid:
#       0 to 1, useful for gates.
#
# Tanh:
#       -1 to +1, useful for information representation.
#
# GRU:
#       Simpler gated recurrent architecture.
#
# GRU gates:
#       Update gate + Reset gate.
#
# =============================================================================


# =============================================================================
# 57. TOP 15 INTERVIEW QUESTIONS
# =============================================================================
#
# 1. What is an RNN?
#
# 2. Why do we use RNNs?
#
# 3. What is the hidden state?
#
# 4. What is long-term dependency?
#
# 5. What is the vanishing gradient problem?
#
# 6. Why does vanilla RNN suffer from vanishing gradients?
#
# 7. What is LSTM?
#
# 8. Why was LSTM introduced?
#
# 9. What is the difference between cell state and hidden state?
#
# 10. Explain the forget gate.
#
# 11. Explain the input gate.
#
# 12. Explain the output gate.
#
# 13. Why does LSTM use sigmoid and tanh?
#
# 14. What is GRU?
#
# 15. What is the difference between LSTM and GRU?
#
# =============================================================================


# =============================================================================
# 58. TOP 10 QUESTIONS - SHORT ANSWERS
# =============================================================================
#
#
# Q1. What is RNN?
#
# A:
#       A neural network designed for sequential data that maintains
#       information from previous time steps through a hidden state.
#
#
# Q2. What problem does LSTM solve?
#
# A:
#       It is designed to handle long-term dependencies more effectively
#       than a basic RNN.
#
#
# Q3. What is vanishing gradient?
#
# A:
#       A situation where gradients become extremely small during
#       backpropagation, making early time steps difficult to train.
#
#
# Q4. What is the cell state?
#
# A:
#       The long-term memory pathway of an LSTM.
#
#
# Q5. What is the hidden state?
#
# A:
#       The current output/short-term representation passed through
#       the sequence.
#
#
# Q6. What does the forget gate do?
#
# A:
#       Controls how much of the previous cell state is retained.
#
#
# Q7. What does the input gate do?
#
# A:
#       Controls how much new candidate information is added to memory.
#
#
# Q8. What does the output gate do?
#
# A:
#       Controls how much of the current cell state is exposed
#       as the hidden state.
#
#
# Q9. What is GRU?
#
# A:
#       A gated recurrent architecture with update and reset gates,
#       generally simpler than LSTM.
#
#
# Q10. Which is better: LSTM or GRU?
#
# A:
#       Neither is universally better. It depends on the task,
#       dataset and computational requirements.
#
# =============================================================================


# =============================================================================
# 59. HOW TO ANSWER IF THE INTERVIEWER ASKS:
#     "EXPLAIN LSTM WITH AN EXAMPLE"
# =============================================================================
#
# Use this structure:
#
#
# STEP 1:
#       Start with the problem.
#
#       "Basic RNNs struggle with long-term dependencies."
#
#
# STEP 2:
#       Explain why.
#
#       "Because gradients can vanish during BPTT."
#
#
# STEP 3:
#       Introduce LSTM.
#
#       "LSTM is a gated RNN architecture."
#
#
# STEP 4:
#       Explain memory.
#
#       "It maintains a cell state for long-term information."
#
#
# STEP 5:
#       Explain gates.
#
#       "Forget gate decides what to remove,
#        input gate decides what to add,
#        and output gate decides what to expose."
#
#
# STEP 6:
#       Give an example.
#
#       "In a long sentence, an earlier word may determine the meaning
#        of a later word. LSTM can selectively preserve that important
#        context through its memory mechanism."
#
#
# This gives a structured answer instead of just listing formulas.
#
# =============================================================================


# =============================================================================
# 60. FINAL INTERVIEW CHEAT SHEET
# =============================================================================
#
#
#                       SEQUENTIAL DATA
#                             |
#                             ↓
#                           RNN
#                             |
#                  Long-term dependency
#                             |
#                             ↓
#                    Vanishing Gradient
#                             |
#                             ↓
#                           LSTM
#                             |
#             +---------------+---------------+
#             |               |               |
#             ↓               ↓               ↓
#         Forget Gate     Input Gate      Output Gate
#             |               |               |
#             |          Candidate Memory      |
#             |               |               |
#             +------- CELL STATE -------------+
#                             |
#                             ↓
#                       Hidden State
#
#
#                           GRU
#                             |
#                 +-----------+-----------+
#                 |                       |
#                 ↓                       ↓
#             Update Gate             Reset Gate
#
#
# =============================================================================


# =============================================================================
# 61. FINAL THINGS TO REMEMBER BEFORE INTERVIEW
# =============================================================================
#
# If you remember ONLY these points, you can still explain the topic:
#
#
# 1.
#       RNN is designed for sequential data.
#
# 2.
#       RNN maintains a hidden state.
#
# 3.
#       RNN can struggle with long-term dependencies.
#
# 4.
#       Vanishing gradients are a major reason.
#
# 5.
#       LSTM is a gated RNN architecture.
#
# 6.
#       LSTM has:
#
#           Cell state
#           Hidden state
#
# 7.
#       LSTM has:
#
#           Forget gate
#           Input gate
#           Output gate
#
# 8.
#       Candidate memory contains potential new information.
#
# 9.
#       Cell state is updated using:
#
#           C_t = f_t * C_(t-1) + i_t * C~_t
#
# 10.
#       Hidden state is:
#
#           h_t = o_t * tanh(C_t)
#
# 11.
#       Sigmoid -> 0 to 1 -> gating
#
# 12.
#       Tanh -> -1 to +1 -> information representation
#
# 13.
#       GRU is a simpler gated recurrent architecture.
#
# 14.
#       GRU mainly uses:
#
#           Update gate
#           Reset gate
#
# 15.
#       LSTM and GRU are not automatically better than each other.
#       Model choice depends on the problem.
#
# =============================================================================


# =============================================================================
#                         END OF NOTES
# =============================================================================
#
# MASTER MEMORY TRICK:
#
#       RNN
#        ↓
#       Has memory
#        ↓
#       Long-term dependency problem
#        ↓
#       Vanishing gradient
#        ↓
#       LSTM
#        ↓
#       Forget -> Input -> Cell State -> Output
#
#
# AND:
#
#       GRU
#        ↓
#       Simpler gated RNN
#        ↓
#       Update + Reset
#
# =============================================================================