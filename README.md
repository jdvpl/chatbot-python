## Initial Setup:

This repo currently contains the starter files.

Clone repo and create a virtual environment

```
$ cd chatbot
$ python app.py
```

Install dependencies

```
pip install Flask torch torchvision nltk
```

Install nltk package to tests

```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```

Modify `intents.json` with different intents and responses for your Chatbot

Run

```
$ (venv) python train.py
```

This will dump data.pth file. And then run
the following command to test it in the console.

```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py` and `app.js`.
