# Binomial Option Pricing Model

This repository contains implementations of the binomial option pricing model for **American** and **European** options. The repository is divided into two main files:

1. `call.py`: Calculates the price of call options.
2. `put.py`: Calculates the price of put options.

## Overview

The binomial option pricing model is a numerical method used to value options by discretizing the underlying asset's price movements over time into an up-and-down lattice. It supports both American and European-style options.

### Features
- Computes the price of both **Call** and **Put** options.
- Supports **American** options (with early exercise) and **European** options.
- Flexible input for various parameters such as stock price, strike price, volatility, time to maturity, and more.

---

## File Descriptions

### `call.py`
- Implements the pricing model for **Call options**.
- Accepts user inputs for:
  - Current stock price (\( S \))
  - Strike price (\( K \))
  - Time to maturity (\( T \))
  - Risk-free interest rate (\( r \))
  - Volatility (\( \sigma \))
  - Number of time steps (\( n \))
  - Option type: `American` or `European`
- Outputs the calculated call option price using a binomial tree.

#### Usage
```bash
python call.py
```

### `put.py`
- Implements the pricing model for **Put options**.
- Accepts user inputs for:
  - Spot price (\( S_0 \))
  - Strike price (\( K \))
  - Risk-free interest rate (\( r \))
  - Time to maturity (\( T \))
  - Volatility (\( \sigma \))
  - Number of time steps (\( N \))
  - Option type: `European` or `American`
- Outputs the calculated put option price using a binomial tree.

#### Usage
```bash
python put.py
```

---

## Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/binomial-option-pricing.git
cd binomial-option-pricing
```

Ensure you have Python installed (version 3.6+ recommended).

---

## Example

### Running the Call Option Pricing Script
```bash
python call.py
```
**Example Inputs:**
```
Enter the current stock price (S): 100
Enter the strike price (K): 110
Enter the time to maturity in years (T): 1
Enter the risk-free interest rate (r) as a decimal: 0.05
Enter the volatility (sigma) as a decimal: 0.2
Enter the number of time steps (n): 100
Enter 'American' or 'European' for the option type: European
```
**Output:**
```
The price of the European call option is: 5.73
```

### Running the Put Option Pricing Script
```bash
python put.py
```
**Example Inputs:**
```
Enter the spot price (S0): 100
Enter the strike price (K): 110
Enter the risk-free interest rate (r, as a decimal): 0.05
Enter the time to maturity (T, in years): 1
Enter the volatility (sigma, as a decimal): 0.2
Enter the number of time steps (N): 100
Enter the option type ('European' or 'American'): American
```
**Output:**
```
The price of the American put option is: 12.34
```

---

## Contributing
Contributions are welcome! If you'd like to improve the code or add features, feel free to fork the repository and submit a pull request.

---


### Notes
- The binomial model assumes constant volatility and risk-free interest rates.
- For a more accurate representation, consider increasing the number of time steps.

Happy coding!
