# Downnload and Train AI model in your local

## Setup
Fork and clone the repo in your system\
Open the folder and setup a Python Virutal Environment\
Make sure that python is installed in your system

```
python --version
pip --version
python -m venv .venv
```
Activate the Virtual Environment

```
source .venv/Scripts/activate
```
## Download the AI model in your local
CodeLlama-7b-Instruct-hf is downloaded here. You can download any open source model from hugging face

```
python download_model.py
```
Model will be available in ./models folder

## Train the model with the dataset
Codellama accepts data in the form of txt file. So convert the file that you have into txt using

```
python convert-data.py
```
Converted dataset will be available in ./dataset/

To train the model with the dataset, run

```
python train-codellama.py
```
Trained model will be available in ./codellama-solidity-finetune (specify your output_dir in the script)
