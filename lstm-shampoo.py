import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
def parser(x):
    return pd.datetime.strptime('190'+x, '%Y-%m')


series = pd.read_csv("datasets/shampoo-sales.csv", header=0,
                     parse_dates=[0],
                     index_col=0,
                     squeeze=True,
                     date_parser=parser)

print(series.head(n=5))
series.plot()
# plt.show(block=True)

# Split data into train and test set
data = series.values
train, test = data[0:-12], data[-12:]
print(train)