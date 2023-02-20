# Installation

Install the following software:

* Git
* Python 3.6 or better
  * Avoid using the Windows Store version
  * During the installation, don’t forget to have Python added to environment variables
  * Also make sure that pip is selected as optional feature
* Visual Studio Code
  * Windows users: during the installation, have it install the explorer context menu additions
  * Install the VSCode Markdown Preview Mermaid extension

## Checking Your Python Installation

It’s important to check that your Python installation works.
This can be slightly tricky, since the details depend on your OS.
There are two kinds of problems that can arise:

* Python cannot be found
* The wrong version of Python is found

Below are instructions that verify both at the same type.
The goal is that you get Python to tell you which version it is, and that this version is 3.6 or higher.
If you encounter problems, inform a lecturer.

**IMPORTANT**

A `$` in the beginning of a line means that you should input that line in a shell.
Do not write the `$` itself though, only what follows.
For example, `$ ls` means you should type `ls` followed by enter.

<details>
<summary>Windows Instructions</summary>
<br>
Make sure you're in the `00-setting-things-up` directory.
In a shell, write
<br>
<br>

```bash
$ py check-python-version.py
```

</details>

<details>
<summary>MacOS Instructions</summary>
<br>
Make sure you're in the `00-setting-things-up` directory.
In the terminal, write
<br>
<br>

```bash
$ python3 check-python-version.py
```

If this does not work, try
<br>
```bash
$ python check-python-version.py
```

</details>

<details>
<summary>Linux Instructions</summary>
<br>
Make sure you're in the `00-setting-things-up` directory.
In the shell, write
<br>

```bash
$ python3 check-python-version.py
```
If this does not work, try
<br>
```bash
$ python check-python-version.py
```

</details>

## Checking Your Pip Installation

Pip is Python’s package manager: it allows you to easily install extra Python packages.
Check if it works by trying out the commands below:

```bash
$ pip --version

$ pip3 --version
```

One of these should work and should output something mentioning Python 3.
If `pip` is not recognized, you will have to look up how to install it.

## Installing extra packages

This course relies on some packages that are not included in the default Python installation.
Here is how you install them:

```bash
$ pip install pytest pytest-timeout

# or, depending on your installation

$ pip3 install pytest pytest-timeout
```

## Checking the extra packages

Run the provided tests to see if pytest is installed correctly.

```bash
$ pytest

..                                   [100%]
2 passed in 0.01s
```