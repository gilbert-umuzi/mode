#Mode / SQL Yammer Tutorial Analysis

##Introduction
This repository contains my analysis and learnings from the [Mode / SQL Yammer tutorial](https://mode.com/sql-tutorial/a-drop-in-user-engagement). The project focuses on investigating user engagement on Yammer, a messaging platform, using Mode and a combination of SQL queries and Python analysis. The tutorial provided an opportunity to delve into real-world data analysis scenarios, enhancing my skills in SQL, Python, and data visualization.

##Key Learnings
###Integration of SQL and Python in Mode
* SQL Query Organization and Graphical Analysis: Mode's effective organization of SQL queries and its graphical analysis capabilities are well-suited for embedding insights directly into reports.
* Python Integration: The use of Python notebooks in conjunction with SQL queries proves valuable, particularly for statistical analysis, offering a significant timesaver compared to complex SQL queries.
* Workflow Consideration: A notable challenge is the need to restart and rerun Python notebooks with each modification in SQL queries, affecting the fluidity of analysis.
###Enhancements in SQL Skills
* Session-Based User Engagement: Learning to aggregate user engagement data into sessions was a major takeaway, providing a new perspective and depth in data analysis.
* Complex Queries: The complexity of nested SQL queries was balanced with the insights they enabled, showcasing the power of SQL in dissecting and understanding data.
* Incremental Query Building: Developing complex SQL queries incrementally, from simpler inner queries to more intricate outer layers, proved beneficial for both understanding and future reusability.

##Repository Structure
* data: Sample data files used in the project are available as part of the [Mode tutorial](https://mode.com/sql-tutorial/a-drop-in-user-engagement).
* sql_queries: Three sample queries are presented: engagement, search, and ab test.
* python_notebook: focusing on the ab test.
* report: Final report detailing the findings and insights from the tutorial.

##Running the Analysis
To replicate or build upon this analysis:

Clone the repository to your local machine.
Ensure you have Mode Analytics set up, or adapt the SQL queries for your SQL environment.
Install Python dependencies as listed in requirements.txt.
Run SQL queries followed by Python notebooks for a comprehensive analysis.

##Dependencies
Mode
Python 3.X
Libraries: pandas, matplotlib, seaborn, scipy (see requirements.txt for
version details)

SQL (compatible with Mode Analytics environment)
How to Contribute
Interested in contributing? Here's how you can help:

Fork the Repository: Start by forking this repository to your GitHub account.
Clone and Make Changes: Clone your forked repository, make your changes, and commit them.
Create a Pull Request: Submit a pull request to merge your changes into the main project.
We welcome enhancements, bug fixes, or improvements in documentation. If you have ideas or suggestions, feel free to open an issue or provide feedback in your pull request.

Contact
For any queries or further discussions, feel free to reach out to me at gilbert.pooley [at] gmail.com
