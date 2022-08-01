# project.fast.ai
This code base is a collection of little utility modules that I'm developing while taking [the course.fast.ai MOOC](https://course.fast.ai/).

## Table of contents
* [Photo Download URL Finder](photo_download_url_finder/README.md)

## Install
For the most part, how to install the code is project-specific, so see project-specific README files.

## Run
For the most part, how to run the code is project-specific, so see project-specific README files.

* Run the auto formatter.
  ```console
  poetry run pre-commit run --all-files
  ```
  * For more usage instructions, see [the pre-commit documentation](https://pre-commit.com/).

## Debug
* Documentation [here](https://docs.python.org/3/library/pdb.html).
* Set a breakpoint with `import pdb; pdb.set_trace()`.
  * If you're using vim with [a project-specific .vimrc](https://andrew.stwrt.ca/posts/project-specific-vimrc/), you can type this with `<leader>db`.
* Show where you are with `list`.
* Continue with `continue`.
* Quit with `quit`.

## Add a new python package
This app makes use of [`poetry`](https://python-poetry.org/) to manage packages. See docs there for how to add packages.
