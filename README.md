# committed
GitHub stats and motivation

### Setup

Install Python3

```
brew install python3
```

Use `virtualenvwrapper`, but point it at the path to your Python3 install

```
PYTHON_3_PATH=$(which python3)   # assign the result of "which python" to a shell variable
mkvirtualenv --python=$PYTHON_3_PATH committed  # use this variable when creating the env
```

You can now work on the repo

```
workon committed
```

Once you've activated the virtual environment, install the packages.

```
pip install -r requirements.txt
```

