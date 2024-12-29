# Serenity Health Systems Dashboard

## Problem Statement

This dashboard is designed to provide insights into patient experiences and operational efficiencies at Serenity Health Systems. By analyzing various aspects of patient feedback and hospital operations, the dashboard aims to:

1. Identify areas requiring improvement to enhance patient satisfaction.
2. Monitor operational metrics like average waiting time and response rates to ensure high-quality healthcare delivery.
3. Support data-driven decisions for resource optimization and workflow enhancements.

With 57% of patients providing neutral or dissatisfied feedback and 43% reporting satisfaction, the focus must be on improving the identified weak areas. Additionally, the average waiting time across departments is 15 minutes, requiring targeted actions to reduce delays and enhance service delivery.

### Steps Followed

Step 1: Load hospital data (in CSV format) into Power BI Desktop.

Step 2: Use Power Query Editor to examine data quality through column distribution, column quality, and column profiling.

Step 3: Address missing or null values, particularly in the "Response Time" column, where less than 1% of values are missing.

Step 4: Create visualizations using Power BI, including:
  - Patient satisfaction ratings.
  - Average waiting times and response times per department.
Step 5: Add slicers for key filters like department, patient type, and location.

Step 6: Include calculated columns and measures for deeper insights, such as patient demographics and service usage.

Step 7: Customize report visuals and themes for clarity and engagement. Include a company logo and tagline.

Step 8: Publish the dashboard to Power BI Service for accessibility.

Visualizations

1. Patient Feedback:

- Ratings for services like cleanliness, doctor-patient interaction, wait times, and facilities.
- Segregated by department and demographic.

2. Operational Metrics:

- Average waiting time per department.
- Response time for emergency cases.

3. Demographic Insights:

- Age and gender distribution of patients.
- Frequency of visits by new and returning patients.

4. Resource Utilization:

- Total patient count by department.
- Efficiency metrics like bed occupancy rates.

Data Calculations

Age Group Calculation:

Age Group =
if(hospital_data[Age] <= 25, "0-25",
if(hospital_data[Age] <= 50, "25-50",
if(hospital_data[Age] <= 75, "50-75", "75-100")))

Count of Patients:

Count of Patients = COUNT(hospital_data[Patient_ID])

Percentage of Patients:

% Patients = (DIVIDE([Count of Patients], TOTAL_COUNT) * 100)

Average Waiting Time:

Average Waiting Time = AVERAGE(hospital_data[Waiting Time])

Insights

1. Patient Satisfaction:

- 43% satisfied patients.
- 57% neutral or dissatisfied patients.
- Focus on reducing dissatisfaction through better service and engagement.

2. Operational Metrics:

- Average waiting time: 15 minutes.
- Emergency response time: 10 minutes.

3. Demographics:

- Majority of patients (52%) belong to the age group 25-50.
- 60% of patients are returning visitors.

4. Department Insights:

- Highest traffic in the OPD and Emergency departments.
- Low satisfaction scores in the billing and registration process.

Future Scope

- Integrate real-time monitoring for better decision-making.
- Implement predictive analytics for patient trends and resource allocation.
- Enhance user experience through automated reporting and dashboards.
