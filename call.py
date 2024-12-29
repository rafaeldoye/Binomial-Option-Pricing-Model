import math

def binomial_option_pricing():
    # Gather inputs
    S = float(input("Enter the current stock price (S): "))
    K = float(input("Enter the strike price (K): "))
    T = float(input("Enter the time to maturity in years (T): "))
    r = float(input("Enter the risk-free interest rate (r) as a decimal: "))
    sigma = float(input("Enter the volatility (sigma) as a decimal: "))
    n = int(input("Enter the number of time steps (n): "))
    option_type = input("Enter 'American' or 'European' for the option type: ").strip().lower()

    # Calculate up and down factors and time step size
    dt = T / n
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    q = (math.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize asset price tree
    asset_prices = [[0] * (i + 1) for i in range(n + 1)]
    asset_prices[0][0] = S
    for i in range(1, n + 1):
        for j in range(i + 1):
            asset_prices[i][j] = S * (u ** j) * (d ** (i - j))

    # Initialize option value tree
    option_values = [[0] * (i + 1) for i in range(n + 1)]

    # Compute option values at maturity
    for j in range(n + 1):
        option_values[n][j] = max(0, asset_prices[n][j] - K)  # Call option payoff

    # Backward induction
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            continuation_value = (q * option_values[i + 1][j + 1] + (1 - q) * option_values[i + 1][j]) * math.exp(-r * dt)
            if option_type == 'american':
                option_values[i][j] = max(continuation_value, asset_prices[i][j] - K)  # Early exercise condition
            else:  # European option
                option_values[i][j] = continuation_value

    # Output result
    print(f"The price of the {option_type.capitalize()} call option is: {option_values[0][0]:.2f}")

if __name__ == "__main__":
    binomial_option_pricing()
