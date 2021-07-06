## Usage

Install dependencies

```
npm install
```
```
pip install pipenv
```
```
pip install pipenv
```
```
pipenv install
```
```
pipenv shell
```
```
nodemon server.js
```
# voice_to_signLanguage
Voice to Sign Language Conversion
<!--lint disable no-literal-urls-->
<p align="center">
  <a href="https://nodejs.org/">
    <img
      alt="Node.js"
      src="https://nodejs.org/static/images/logo-light.svg"
      width="400"
    />
  </a>
  <br>
</p>  
Pipenv: Python Development Workflow for Humans
==============================================

[![image](https://img.shields.io/pypi/v/pipenv.svg)](https://python.org/pypi/pipenv)
[![image](https://img.shields.io/pypi/l/pipenv.svg)](https://python.org/pypi/pipenv)
[![Azure Pipelines Build Status](https://dev.azure.com/pypa/pipenv/_apis/build/status/Pipenv%20CI?branchName=master)](https://dev.azure.com/pypa/pipenv/_build/latest?definitionId=16&branchName=master)
[![image](https://img.shields.io/pypi/pyversions/pipenv.svg)](https://python.org/pypi/pipenv)


------------------------------------------------------------------------ 

**Pipenv** is a tool that aims to bring the best of all packaging worlds
(bundler, composer, npm, cargo, yarn, etc.) to the Python world.
*Windows is a first-class citizen, in our world.*

It automatically creates and manages a virtualenv for your projects, as
well as adds/removes packages from your `Pipfile` as you
install/uninstall packages. It also generates the ever-important
`Pipfile.lock`, which is used to produce deterministic builds.

![GIF demonstrating Pipenv's usage](https://gist.githubusercontent.com/jlusk/855d611bbcfa2b159839db73d07f6ce9/raw/7f5743401809f7e630ee8ff458faa980e19924a0/pipenv.gif)

The problems that Pipenv seeks to solve are multi-faceted:

-   You no longer need to use `pip` and `virtualenv` separately. They
    work together.
-   Managing a `requirements.txt` file [can be
    problematic](https://kennethreitz.org/essays/2016/02/25/a-better-pip-workflow),
    so Pipenv uses the upcoming `Pipfile` and `Pipfile.lock` instead,
    which is superior for basic use cases.
-   Hashes are used everywhere, always. Security. Automatically expose
    security vulnerabilities.
-   Give you insight into your dependency graph (e.g. `$ pipenv graph`).
-   Streamline development workflow by loading `.env` files.

You can quickly play with Pipenv right in your browser:
