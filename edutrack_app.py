import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("EduTrack - Student Performance & Attendance Analytics")

data = pd.read_csv("student_data.csv")
total_students = len(data)
avg_attendance = data["Attendance"].mean()
avg_marks = data[["Maths","Science","English"]].mean().mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", total_students)
col2.metric("Average Attendance", f"{avg_attendance:.1f}%")
col3.metric("Average Marks", f"{avg_marks:.1f}")

st.subheader("Student Dataset")
st.dataframe(data)
st.subheader("Filter Students by Attendance")

attendance_filter = st.slider("Minimum Attendance", 0, 100, 50)

filtered_data = data[data["Attendance"] >= attendance_filter]

st.dataframe(filtered_data)

st.subheader("Attendance Analysis")

fig, ax = plt.subplots()
sns.barplot(x="Name", y="Attendance", data=data)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Subject Performance")

subjects = ["Maths","Science","English"]
avg_scores = data[subjects].mean()

fig2, ax2 = plt.subplots()
avg_scores.plot(kind="bar")
plt.ylabel("Average Score")

st.pyplot(fig2)

st.subheader("Top Performing Students")

data["Average"] = data[subjects].mean(axis=1)
top_students = data.sort_values(by="Average", ascending=False).head(3)

st.table(top_students[["Name","Average"]])

st.subheader("Low Attendance Warning")

low_attendance = data[data["Attendance"] < 75]
st.table(low_attendance[["Name","Attendance"]])
st.subheader("Student Subject Comparison")

student = st.selectbox("Select Student", data["Name"])

student_data = data[data["Name"] == student]

subjects = ["Maths","Science","English"]

fig3, ax3 = plt.subplots()

ax3.bar(subjects, student_data[subjects].values[0])

plt.ylabel("Marks")

st.pyplot(fig3)
st.subheader("At-Risk Students (Low Attendance or Low Marks)")

subjects = ["Maths","Science","English"]

data["Average"] = data[subjects].mean(axis=1)

risk_students = data[(data["Attendance"] < 75) | (data["Average"] < 60)]

st.table(risk_students[["Name","Attendance","Average"]])