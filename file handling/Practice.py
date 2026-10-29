# LINE GRAPH
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("Line Graph")
# plt.show()

# bar chart 

# import matplotlib.pyplot as plt

# names = ["A", "B", "C", "D"]
# marks = [80, 70, 90, 60]

# plt.bar(names, marks)
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Student Marks")
# plt.show()

# pie chart
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C", "SQL"]
marks = [40, 25, 20, 15]

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)
plt.title("Subject Distribution")
plt.show()