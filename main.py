import numpy as np

# Function to calculate option price using Binomial Model
def binomial_option_pricing(S0, K, T, r, sigma, N, option_type="European"):
    # Calculate the parameters for the binomial tree
    dt = T / N  # Time step
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral up probability
    q = 1 - p  # Risk-neutral down probability
    discount_factor = np.exp(-r * dt)  # Discount factor

    # Initialize the binomial tree for stock prices
    ST = np.zeros((N + 1, N + 1))  # Stock price tree
    option_tree = np.zeros((N + 1, N + 1))  # Option price tree
    
    # Fill the tree with stock prices at maturity
    for i in range(N + 1):
        ST[i, N] = S0 * (u ** (N - i)) * (d ** i)
    
    # Backward induction to calculate option prices
    for j in range(N, -1, -1):
        for i in range(j + 1):
            if j == N:  # At maturity, calculate option value (European or American)
                if option_type == "European":
                    option_tree[i, j] = max(0, ST[i, j] - K)  # Call option payoff
                elif option_type == "American":
                    option_tree[i, j] = max(0, ST[i, j] - K)  # Call option payoff
            else:
                # For non-terminal nodes, calculate the option price
                if option_type == "European":
                    option_tree[i, j] = discount_factor * (p * option_tree[i, j + 1] + q * option_tree[i + 1, j + 1])
                elif option_type == "American":
                    exercise_value = max(0, ST[i, j] - K)  # Early exercise value
                    option_tree[i, j] = max(exercise_value, discount_factor * (p * option_tree[i, j + 1] + q * option_tree[i + 1, j + 1]))

    # The option price at the root of the tree
    return option_tree[0, 0]

# Main function to input parameters and run the model
def main():
    # User inputs
    S0 = float(input("Enter initial stock price (S0): "))  # Initial stock price
    K = float(input("Enter strike price (K): "))  # Strike price
    T = float(input("Enter time to maturity in years (T): "))  # Time to maturity in years
    r = float(input("Enter annual risk-free rate (r): "))  # Risk-free interest rate
    sigma = float(input("Enter volatility (sigma): "))  # Volatility of the stock
    N = int(input("Enter number of periods (N): "))  # Number of periods (steps in the binomial tree)
    option_type = input("Enter option type (European or American): ").strip()  # European or American option
    
    # Price the option
    option_price = binomial_option_pricing(S0, K, T, r, sigma, N, option_type)
    
    # Output the option price
    print(f"\nThe option price is: {option_price:.2f}")

# Run the program
if __name__ == "__main__":
    main()
