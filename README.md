# Canada Housing Prices

## Team Introduction

This project was successful due to active participation of following team members:

- Janaparan (Jay)
- Yixi (Grace) Gong
- Dmytro Malyk
- Phoebe Z Wei
- Yuriy Koshulap

## Project Overview

Our project aims to develop a machine learning model to predict housing prices in Canada by analyzing various economic factors, such as Consumer Price Index (CPI), unemployment rates, GDP rates, immigration dynamics, interest rates, and minimum wages. 

Until June 2024, interest rates, inflation rates, and immigration numbers have reached a 20-year maximum. Our team is particularly interested in exploring how these significant increases will affect housing prices across different regions.

Canada is in the housing crisis, federal and provincial governments are looking for ways how to build more homes as well as make them affordable. Thus, our team decided to explore different factors that are affecting housing prices accross Canada and its distinct regions. 

### Project Question

Can we predict housing prices across various regions in Canada using consumer price index, interes rates, unemployment rates, immigration data, and other variables through a machine learning model?

## Index

- [Delivery Approach](/README.md#delivery-approach)
- [Project Outline](/README.md#project-outline)
- [Data Sources](/README.md#data-sources)
- [Technologies Used](/README.md#technology-used)
- [Data Transformation](/README.md#data-transformation)
- [Machine Learning Model](/README.md#machine-learning-model)
  - [Feature Engineering](/README.md#feature-and-target-variables)
  - [Data Pre-Processing](/README.md#data-pre-processing)
- [Modeling Process](/README.md#modeling-process)
  - [Machine Learning Model - Multiple Linear Regression (MLR)](/README.md#machine-learning-model---multiple-linear-regression-mlr)
  - Random Forest Regressor
  - Neural Network
  - [Model Results](/README.md#models-and-results)
- Database
- Future Steps
- [Scalling to Production and Operationalization of the Models](/README.md#scalling-to-production-and-operationalization-of-the-models)
- [Appendix](/README.md#appendix)
  - [Sources](/README.md#sources-and-references-utilized-for-this-project-can-be-accessed-in)
  - [Videos](/README.md#links-to-individual-videos)

## Delivery Approach

Effective collaboration was achieved through:

- **Defined Roles**: Team members were assigned roles based on expertise in data cleaning, analysis, visualization, and project management.
- **Regular Meetings**: Scheduled meetings facilitated progress updates, decision-making, and feedback incorporation.
- **Shared Workspace**: Utilized GitHub for version control and Slack for real-time communication to streamline collaboration and documentation.
- **Documentation**: Maintained detailed records to track project progress, methodologies, and decisions throughout the project lifecycle.

![project board](/img/projectboard.png)

### Decision-Making Process

Decision-making was guided by:

- **Consensus-Based Approach**: Encouraged open discussions to gather input from all team members on critical decisions.
- **Voting**: Employed for resolving disagreements and making key project decisions when consensus was challenging.
- **Lead Roles**: Designated leads for specific project components to enhance accountability and streamline decision processes.
- **Feedback Loop**: Established mechanisms for continuous feedback to address concerns promptly and optimize project outcomes iteratively.


### Project Outline
![image](/img/projectoutline.png)

### Data Sources
- Housing Prices
- Housing Price Index
- Consumer Price Index
- Interest Rates
- Minimum Wage
- GDP
- Immigration Data

We will combine these datasets together to create one comprehensive view that can be used for the remainder of this analysis.

Datasets were chosen based on rigorous criteria:

- **Relevance**: Included variables pertinent to minimum wage and unemployment rates across Canadian provinces.
- **Completeness**: Ensured minimal missing values and comprehensive coverage over significant time periods.
- **Accuracy**: Sourced data from reliable authorities such as Statistics Canada.
- **Format**: Preferred formats were CSV and Excel for compatibility with statistical software.
- **Database**: SQLite

### Data Exploration
Our team started this project continuing working with housing prices and consumer price indes datasets. The other datasources listed above were slowly added. These data sources were cleaned by dropping or imputing null values, limiting the data range and dropping unnecessary columns. All of this data was filtered to be specific to Canada and limited to years between 2005 and 2024. 

## Technology Used

We used a variety of technologies, languages and libraries during the different stages of our project and you can see a comprehensive list of them here:

#### Data Transformation

- Python (pandas, Numpy) Jupyter Notebook, csv

#### Database

- SQLite, Microsoft Excel

#### Machine Learning Model

- Python (pandas, numpy, matplotlib, seaborn, sci-kit learn, tensorflow), Jupyter Notebook, csv file

## Machine Learning Model

To find an answer to our project question, we tested out three different machine learning algorithms to see which one works best:

- Multiple Linear Regression
- Random Forest Regression
- Neural Network Algorithm

### Feature and Target Variables

Based on our project question, our target/ dependent variable is:

- Housing Prices in Canada and various regions of the country

Feature/ Independent Variables are:
- Unemployment Rates
- GDP
- Consumer Price Index (Inflation)
- Bank of Canada Interest Rates
- Immigration (monthly data)
- Minimum Wages

### Data Pre-Processing
In addition to the transformation conducted and detailed above, additional pre-processing was performed prior to implementing a machine learning model:

- Import the libraries
- Import the final dataset as a csv file
- Check for missing values
- No encoding is necessary. All data in our dataset is numeric.
- Splitting the dataset into training and testing set
- Feature scaling in porder to minimize the variations in our dataset. 

### Correlation Analysis
![image](/img/correlation_matrix.png)
The correlation matrix provides some insights into the relationships between different variables in the dataset. Here are some key takeaways:

1. **Strong Positive Correlations:**

    - **Housing Price Indexes (HPI):** The various housing price indexes (e.g., Composite_HPI_SA, Single_Family_HPI_SA, etc.) are all highly correlated with each other, with correlation coefficients close to 1.0. This indicates that as one type of housing price increases, the others tend to increase as well.

    - **Benchmark Prices:** Similarly, the benchmark prices for different housing types (e.g., Composite_Benchmark_SA, Single_Family_Benchmark_SA) are also highly correlated with each other and with the corresponding HPI values.

    - **CPI (Consumer Price Index):** The All-items CPI shows a strong positive correlation with the housing prices and benchmarks, suggesting that as consumer prices rise, housing prices also tend to rise.

2. **Negative Correlations:**

    - **Interest Rate and Housing Prices:** The Interest Rate shows a weak to very weak negative correlation with the housing price indexes (correlations close to -0.01 to -0.05). This suggests that higher interest rates might slightly discourage housing prices, but the effect is not strong in your data.

    - **Unemployment Rate and Housing Prices:** The Unemployment Rate has a moderate negative correlation with housing prices (around -0.28 to -0.29), which suggests that higher unemployment rates tend to be associated with lower housing prices.

3. **Other Observations:**

    - **Immigration and Economic Activity:** The Immigration Num has a moderate positive correlation with various economic indicators, such as Active businesses, Opening businesses, and All-items CPI. This could indicate that higher immigration is associated with increased economic activity and possibly higher prices.

    - **Business Activity:** Active businesses, Opening businesses, and Closing businesses have varying correlations with other economic indicators Notably, Active businesses is negatively correlated with the Unemployment Rate, which makes sense as more active businesses often correspond to lower unemployment.

### Modeling Process
![image](/img/modeling_process.png)


### Machine Learning Model - Multiple Linear Regression (MLR)
A linear regression model is an appropriate choice for making numerical predictions, especially when there is linear relation between the features. In our case, since we have multiple features in our dataset, a multiple linear regression model is applicable. The Multiple linear regression algorithm, models the linear relationship between a single dependent continuous variable and more than one independent variables.

In the context of the linear regression model that we used for predicting house prices, the general formula for linear regression is:

$\hat{y}$ = $𝛽_0$ + $𝛽_1$ ⋅ $𝑥_1$ + $𝛽_2$ ⋅ $𝑥_2$ + ⋯ + $𝛽_𝑛$ ⋅ $𝑥_𝑛$

***Where:***

- $\hat{y}$ is the predicted value (e.g., the predicted house price).
- $𝛽_0$ is the intercept (also known as the bias term), which is the value of 𝑦^ when all input features $𝑥_1$,$𝑥_2$,…,$𝑥_𝑛$​  are 0.
- $𝛽_1$, $𝛽_2$,…,$𝛽_𝑛$ are the coefficients (weights) for the corresponding input eatures $𝑥_1$,$𝑥_2$,…,$𝑥_𝑛$.
- $𝑥_1$,$𝑥_2$,…,$𝑥_𝑛$ are the input features (e.g., interest rate, unemployment rate, CPI, etc.).

**Applying the Formula to Our Model**

- Let's say we were predicting the ***Single_Family_Benchmark_SA*** using several input features like ***Interest Rate***, ***Unemployment Rate***, ***All-items CPI***, and others. The formula would look something like this:

  - Single_Family_Benchmark_SA (Single Family house price) = $𝛽_0$ + $𝛽_1$ ⋅ Interest Rate + $𝛽_2$ ⋅ Unemployment Rate + $𝛽_3$ ⋅ All-items CPI+ ⋯ + $𝛽_𝑛$ ⋅ $Feature_𝑛$

**Example with Specific Features**

- Suppose we only had three features: ***Interest Rate, Unemployment Rate, and All-items CPI***. The formula for our linear regression model would be:

  - ***Single_Family_Benchmark_SA = $β_0$​ + $β_1$​ ⋅Interest Rate + $β_2$​ ⋅ Unemployment Rate + $β_3$​ ⋅ All-items CPI***

- ***Interpretation:***

  - **$𝛽_0$ (Intercept):** This is the predicted Single_Family_Benchmark_SA when all the features are 0.

  - **$β_1$​ (Coefficient for Interest Rate):** This represents how much the Single_Family_Benchmark_SA is expected to change for a one-unit change in Interest Rate, holding all other features constant.

  - **$β_2$​ (Coefficient for Unemployment Rate):** This shows the expected change in Single_Family_Benchmark_SA for a one-unit change in Unemployment Rate, holding all other features constant.

  - **$β_3$ (Coefficient for All-items CPI):** This indicates the expected change in Single_Family_Benchmark_SA for a one-unit change in All-items CPI, holding all other features constant.

**How Coefficients Were Determined**

- The coefficients ($𝛽_0$,$𝛽_1$,…,$𝛽_𝑛$) were determined during the training of the linear regression model. The training process involves minimizing the loss function, typically the ***Mean Squared Error (MSE)***, which measures the difference between the predicted values and the actual values in the training data. The model finds the set of coefficients that best fits the training data.

- **Summary**

  - The formula for linear regression models the relationship between the target variable (house prices) and the input features by assigning a weight (coefficient) to each feature. These coefficients are learned from the training data, and they reflect the contribution of each feature to the predicted house price.

![image](/img/signle_houses_coefficients.png)

## Models and Results
![image](/img/apartment_prices.png)

### Multiple Linear Regression

- MSE (Mean Squared Error): 3903.93
- R² (Coefficient of Determination): 0.99999971
- Interpretation: The Multiple Linear Regression model achieves an exceptionally low MSE and an extraordinarily high R². This indicates that the model predicts the apartment benchmark values with outstanding accuracy, explaining nearly all of the variance in the target variable. This model is highly effective for this dataset.

### Random Forest Regressor

- MSE: 19,762,973.04
- R²: 0.99852134
- Interpretation: The Random Forest model has a significantly higher MSE compared to the linear regression model. This suggests potential overfitting or a misalignment with the dataset’s characteristics. Despite still explaining a high proportion of the variance, it is less effective than the linear regression model for this dataset.

### Decision Tree Regressor

- MSE: 30,244,042.55
- R²: 0.99773715
- Interpretation: The Decision Tree model also shows a high MSE, indicating possible overfitting or excessive model complexity. While it performs well, it is less effective compared to the linear regression model, as evidenced by its higher MSE and lower R².

### Neural Network

- MAE (Mean Absolute Error): 261,108.69
- Interpretation: The Neural Network model's MAE is higher compared to the MSE of the other models, suggesting larger typical prediction errors. This indicates that the neural network may require further tuning or may not be as well-suited for this prediction task.

### Conclusion

- The Multiple Linear Regression model is the most accurate and effective for predicting the Apartment Benchmark SA in this dataset, given its very low MSE and exceptionally high R². The Random Forest and Decision Tree models, although still performing well, exhibit higher MSE values, indicating potential overfitting. The Neural Network model, with the largest average errors, suggests that further optimization is needed for better performance.


## Scalling to Production and Operationalization of the Models

- The 1st project phase analyzed the data sources, set data pre-processing methodology, and built the baseline models. 
- The baseline models have been saved in .keras format to ensure re-usability, compatibility, extensibility, and portability. 

- As we have more than **60 datasets** by Canada's regions, we need to build a re-usable system that could help process all the data, predicting housing prices for each region. 

### Scalling to Production process

- Step 1: Load the Saved Model

![image](/img/load_models.png)

- Step 2: Prepare the New Dataset

![image](/img/load_new_data.png)

- Step 3: Make Predictions

![image](/img/predict.png)

- Step 4: Interpret the Predictions

![image](/img/convert_df.png)

- Additional Considerations:
  - Consistency: Ensure that the features in your new dataset match the features used to train the model. Any mismatch in columns will cause errors.
  - Scaling: Always apply the same scaler used during training to your new data. If the scaler was saved, load it and use it to transform the new data.

By following these steps, you can effectively use your saved neural network models to make predictions on new datasets, ensuring that your preprocessing steps remain consistent with the original training process.

### Automation

- Step 1: Create the Automation Function
- Step 2: Save and Load the Scaler
- Step 3: Running the Script
- [Automation Notebook](/src/scalling_to_production.ipynb)

#### Benefits of Automation:
- Reusability: This script can be reused for any new datasets with minimal changes.
- Consistency: Ensures that the preprocessing steps and predictions are consistent across different datasets.
- Efficiency: Saves time by automating the process, especially when working with multiple datasets.

### Appendix

- #### Sources and references utilized for this project can be accessed in:
  - [Data folder](./data/)
  - [Reports](./reports/)
  - [Source Code and Models](./src/)

- #### Links to individual videos**
  - [Janaparan (Jay)](https://)
  - [Yixi (Grace) Gong](https://)
  - [Dmytro Malyk](https://)
  - [Phoebe Z Wei](https://)
  - [Yuriy Koshulap](https://)


<details>
<summary>Original Requirements - cohort #3</summary>

## Description

The team project consists of two modules. Each module requires participants to apply the skills they have learned to date, and explore a dataset of their choosing. The first part of the team project involves creating a simple program with a database in order to analyze a dataset from an open source, such as Kaggle. In the second part of the team project, teams will come together again and apply the skills developed in each of the data science or machine learning foundations certificate streams. Teams will either create a data visualization or a machine learning model.



Participants will work in assigned teams of 4-5. 

#### Project Descriptions

* [First Team Project Description](./team_project_1.md)
* [Second Team Project Description](./team_project_2.md)

## Learning Outcomes
By the end of Team Project Module 1, participants will be able to:
* Resolve merge conflicts
* Describe common problems or challenges a team encounters when working collaboratively using Git and GitHub
* Create a program to analyze a dataset with contributions from multiple team members

By the end of Team Project Module 2, participants will be able to:
* Create a data visualization as a team
* Create a machine learning model as a team

### Contacts
**Questions can be submitted to the _#cohort-3-help_ channel on Slack**

* Technical Facilitator: 
  * **Kamilah Ebrahim**(she/her)
  kamilah.ebrahim@mail.utoronto.ca

* Learning Support Staff:

  * **Farzaneh Hashemi** (she/her )
  fhashemi.ma@gmail.com
  * **Tong Su** (she/her)
  tong.su@mail.utoronto.ca

### Delivery of Team Project Modules

Each Team Project module will include two live learning sessions and one case study presentation. During live learning sessions, facilitators will introduce the project, walk through relevant examples, and introduce various team skills that support project success. The remaining time will be used for teams to assemble and work on their projects, as well as get help from the facilitator or the learning support to troubleshoot any issues a team may be encountering. 

Work periods will also be used as opportunities for teams to collaborate and work together, while accessing learning support. 

### Schedule

|Day 1|Day 2|Day 3|Day 4|Day 5|
|-----|-----|-----|-----|-----|
|Live Learning Session |Live Learning Session|Case Study|Work Period|Work Period|

## Requirements
* Participants are expected to attend live learning sessions and the case study as part of the learning experience. Participants are encouraged to use the scheduled work period time to complete their projects.
* Participants are encouraged to ask questions and collaborate with others to enhance learning.
* Participants must have a computer and an internet connection to participate in online activities.
* Participants must not use generative AI such as ChatGPT to generate code to complete assignments. It should be used as a supportive tool to seek out answers to questions you may have.
* We expect participants to have completed the [onboarding repo](https://github.com/UofT-DSI/onboarding/tree/main/onboarding_documents).
* We encourage participants to default to having their camera on at all times, and turning the camera off only as needed. This will greatly enhance the learning experience for all participants and provides real-time feedback for the instructional team. 

### How to get help
![image](/steps-to-ask-for-help.png)

## Folder Structure

### Project 1
```markdown
|-- data
|---- processed
|---- raw
|---- sql
|-- reports
|-- src
|-- README.md
|-- .gitignore
```

### Project 2
```markdown
|-- data
|---- processed
|---- raw
|---- sql
|-- experiments
|-- models
|-- reports
|-- src
|-- README.md
|-- .gitignore
```

* **Data:** Contains the raw, processed and final data. For any data living in a database, make sure to export the tables out into the `sql` folder, so it can be used by anyone else.
* **Experiments:** A folder for experiments
* **Models:** A folder containing trained models or model predictions
* **Reports:** Generated HTML, PDF etc. of your report
* **src:** Project source code
* README: This file!
* .gitignore: Files to exclude from this folder, specified by the Technical Facilitator

</details>
