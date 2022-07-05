Install the following packages:
    . numpy:
        . 1st:
            In a terminal window run ' pip install numpy '

        . 2nd:
            Go to 'File' --> 'Settings' --> 'project_name' --> 'Python Interpreter' --> ' numpy '
            see 'https://www.youtube.com/watch?v=pVLmWlRT55E'

    . pandas:
        . 1st:
            In a terminal window run ' pip install pandas '

        . 2nd:
            Go to 'File' --> 'Settings' --> 'project_name' --> 'Python Interpreter' --> ' pandas '

    . seaborn:
        . 1st:
            In a terminal window run ' pip install seaborn '

        . 2nd:
            Go to 'File' --> 'Settings' --> 'project_name' --> 'Python Interpreter' --> ' seaborn '

    . matplotlib:
        . 1st:
            In a terminal window run ' pip install matplotlib '

        . 2nd:
            Go to 'File' --> 'Settings' --> 'project_name' --> 'Python Interpreter' --> ' matplotlib '

    . pytest: ' pip install -U pytest '

    . NOTE: if it returns an error try to check if pip, setuptools, and wheel are up to date:
            ' py -m pip install --upgrade pip setuptools wheel '


Program Description:
Clean and visualize data from a CSV file, containing the number of page views each day on the
freeCodeCamp.org forum from 2016-05-09 to 2019-12-03, using Matplotlib, Pandas and Seaborn.

This program creates three types of charts:
    - Line Plot;
    - Bar Plot;
    - Box Plot.

These charts will help to understand the patterns in visits and identify yearly and monthly growth.

Using the available data, the following tasks in time_series_visualizer.py will be executed:

. Using Pandas the data will be imported from "fcc-forum-pageviews.csv". The index to the date column will
  be set.

. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom
  2.5% of the dataset.

. Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to
  "examples/Figure_1.png".
  The title will be 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
  The label on the x axis will be Date and the label on the y axis will be Page Views.

. Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png".
  It will show average daily page views for each month grouped by year.
  The legend will show month labels and have a title of Months.
  On the chart, the label on the x axis will be Years and the label on the y axis will be Average Page Views.

. Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to
  "examples/Figure_3.png".
  These box plots will show how the values are distributed within a given year or month and how it compares
  over time.
  The title of the first chart will be Year-wise Box Plot (Trend) and the title of the second chart will be
  Month-wise Box Plot (Seasonality).
  The month labels on bottom start at Jan.

. Any time a variable is set to None, the program makes sure to set it to the correct code.

Note: see examples figures of the expected output charts.


Data Description:
Number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03

File name: fcc-forum-pageviews.csv


The file test_module.py is a unit test.
