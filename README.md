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

## Server


