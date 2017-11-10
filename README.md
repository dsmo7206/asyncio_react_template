# asyncio_react_template

This is an example of a "full-stack" web application for people like myself who have come from a traditional programming background (C++/Java/Python/Assembler/whatever) - people that are more comfortable with A* and O(n) than *polyfill*s and *browserify*s.

The project is clearly split into client and server. The client is ReactJS and the backend is Python 3.6 using the new asyncio await stuff.

## Client

The client consists of code written in React's JSX format - a hybrid of enhanced Javascript with inline HTML. This code needs to be transpiled into plain old Javascript before it can be safely run on any browser.

The JSX code itself does very little - just attaches an *App* (the name is arbitrary) instance into the document's *content* tag. The *App* class renders a string and an image.

The tool that does the transpilation is called *Babel*, and is written in [Node.js](https://nodejs.org) - a standalone runtime for Javascript that is popular among web developers for writing server code.

The tool that gathers together the source files, resolves imports etc is called *Webpack* - it's also written in Node.js.

Various other Javascript libraries need to be downloaded and this is done automatically via a tool called *npm* which is part of Node.js.

The *package.json* file defines all the dependencies the Javascript code requires. *npm* can then be used to install these, as described below.

### Prerequisites

* Install npm: `sudo apt install npm` (on Ubuntu)
* Download all the JS dependencies: `npm install` (reads *package.json* and creates a *node_modules* directory)

### Building

The *package.json* file has a *scripts* object that defines all command line scripts, which are executed as follows:

* Build production code: `npm run build`
* Build development code: `npm run dev-build`  
* Run tests: `npm run test` (currently does nothing and exits with error)
* Build dev code and watch: `npm build watch` (builds development code and monitors the js directory for changes to code, then automatically rebuilds)

Note that the builds will take all the JSX files and combine them into file **dist/bundle.js**, which is the only Javascript file referred to by index.html.

## Server

The server is a Python 3.6+ process that uses the [aiohttp](https://aiohttp.readthedocs.io/en/stable/) library which is based on the new(ish) [asyncio](https://docs.python.org/3/library/asyncio.html) library.

The server runs on a single thread with the asyncio-controlled event loop managing the work.

[pipenv](https://docs.pipenv.org/) is used for managing Python package dependencies - these are stored in the file *Pipfile*. This is a higher level wrapper around [pip](https://pypi.python.org/pypi/pip), which must also be installed.

### Prerequisites

* Python 3.6 must be installed - if it's not on your system, install via apt, yum etc.
* Install pip: `sudo apt-get install python-pip`
* Install pipenv: `pip install pipenv`
* Install Python packages for project: `pipenv install`

