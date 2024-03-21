def bayes_theorem():
    try:
        prior_a = float(input("Enter prior probability of A: "))
        prior_b = float(input("Enter prior probability of B: "))
        conditional_b_given_a = float(input("Enter conditional probability of B given A: "))

        # Validate input probabilities
        if not 0 <= prior_a <= 1 or not 0 <= prior_b <= 1 or not 0 <= conditional_b_given_a <= 1:
            raise ValueError("Probabilities must be between 0 and 1")

        # Calculate probability of event B
        probability_b = prior_a * conditional_b_given_a + prior_b * (1 - conditional_b_given_a)

        # Check if the denominator is zero
        if probability_b == 0:
            raise ValueError("Denominator in Bayes' theorem cannot be zero")

        # Calculate and return the probability of A given B
        probability_a_given_b = (prior_a * conditional_b_given_a) / probability_b

        return probability_a_given_b
    except ValueError as e:
        print("Error:", e)
        return None

# Calculate and print the probability of A given B
result = bayes_theorem()
if result is not None:
    print("Probability of A given B:", result)
