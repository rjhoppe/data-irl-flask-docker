from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
#from collections import Counter
import threading
import time
import random
import app

respGen = app.RespGen.respGen
userEmail = app.RespGen.email
responseType = app.RespGen.responseType
surveyLink = app.RespGen.surveyLink
respSent = ''
respGenCount = 0

cxCustCareNeu = ['Nothing', 'N/A', 'Meh', 'Nothing to add', 'Nothing to add at this time', 'Unremarkable experience', 'some good, some bad', 'Might come back',
                    'Acceptable']
    
cxCustCareNeg = ['Hire more thoughtful customer service reps', 'Lower prices', 'This location didn\'t have a useable bathroom', 'No one on the floor to help me',
                    'No one could help me', 'product I wanted was out of stock', 'Product was unavailable',
                    'Mediocre experience, will not be returning', 'Staff was rude', 'Customer service was rude and couldn\'t help me',
                    'Store was difficult to navigate', 'Store was hard to navigate for someone with disabilities', 'Lighting inside the location was poor',
                    'Long lines when I went to checkout', 'Staff was nowhere to be found', 'GARBAGE CUSTOMER SERVICE','Experience left me very frustrated', 
                    'Experience was exhausting', 'Very frustrating', 'Product came without instructions',
                    'A customer service rep advised me to purchase an item. The product did not solve my issue and it broke in the process. Now I can\'t return it.'
                    'I wish I could get the time back', 'Nothing to write home about', 'Can\'t say, as the story was closed when I got there, despite saying it should be open online...',
                    'Product is TRASH', 'Regrettable', 'Staff argued with me about what I needed...', 'Staff was rude to me over the phone', 'Floor attendants were useless', 'Gary is the worst',
                    'Whoever hired Gary should be fired', 'Customer service lacks empathy for customers']

cxCustCarePos = ['I wouldn\'t change a thing!', 'My customer service agent was fantastic!', 'Nothing at all! Great experience','product was exactly what I needed',
                    'Store was very easy to navigate', 'It was easy to find exactly what I needed', 'Speedy checkout process, very nice', 'Staff was very helpful', 'Great service', 
                    'GREAT', 'OUTSTANDING', 'WONDERFUL customer service', 'Product came with excellent instructions', 'A customer service rep spent over an hour with me making sure I got exactly what I needed',
                    'A customer service rep advised me to purchase an item that perfectly solved my issue.', 'Store layout made it very easy to find what I needed', 'My wife loved the store', 
                    'My kids loved the store', 'My wife loved the product', 'My husband loved the product', 'Store was very well stocked', 'Floor attendants were very helpful', 
                    'Received very kind customer service over the phone, thank you Jim!', 'Jim was really great and helped me out', 'Sarah was very kind and helpful']

cxDigExpNeu = []

cxDigExpNeg = []

cxDigExpPos = []

exCanExpAppNeu = []

exCanExpAppNeg = []

exCanExpAppPos = []

exEmpExpNeu = []

exEmpExpNeg = []

exEmpExpPos = []



