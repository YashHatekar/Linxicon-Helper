# Linxicon-Helper
Using Llama to solve Linxicon Daily
Linxicon-Helper is a Python script that uses Selenium and Llama3-based LLM using Ollama to solve the Linxicon game in the shortest way possible. The script automatically opens the game, configures the LLM, and uses its output to solve the game.

## Prerequisites

- Python 3.x
- Selenium
- WebDriver Manager for Edge
- Ollama

## Installation
**Clone the repository:**
   ```
   bash
   git clone https://github.com/YashHatekar/Linxicon-Helper.git
   cd Linxicon-Helper
   pip install selenium webdriver-manager ollama
```
## Configure the LLM with Ollama:
```
modelfile = '''
  FROM llama3
  SYSTEM Linxicon is a game that teaches you what words mean! Your goal is to connect two random words by creating a chain of new words that bridge the gap in their meanings. To join the 2 corner words using as few words as necessary. Words can be joined to each other by adding new words to the graph that are similar in meaning to words that are already there. For an extra challenge, see if you can get your average connection between each word as high as possible. If a word doesn't form any links, it's because that the word is too dissimilar to the words that are already in the graph. You can see how similar words are to each other by clicking on the word and looking at the information displayed in the sidebar. For a link to form between 2 words, they must have a similarity of more than 38%. There can only be a maxiumum of 50 words on the board before the game ends, even if the corner words haven't been connected. Linxicon determines how similar words are to each other by entering the words in a machine learning model (Sentence Transformer SBERT) that returns a score which indicates how similar words are to each other. You are an expert at Linxicon. Answer the query in a single word which is most relevant in creating a bridge. Try to keep the length of the bridge as small as possible.'''
```
```
ollama.create(model='linxicon-v2', modelfile=modelfile)
```
  <br>
This code uses Llama3 as the base model

## Usage:
  1. For the first run uncomment the modelfile and LLM configuration line of code from lines 38 to 42. This can be commented after the first run or it will try to recreate the same llm.
  2. Change to your ideal browser by changing the selenium imports and driver initialization.
  3. run the code using python /path/linx_help.py
  4. Do not interfere with the newly opened browser window since its code-controlled and manual intervention might lead to unexpected crashes.
  5. On a successful solution the shortest path and the number of words used stats will be printed in the terminal.
