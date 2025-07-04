# nivesha_backend.py

def get_signals(segment):
    if segment == "nifty":
        return "Buy Signal - Nifty strong above 22500 [Supertrend, RSI > 55, OI support]"
    elif segment == "banknifty":
        return "Sell Signal - BankNifty weak below 48200 [PCR, IV skew, MACD cross]"
    elif segment == "stocks":
        return "Watch HDFCBANK, RELIANCE - Volume spike + Bollinger band breakout"
    elif segment == "options":
        return "Call buildup in 22500CE | IV rising | Delta 0.55 | Gamma stable"
    else:
        return "No signals"
