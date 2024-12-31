import random
from collections import Counter

def generate_spin_history(spins):
    history = [random.randint(0, 36) for _ in range(spins)]
    return history

def analyze_spin_history(history):
    frequency = Counter(history)
    total_spins = sum(frequency.values())
    probabilities = {number: round((count / total_spins) * 100, 2) for number, count in frequency.items()}
    sorted_probabilities = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
    return sorted_probabilities

def predict_next_spin(probabilities):
    if not probabilities:
        return None
    most_likely = max(probabilities, key=probabilities.get)
    return most_likely

def main():
    print("Roulette Prediction Assistant")
    try:
        spins = int(input("Enter the number of past roulette spins to analyze: "))
        if spins <= 0:
            print("Invalid input. Number of spins must be a positive integer.")
            return
        history = generate_spin_history(spins)
        probabilities = analyze_spin_history(history)
        print("Frequency and Probabilities of Each Number:")
        for number, prob in probabilities.items():
            print(f"Number {number}: {prob}%")
        prediction = predict_next_spin(probabilities)
        print(f"The number with the highest probability of appearing next is: {prediction}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
