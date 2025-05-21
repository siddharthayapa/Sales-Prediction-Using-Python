# Sales prediction program

def mean(values): 
    return sum(values) / len(values)

def predict_sales(sales_data, next_month):
    # Handle insufficient data
    if len(sales_data) < 2:
        return sales_data[-1] if sales_data else 0

    # Calculate the average sales growth rate
    growth_rates = []
    for i in range(1, len(sales_data)):
        if sales_data[i - 1] != 0:
            growth_rate = (sales_data[i] - sales_data[i - 1]) / sales_data[i - 1]
            growth_rates.append(growth_rate)

    if not growth_rates:
        return sales_data[-1]

    average_growth_rate = mean(growth_rates)

    # Predict the sales for the next month
    last_month_sales = sales_data[-1]
    predicted_sales = last_month_sales * (1 + average_growth_rate)
    return round(predicted_sales, 2)

# Example sales data (sales for each month)
sales_data = [100, 120, 140, 160, 180]

# Predict sales for the next month
next_month = len(sales_data) + 1
predicted_sales = predict_sales(sales_data, next_month)

print(f"Predicted sales for month {next_month}: {predicted_sales}")
