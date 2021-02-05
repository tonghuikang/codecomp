# Quora Programming Contest Setup Guide

```bash
conda create -n quora python=3.6.9 -y
conda activate quora
pip install -r requirements.txt
```

`import getpass` is not allowed


The site listed `xgboost 1.7.1`, but the latest version is `1.3.3`. I assume the version number is `1.3.1`.


For lightGBM example, refer to https://www.kaggle.com/huikang/lightgbm-example
For pytorch CNN model, refer to https://www.kaggle.com/huikang/sml-hw2

Comment out all `matplotlib` code before submission.

The server runs these instructions, but I do not know what is going on here.

```bash
/usr/bin/python3 -m compileall -b .
/bin/mv example.pyc __main__.pyc
/usr/bin/zip -r example.zip __main__.pyc
/bin/mv example.zip example
```