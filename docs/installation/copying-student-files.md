---
layout: page
---

# Copying Student Files

This pages assumes the following:

* Your local repository (the one stored on your machine) is messed up and you have difficulties pushing/pulling/...
* Your remote repository on GitHub exists but is not fully up to date.
* You want to "reset" your local repository, but don't want to lose your `student.py` files.

If these assumptions hold, you can follow the instructions below.
If at any point you get error messages, it might be safer to ask for help.

## Cloning Anew

The goal of this section is to download your GitHub repository to your laptop in a new location.

First, you'll need to know what your GitHub repository's URL is.
You can find out as follows:

```bash
# Inside your broken local repository
$ git remote -v
```

This should output a few lines.
The URL to the right of `origin` should be the one you need.

Next, we will clone the remote repository.
You don't want to clone it inside an already existing repository, so you'll need a new location.
Say for example that this is your directory structure:

```text
school
   |
   +-- p2
       |
       +-- exercises     <-- broken repo
```

We suggest you put the fresh repository in the same parent directory as your current broken repository:

```text
school
   |
   +-- p2                     <-- open terminal here
       |
       +-- exercises
       |
       +-- new-exercises      <-- will be your new repository
```

Inside the `p2` directory (or the corresponding directory on your machine, whatever it may be called), run the following command:

```bash
$ git clone URL new-exercises
```

where you replace URL by your GitHub repository's URL.
If all goes well, a new directory `new-exercises` should have been created with all your files in it.

## Updating the New Repository

First, we should update `new-exercises` so that it has the latest version of the exercises.

```bash
# Inside new-exercises
$ git remote add upstream https://github.com/UCLL-PR2/exercises.git

$ git pull upstream main
```

## Copying the Script

Under `new-exercises/scripts` there should be a file named `generate-copy-script.py`.
Copy this file to the parent directory of both repositories.
In our example this is `p2`.

```text
school
   |
   +-- p2                     <-- copy script here
       |
       +-- exercises
       |
       +-- new-exercises
```

Next, in your terminal, go to `p2`.
Now we will run the script.
This is perfectly safe to do, as it performs no changes.

```bash
$ py generate-copy-script.py > copy-files.sh
```

If all goes well, this script ends with `Finished successfully`.
A new file `copy-files.sh` has been generated.

## Checking `copy-files.sh`

`copy-files.sh` is a shell script.
Open it in an editor such as Visual Studio Code.

It contains `cp` commands for each of your `student.py` files.
You can edit this file as you see fit.

Note that if the overwritten `student.py` is larger than the copied `student.py`, a comment will point it out and the `cp` will be commented out.
You might want to check out these files.

If you are happy with `copy-files.sh`, you can start the actual copying using

```bash
$ source copy-files.sh
```
