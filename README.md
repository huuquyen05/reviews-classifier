ECE4010 final project. We introduce many methods to do text classification (1-5 stars) on Amazon reviews data: using Vader, LSTM and CNN-LSTM hybrid model. 
Since the taste is different among people, we introduce off-by-one accuracy as one of the evaluation metric.
LSTM model performs well with 90% off-by-one accuracy, while CNN-LSTM has slightly less accuracy but outperforms on training and inference time.
When viewing a task as a regression problem, it gets lower accuracy but higher off-by-one accuracy, interestingly.

Data source: https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews
