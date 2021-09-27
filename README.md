# Bink Task
Here is my attempt at the technical task for Bink.


### How to run the task
To run the task you need:
1. Set up a virtual environment (venv preferably)
2. Activate the virtual environment
3. Install all requirements from the requirements.txt file
4. Run `main.py` and provide the required argument `-t` or `--task` id, which will start any of the four tasks as per the requirements. 

e.g `python main.py -t 1` - Starts task 1 

```
1.	Read in the attached file
    a.	Produce a list sorted by “Current Rent” in ascending order
    b.	Obtain the first 5 items from the resultant list and output to the console
```

### Running the tests
To run the tests please have pytest installed (included in the requirements.txt) and run in the console on the root of the project - `python -m pytest tests`


### Coverage run
```
Name              Stmts   Miss  Cover
-------------------------------------
common/utils.py      28      0   100%
main.py              47     34    28%
-------------------------------------
TOTAL                75     34    55%
```
> Unfortunately, I couldn't get coverage to run inside the subprocesses, hence the lower coverage on main.py.


