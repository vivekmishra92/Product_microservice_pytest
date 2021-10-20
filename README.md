**Docker compose to run the products services all in one**

It runs a mongo db, product service and price engine after running the following command.

`docker-compose up`

## Test product microservice using pytest

Pre-requisite:
Run pytest from `test` directory

Follow below steps to run testcase to test different APIs of product.
1. Install packages 
`pip install -r requirements.txt`
   
2. Run pytest and generate html report
`pytest –html=report.html`


##### File Description:

+ `conftest.py`: include all the fixture of the pytest
+ `data.py`: contains test data which will be used during testing
+ `helper.py`: contains the function for the api call which are required during testing
+ `test_product_apis.py`: conatins all the test cases for the POST, GET, PUT and DELETE APIs
