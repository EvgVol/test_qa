# test_qa

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository using:
```
git clone https://github.com/evgvol/test_qa.git
```
2. Navigate to the project directory using:
```
cd test_qa
```
3. Create of virtual environments by executing the command:
```
python -m venv venv
```
4. Run of virtual environments by executing the command:
```
. venv/Scripts/activate
```
5. Install the dependencies using the following command: 
```
pip install -r requirements.txt
```
6.  Start the project for Chrome using the following command:
```
pytest -v --tb=line --reruns 2 --browser_name=chrome ritm/tests/test_check_box.py
```
7.  Start the project for Firefox using the following command:
```
pytest -v --tb=line --reruns 2 --browser_name=firefox ritm/tests/test_check_box.py
```