def main():


    def generate_responses(respGenCount, respSent, respGen):

        # Determine response sentiment - can adjust weighting here
        sentGen = random.randrange(1, 5)
        if sentGen > 3:
            respSent = 'Positive'

        elif sentGen == 3:
            respSent = 'Neutral'

        else:
            respSent = 'Negative'

        try:    
            # Reopen the browser
            driver = webdriver.Chrome()
            driver.get('https://tamearlyaccess.sjc1.qualtrics.com/jfe/form/SV_0B1AFvEtS8Ji2oK')
            time.sleep(1)

            # Block 1 pg2Actions
            pg1Next = driver.find_element(By.ID, 'next-button')
            pg1Actions = ActionChains(driver)
            pg1Actions.move_to_element(pg1Next)
            pg1Actions.click(pg1Next)
            pg1Actions.perform()   
            time.sleep(1)

            # Block 2 pg2Actions
            pg2Actions = ActionChains(driver)

            if respSent == 'Positive':
                q1PosOpt = ['choice-display-QID1-14', 'choice-display-QID1-15']
                q1choice = random.choice(q1PosOpt)
                q1_button = driver.find_element(By.ID, q1choice)
                # Continue for each positive option
                q2PosOpt = ['choice-display-QID14-14', 'choice-display-QID14-15']
                q2choice = random.choice(q2PosOpt)
                q2_button = driver.find_element(By.ID, q2choice)
                q3PosOpt = ['choice-display-QID15-14', 'choice-display-QID15-15']
                q3choice = random.choice(q3PosOpt)
                q3_button = driver.find_element(By.ID, q3choice)
                q4PosOpt = ['choice-display-QID16-14', 'choice-display-QID16-15']
                q4choice = random.choice(q4PosOpt)
                q4_button = driver.find_element(By.ID, q4choice)
                q5_comment = driver.find_element(By.XPATH, '//*[@id="question-QID10"]/div/div/div/div/div/div[2]/textarea')
                q6_comment = driver.find_element(By.XPATH, '//*[@id="question-QID9"]/div/div/div/div/div/div[2]/textarea')
            
            elif respSent == 'Neutral':
                q1NeuOpt = ['choice-display-QID1-12', 'choice-display-QID1-13', 'choice-display-QID1-14']
                q1choice = random.choice(q1NeuOpt)
                q1_button = driver.find_element(By.ID, q1choice)
                q2PosOpt = ['choice-display-QID14-12', 'choice-display-QID14-13', 'choice-display-QID14-14']
                q2choice = random.choice(q2PosOpt)
                q2_button = driver.find_element(By.ID, q2choice)
                q3PosOpt = ['choice-display-QID15-12', 'choice-display-QID15-13', 'choice-display-QID15-14']
                q3choice = random.choice(q3PosOpt)
                q3_button = driver.find_element(By.ID, q3choice)
                q4PosOpt = ['choice-display-QID16-12', 'choice-display-QID16-13', 'choice-display-QID16-14']
                q4choice = random.choice(q4PosOpt)
                q4_button = driver.find_element(By.ID, q4choice)
                q5_comment = driver.find_element(By.XPATH, '//*[@id="question-QID10"]/div/div/div/div/div/div[2]/textarea')
                q6_comment = driver.find_element(By.XPATH, '//*[@id="question-QID9"]/div/div/div/div/div/div[2]/textarea')

            else:
                q1NegOpt = ['choice-display-QID1-11', 'choice-display-QID1-12']
                q1choice = random.choice(q1NegOpt)
                q1_button = driver.find_element(By.ID, q1choice)
                q2PosOpt = ['choice-display-QID14-11', 'choice-display-QID14-12']
                q2choice = random.choice(q2PosOpt)
                q2_button = driver.find_element(By.ID, q2choice)
                q3PosOpt = ['choice-display-QID15-11', 'choice-display-QID15-12']
                q3choice = random.choice(q3PosOpt)
                q3_button = driver.find_element(By.ID, q3choice)
                q4PosOpt = ['choice-display-QID16-11', 'choice-display-QID16-12']
                q4choice = random.choice(q4PosOpt)
                q4_button = driver.find_element(By.ID, q4choice)
                q5_comment = driver.find_element(By.XPATH, '//*[@id="question-QID10"]/div/div/div/div/div/div[2]/textarea')
                q6_comment = driver.find_element(By.XPATH, '//*[@id="question-QID9"]/div/div/div/div/div/div[2]/textarea')

            # Action Block
            pg2Submit = driver.find_element(By.ID, 'next-button')
            pg2Actions = ActionChains(driver)
            pg2Actions.move_to_element(q1_button)
            pg2Actions.click(q1_button)
            pg2Actions.move_to_element(q2_button)
            pg2Actions.click(q2_button)
            pg2Actions.move_to_element(q3_button)
            pg2Actions.click(q3_button)
            pg2Actions.move_to_element(q4_button)
            pg2Actions.click(q4_button)

            pg2Actions.move_to_element(q5_comment)
            time.sleep(1)
            if respSent == 'Positive':
                q5_comment.send_keys(random.choice(cxAddCommentsPos))
            elif respSent == 'Neutral':
                q5_comment.send_keys(random.choice(cxAddCommentsNeu))
            else:
                q5_comment.send_keys(random.choice(cxAddCommentsNeg))

            pg2Actions.move_to_element(q6_comment)
            time.sleep(1)
            if respSent == 'Positive':
                q6_comment.send_keys(random.choice(cxAddCommentsPos))
            elif respSent == 'Neutral':
                q6_comment.send_keys(random.choice(cxAddCommentsNeu))
            else:
                q6_comment.send_keys(random.choice(cxAddCommentsNeg))

            pg2Actions.move_to_element(pg2Submit)
            pg2Actions.click(pg2Submit)
            pg2Actions.perform()

        except:
            print('Something went wrong...')

        time.sleep(1)
        driver.quit()
        
        respGenCount += 1
        loopsRemaining = (int(respGen) - int(respGenCount))
        print(f'Loop complete, loops remaining: {loopsRemaining}')
        print(respGenCount)
        print(type(respGenCount))
        return respGenCount

    respGenCount = generate_responses(respGenCount, respSent, respGen)

    def gen_loop (respGen, respGenCount):
        #threads = [] 
        while respGen > respGenCount:
            t1 = threading.Thread(target=generate_responses, args=(respGenCount, respSent, respGen))
            t1.start()
            respGenCount +=1
            t2 = threading.Thread(target=generate_responses, args=(respGenCount, respSent, respGen))
            t2.start()
            respGenCount +=1
            t3 = threading.Thread(target=generate_responses, args=(respGenCount, respSent, respGen))
            t3.start()
            respGenCount +=1
            t4 = threading.Thread(target=generate_responses, args=(respGenCount, respSent, respGen))
            t4.start()
            respGenCount +=1
            
            generate_responses(respGenCount, respSent, respGen)
            respGenCount +=1

    gen_loop(respGen, respGenCount)

    print('Job complete!')

if __name__ == "__main__":
    main()