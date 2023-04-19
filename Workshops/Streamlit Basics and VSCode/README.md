## Web Workshop
- by Victor Tuekam

### Python Setup

To setup the programming environment you'd need to install the packages in the `requirements.txt` file.

I would suggest using `conda` to create an environment and install the packages with:
```
conda create -n workshop pip python

# activate
conda activate workshop

pip install -r requirements.txt
```

Alternatively run (if you don't have conda): `pip install -r requirements.txt`

#### The App

We will use an NLP model to showcase streamlit, so you'd be required to download this model and cache it.
- Create a Python file, say, `app.py` and paste the following code.

```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")
```
- Then run the program with: `python app.py`

### Running this app
```sh
streamlit run Welcome.py
```
