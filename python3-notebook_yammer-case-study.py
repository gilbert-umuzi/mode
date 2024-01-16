# Python Notebook - Yammer Case Study

import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Find the right Mode data set to work with
datasets

a = datasets['z A/B test (2) a']

a.columns

control_group_data = a[a['experiment_group'] == 'control_group']['metric']

control_group_data.describe()

# Variance
control_group_data.var()

# Create a histogram
control_group_data.hist()

# Create a boxplot
plt.boxplot(control_group_data)
plt.title('Boxplot of Metric for Control Group')
plt.ylabel('Metric')
plt.show()

# Remove outliers (1.5 * IQR)

# Calculate Q1 and Q3
Q1 = control_group_data.quantile(0.25)
Q3 = control_group_data.quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
filtered_control_group_data = control_group_data[(control_group_data >= lower_bound) & (control_group_data <= upper_bound)]


filtered_control_group_data.describe()

test_group_data = a[a['experiment_group'] == 'test_group']['metric']

test_group_data.describe()

# Create a histogram
test_group_data.hist()

# Create a boxplot
plt.boxplot(test_group_data)
plt.title('Boxplot of Metric for Test Group')
plt.ylabel('Metric')
plt.show()

# Remove outliers (1.5 * IQR)

# Calculate Q1 and Q3
Q1 = test_group_data.quantile(0.25)
Q3 = test_group_data.quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
filtered_test_group_data = test_group_data[(test_group_data >= lower_bound) & (test_group_data <= upper_bound)]


filtered_test_group_data.describe()

a.columns

# Variance
test_group_data.var()

# Plot age of users by group

def plot_data(data):
    # Manually define a color map for the groups
    color_map = {'test_group': 'blue', 'control_group': 'red'}
    
    # Create the scatter plot using the defined color map
    sns.scatterplot(x='age', y='metric', hue='experiment_group', data=data, palette=color_map)

    # Calculate the mean 'metric' for each 'experiment_group', plot a line, and add a label
    for group in data['experiment_group'].unique():
        mean_value = data[data['experiment_group'] == group]['metric'].mean()
        plt.axhline(y=mean_value, color=color_map[group], linestyle='--', alpha=0.7)
        
        # Adjust the position of the text label outside the plot area
        plt.text(data['age'].max() * 1.05, mean_value, f'{round(mean_value, 2)}', va='center', color=color_map[group])

    # Adjust the legend position outside the plot
    plt.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adding labels and title
    plt.xlabel('Days Since Activation')
    plt.ylabel('Posts')
    plt.title('Age of Users by Group')
    plt.ylim(top=10)

    # Display the plot
    plt.show()


plot_data(a)

# Filter out newer users (all control_group) by removing age_buckets 1,2,3,4
a_filtered = a[~a['age_bucket'].isin([1, 2, 3, 4])]

plot_data(a_filtered)

# Perform the two-tailed t-test
t_stat, p_value = stats.ttest_ind(test_group_data, control_group_data)

# Print the results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Perform the two-tailed t-test
t_stat, p_value = stats.ttest_ind(filtered_test_group_data, filtered_control_group_data)

# Print the results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

a_filtered_test = a_filtered[a_filtered['experiment_group'] == 'test_group']['metric']
a_filtered_control = a_filtered[a_filtered['experiment_group'] == 'control_group']['metric']

# Perform the two-tailed t-test on a_filtered
t_stat, p_value = stats.ttest_ind(a_filtered_test, a_filtered_control)

# Print the results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

ex = datasets['z A/B test (1) ex']

ex.describe()

# Check for duplicates - Are there any users in both Test and Control groups?

ex['user_id'].duplicated().any()

a = datasets['z A/B test (2) a']

a.info()

# Check that users were activated before the experiment started
a[a['treatment_start']>a['activated_at']].count()

a[a['treatment_start']>a['activated_at']].head()

[a['treatment_start']<a['activated_at']].count()

a[a['treatment_start']==a['activated_at']].count()

# New users in control group
a[(a['treatment_start']==a['activated_at'])&(a['experiment_group']=='control_group')].info()

# New users in test group
a[(a['treatment_start']==a['activated_at'])&(a['experiment_group']=='test_group')].info()

