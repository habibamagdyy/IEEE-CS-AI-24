def conditional_probability(event_a, event_b):
    if len(event_a) != len(event_b):
        raise ValueError("Lengths of event_a and event_b must be the same")
    count_a = sum(event_a)
    count_b_given_a = sum(b for a, b in zip(event_a, event_b) if a == 1)

    if count_a == 0:
        return 0

    return count_b_given_a / count_a

event_a = list(map(int, input("Enter numbers of event A (0s and 1s separated by spaces): ").split()))
event_b = list(map(int, input("Enter numbers of event B (0s and 1s separated by spaces): ").split()))

print("Conditional Probability of B given A:", conditional_probability(event_a, event_b))
