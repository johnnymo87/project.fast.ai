# Photo Sandbox
I want to use my own photos for deep learning projects, as that will make the material more engaging for me. After some tinkering, I've arrived at the following approach.

I use google to store my photos, and they offer [a REST API](https://developers.google.com/photos/library/guides/get-started) to access them programmatically. I'm using the [`gphotospy`](https://pypi.org/project/gphotospy/) package to wrap this API. It has a pretty handy tutorial [here](https://github.com/davidedelpapa/gphotospy/wiki/tut_02) that outlines all of its capacities.

The fast.ai library has a [`download_images`](https://docs.fast.ai/vision.utils.html#download_images) which takes a list of URLs. And `gphotospy` has a way to look up URLs for my photos. These URLs are public, and they expire after one hour. So In my deep learning experiments, I intend to somehow pass these URLs to `download_images`.

To do my deep learning experiments, I am using Jupyter notebooks (in Kaggle), as the course recommends. But I can't run this app's code there because this app needs to briefly run a server to handle the callback in the OAuth handshake with google when I authenticate with their API. Notebooks are a bad fit for this because they don't have a public IP address that I can direct this callback to. (Also for this reason docker -- which I nearly always use -- is a bad fit because servers in docker need to bind to 0.0.0.0 to be callable, and the google auth library I'm using [doesn't currently support that](https://github.com/googleapis/google-auth-library-python-oauthlib/issues/201).)

## Install
Since I can't use docker for this app, I use these steps to install this app on my local machine.

* Install pyenv.
  ```console
  bew install pyenv
  ```
* Install python 3.10.
  ```console
  pyenv install 3.10.5
  ```
* Set the local version of python to 3.10.
  ```console
  pyenv local 3.10.5
  eval "$(pyenv init -)"
  ```
* Install poetry.
  ```console
  curl -sSL https://install.python-poetry.org | python3 -
  ```
  * This will output instructions for how to add poetry to the PATH. Follow them.
* Install dependencies.
  ```console
  poetry install
  ```
* Create the file that contains the environment variables.
  ```console
  cp photo_sandbox/.env.example photo_sandbox/.env
  ```
* Set the OAuth2 credentials as environment variables in this `.env` file.

## Run
* Make sure that port `8080` is free, because this app needs to run a local server on this port to handle the OAuth2 callback.
* Run the `photo_sandbox` module.
  ```console
  poetry run python -m photo_sandbox
  ```
* Run the auto formatter.
  ```console
  poetry run pre-commit run --all-files
  ```
  * For more usage instructions, see [the pre-commit documentation](https://pre-commit.com/).
