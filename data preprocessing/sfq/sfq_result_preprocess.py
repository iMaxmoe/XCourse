
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def force_num(x):
    if (type(x) != int) and (type(x) != float):
        return 0
    else:
        return x
    
def remove_dup(s):
    return ",".join(set(s.split(",")))


# In[29]:


school_codes = ["bm", "eng", "sci", "hss"]
dataset = {}

for school_code in school_codes:
    
    print school_code
    
    path = "Data/" + school_code + "-f17.xlsx"
    data = pd.read_excel(path)
    
    school_dataset = {}
    dataset[school_code] = school_dataset    
    
    response_lb = 10
    response_rate_lb = 0.5
    enrolment_lb = 40
    
    data["Course Code"] = data["Course Group"] + data["Course No"].astype(str)
    data["Instructor"] = data["Instructor's Name"]
    data = data[data["Low Response Rate Indicator"] != "Y"] # Remove records with low response
    
    # Course
    
    df = data[data["Level of Statistics"]=="Section"] # Select records of course 
    df["Course Overall - Mean"] = df["Course Overall - Mean"].map(force_num)
    df = df[df["Course Overall - Mean"] > 0] # Remove null records
    
    df["Response"] = (df["Response Rate"] * df["Enrolment"]).astype(int)
    df["Course Overall - Sum"] = df["Response"] * df["Course Overall - Mean"]
    df = df[["Course Code", "Enrolment", "Response", "Course Overall - Sum"]]

    df = df.groupby("Course Code", as_index=False).agg({"Enrolment" : "sum", "Response" : "sum", "Course Overall - Sum" : "sum"}) # Aggregate
    df["Course Overall - Mean"] = df["Course Overall - Sum"].divide(df["Response"])
    df["Response Rate"] = df["Response"] / df["Enrolment"]
    df = df[["Course Code", "Course Overall - Mean", "Enrolment", "Response", "Response Rate"]]
    
    course_data = df
    course_data = course_data[course_data["Enrolment"] >= enrolment_lb]
    course_data = course_data[course_data["Response"] >= response_lb]
    course_data = course_data[course_data["Response Rate"] >= response_rate_lb]
    course_data = course_data.sort_values(["Course Overall - Mean"], ascending=False)
    
    school_dataset["course"] = course_data
    
    print "# course: ", course_data.shape[0]
    
    # Instructor
    
    df = data[data["Level of Statistics"]=="Instructor"] # Select records of instructor    
    df["Instructor Overall - Mean"] = df["Instructor Overall - Mean"].map(force_num)
    df = df[df["Instructor Overall - Mean"] > 0]  # Remove null records

    df["Response"] = (df["Response Rate"] * df["Enrolment"]).astype(int)
    df["Instructor Overall - Sum"] = df["Response"] * df["Instructor Overall - Mean"]
    df = df[["Instructor", "Enrolment", "Response", "Instructor Overall - Sum", "Course Code"]]

    df = df.groupby("Instructor", as_index=False).agg({"Enrolment" : "sum", "Response" : "sum", "Instructor Overall - Sum" : "sum", "Course Code" : lambda col: ','.join(col)}) # Aggregate
    df["Instructor Overall - Mean"] = df["Instructor Overall - Sum"].divide(df["Response"])
    df["Response Rate"] = df["Response"] / df["Enrolment"]
    df = df[["Instructor", "Instructor Overall - Mean", "Enrolment", "Response", "Response Rate", "Course Code"]]
    df["Course Code"] = df["Course Code"].map(remove_dup)
    
    instructor_data = df
    instructor_data = instructor_data[instructor_data["Enrolment"] >= enrolment_lb]
    instructor_data = instructor_data[instructor_data["Response"] >= response_lb]
    instructor_data = instructor_data[instructor_data["Response Rate"] >= response_rate_lb]
    instructor_data = instructor_data.sort_values(["Instructor Overall - Mean"], ascending=False)
    
    school_dataset["instructor"] = instructor_data
    
    print "# instructor: ", instructor_data.shape[0]


# In[21]:


dataset["eng"]["instructor"].head()


# In[22]:


dataset["eng"]["course"].head()


# In[23]:


dataset["eng"]["instructor"].tail()


# In[24]:


dataset["eng"]["course"].tail()


# In[30]:


for school_code in school_codes:
    for item in {"course", "instructor"}:
        file_name = school_code + "_" + item + ".csv"
        dataset[school_code][item].reset_index().drop(['index'], axis=1).to_csv(file_name)
        print "exported: " + file_name

