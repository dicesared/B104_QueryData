# Developer: Cruz, Brendan and Daniel, DiCesare
# Course: B104
# Assignment: Final Project

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/dicesared/B104_QueryData/refs/heads/dev/B104_Project_QueryV3.csv?token=GHSAT0AAAAAAD22X27OAVSCIK6MORMLNAFC2PJPXMQ")


# ## Question Answer Maps
# # q1 - how old are you
q1_map = {1: "12 years old or younger", 2: "13 years old", 3: "14 years old", 4: "15 years old", 5: "16 years old", 6: "17 years old", 7: "18 years old"}
# # q2 - gender
q2_map = {1: "female", 2: "male"}
# # q3 - what grade
q3_map = {1: "9th grade", 2: "10th grade", 3: "11th grade", 4: "12th grade", 5: "ungraded"}
# q66 - how would you describe your weight
q66_map = {1: "Very underweight", 2: "Slightly underweight", 3: "About the right weight", 4: "Slightly overweight", 5: "Very overweight"}
# q80 - how often do you use social media
q80_map = {1: "I don't use social media", 2: "A few time a month", 3: "About once a week", 4: "A few time a week", 5: "About once a day", 6: "Several times a day", 7: "About once an hour", 8: "More than once an hour"}
# q84 - past 30 days, how often was your mental health not good 
q84_map = {1: "Never", 2: "Rarely", 3: "Sometimes", 4: "Most of the time", 5: "Always"}

# Translate answers
df["q1"] = df["q1"].replace(q1_map)
df["q2"] = df["q2"].replace(q2_map)
df["q3"] = df["q3"].replace(q3_map)
#df["q66"] = df["q66"].replace(q66_map)
#df["q80"] = df["q80"].replace(q80_map)
#df["q84"] = df["q84"].replace(q84_map)


print(df.head())

#df.plot(kind = 'bar', x = 'q3', y = 'q80')
# Average Social Media USage by Grade
df.groupby('q3')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Grade Level')
plt.ylabel('Avg Social Media Use')
plt.title('Average Social Media Use by Grade Level')
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ],)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q3')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Grade Level')
plt.ylabel('Avg Mental Health')
plt.title('Average Mental Health level being rated poor by Grade Level')
plt.yticks([1, 2, 3, 4, 5], ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], )
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q3')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Grade Level')
plt.ylabel('Avg Weight Self-Reflection')
plt.title('Average Weight Self-Reflection by Grade Level')
plt.yticks([1, 2, 3, 4, 5], ["Very underweight", "Slightly underweight", "Aout the right weight", "Slightly overweight", "Very overweight"], )
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q2')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Gender')
plt.ylabel('Avg Weight Self-Reflection')
plt.title('Average Weight Self-Reflection by Gender')
plt.yticks([1, 2, 3, 4, 5], ["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"], )
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q1')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Avg Weight Self-Reflection')
plt.title('Average Weight Self-Reflection by Age')
plt.yticks([1, 2, 3, 4, 5], ["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"], )
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q2')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Gender')
plt.ylabel('Avg Mental Health')
plt.title('Average Mental Health level being rated poor by Gender')
plt.yticks([1, 2, 3, 4, 5], ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], )
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q1')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Avg Mental Health')
plt.title('Average Mental Health level being rated poor by Age')
plt.yticks([1, 2, 3, 4, 5], ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], )
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q2')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Gender')
plt.ylabel('Avg Social Media Use')
plt.title('Average Social Media Use by Gender')
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ],)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby('q1')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Avg Social Media Use')
plt.title('Average Social Media Use by Age')
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ],)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

