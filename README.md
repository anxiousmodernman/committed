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

### Front End

Here are the steps to get the front end build to work. Gulp is our build tool, Browserify is
a library that bundles all JavaScript files into one.

First, make sure you have node available to your shell

```
node -v
```

If you don't see a version of node printed to the console, try activating it with nvm, the
nice version manager for node.

```
nvm use node
```

If that doesn't work, install nvm and use nvm to get the latest stable release of node.

Next, install the JavaScript dependendies.

```
npm install
```

Once that's done, execute the Gulp `build` task, and confirm that a bundled javascript file
ends up in a `./static/public/js`. The folder might not exist yet.

```
gulp build
```

If that works, use the default gulp task to watch the front end files for changes and 
rebuild if any changes occur. You'll probably want to do this in its own terminal.

```
gulp
```

Hooray, JavaScript!


