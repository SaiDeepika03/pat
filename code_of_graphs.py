#graph1
import matplotlib.pyplot as plt
import pandas as pd


# Initialize the lists for X and Y
data = pd.read_csv('C:\\Users\\Student\\Downloads\\scipy-main (1)\\scipy-main\\sample1.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Occurrencies of Assert statements in test file")
plt.xlabel("Frequency of assert statements")
plt.ylabel("Occurences of assertions")

# Show the plot
plt.show()




#graph2
import matplotlib.pyplot as plt
import pandas as pd


# Initialize the lists for X and Y
data = pd.read_csv('C:\\Users\\Student\\Downloads\\scipy-main (1)\\scipy-main\\task2.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Occurrencies of Assert statements in test file")
plt.xlabel("Frequency of assert statements")
plt.ylabel("Occurences of debug")

# Show the plot
plt.show()




#graph3
import matplotlib.pyplot as plt
import pandas as pd


# Initialize the lists for X and Y
data = pd.read_csv('C:\\Users\\Student\\Downloads\\scipy-main (1)\\scipy-main\\sample3.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Occurrencies of Assert statements in production file")
plt.xlabel("Frequency of assert statements in production files")
plt.ylabel("Occurences of assert statements")

# Show the plot
plt.show()
