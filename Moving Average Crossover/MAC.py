"""
Moving Average Crossover Strategy - Pure Python Version

Author: Anshuman Sinha
Date: July 2025

Description:
    A minimal, self-contained trading strategy implementation using hardcoded data.
    This script demonstrates how a moving average crossover system generates buy/sell
    signals and evaluates strategy returns — without using any external libraries or files.
"""

# Hardcoded stock closing prices for 30 days (can be extended)
dates = [
    "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
    "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10",
    "2024-01-11", "2024-01-12", "2024-01-13", "2024-01-14", "2024-01-15",
    "2024-01-16", "2024-01-17", "2024-01-18", "2024-01-19", "2024-01-20",
    "2024-01-21", "2024-01-22", "2024-01-23", "2024-01-24", "2024-01-25",
    "2024-01-26", "2024-01-27", "2024-01-28", "2024-01-29", "2024-01-30"
]

# Simulated closing prices
close_prices = [
    100, 102, 101, 103, 104,
    105, 107, 106, 108, 110,
    109, 111, 113, 112, 114,
    115, 117, 116, 118, 119,
    120, 122, 121, 123, 125,
    124, 126, 127, 129, 130
]

# Configuration
short_window = 3
long_window = 5

# Helper function: calculate simple moving average
def moving_average(data, window, index):
    if index + 1 < window:
        return None
    return sum(data[index - window + 1 : index + 1]) / window

# Main logic
signals = []
positions = []
strategy_returns = []
daily_returns = []

print("📊 Buy/Sell Signals:\n")

for i in range(len(close_prices)):
    short_ma = moving_average(close_prices, short_window, i)
    long_ma = moving_average(close_prices, long_window, i)

    signal = 0  # default: hold

    if short_ma is not None and long_ma is not None:
        if short_ma > long_ma:
            signal = 1  # buy
        elif short_ma < long_ma:
            signal = -1  # sell

    signals.append(signal)

    if signal == 1:
        print(f"{dates[i]} - BUY  at ${close_prices[i]}")
    elif signal == -1:
        print(f"{dates[i]} - SELL at ${close_prices[i]}")

# Generate positions (shift signals forward by one day to avoid lookahead)
for i in range(len(signals)):
    if i == 0:
        positions.append(0)
    else:
        positions.append(signals[i - 1])

# Calculate returns
for i in range(len(close_prices)):
    if i == 0:
        daily_returns.append(0)
        strategy_returns.append(0)
        continue

    ret = (close_prices[i] - close_prices[i - 1]) / close_prices[i - 1]
    strat_ret = positions[i] * ret
    daily_returns.append(ret)
    strategy_returns.append(strat_ret)

# Calculate cumulative return
def cumulative_product(returns):
    result = 1
    for r in returns:
        result *= (1 + r)
    return result

hold_return = cumulative_product(daily_returns)
strategy_return = cumulative_product(strategy_returns)

# Summary
print("\n📈 Strategy Performance Summary:")
print(f"   Strategy Return : {strategy_return:.2f}x")
print(f"   Buy & Hold Return: {hold_return:.2f}x")
