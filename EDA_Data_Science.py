#!/usr/bin/env python
# coding: utf-8

# # Univariate Analysis

# # Understanding Univariate Analysis: A Comprehensive Guide
# 
# Univariate analysis serves as a cornerstone in the realm of statistics, providing a foundational framework for exploring and comprehending individual variables within a dataset. In this comprehensive guide, we delve into the essence of univariate analysis, elucidating its significance, methodologies, and applications.
# 
# ## What is Univariate Analysis?
# 
# Univariate analysis is a statistical technique focused on scrutinizing a single variable at a time within a dataset. Unlike multivariate analysis, which examines relationships between multiple variables, univariate analysis isolates one variable to unravel its intrinsic characteristics, including distribution, central tendency, and variability.
# 
# ## Methods and Techniques
# 
# Univariate analysis employs a plethora of methods and techniques to dissect the properties of a single variable:
# 
# 1. **Measures of Central Tendency**: Measures such as the mean, median, and mode provide insights into the typical or central value of the variable.
# 
# 2. **Measures of Dispersion**: Techniques like range, variance, and standard deviation unveil the spread or variability of the variable's values.
# 
# 3. **Frequency Distributions**: Graphical representations like histograms and frequency polygons depict the distribution of values across different intervals or categories.
# 
# 4. **Box Plots**: These visualizations offer a succinct summary of the variable's distribution, showcasing key statistical metrics like the median, quartiles, and outliers.
# 
# 5. **Summary Statistics**: Concise numerical summaries encapsulate essential characteristics of the variable, facilitating quick interpretation and comparison.
# 
# ## Significance and Applications
# 
# Univariate analysis plays a pivotal role across various domains and disciplines:
# 
# 1. **Exploratory Data Analysis (EDA)**: As a precursor to more intricate analyses, univariate analysis unveils initial insights into the dataset's structure and characteristics.
# 
# 2. **Descriptive Statistics**: By delineating the fundamental attributes of individual variables, univariate analysis forms the bedrock of descriptive statistics, aiding in data summarization and interpretation.
# 
# 3. **Hypothesis Testing**: Univariate analysis serves as a crucial component in hypothesis testing, enabling researchers to evaluate the significance of observed differences or relationships within a single variable.
# 
# 4. **Predictive Modeling**: In predictive analytics, univariate analysis aids in feature selection and variable screening, identifying predictors that significantly influence the target variable.
# 
# 5. **Quality Control and Process Improvement**: By scrutinizing key performance indicators and process variables, univariate analysis facilitates quality control initiatives and process optimization in various industries.
# 
# ## Conclusion
# 
# Univariate analysis stands as an indispensable tool in the statistical toolkit, offering a comprehensive lens through which to scrutinize and comprehend individual variables within a dataset. By unraveling the distribution, central tendency, and variability of each variable, univariate analysis not only fosters a deeper understanding of the data but also lays the groundwork for more sophisticated analyses and insights. Whether in research, business, or academia, the principles of univariate analysis serve as a cornerstone for data-driven decision-making and empirical inquiry.
# 

# ## Types of Data
# 
# In the context of data analysis, there are several types of data, commonly categorized as follows:
# 
# 1. **Numerical Data:**
#    - *Continuous Data:* Data that can take any value within a range. Examples include height, weight, temperature.
#    - *Discrete Data:* Data that can only take specific, distinct values. Examples include counts of items, such as the number of students in a class.
# 
# 2. **Categorical Data:**
#    - *Nominal Data:* Data that represent categories with no inherent order or ranking. Examples include gender, color, or type of car.
#    - *Ordinal Data:* Data that represent categories with a specific order or ranking. Examples include ratings (e.g., "low," "medium," "high") or educational levels (e.g., "elementary," "high school," "college").
# 
# 3. **Time Series Data:**
#    - Data collected over time intervals. Examples include stock prices, temperature readings over days, or monthly sales figures.
# 
# 4. **Text Data:**
#    - Unstructured data consisting of text. Examples include emails, social media posts, or documents.
# 
# 5. **Spatial Data:**
#    - Data associated with geographic locations. Examples include GPS coordinates, maps, or satellite images.
# 
# Understanding the type of data you're working with is crucial as it dictates the appropriate analysis techniques and visualizations to use.
# 

