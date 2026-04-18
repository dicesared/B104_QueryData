# Developer: Cruz, Brendan and Daniel, DiCesare
# Course: B104
# Assignment: Final Project

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/dicesared/B104_QueryData/refs/heads/main/B104_Project_Queryv2.csv?token=GHSAT0AAAAAADZX7LOORM2OQ2G23WFGXEOY2PC5WPQ")


## Question Answer Maps
# q1 - how old are you
q1_map = {1: "12 years old or younger", 2: "13 years old", 3: "14 years old", 4: "15 years old", 5: "16 years old", 6: "17 years old", 7: "18 years old"}
# q2 - gender
q2_map = {1: "female", 2: "male"}
# q3 - what grade
q3_map = {1: "9th grade", 2: "10th grade", 3: "11th grade", 4: "12th grade", 5: "ungraded"}
# q12 - past 30 days, how many days did you carry a weapon on school property
q12_map = {1: "0 days", 2: "1 day", 3: "2 or 3 days", 4: "4 or 5 days", 5: "6 or more days"}
# q14 - past 30 days, how many days did you not go to scool because felt unsafe at school or on your to or from school
q14_map = {1: "0 days", 2: "1 day", 3: "2 or 3 days", 4: "4 or 5 days", 5: "6 or more days"}
# q16 -  past 12 months, how many times were you in a physical fight
q16_map = {1: "0 times", 2: "1 time", 3: "2 or 3 times", 4: "4 or 5 times", 5: "6 or 7 times", 6: "8 or 9 times", 7: "10 or 11 times", 8: "12 or more times"}
q18_map ={1: "yes", 2: "no"}

df["q1"] = df["q1"].replace(q1_map)
df["q2"] = df["q2"].replace(q2_map)
df["q3"] = df["q3"].replace(q3_map)
df["q12"] = df["q12"].replace(q12_map)
df["q14"] = df["q14"].replace(q14_map)
df["q16"] = df["q16"].replace(q16_map)
df["q18"] = df["q18"].replace(q18_map)

print(df.head())

