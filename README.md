## Task

These files are intended to run on Debian/Ubuntu based systems.

### Prerequisites

These can be installed by launching the prepare.sh script
```
git clone https://github.com/geris1337/task.git
cd task
chmod +x prepare.sh
./prepare.sh
```
## Running the tests

To launch task1.py and task3.py execute like this
```
python3 task1.py
python3 task3.py
```

To launch test_task4.py with pytest
```
python3 -m pytest -v -s
```
