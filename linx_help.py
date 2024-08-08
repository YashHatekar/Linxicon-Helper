#Linxicon Helper

# Steps -

# 1. Open linxicon.com in private Tab
# 2. Configure an llm using Ollama and explain it the game
# 3. Use llm output to solve Linxicon using the script in the shortest way possible.

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import ollama

# Set up Edge options for InPrivate mode
edge_options = Options()
edge_options.add_argument("--inprivate")

# Initialize the Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

# Open linxicon.com in a private tab
driver.get("https://linxicon.com")
time.sleep(2)
start_game_element = driver.find_element(By.NAME, 'enterGame')
start_game_element.click()
time.sleep(2)
guess_element = driver.find_element(By.NAME,'guess')

first_word = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[3]/div/div/p/span[1]').text
second_word = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[3]/div/div/p/span[2]').text

print(first_word)
print(second_word)

# modelfile = '''
# FROM llama3
# SYSTEM Linxicon is a game that teaches you what words mean! Your goal is to connect two random words by creating a chain of new words that bridge the gap in their meanings. To join the 2 corner words using as few words as necessary. Words can be joined to each other by adding new words to the graph that are similar in meaning to words that are already there. For an extra challenge, see if you can get your average connection between each word as high as possible. If a word doesn't form any links, it's because that the word is too dissimilar to the words that are already in the graph. You can see how similar words are to each other by clicking on the word and looking at the information displayed in the sidebar. For a link to form between 2 words, they must have a similarity of more than 38%. There can only be a maxiumum of 50 words on the board before the game ends, even if the corner words haven't been connected. Linxicon determines how similar words are to each other by entering the words in a machine learning model (Sentence Transformer SBERT) that returns a score which indicates how similar words are to each other. You are an expert at Linxicon. Answer the query in a single word which is most relevant in creating a bridge. Try to keep the length of the bridge as small as possible.
# '''
# ollama.create(model='linxicon-v2', modelfile=modelfile)
tries = 50
guesses = [first_word,second_word]
while tries > 0:
    print('Try '+str(50-tries)+': ')
    word_guess= ollama.generate(model='linxicon-v2',prompt='Provide just a word guess that connects the '+first_word+' and the '+second_word+'no explanation or anything is needed just provide a single word in response. The word should not be from this list of words: '+str(guesses))
    # print(type(word_guess['response']))
    if word_guess['response'] not in guesses:
        guesses.append(word_guess['response'])
        print(word_guess['response'])
        print('Guesses yet: ', guesses)
        # print('--------'*12)
        # print(str(word_guess['response']).split('\n')[0])
        try:
            guess_element.send_keys(word_guess['response'])
            time.sleep(3)
            submit_element = driver.find_element(By.NAME,'submitWord')
            submit_element.click()
            time.sleep(5)
            first_word = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[3]/div/div/div/div/span[1]').text
            second_word = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[3]/div/div/div/div/span[3]').text
            print(first_word,second_word)
            time.sleep(3)
            tries-=1
        except:
            print('Success')
            shortest_path = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[3]/div/div/div').text
            final_count = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[3]/div/p[1]').text
            print('Shortest path : ',shortest_path)
            print(final_count)
            time.sleep(30)
            driver.quit()
            break


