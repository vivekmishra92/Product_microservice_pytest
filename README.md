**Docker compose to run the products services all in one**

It runs a mongo db, product service and price engine after running the following command.

`docker-compose up`

##Test product microservice using pytest

Pre-requisite:
Run pytest from `test` directory

Follow below steps to run testcase to test different APIs of product.
1. Install packages 
`pip install -r requirements.txt`
   
2. Run pytest and generate html report
`pytest –html=report.html`