# Developer: Cruz, Brendan and Daniel, DiCesare
# Course: B104
# Assignment: Final Project

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import os

df = pd.read_csv("https://raw.githubusercontent.com/dicesared/B104_QueryData/refs/heads/dev/B104_Project_QueryV3.csv?token=GHSAT0AAAAAAD22X27OMNGWSRB4EWGGJ2O62PP7OJQ")

print(df.head())

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
# df.groupby('q3')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Grade Level')
# plt.ylabel('Avg Social Media Use')
# plt.title('Average Social Media Use by Grade Level')
# plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ],)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def socialmedia_grade():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))

    df.groupby('q3')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Grade Level')
    ax.set_ylabel('Avg Social Media Use')
    ax.set_title('Average Social Media Use by Grade Level')
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8])
    ax.set_yticklabels(["I don't use social media", "A few times a month", "About once a week", "A few times a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q3')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Grade Level')
# plt.ylabel('Avg Mental Health')
# plt.title('Average Mental Health level being rated poor by Grade Level')
# plt.yticks([1, 2, 3, 4, 5], ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def mentalhealth_grade():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    
    df.groupby('q3')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Grade Level')
    ax.set_ylabel('Avg Mental Health')
    ax.set_title('Average Mental Health level being rated poor by Grade Level')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Never", "Rarely", "Sometimes", "Most of the time", "Always"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q3')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Grade Level')
# plt.ylabel('Avg Weight Self-Reflection')
# plt.title('Average Weight Self-Reflection by Grade Level')
# plt.yticks([1, 2, 3, 4, 5], ["Very underweight", "Slightly underweight", "Aout the right weight", "Slightly overweight", "Very overweight"], )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def weight_grade():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    
    df.groupby('q3')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Grade Level')
    ax.set_ylabel('Avg Weight Self-Reflection')
    ax.set_title('Average Weight Self-Reflection by Grade Level')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Very underweight", "Slightly underweight", "Aout the right weight", "Slightly overweight", "Very overweight"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q2')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Gender')
# plt.ylabel('Avg Weight Self-Reflection')
# plt.title('Average Weight Self-Reflection by Gender')
# plt.yticks([1, 2, 3, 4, 5], ["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"], )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def weight_gender():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    
    df.groupby('q2')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Avg Weight Self-Reflection')
    ax.set_title('Average Weight Self-Reflection by Gender')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q1')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Age')
# plt.ylabel('Avg Weight Self-Reflection')
# plt.title('Average Weight Self-Reflection by Age')
# plt.yticks([1, 2, 3, 4, 5], ["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"], )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def weight_age():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    df.groupby('q1')['q66'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Age')
    ax.set_ylabel('Avg Weight Self-Reflection')
    ax.set_title('Average Weight Self-Reflection by Age')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q2')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Gender')
# plt.ylabel('Avg Mental Health')
# plt.title('Average Mental Health level being rated poor by Gender')
# plt.yticks([1, 2, 3, 4, 5], ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def mentalhealth_gender():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    df.groupby('q2')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Avg Mental Health')
    ax.set_title('Average Mental Health level being rated poor by Gender')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Never", "Rarely", "Sometimes", "Most of the time", "Always"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q1')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Age')
# plt.ylabel('Avg Mental Health')
# plt.title('Average Mental Health level being rated poor by Age')
# plt.yticks([1, 2, 3, 4, 5], ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def mentalhealth_age():
    for widget in frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    df.groupby('q1')['q84'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Age')
    ax.set_ylabel('Avg Mental Health')
    ax.set_title('Average Mental Health level being rated poor by Age')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Never", "Rarely", "Sometimes", "Most of the time", "Always"])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q2')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Gender')
# plt.ylabel('Avg Social Media Use')
# plt.title('Average Social Media Use by Gender')
# plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ],)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def socialmedia_gender():
    for widget in frame.winfo_children():
        widget.destroy()
        
    fig, ax = plt.subplots(figsize=(6, 3))
    df.groupby('q2')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Avg Social Media Use')
    ax.set_title('Average Social Media Use by Gender')
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8])
    ax.set_yticklabels(["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# df.groupby('q1')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black')
# plt.xlabel('Age')
# plt.ylabel('Avg Social Media Use')
# plt.title('Average Social Media Use by Age')
# plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ],)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

def socialmedia_age():
    for widget in frame.winfo_children():
        widget.destroy()
        
    fig, ax = plt.subplots(figsize=(6, 3))
    df.groupby('q1')['q80'].mean().plot(kind='bar', color='steelblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Age')
    ax.set_ylabel('Avg Social Media Use')
    ax.set_title('Average Social Media Use by Age')
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8])
    ax.set_yticklabels(["I don't use social media", "A few time a month", "About once a week", "A few time a week", "About once a day", "Several times a day", "About once an hour", "More than once an hour" ])
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
# Tkinter GUI
root = tk.Tk()
root.title("Brendan and Dan's B104 GUI of Greatness")
root.geometry("900x600")

# exit button additional code
def close_app():
    try:
        root.quit()
    except:
        pass
    try:
        root.destroy()
    except:
        pass
    os._exit(0)

# Buttons

exit_button = tk.Button(
    root,
    text="EXIT PROGRAM",
    command=close_app)
exit_button.pack(side=tk.BOTTOM, padx=20, pady=20)

socialmedia_grade = tk.Button(root,
                               text="Social Media by Grade Level",
                               command=socialmedia_grade)
socialmedia_grade.pack(side=tk.BOTTOM, padx=20, pady=20)

mentalhealth_grade = tk.Button(root,
                               text="Poor Mental Health by Grade Level",
                               command=mentalhealth_grade)
mentalhealth_grade.pack(side=tk.BOTTOM, padx=20, pady=20)

weight_grade = tk.Button(root,
                             text="Body Weight Self Reflection by Grade Level",
                             command=weight_grade)
weight_grade.pack(side=tk.BOTTOM, padx=20,pady=20)

weight_gender = tk.Button(root,
                             text="Body Weight Self Reflection by Gender",
                             command=weight_age)
weight_gender.pack(side=tk.BOTTOM, padx=20,pady=20)

weight_age = tk.Button(root,
                             text="Body Weight Self Reflection by Age",
                             command=weight_age)
weight_age.pack(side=tk.BOTTOM, padx=20,pady=20)

mentalhealth_gender = tk.Button(root,
                             text="Poor Mental Health by Gender",
                             command=mentalhealth_gender)
mentalhealth_gender.pack(side=tk.BOTTOM, padx=20,pady=20)

mentalhealth_age = tk.Button(root,
                               text="Poor Mental Health by Age",
                               command = mentalhealth_age)
mentalhealth_age.pack(side=tk.BOTTOM, padx=20,pady=20)

socialmedia_gender = tk.Button(root,
                               text="Social Media by Gender",
                               command = socialmedia_gender)
socialmedia_gender.pack(side=tk.BOTTOM, padx=20,pady=20)

socialmedia_age = tk.Button(root, 
                   text = "Social Media Use by Age",
                   command = socialmedia_age)

socialmedia_age.pack(side=tk.BOTTOM, padx=20, pady=20)

frame = tk.Frame(root, width = 800, height = 450)
frame.pack_propagate(False)
frame.pack(fill=tk.BOTH, expand=True)


# label = tk.Label(root, text="4/25 test message")
# label.pack(pady=20)

root.mainloop()