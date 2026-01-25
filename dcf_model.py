# Discounted Cash Flow (DCF) Model
# This script replicates the Excel-based DCF valuation

base_fcf = 1422  # Base year free cash flow
growth_rate = 0.10
discount_rate = 0.12
terminal_growth = 0.04
forecast_years = 10

fcf_forecast = []

for year in range(1, forecast_years + 1):
    fcf = base_fcf * (1 + growth_rate) ** year
    fcf_forecast.append(fcf)

discounted_fcf = [
    fcf / (1 + discount_rate) ** year
    for year, fcf in enumerate(fcf_forecast, start=1)
]

terminal_value = (
    fcf_forecast[-1] * (1 + terminal_growth)
) / (discount_rate - terminal_growth)

discounted_terminal_value = terminal_value / (
    1 + discount_rate
) ** forecast_years

enterprise_value = sum(discounted_fcf) + discounted_terminal_value

print(f"Enterprise Value: {enterprise_value:.2f}")
