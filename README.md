ECE4010 final project. We introduce many methods to do text classification (1-5 stars) on Amazon reviews data: using Vader, LSTM and CNN-LSTM hybrid model. 
Since the taste is different among people, we introduce off-by-one accuracy as one of the evaluation metric.
LSTM model performs well with 90% off-by-one accuracy, while CNN-LSTM has slightly less accuracy but outperforms on training and inference time.
When viewing a task as a regression problem, it gets lower accuracy but higher off-by-one accuracy, interestingly.

I implemented a web interface using Bootstrap, JS and Flask for the model if you want to have a try.

To run the model, simply follow these steps:

Clone the repo:
```
git clone https://github.com/huuquyen05/reviews-classifier.git
```
Go to the web app folder:
```
cd webapp
```
Create virtual environment and install required packages:
```
python -m venv .venv
source .venv/bin/activate (for Linux)
pip install -r requirements.txt
```
Run the server with:
```
python app.py
```
![alt text](<web screenshot.png>)
Data source: https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews
