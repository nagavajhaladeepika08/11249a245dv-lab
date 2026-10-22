# Experiment No. 2: Basic Visualization in Python

## Aim
To create and display different types of data visualizations, including line graphs, bar charts, pie charts, scatter plots, and histograms using Python's Matplotlib library.

## Algorithm
1. Start the program.
2. Import the `matplotlib.pyplot` module.
3. Define the data required for each visualization.
4. Create a line graph using `plt.plot()` to represent changes in values.
5. Create a bar chart using `plt.bar()` to compare marks across different subjects.
6. Create a pie chart using `plt.pie()` to represent the percentage distribution of values.
7. Create a scatter plot using `plt.scatter()` to show the relationship between study hours and marks.
8. Create a histogram using `plt.hist()` to display the frequency distribution of marks.
9. Add appropriate titles and axis labels to the graphs wherever required.
10. Display each visualization using `plt.show()`.
11. Stop the program.

## Description
Data visualization is the graphical representation of information and data. It helps users understand patterns, trends, distributions, and relationships in a dataset.

The Matplotlib library provides several functions for creating different types of visualizations.

- **Line Graph:** Represents changes in data values and helps identify trends.
- **Bar Chart:** Compares values across different categories.
- **Pie Chart:** Displays the proportion of each category as a percentage of the total.
- **Scatter Plot:** Shows the relationship between two numerical variables.
- **Histogram:** Represents the frequency distribution of numerical data by grouping values into intervals called bins.

These visualizations are useful for analyzing data and presenting information in an understandable graphical format.

## Program

```python
# Experiment No. 2: Basic Visualization in Python
# Aim: Create line, bar, pie, scatter and histogram visualizations.

import matplotlib.pyplot as plt

# Line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y, marker="o")
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Bar chart
subjects = ["Python", "Java", "R", "Tableau"]
marks = [85, 75, 80, 90]
plt.bar(subjects, marks)
plt.title("Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()

# Pie chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Technology Usage")
plt.show()

# Scatter plot
hours = [1, 2, 3, 4, 5, 6]
student_marks = [45, 50, 58, 65, 72, 80]
plt.scatter(hours, student_marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Histogram
all_marks = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70,
             72, 75, 78, 80, 82, 85, 88, 90]
plt.hist(all_marks, bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
```

## Explanation

### 1. Importing the Library
`import matplotlib.pyplot as plt` imports the plotting module and assigns it the alias `plt`.

### 2. Line Graph
- `plt.plot(x, y, marker="o")` draws a line connecting the given data points.
- `plt.title()` adds a title.
- `plt.xlabel()` and `plt.ylabel()` label the axes.
- `plt.show()` displays the graph.

### 3. Bar Chart
- `subjects` contains the subject names.
- `marks` contains the corresponding marks.
- `plt.bar(subjects, marks)` creates a bar for each subject, making comparisons easy.

### 4. Pie Chart
- `plt.pie(marks, labels=subjects, autopct="%1.1f%%")` creates a pie chart.
- `labels` specifies the category names.
- `autopct="%1.1f%%"` displays each category's percentage to one decimal place.

### 5. Scatter Plot
- `hours` represents the number of study hours.
- `student_marks` represents the corresponding marks.
- `plt.scatter(hours, student_marks)` displays individual data points to show the relationship between study time and marks.

### 6. Histogram
- `all_marks` contains the marks obtained by students.
- `plt.hist(all_marks, bins=5)` groups the marks into five intervals and displays their frequency distribution.
- The X-axis represents marks, while the Y-axis represents frequency.

## Output
The program displays five separate visualizations in sequence:

1. A line graph showing changes in the given values.
2. A bar chart comparing marks in Python, Java, R, and Tableau.
3. A pie chart showing the percentage distribution of the four values.
4. A scatter plot showing the relationship between study hours and student marks.
5. A histogram showing the frequency distribution of marks.

## Result
Thus, line graphs, bar charts, pie charts, scatter plots, and histograms were successfully created and displayed using Python's Matplotlib library.

## Applications
- Analyzing trends and patterns in datasets.
- Comparing student marks and academic performance.
- Representing percentage distributions.
- Studying relationships between numerical variables.
- Understanding the frequency distribution of data.
