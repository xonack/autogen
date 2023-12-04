import pandas as pd
import matplotlib.pyplot as plt
import wget

# Download the file
url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"
filename = wget.download(url, out="./visualize/cars.csv")

# Load the data into pandas dataframe
df = pd.read_csv(filename)

# Print the fields in the dataset
print(df.columns)

# Plot the relationship between weight and horsepower
plt.figure(figsize=(10,6))
plt.scatter(df['Weight'], df['Horsepower(HP)'])
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.title('Relationship between weight and horsepower')

# Save the plot to a file
plt.savefig("./visualize/weight_horsepower_relationship.png")
plt.show()