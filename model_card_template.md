
# Model Card

## Model Details
The model is a Random Forest Classifier trained on census data to predict whether an individual's income is above or below $50,000 per year based on various demographic and socioeconomic features. Created by: Jared Plaisance Date Created: 04/07/2024

## Intended Use
The intended use of this model is to assist in predicting income levels based on demographic and socioeconomic features. It can be used by individuals, organizations, or policymakers for tasks such as targeted marketing, resource allocation, or policy planning.

## Training Data
The model was trained on a dataset obtained from the UCI Machine Learning Repository using one-hot encoding, containing census data from the United States. The dataset includes features such as age, education level, occupation, and native country, with the target variable being the individual's income level categorized as ">50K" or "<=50K".

## Evaluation Data
The model's performance was evaluated using a separate portion of the same dataset that was not used during training. This evaluation dataset contains similar demographic and socioeconomic features as the training data.

## Metrics
The following metrics were used to evaluate the model's performance:
Precision: The proportion of true positive predictions among all positive predictions.
Recall: The proportion of true positive predictions among all actual positive instances.
F1 Score: The harmonic mean of precision and recall, providing a balance between the two metrics.

The model achieved the following performance on these metrics:
Precision: 0.7419
Recall: 0.6384
F1 Score: 0.6863

## Ethical Considerations
Fairness: Care should be taken to ensure that the model does not disproportionately disadvantage certain demographic groups.
Privacy: As the model deals with sensitive demographic information, steps should be taken to protect individual privacy and prevent unauthorized access to the data.
Transparency: Users should be provided with information about how the model works, what data it uses, and how predictions are made.

## Caveats and Recommendations
The model's performance may vary depending on the quality and representativeness of the training data.
It is important to consider the limitations of using census data for predicting income, as it may not capture all relevant factors influencing an individual's earnings.
Regular monitoring and updating of the model may be necessary to maintain its accuracy and relevance over time.