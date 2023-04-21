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

### Running this app
```sh
streamlit run Welcome.py
```

or checkout the [deployed app](https://streamlit-workshop.victortuekam.com).

![streamlit-workshop](https://github.com/ifo-institute/ifohack2023/blob/web-workshop/Workshops/Streamlit%20Basics%20and%20VSCode/images/qrcode.png | width=100)
