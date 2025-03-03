import math
from scipy.stats import norm

def black_scholes(option_type,S,K,daysTill,r,sigma,days_in_year):
    T = daysTill / days_in_year

    # Calculate d1 and d2
        #d1 needed for delta
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Calculate the option price based on option type (call or put)
    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")

    return option_price