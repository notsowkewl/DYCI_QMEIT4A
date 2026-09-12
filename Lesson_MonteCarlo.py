import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

# Parameters
avg = 1.00
std_dev = 0.10
num_reps = 100
num_simulations = 500

# Generate percent target
pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)

# Generate sales target
sales_target_val = [500000, 1000000, 2000000]
sales_target_prob = [0.25, 0.50, 0.25]
sales_target = np.random.choice(sales_target_val, num_reps, p=sales_target_prob)

# Calculate sales amount
sales_amt = sales_target * pct_to_target

# Calculate commission rate
commission_rate = np.where(pct_to_target >= 1.00, 0.04, np.where(pct_to_target >= 0.91, 0.03, 0.02)
)

# Calculate commission amount
commission_amt = sales_amt * commission_rate

mydf = pd.DataFrame({"Percent Target": pct_to_target, "Sales Target": sales_target, "Sales Amt": sales_amt, "Commission Rate": commission_rate, "Commission Amt": commission_amt})

print(mydf.head(10))

mydf.to_csv("myoutput.csv", index=False)