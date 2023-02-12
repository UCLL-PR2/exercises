# Python Exercise Repository

## About This Course

This course teaches you how to write small scripts that automate tasks, object oriented programming, webscraping,....
For this, we will rely on the Python programming language:

* It is one of the most used programming languages.
* It is one of the most user-friendly languages out there.
* A very large number of packages are available, which is essential for scripting.

The focus lies on *learning programming more efficiently*.
Your code have to produce correct results, it is your responsibility to check your work properly and if it is written efficiently.
The first series of exercises are accompanied by tests, but with the 'real deal' exercises, that won't be the case anymore.
You will have to split up the task at hand in smaller pieces, implement helper functions, check them, etc.

You are free to use all of the functionality Python provides.
It is not our goal to have you write complex algorithms.
So, please do not write your own `sum` function, use the built-in one.
You will see that Python has *a lot* of built-in functions for you to make use of.
Therefore, it is very important that you develop the habit of skimming through the documentation and looking up information online.

* [Installation](http://scripting.leone.ucll.be/docs/guides/installation.html)
* [Remaining Up-To-Date](http://scripting.leone.ucll.be/docs/guides/updating.html)
* [Usage](http://scripting.leone.ucll.be/docs/guides/usage.html)
* [Useful Shell Commands](http://scripting.leone.ucll.be/docs/guides/shell.html)
* [Planning](http://scripting.leone.ucll.be/docs/guides/planning.html)

## Installation

Install the following software:

- Git
- Python 3
    - Avoid using the Windows Store version
    - During the installation, don’t forget to have Python added to environment variables
    - Also make sure that pip is selected as optional feature
- Visual Studio Code
    - Windows users: during the installation, have it install the explorer context menu additions
    - Install the VSCode Markdown Preview Mermaid extension

## Checking Your Python Installation

It’s important to check that your Python installation works. This can be slightly tricky, since the details depend on your OS. There are two kinds of problems that can arise:

- Python cannot be found
- The wrong version of Python is found

Below are instructions that verify both at the same type. The goal is that you get Python to tell you which version it is, and that this version is 3.6 or higher. If you encounter problems, inform a lecturer.

### IMPORTANT
```
A $ in the beginning of a line means that you should input that line in a shell. Do not write the $ itself though, only what follows. For example, $ ls means you should enter ls.
```

<details>
<summary>Windows Instructions</summary>
<br>
In a shell, write
<br>

```
$ python --version
```
If this gives you trouble, try instead
<br>
```
$ py --version
```

</details>

<details>
<summary>MacOS Instructions</summary>
<br>
In the terminal, write
<br>

```
$ python --version
```
If this doesn’t work or prints out the wrong version, try
<br>
```
$ python3 --version
```

</details>

<details>
<summary>Linux Instructions</summary>
<br>
In the shell, write
<br>

```
$ python --version
```
If this doesn’t work or prints out the wrong version, try
<br>
```
$ python3 --version
```

</details>

## Checking Your Pip Installation

Pip is Python’s package manager: it allows you to easily install now components. Check if it works by trying out the commands below:
```
$ pip --version

$ pip3 --version
```

One of these should work and should output something mentioning Python 3. If pip is not recognized, you will have to look up how to install it.

## Course Related Material

Open a terminal in a directory where you wish to store your course-related files. Let’s first install the testing framework:

```
$ pip install git+https://github.com/UCLL-PR2/testing-framework.git
```

Test the installation of the scripting package by executing the following command. It should show the output below (or something similar to it, as long as it’s not an error message.)
```
$ scripting
usage: scripting [-h] {version,test} ...

positional arguments:
  {version,test}  sub-command help
    version       returns version
    test          runs tests in all subdirectories

optional arguments:
  -h, --help      show this help message and exit
```

Next, you need to get access to the course material. The simplest way is cloning, but you can also choose to create your own fork. This allows you to save your work on GitHub, so that you’re sure never to lose any of it.