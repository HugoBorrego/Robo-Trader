import yfinance as yf

# Função para buscar dados
def get_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="12mo")
    return df
