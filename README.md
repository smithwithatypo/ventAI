# Vent AI

Vent to an AI that knows your background and adjusts its tone to your preferences.  Small project to play with Langchain.

## Installation

```bash
$ pip install -r requirements.txt
```

## How to Use
1. rename `.env.sample` to `.env`
    - update "ANTHROPIC_API_KEY" to your own Anthropic API key
1. in the data directory, rename `me.sample.py` to `me.py`
    - update "me" with your own data
    - modify the AI demeanor scripts if you want to
    - update your preferences at the bottom of me.py
1. update your user_text in `main.py`
1. run in terminal with `$ python main.py`
1. see your output in `output.txt`


## License

MIT License