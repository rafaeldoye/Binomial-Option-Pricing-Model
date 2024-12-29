import math

def binomial_tree_put_price(S0, K, r, T, sigma, N, option_type="European"):
    # Calculate time step size and discount factor
    dt = T / N
    discount_factor = math.exp(-r * dt)
    
    # Calculate u and d (up and down factors)
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    
    # Risk-neutral probability
    p = (math.exp(r * dt) - d) / (u - d)
    
    # Initialize asset prices at each node
    asset_prices = [[0] * (N + 1) for _ in range(N + 1)]
    option_values = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Calculate asset prices at maturity (final nodes)
    for j in range(N + 1):
        asset_prices[N][j] = S0 * (u ** (N - j)) * (d ** j)
    
    # Calculate option values at maturity for put option
    for j in range(N + 1):
        option_values[N][j] = max(K - asset_prices[N][j], 0)
    
    # Backward induction for option pricing
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            # Calculate the asset price at the current node
            asset_prices[i][j] = S0 * (u ** (i - j)) * (d ** j)
            
            # Calculate the option value based on the option type
            if option_type == "European":
                option_values[i][j] = discount_factor * (p * option_values[i + 1][j] + (1 - p) * option_values[i + 1][j + 1])
            elif option_type == "American":
                option_values[i][j] = max(K - asset_prices[i][j], discount_factor * (p * option_values[i + 1][j] + (1 - p) * option_values[i + 1][j + 1]))

    return option_values[0][0]


# Main function to take user inputs
if __name__ == "__main__":
    # Input parameters
    S0 = float(input("Enter the spot price (S0): "))
    K = float(input("Enter the strike price (K): "))
    r = float(input("Enter the risk-free interest rate (r, as a decimal): "))
    T = float(input("Enter the time to maturity (T, in years): "))
    sigma = float(input("Enter the volatility (sigma, as a decimal): "))
    N = int(input("Enter the number of time steps (N): "))
    option_type = input("Enter the option type ('European' or 'American'): ")

    # Calculate the option price
    option_price = binomial_tree_put_price(S0, K, r, T, sigma, N, option_type)
    
    # Output the result
    print(f"The price of the {option_type} put option is: {option_price:.2f}")
