# Semantic Similarity Analysis with SpaCy

## Overview

This project explores semantic similarities between words using the SpaCy library in Python. By leveraging pre-trained word embeddings from the `en_core_web_md` model, the script calculates and compares semantic similarities among a set of words provided as input. 

## Features

- Utilizes SpaCy library for natural language processing.
- Calculates semantic similarities between words using pre-trained word embeddings.
- Supports customization of input words for analysis.

## Usage

1. **Installation**:
   - Ensure you have Python installed on your system.
   - Install the SpaCy library and download the English model by running:
     ```bash
     pip install spacy
     python -m spacy download en_core_web_md
     ```

2. **Execution**:
   - Clone this repository or download the `semantic.py` file.
   - Open a terminal and navigate to the directory containing `semantic.py`.
   - Run the script using the following command:
     ```bash
     python semantic.py
     ```

3. **Customization**:
   - You can customize the input words for semantic analysis by modifying the `tokens` variable in the `semantic.py` script.

## Example Output

After executing the script, it will output the semantic similarity scores between each pair of words provided as input. For example:

