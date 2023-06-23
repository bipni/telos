# telos

My Python Framework (Learning Purpose)

## Installation

Follow these steps:

-   Install the latest version of Python3 Anaconda
-   Make sure anaconda is activated with `which python` (see if it's anaconda python)
-   Install `virtualenv` with `pip install virtualenv`

## Run telos

Create an env in `telos` folder called `ENV` -

```bash
$ virtualenv ./ENV
```

Activate the `ENV` -

```bash
$ . ./ENV/bin/activate
```

Install all the dependency from the requirements file -

```bash
$ pip install -r requirements.txt
```

Install `telos` -

```bash
$ pip install -e .
```

Run `telos` -

```bash
$ telos hello
```

You will get the following message -

```bash
Welcome to the telos World!!!
```

Congratulations... Your `telos` setup is perfectly working.

## Rules and Regulations

-   All the folders name should be single word and started with small letter.

```
src/telos/services
```

-   All the files name should follow the properties of `Pascal Case`.

```
SomeFile.py
```

-   All the class name should follow the properties of `Pascal Case`.

```python
class SomeClass:
    pass
```

-   All the functions name should follow the properties of `Snake Case` except Provider Functions (Provider Functions name should follow the properties of `Pascal Case`).

```python
def some_function:
    pass
```