# ### Univariate Techniques for Numerical Data:
# 
# 1. **Continuous Data:**
#    - *Measures of Central Tendency:* Mean, Median, Mode
#    - *Measures of Dispersion:* Range, Variance, Standard Deviation
#    - *Histograms:* Visualize the distribution of continuous data.
#    - *Box Plots:* Summarize the distribution and identify outliers.
#    - *Kernel Density Estimation (KDE):* Estimate the probability density function of continuous data.
# 
# 2. **Discrete Data:**
#    - *Frequency Tables:* Count the occurrences of each discrete value.
#    - *Bar Charts:* Visualize the frequency distribution of discrete values.
#    - *Pie Charts:* Show the proportion of each category within the discrete data.
# 
# ### Univariate Techniques for Categorical Data:
# 
# 1. **Nominal Data:**
#    - *Frequency Tables:* Count the occurrences of each category.
#    - *Bar Charts:* Visualize the frequency distribution of nominal categories.
#    - *Pie Charts:* Show the proportion of each category within the nominal data.
#    - *Mode:* Identify the most frequent category.
# 
# 2. **Ordinal Data:**
#    - *Frequency Tables:* Count the occurrences of each ordinal category.
#    - *Bar Charts:* Visualize the frequency distribution of ordinal categories.
#    - *Pie Charts:* Show the proportion of each category within the ordinal data.
#    - *Median:* Identify the central value of the ordered categories.
# 
# ### Examples:
# 
# - **Numerical Data:**
#   - Continuous: Analyzing the distribution of heights in a population using histograms.
#   - Discrete: Examining the frequency distribution of the number of children in families using bar charts.
# 
# - **Categorical Data:**
#   - Nominal: Investigating the distribution of car colors in a parking lot using a bar chart.
#   - Ordinal: Exploring the frequency distribution of satisfaction ratings (e.g., "low," "medium," "high") using a bar chart.
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Data Science\Dataset\titanic_data.csv")


# In[3]:


df.head()


# # Count Plot

# In[4]:


import seaborn as sns


# In[5]:


df['Survived'].value_counts()


# In[6]:


sns.countplot(df,x='Survived')


# In[7]:


sns.countplot(df,x='Pclass')


# In[8]:


sns.countplot(df,x='Sex')


# # Pie Chart

# In[9]:


df['Survived'].value_counts().plot(kind='pie',autopct='%.2f')


# In[10]:


df['Sex'].value_counts().plot(kind='pie',autopct='%.2f')


# In[11]:


df['Pclass'].value_counts().plot(kind='pie',autopct='%.2f')


# In[12]:


sns.displot(df['Age'],kind='kde')


# In[13]:


sns.distplot(df['Age'])


# In[14]:


sns.boxplot(df['Age'])


# In[15]:


df.info()


# In[16]:


df.describe()


# In[17]:


df.describe(include=object)


# In[21]:


tips = sns.load_dataset('tips')


# In[22]:


flight= sns.load_dataset('flights')


# In[23]:


iris= sns.load_dataset('iris')


# # Sactter Plot

# # ### Common Plot Types Based on Data Type Combinations
# 
# 1. **Numerical vs. Numerical:**
#    - Scatter plot: to visualize the relationship between two numerical variables.
#    - Line plot: to show trends over time or continuous data points.
# 
# 2. **Categorical vs. Categorical:**
#    - Bar plot: to compare the frequencies of different categories.
#    - Heatmap: to visualize the frequency of occurrence or relationship between categories.
# 
# 3. **Numerical vs. Categorical:**
#    - Box plot: to compare the distribution of a numerical variable across different categories.
#    - Violin plot: similar to box plot but provides a more detailed view of the distribution.
#    - Swarm plot: to show the distribution of numerical data points within each category.
# 
# 4. **Time Series Data:**
#    - Line plot: to visualize trends over time.
#    - Area plot: to show cumulative trends or stacked time series data.
#    - Heatmap: to visualize patterns or correlations over time.
# 
# 5. **Text Data:**
#    - Word cloud: to visualize the frequency of words in a text document.
#    - Bar plot: to show the frequency of occurrence of different categories within text data.
#    - Histogram: to display the distribution of text 
# 

# In[25]:


sns.scatterplot(x=tips['total_bill'],y=tips['tip'])


# In[26]:


sns.scatterplot(x=tips['total_bill'],y=tips['tip'],hue=tips['sex'])


# In[27]:


sns.scatterplot(x=tips['total_bill'],y=tips['tip'],hue=tips['sex'],style=tips['smoker'])


# In[29]:


sns.scatterplot(x=tips['total_bill'],y=tips['tip'],hue=tips['sex'],style=tips['smoker'],size=tips['size'])


# In[31]:


sns.barplot(x=df['Pclass'],y=df['Age'])


# In[32]:


sns.barplot(x=df['Pclass'],y=df['Age'],hue=df['Sex'])


# In[34]:


sns.boxplot(y=df['Age'],x=df['Sex'])


# In[39]:


sns.distplot(df[df['Survived']==0]['Age'],hist=False)
sns.distplot(df[df['Survived']==1]['Age'],hist=False)


# In[46]:


df.info()


# In[55]:


tips.info()


# In[63]:


df.groupby('Embarked').mean(numeric_only=True)['Age'].plot(kind='bar')


# In[64]:


sns.pairplot(df)


# In[66]:


sns.heatmap(pd.crosstab(df['Sex'],df['Embarked']))


# In[67]:


sns.clustermap(pd.crosstab(df['Sex'],df['Embarked']))

