from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
#from collections import Counter
import threading
import time
import random

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

cxDigExpNeu = ['Test cxDigExpNeu']

cxDigExpNeg = ['Test cxDigExpNeg']

cxDigExpPos = ['Test cxDigExpPos']

exCanExpAppNeu = ['Test exCanExpAppNeu']

exCanExpAppNeg = ['Test exCanExpAppNeg']

exCanExpAppPos = ['Test exCanExpAppPo']

exEmpExpNeu = ['Test exEmpExpNeu']

exEmpExpNeg = ['Test exEmpExpNeg']

exEmpExpPos = ['Test exEmpExpPos']

# def define_resp_sent(respSent):

#     # Determine response sentiment - can adjust weighting here
#     # Future enhancement - allow adjustable sentiment scaling
#     sentGen = random.randrange(1, 5)
#     if sentGen > 3:
#         respSent = 'Positive'

#     elif sentGen == 3:
#         respSent = 'Neutral'

#     else:
#         respSent = 'Negative'

# respSent = define_resp_sent(respSent)


def main(email, surveyLink, respGen, responseType):

    respGen = int(respGen)
    userEmail = email
    responseType = responseType
    surveyLink = surveyLink
    respSent = ''
    respGenCount = 0


    def define_resp_sent(respSent):

        # Determine response sentiment - can adjust weighting here
        # Future enhancement - allow adjustable sentiment scaling
        sentGen = random.randrange(1, 5)
        if sentGen > 3:
            respSent = 'Positive'

        elif sentGen == 3:
            respSent = 'Neutral'

        else:
            respSent = 'Negative'

    respSent = define_resp_sent(respSent)


    # Determine what temp survey to use and then run the correct response gen operation
    if responseType == 'cx_cust_care':
    
        def cx_cust_care(respGenCount, respSent, respGen):

            try:    
                # Open the browser
                driver = webdriver.Chrome()
                driver.get(surveyLink)
                time.sleep(1)

                # Block 1 pg1Actions
                pg1_actions = ActionChains(driver)

                if respSent == 'Positive':
                    # Demographic question on race, can be reused, no logic applied
                    q1_pos_opt = ['mc-choice-input-QID16-1', 'mc-choice-input-QID16-2', 'mc-choice-input-QID16-3', 
                                  'mc-choice-input-QID16-4', 'mc-choice-input-QID16-5', 'mc-choice-input-QID16-6',
                                  'mc-choice-input-QID16-7']
                    q1_choice = random.choice(q1_pos_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    # Demographic question on education, can be reused, no logic applied
                    q2_pos_opt = ['mc-choice-input-QID17-1', 'mc-choice-input-QID17-2', 'mc-choice-input-QID17-3',
                                  'mc-choice-input-QID17-4', 'mc-choice-input-QID17-5', 'mc-choice-input-QID17-6',
                                  'mc-choice-input-QID17-7']
                    q2_choice = random.choice(q2_pos_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    # Demographic question on income, can be reused, no logic applied
                    q3_pos_opt = ['mc-choice-input-QID18-1', 'mc-choice-input-QID18-2', 'mc-choice-input-QID18-3',
                                  'mc-choice-input-QID18-4', 'mc-choice-input-QID18-5', 'mc-choice-input-QID18-6',
                                  'mc-choice-input-QID18-7']
                    q3_choice = random.choice(q3_pos_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_pos_opt = ['mc-choice-input-QID8-4', 'mc-choice-input-QID8-5']
                    q4_choice = random.choice(q4_pos_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_pos_opt = ['mc-choice-input-QID1-4', 'mc-choice-input-QID1-5']
                    q5_choice = random.choice(q5_pos_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_pos_opt = ['mc-choice-input-QID9-4', 'mc-choice-input-QID9-5']
                    q6_choice = random.choice(q6_pos_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_pos_opt = ['mc-choice-input-QID11-4', 'mc-choice-input-QID11-5']
                    q7_choice =random.choice(q7_pos_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_pos_opt = ['mc-choice-input-QID12-5', 'mc-choice-input-QID12-4']
                    q8_choice = random.choice(q8_pos_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_pos_opt = ['mc-choice-input-QID13-1']
                    q9_choice = random.choice(q9_pos_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_comment = driver.find_element(By.XPATH, '//*[@id="question-QID14"]/div/div/div/div/div/div[2]/textarea')
                    q11_comment = driver.find_element(By.XPATH, '//*[@id="question-QID15"]/div/div/div/div/div/div[2]/textarea')
                
                elif respSent == 'Neutral':
                    q1_neu_opt = ['mc-choice-input-QID16-1', 'mc-choice-input-QID16-2', 'mc-choice-input-QID16-3', 
                                  'mc-choice-input-QID16-4', 'mc-choice-input-QID16-5', 'mc-choice-input-QID16-6',
                                  'mc-choice-input-QID16-7']
                    q1_choice = random.choice(q1_neu_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neu_opt = ['mc-choice-input-QID17-1', 'mc-choice-input-QID17-2', 'mc-choice-input-QID17-3',
                                  'mc-choice-input-QID17-4', 'mc-choice-input-QID17-5', 'mc-choice-input-QID17-6',
                                  'mc-choice-input-QID17-7']
                    q2_choice = random.choice(q2_neu_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neu_opt = ['mc-choice-input-QID18-1', 'mc-choice-input-QID18-2', 'mc-choice-input-QID18-3',
                                  'mc-choice-input-QID18-4', 'mc-choice-input-QID18-5', 'mc-choice-input-QID18-6',
                                  'mc-choice-input-QID18-7']
                    q3_choice = random.choice(q3_neu_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neu_opt = ['mc-choice-input-QID8-2', 'mc-choice-input-QID8-3', 'mc-choice-input-QID8-4']
                    q4_choice = random.choice(q4_neu_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neu_opt = ['mc-choice-input-QID1-2', 'mc-choice-input-QID1-3', 'mc-choice-input-QID1-4']
                    q5_choice = random.choice(q5_neu_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neu_opt = ['mc-choice-input-QID9-4', 'mc-choice-input-QID9-3', 'mc-choice-input-QID9-2']
                    q6_choice = random.choice(q6_neu_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_neu_opt = ['mc-choice-input-QID11-2', 'mc-choice-input-QID11-3','mc-choice-input-QID11-4']
                    q7_choice = random.choice(q7_neu_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_neu_opt = ['mc-choice-input-QID12-4', 'mc-choice-input-QID12-3', 'mc-choice-input-QID12-2']
                    q8_choice = random.choice(q8_neu_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_neu_opt = ['mc-choice-input-QID13-1', 'mc-choice-input-QID13-2']
                    q9_choice = random.choice(q9_neu_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_comment = driver.find_element(By.XPATH, '//*[@id="question-QID14"]/div/div/div/div/div/div[2]/textarea')
                    q11_comment = driver.find_element(By.XPATH, '//*[@id="question-QID15"]/div/div/div/div/div/div[2]/textarea')

                else:
                    q1_neg_opt = ['mc-choice-input-QID16-1', 'mc-choice-input-QID16-2', 'mc-choice-input-QID16-3', 
                                  'mc-choice-input-QID16-4', 'mc-choice-input-QID16-5', 'mc-choice-input-QID16-6',
                                  'mc-choice-input-QID16-7']
                    q1_choice = random.choice(q1_neg_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neg_opt = ['mc-choice-input-QID17-1', 'mc-choice-input-QID17-2', 'mc-choice-input-QID17-3',
                                  'mc-choice-input-QID17-4', 'mc-choice-input-QID17-5', 'mc-choice-input-QID17-6',
                                  'mc-choice-input-QID17-7']
                    q2_choice = random.choice(q2_neg_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neg_opt = ['mc-choice-input-QID18-1', 'mc-choice-input-QID18-2', 'mc-choice-input-QID18-3',
                                  'mc-choice-input-QID18-4', 'mc-choice-input-QID18-5', 'mc-choice-input-QID18-6',
                                  'mc-choice-input-QID18-7']
                    q3_choice = random.choice(q3_neg_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neg_opt = ['mc-choice-input-QID8-1', 'mc-choice-input-QID8-2']
                    q4_choice = random.choice(q4_neg_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neg_opt = ['mc-choice-input-QID1-1', 'mc-choice-input-QID1-2']
                    q5_choice = random.choice(q5_neg_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neg_opt = ['mc-choice-input-QID9-2', 'mc-choice-input-QID9-1']
                    q6_choice = random.choice(q6_neg_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_neg_opt = ['mc-choice-input-QID11-1', 'mc-choice-input-QID11-2']
                    q7_choice = random.choice(q7_neg_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_neg_opt = ['mc-choice-input-QID12-2', 'mc-choice-input-QID12-1']
                    q8_choice = random.choice(q8_neg_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_neg_opt = ['mc-choice-input-QID13-2']
                    q9_choice = random.choice(q9_neg_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_comment = driver.find_element(By.XPATH, '//*[@id="question-QID14"]/div/div/div/div/div/div[2]/textarea')
                    q11_comment = driver.find_element(By.XPATH, '//*[@id="question-QID15"]/div/div/div/div/div/div[2]/textarea')


                # Action Block
                pg1_submit = driver.find_element(By.ID, 'next-button')
                pg1_actions = ActionChains(driver)
                pg1_actions.move_to_element(q1_button)
                pg1_actions.click(q1_button)
                pg1_actions.move_to_element(q2_button)
                pg1_actions.click(q2_button)
                pg1_actions.move_to_element(q3_button)
                pg1_actions.click(q3_button)
                pg1_actions.move_to_element(q4_button)
                pg1_actions.click(q4_button)
                pg1_actions.move_to_element(q5_button)
                pg1_actions.click(q5_button)
                pg1_actions.move_to_element(q6_button)
                pg1_actions.click(q6_button)
                pg1_actions.move_to_element(q7_button)
                pg1_actions.click(q7_button)
                pg1_actions.move_to_element(q8_button)
                pg1_actions.click(q8_button)
                pg1_actions.move_to_element(q9_button)
                pg1_actions.click(q9_button)

                # Open text elements
                pg1_actions.move_to_element(q10_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q10_comment.send_keys(random.choice(cxCustCarePos))
                elif respSent == 'Neutral':
                    q10_comment.send_keys(random.choice(cxCustCareNeu))
                else:
                    q10_comment.send_keys(random.choice(cxCustCareNeg))

                pg1_actions.move_to_element(q11_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q11_comment.send_keys(random.choice(cxCustCarePos))
                elif respSent == 'Neutral':
                    q11_comment.send_keys(random.choice(cxCustCareNeu))
                else:
                    q11_comment.send_keys(random.choice(cxCustCareNeg))

                # Submit response
                pg1_actions.move_to_element(pg1_submit)
                pg1_actions.click(pg1_submit)
                pg1_actions.perform()

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

        respGenCount = cx_cust_care(respGenCount, respSent, respGen)

        # Scaling the generation of responses via threading
        def gen_loop (respGen, respGenCount):
            #threads = [] 
            while respGen > respGenCount:
                t1 = threading.Thread(target=cx_cust_care, args=(respGenCount, respSent, respGen))
                t1.start()
                respGenCount +=1
                t2 = threading.Thread(target=cx_cust_care, args=(respGenCount, respSent, respGen))
                t2.start()
                respGenCount +=1
                t3 = threading.Thread(target=cx_cust_care, args=(respGenCount, respSent, respGen))
                t3.start()
                respGenCount +=1
                t4 = threading.Thread(target=cx_cust_care, args=(respGenCount, respSent, respGen))
                t4.start()
                respGenCount +=1
                
                cx_cust_care(respGenCount, respSent, respGen)
                respGenCount +=1

        gen_loop(respGen, respGenCount)

        print('Job complete!')

    elif responseType == 'cx_digital_xp':
        
        def digital_xp(respGenCount, respSent, respGen):
            
            try:    
                # Open the browser
                driver = webdriver.Chrome()
                driver.get(surveyLink)
                time.sleep(1)

                # Block 1 pg1Actions
                pg1_actions = ActionChains(driver)

                if respSent == 'Positive':
                    # Demographic question on race, can be reused, no logic applied
                    q1_pos_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_pos_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    # Demographic question on education, can be reused, no logic applied
                    q2_pos_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_pos_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    # Demographic question on income, can be reused, no logic applied
                    q3_pos_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_pos_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_pos_opt = ['mc-choice-input-QID8-4', 'mc-choice-input-QID8-5']
                    q4_choice = random.choice(q4_pos_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_pos_opt = ['mc-choice-input-QID9-4', 'mc-choice-input-QID9-5']
                    q5_choice = random.choice(q5_pos_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_pos_opt = ['mc-choice-input-QID10-1']
                    q6_choice = random.choice(q6_pos_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_comment = driver.find_element(By.XPATH, '//*[@id="question-QID12"]/div/div/div/div/div/div[2]/textarea')
                    q8_comment = driver.find_element(By.XPATH, '//*[@id="question-QID13"]/div/div/div/div/div/div[2]/textarea')
                
                elif respSent == 'Neutral':
                    q1_neu_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_neu_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neu_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_neu_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neu_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_neu_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neu_opt = ['mc-choice-input-QID8-2', 'mc-choice-input-QID8-3', 'mc-choice-input-QID8-4']
                    q4_choice = random.choice(q4_neu_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neu_opt = ['mc-choice-input-QID9-2', 'mc-choice-input-QID9-3', 'mc-choice-input-QID9-4']
                    q5_choice = random.choice(q5_neu_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neu_opt = ['mc-choice-input-QID10-1', 'mc-choice-input-QID10-2']
                    q6_choice = random.choice(q6_neu_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_comment = driver.find_element(By.XPATH, '//*[@id="question-QID12"]/div/div/div/div/div/div[2]/textarea')
                    q8_comment = driver.find_element(By.XPATH, '//*[@id="question-QID13"]/div/div/div/div/div/div[2]/textarea')

                else:
                    q1_neg_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_neg_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neg_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_neg_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neg_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_neg_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neg_opt = ['mc-choice-input-QID8-1', 'mc-choice-input-QID8-2']
                    q4_choice = random.choice(q4_neg_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neg_opt = ['mc-choice-input-QID9-1', 'mc-choice-input-QID9-2']
                    q5_choice = random.choice(q5_neg_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neg_opt = ['mc-choice-input-QID10-2']
                    q6_choice = random.choice(q6_neg_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_comment = driver.find_element(By.XPATH, '//*[@id="question-QID12"]/div/div/div/div/div/div[2]/textarea')
                    q8_comment = driver.find_element(By.XPATH, '//*[@id="question-QID13"]/div/div/div/div/div/div[2]/textarea')


                # Action Block
                pg1_submit = driver.find_element(By.ID, 'next-button')
                pg1_actions = ActionChains(driver)
                pg1_actions.move_to_element(q1_button)
                pg1_actions.click(q1_button)
                pg1_actions.move_to_element(q2_button)
                pg1_actions.click(q2_button)
                pg1_actions.move_to_element(q3_button)
                pg1_actions.click(q3_button)
                pg1_actions.move_to_element(q4_button)
                pg1_actions.click(q4_button)
                pg1_actions.move_to_element(q5_button)
                pg1_actions.click(q5_button)
                pg1_actions.move_to_element(q6_button)
                pg1_actions.click(q6_button)

                # Open text elements
                pg1_actions.move_to_element(q7_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q7_comment.send_keys(random.choice(cxDigExpPos))
                elif respSent == 'Neutral':
                    q7_comment.send_keys(random.choice(cxDigExpNeu))
                else:
                    q7_comment.send_keys(random.choice(cxDigExpNeg))

                pg1_actions.move_to_element(q8_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q8_comment.send_keys(random.choice(cxDigExpPos))
                elif respSent == 'Neutral':
                    q8_comment.send_keys(random.choice(cxDigExpNeu))
                else:
                    q8_comment.send_keys(random.choice(cxDigExpNeg))

                # Submit response
                pg1_actions.move_to_element(pg1_submit)
                pg1_actions.click(pg1_submit)
                pg1_actions.perform()

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

        respGenCount = digital_xp(respGenCount, respSent, respGen)

        # Scaling the generation of responses via threading
        def gen_loop (respGen, respGenCount):
            while respGen > respGenCount:
                t1 = threading.Thread(target=digital_xp, args=(respGenCount, respSent, respGen))
                t1.start()
                respGenCount +=1
                t2 = threading.Thread(target=digital_xp, args=(respGenCount, respSent, respGen))
                t2.start()
                respGenCount +=1
                t3 = threading.Thread(target=digital_xp, args=(respGenCount, respSent, respGen))
                t3.start()
                respGenCount +=1
                t4 = threading.Thread(target=digital_xp, args=(respGenCount, respSent, respGen))
                t4.start()
                respGenCount +=1
                
                digital_xp(respGenCount, respSent, respGen)
                respGenCount +=1

        gen_loop(respGen, respGenCount)

        print('Job complete!')


    elif responseType == 'ex_can_xp':
        
        def ex_can_xp(respGenCount, respSent, respGen):
    
            try:    
                # Open the browser
                driver = webdriver.Chrome()
                driver.get(surveyLink)
                time.sleep(1)

                # Block 1 pg1Actions
                pg1_actions = ActionChains(driver)

                if respSent == 'Positive':
                    # Demographic question on race, can be reused, no logic applied
                    q1_pos_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_pos_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    # Demographic question on education, can be reused, no logic applied
                    q2_pos_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_pos_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    # Demographic question on income, can be reused, no logic applied
                    q3_pos_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_pos_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_pos_opt = ['mc-choice-input-QID1213989827-9', 'mc-choice-input-QID1213989827-10']
                    q4_choice = random.choice(q4_pos_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_pos_opt = ['mc-choice-input-QID1213989828-9', 'mc-choice-input-QID1213989828-10']
                    q5_choice = random.choice(q5_pos_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_pos_opt = ['mc-choice-input-QID1213989830-10', 'mc-choice-input-QID1213989830-9']
                    q6_choice = random.choice(q6_pos_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_pos_opt = ['mc-choice-input-QID1213989832-5', 'mc-choice-input-QID1213989832-4']
                    q7_choice =random.choice(q7_pos_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_pos_opt = ['mc-choice-input-QID1213989833-5', 'mc-choice-input-QID1213989833-4']
                    q8_choice = random.choice(q8_pos_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_pos_opt = ['mc-choice-input-QID1213989834-15', 'mc-choice-input-QID1213989834-14']
                    q9_choice = random.choice(q9_pos_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_pos_opt = ['mc-choice-input-QID1213989835-1', 'mc-choice-input-QID1213989835-2', 'mc-choice-input-QID1213989835-3', 
                                   'mc-choice-input-QID1213989835-4', 'mc-choice-input-QID1213989835-5']
                    q10_choice = random.choice(q10_pos_opt)
                    q10_button = driver.find_element(By.ID, q10_choice)                   
                    q11_pos_opt = ['mc-choice-input-QID1213989836-15', 'mc-choice-input-QID1213989836-14']
                    q11_choice = random.choice(q11_pos_opt)
                    q11_button = driver.find_element(By.ID, q11_choice)
                    q12_comment = driver.find_element(By.XPATH, '//*[@id="question-QID1213989831"]/div/div/div/div/div/div[2]/textarea')
                    q13_comment = driver.find_element(By.XPATH, '//*[@id="question-QID1213989837"]/div/div/div/div/div/div[2]/textarea')
                
                elif respSent == 'Neutral':
                    q1_neu_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_neu_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neu_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_neu_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neu_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_neu_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neu_opt = ['mc-choice-input-QID1213989827-7', 'mc-choice-input-QID1213989827-8', 'mc-choice-input-QID1213989827-9']
                    q4_choice = random.choice(q4_neu_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neu_opt = ['mc-choice-input-QID1213989828-9', 'mc-choice-input-QID1213989828-8', 'mc-choice-input-QID1213989828-7']
                    q5_choice = random.choice(q5_neu_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neu_opt = ['mc-choice-input-QID1213989830-9', 'mc-choice-input-QID1213989830-8', 'mc-choice-input-QID1213989830-7']
                    q6_choice = random.choice(q6_neu_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_neu_opt = ['mc-choice-input-QID1213989832-4', 'mc-choice-input-QID1213989832-3','mc-choice-input-QID1213989832-2']
                    q7_choice = random.choice(q7_neu_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_neu_opt = ['mc-choice-input-QID1213989833-4', 'mc-choice-input-QID1213989833-3', 'mc-choice-input-QID1213989833-2']
                    q8_choice = random.choice(q8_neu_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_neu_opt = ['mc-choice-input-QID1213989834-14', 'mc-choice-input-QID1213989834-13', 'mc-choice-input-QID1213989834-12']
                    q9_choice = random.choice(q9_neu_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_neu_opt = ['mc-choice-input-QID1213989835-1', 'mc-choice-input-QID1213989835-2', 'mc-choice-input-QID1213989835-3', 
                                   'mc-choice-input-QID1213989835-4', 'mc-choice-input-QID1213989835-5']
                    q10_choice = random.choice(q10_neu_opt)
                    q10_button = driver.find_element(By.ID, q10_choice)                   
                    q11_neu_opt = ['mc-choice-input-QID1213989836-14', 'mc-choice-input-QID1213989836-13', 'mc-choice-input-QID1213989836-12']
                    q11_choice = random.choice(q11_neu_opt)
                    q11_button = driver.find_element(By.ID, q11_choice)
                    q12_comment = driver.find_element(By.XPATH, '//*[@id="question-QID1213989831"]/div/div/div/div/div/div[2]/textarea')
                    q13_comment = driver.find_element(By.XPATH, '//*[@id="question-QID1213989837"]/div/div/div/div/div/div[2]/textarea')

                else:
                    q1_neg_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_neg_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neg_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_neg_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neg_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_neg_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neg_opt = ['mc-choice-input-QID1213989827-6', 'mc-choice-input-QID1213989827-7']
                    q4_choice = random.choice(q4_neg_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neg_opt = ['mc-choice-input-QID1213989828-7', 'mc-choice-input-QID1213989828-6']
                    q5_choice = random.choice(q5_neg_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neg_opt = ['mc-choice-input-QID1213989830-6', 'mc-choice-input-QID1213989830-7']
                    q6_choice = random.choice(q6_neg_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_neg_opt = ['mc-choice-input-QID1213989832-1', 'mc-choice-input-QID1213989832-2']
                    q7_choice = random.choice(q7_neg_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_neg_opt = ['mc-choice-input-QID1213989833-1', 'mc-choice-input-QID1213989833-2']
                    q8_choice = random.choice(q8_neg_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_neg_opt = ['mc-choice-input-QID1213989834-11', 'mc-choice-input-QID1213989834-12']
                    q9_choice = random.choice(q9_neg_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_neg_opt = ['mc-choice-input-QID1213989835-1', 'mc-choice-input-QID1213989835-2', 'mc-choice-input-QID1213989835-3', 
                                   'mc-choice-input-QID1213989835-4', 'mc-choice-input-QID1213989835-5']
                    q10_choice = random.choice(q10_neg_opt)
                    q10_button = driver.find_element(By.ID, q10_choice)                   
                    q11_neg_opt = ['mc-choice-input-QID1213989836-11', 'mc-choice-input-QID1213989836-12']
                    q11_choice = random.choice(q11_neg_opt)
                    q11_button = driver.find_element(By.ID, q11_choice)
                    q12_comment = driver.find_element(By.XPATH, '//*[@id="question-QID1213989831"]/div/div/div/div/div/div[2]/textarea')
                    q13_comment = driver.find_element(By.XPATH, '//*[@id="question-QID1213989837"]/div/div/div/div/div/div[2]/textarea')


                # Action Block
                pg1_submit = driver.find_element(By.ID, 'next-button')
                pg1_actions = ActionChains(driver)
                pg1_actions.move_to_element(q1_button)
                pg1_actions.click(q1_button)
                pg1_actions.move_to_element(q2_button)
                pg1_actions.click(q2_button)
                pg1_actions.move_to_element(q3_button)
                pg1_actions.click(q3_button)
                pg1_actions.move_to_element(q4_button)
                pg1_actions.click(q4_button)
                pg1_actions.move_to_element(q5_button)
                pg1_actions.click(q5_button)
                pg1_actions.move_to_element(q6_button)
                pg1_actions.click(q6_button)
                pg1_actions.move_to_element(q7_button)
                pg1_actions.click(q7_button)
                pg1_actions.move_to_element(q8_button)
                pg1_actions.click(q8_button)
                pg1_actions.move_to_element(q9_button)
                pg1_actions.click(q9_button)
                pg1_actions.move_to_element(q10_button)
                pg1_actions.click(q10_button)                
                pg1_actions.move_to_element(q11_button)
                pg1_actions.click(q11_button)

                # Open text elements
                pg1_actions.move_to_element(q12_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q12_comment.send_keys(random.choice(exCanExpAppPos))
                elif respSent == 'Neutral':
                    q12_comment.send_keys(random.choice(exCanExpAppNeu))
                else:
                    q12_comment.send_keys(random.choice(exCanExpAppNeg))

                pg1_actions.move_to_element(q13_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q13_comment.send_keys(random.choice(exCanExpAppPos))
                elif respSent == 'Neutral':
                    q13_comment.send_keys(random.choice(exCanExpAppNeu))
                else:
                    q13_comment.send_keys(random.choice(exCanExpAppNeg))

                # Submit response
                pg1_actions.move_to_element(pg1_submit)
                pg1_actions.click(pg1_submit)
                pg1_actions.perform()

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

        respGenCount = ex_can_xp(respGenCount, respSent, respGen)

        # Scaling the generation of responses via threading
        def gen_loop (respGen, respGenCount):
            while respGen > respGenCount:
                t1 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t1.start()
                respGenCount +=1
                t2 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t2.start()
                respGenCount +=1
                t3 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t3.start()
                respGenCount +=1
                t4 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t4.start()
                respGenCount +=1
                
                ex_can_xp(respGenCount, respSent, respGen)
                respGenCount +=1

        gen_loop(respGen, respGenCount)

        print('Job complete!')



    elif responseType == 'ex_em_xp':
        
        def ex_can_xp(respGenCount, respSent, respGen):

            try:    
                # Open the browser
                driver = webdriver.Chrome()
                driver.get(surveyLink)
                time.sleep(1)

                # Block 1 pg1Actions
                pg1_actions = ActionChains(driver)

                if respSent == 'Positive':
                    # Demographic question on race, can be reused, no logic applied
                    q1_pos_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_pos_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    # Demographic question on education, can be reused, no logic applied
                    q2_pos_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_pos_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    # Demographic question on income, can be reused, no logic applied
                    q3_pos_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_pos_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_pos_opt = ['mc-choice-input-QID1213990013-5', 'mc-choice-input-QID1213990013-4']
                    q4_choice = random.choice(q4_pos_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_pos_opt = ['mc-choice-input-QID1213990014-5', 'mc-choice-input-QID1213990014-4']
                    q5_choice = random.choice(q5_pos_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_pos_opt = ['mc-choice-input-QID1213990015-5', 'mc-choice-input-QID1213990015-4']
                    q6_choice = random.choice(q6_pos_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_pos_opt = ['mc-choice-input-QID1213990016-5', 'mc-choice-input-QID1213990016-4']
                    q7_choice =random.choice(q7_pos_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_pos_opt = ['mc-choice-input-QID1213990017-5', 'mc-choice-input-QID1213990017-4']
                    q8_choice = random.choice(q8_pos_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_pos_opt = ['mc-choice-input-QID1213990018-10', 'mc-choice-input-QID1213990018-9']
                    q9_choice = random.choice(q9_pos_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_pos_opt = ['mc-choice-input-QID1213990019-10', 'mc-choice-input-QID1213990019-9']
                    q10_choice = random.choice(q10_pos_opt)
                    q10_button = driver.find_element(By.ID, q10_choice)                   
                    q11_pos_opt = ['mc-choice-input-QID1213990020-10', 'mc-choice-input-QID1213990020-9']
                    q11_choice = random.choice(q11_pos_opt)
                    q11_button = driver.find_element(By.ID, q11_choice)
                    q12_pos_opt = ['mc-choice-input-QID1213990021-5', 'mc-choice-input-QID1213990021-4']
                    q12_choice = random.choice(q12_pos_opt)
                    q12_button = driver.find_element(By.ID, q12_choice)                    
                    q13_pos_opt = ['mc-choice-input-QID1213990022-5', 'mc-choice-input-QID1213990022-4']
                    q13_choice = random.choice(q13_pos_opt)
                    q13_button = driver.find_element(By.ID, q13_choice)
                    q14_pos_opt = ['mc-choice-input-QID1213990023-5', 'mc-choice-input-QID1213990023-4']
                    q14_choice = random.choice(q14_pos_opt)
                    q14_button = driver.find_element(By.ID, q14_choice)
                    q15_pos_opt = ['mc-choice-input-QID1213990025-5', 'mc-choice-input-QID1213990025-4']
                    q15_choice = random.choice(q15_pos_opt)
                    q15_button = driver.find_element(By.ID, q15_choice)
                    q16_pos_opt = ['mc-choice-input-QID1213990026-5', 'mc-choice-input-QID1213990026-4']
                    q16_choice = random.choice(q16_pos_opt)
                    q16_button = driver.find_element(By.ID, q16_choice)
                    q17_pos_opt = ['mc-choice-input-QID1213990027-5', 'mc-choice-input-QID1213990027-4']
                    q17_choice = random.choice(q17_pos_opt)
                    q17_button = driver.find_element(By.ID, q17_choice)                    
                    q18_pos_opt = ['mc-choice-input-QID1213990031-5', 'mc-choice-input-QID1213990031-4']
                    q18_choice = random.choice(q18_pos_opt)
                    q18_button = driver.find_element(By.ID, q18_choice)
                    q19_pos_opt = ['mc-choice-input-QID1213990040-5', 'mc-choice-input-QID1213990040-4']
                    q19_choice = random.choice(q19_pos_opt)
                    q19_button = driver.find_element(By.ID, q19_choice)
                    q20_pos_opt = ['mc-choice-input-QID1213990045-5', 'mc-choice-input-QID1213990045-4']
                    q20_choice = random.choice(q20_pos_opt)
                    q20_button = driver.find_element(By.ID, q20_choice)
                    q21_pos_opt = ['mc-choice-input-QID1213990047-5', 'mc-choice-input-QID1213990047-4']
                    q21_choice = random.choice(q21_pos_opt)
                    q21_button = driver.find_element(By.ID, q21_choice)
                    q22_comment = driver.find_element(By.XPATH, '//*[@id="question-QID40"]/div/div/div/div/div/div[2]/textarea')
                    q23_comment = driver.find_element(By.XPATH, '//*[@id="question-QID41"]/div/div/div/div/div/div[2]/textarea')

                
                elif respSent == 'Neutral':
                    q1_neu_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_neu_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neu_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_neu_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neu_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_neu_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neu_opt = ['mc-choice-input-QID1213990013-2', 'mc-choice-input-QID1213990013-3', 'mc-choice-input-QID1213990013-4']
                    q4_choice = random.choice(q4_neu_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neu_opt = ['mc-choice-input-QID1213990014-2', 'mc-choice-input-QID1213990014-3', 'mc-choice-input-QID1213990014-4']
                    q5_choice = random.choice(q5_neu_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neu_opt = ['mc-choice-input-QID1213990015-2', 'mc-choice-input-QID1213990015-3', 'mc-choice-input-QID1213990015-4']
                    q6_choice = random.choice(q6_neu_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_neu_opt = ['mc-choice-input-QID1213990016-2', 'mc-choice-input-QID1213990016-3','mc-choice-input-QID1213990016-4']
                    q7_choice = random.choice(q7_neu_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_neu_opt = ['mc-choice-input-QID1213990017-2', 'mc-choice-input-QID1213990017-3', 'mc-choice-input-QID1213990017-4']
                    q8_choice = random.choice(q8_neu_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_neu_opt = ['mc-choice-input-QID1213990018-7', 'mc-choice-input-QID1213990018-8', 'mc-choice-input-QID1213990018-9']
                    q9_choice = random.choice(q9_neu_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_neu_opt = ['mc-choice-input-QID1213990019-7', 'mc-choice-input-QID1213990019-8', 'mc-choice-input-QID1213990019-9']
                    q10_choice = random.choice(q10_neu_opt)
                    q10_button = driver.find_element(By.ID, q10_choice)                   
                    q11_neu_opt = ['mc-choice-input-QID1213990020-7', 'mc-choice-input-QID1213990020-8', 'mc-choice-input-QID1213990020-9']
                    q11_choice = random.choice(q11_neu_opt)
                    q11_button = driver.find_element(By.ID, q11_choice)
                    q12_neu_opt = ['mc-choice-input-QID1213990021-2', 'mc-choice-input-QID1213990021-3', 'mc-choice-input-QID1213990021-4']
                    q12_choice = random.choice(q12_neu_opt)
                    q12_button = driver.find_element(By.ID, q12_choice)                    
                    q13_neu_opt = ['mc-choice-input-QID1213990022-2', 'mc-choice-input-QID1213990022-3', 'mc-choice-input-QID1213990022-4']
                    q13_choice = random.choice(q13_neu_opt)
                    q13_button = driver.find_element(By.ID, q13_choice)
                    q14_neu_opt = ['mc-choice-input-QID1213990023-2', 'mc-choice-input-QID1213990023-3', 'mc-choice-input-QID1213990023-4']
                    q14_choice = random.choice(q14_neu_opt)
                    q14_button = driver.find_element(By.ID, q14_choice)
                    q15_neu_opt = ['mc-choice-input-QID1213990025-2', 'mc-choice-input-QID1213990025-3', 'mc-choice-input-QID1213990025-4']
                    q15_choice = random.choice(q15_neu_opt)
                    q15_button = driver.find_element(By.ID, q15_choice)
                    q16_neu_opt = ['mc-choice-input-QID1213990026-2', 'mc-choice-input-QID1213990026-3', 'mc-choice-input-QID1213990026-4']
                    q16_choice = random.choice(q16_neu_opt)
                    q16_button = driver.find_element(By.ID, q16_choice)
                    q17_neu_opt = ['mc-choice-input-QID1213990027-2', 'mc-choice-input-QID1213990027-3', 'mc-choice-input-QID1213990027-4']
                    q17_choice = random.choice(q17_neu_opt)
                    q17_button = driver.find_element(By.ID, q17_choice)                    
                    q18_neu_opt = ['mc-choice-input-QID1213990031-2', 'mc-choice-input-QID1213990031-3', 'mc-choice-input-QID1213990031-4']
                    q18_choice = random.choice(q18_neu_opt)
                    q18_button = driver.find_element(By.ID, q18_choice)
                    q19_neu_opt = ['mc-choice-input-QID1213990040-2', 'mc-choice-input-QID1213990040-3', 'mc-choice-input-QID1213990040-4']
                    q19_choice = random.choice(q19_neu_opt)
                    q19_button = driver.find_element(By.ID, q19_choice)
                    q20_neu_opt = ['mc-choice-input-QID1213990045-2', 'mc-choice-input-QID1213990045-3', 'mc-choice-input-QID1213990045-4']
                    q20_choice = random.choice(q20_neu_opt)
                    q20_button = driver.find_element(By.ID, q20_choice)
                    q21_neu_opt = ['mc-choice-input-QID1213990047-2', 'mc-choice-input-QID1213990047-3', 'mc-choice-input-QID1213990047-4']
                    q21_choice = random.choice(q21_neu_opt)
                    q21_button = driver.find_element(By.ID, q21_choice)

                    q22_comment = driver.find_element(By.XPATH, '//*[@id="question-QID40"]/div/div/div/div/div/div[2]/textarea')
                    q23_comment = driver.find_element(By.XPATH, '//*[@id="question-QID41"]/div/div/div/div/div/div[2]/textarea')


                else:
                    q1_neg_opt = ['mc-choice-input-QID2-1', 'mc-choice-input-QID2-2', 'mc-choice-input-QID2-3', 
                                  'mc-choice-input-QID2-4', 'mc-choice-input-QID2-5', 'mc-choice-input-QID2-6',
                                  'mc-choice-input-QID2-7']
                    q1_choice = random.choice(q1_neg_opt)
                    q1_button = driver.find_element(By.ID, q1_choice)
                    q2_neg_opt = ['mc-choice-input-QID3-1', 'mc-choice-input-QID3-2', 'mc-choice-input-QID3-3',
                                  'mc-choice-input-QID3-4', 'mc-choice-input-QID3-5', 'mc-choice-input-QID3-6',
                                  'mc-choice-input-QID3-7']
                    q2_choice = random.choice(q2_neg_opt)
                    q2_button = driver.find_element(By.ID, q2_choice)
                    q3_neg_opt = ['mc-choice-input-QID4-1', 'mc-choice-input-QID4-2', 'mc-choice-input-QID4-3',
                                  'mc-choice-input-QID4-4', 'mc-choice-input-QID4-5', 'mc-choice-input-QID4-6',
                                  'mc-choice-input-QID4-7']
                    q3_choice = random.choice(q3_neg_opt)
                    q3_button = driver.find_element(By.ID, q3_choice)
                    q4_neg_opt = ['mc-choice-input-QID1213990013-1', 'mc-choice-input-QID1213990013-2']
                    q4_choice = random.choice(q4_neg_opt)
                    q4_button = driver.find_element(By.ID, q4_choice)
                    q5_neg_opt = ['mc-choice-input-QID1213990014-1', 'mc-choice-input-QID1213990014-2']
                    q5_choice = random.choice(q5_neg_opt)
                    q5_button = driver.find_element(By.ID, q5_choice)
                    q6_neg_opt = ['mc-choice-input-QID1213990015-1', 'mc-choice-input-QID1213990015-2']
                    q6_choice = random.choice(q6_neg_opt)
                    q6_button = driver.find_element(By.ID, q6_choice)
                    q7_neg_opt = ['mc-choice-input-QID1213990016-1', 'mc-choice-input-QID1213990016-2']
                    q7_choice = random.choice(q7_neg_opt)
                    q7_button = driver.find_element(By.ID, q7_choice)
                    q8_neg_opt = ['mc-choice-input-QID1213990017-1', 'mc-choice-input-QID1213990017-2']
                    q8_choice = random.choice(q8_neg_opt)
                    q8_button = driver.find_element(By.ID, q8_choice)
                    q9_neg_opt = ['mc-choice-input-QID1213990018-6', 'mc-choice-input-QID1213990018-7']
                    q9_choice = random.choice(q9_neg_opt)
                    q9_button = driver.find_element(By.ID, q9_choice)
                    q10_neg_opt = ['mc-choice-input-QID1213990019-6', 'mc-choice-input-QID1213990019-7']
                    q10_choice = random.choice(q10_neg_opt)
                    q10_button = driver.find_element(By.ID, q10_choice)                   
                    q11_neg_opt = ['mc-choice-input-QID1213990020-6', 'mc-choice-input-QID1213990020-7']
                    q11_choice = random.choice(q11_neg_opt)
                    q11_button = driver.find_element(By.ID, q11_choice)
                    q12_neg_opt = ['mc-choice-input-QID1213990021-1', 'mc-choice-input-QID1213990021-2']
                    q12_choice = random.choice(q12_neg_opt)
                    q12_button = driver.find_element(By.ID, q12_choice)                    
                    q13_neg_opt = ['mc-choice-input-QID1213990022-1', 'mc-choice-input-QID1213990022-2']
                    q13_choice = random.choice(q13_neg_opt)
                    q13_button = driver.find_element(By.ID, q13_choice)
                    q14_neg_opt = ['mc-choice-input-QID1213990023-1', 'mc-choice-input-QID1213990023-2']
                    q14_choice = random.choice(q14_neg_opt)
                    q14_button = driver.find_element(By.ID, q14_choice)
                    q15_neg_opt = ['mc-choice-input-QID1213990025-1', 'mc-choice-input-QID1213990025-2']
                    q15_choice = random.choice(q15_neg_opt)
                    q15_button = driver.find_element(By.ID, q15_choice)
                    q16_neg_opt = ['mc-choice-input-QID1213990026-1', 'mc-choice-input-QID1213990026-2']
                    q16_choice = random.choice(q16_neg_opt)
                    q16_button = driver.find_element(By.ID, q16_choice)
                    q17_neg_opt = ['mc-choice-input-QID1213990027-1', 'mc-choice-input-QID1213990027-2']
                    q17_choice = random.choice(q17_neg_opt)
                    q17_button = driver.find_element(By.ID, q17_choice)                    
                    q18_neg_opt = ['mc-choice-input-QID1213990031-1', 'mc-choice-input-QID1213990031-2']
                    q18_choice = random.choice(q18_neg_opt)
                    q18_button = driver.find_element(By.ID, q18_choice)
                    q19_neg_opt = ['mc-choice-input-QID1213990040-1', 'mc-choice-input-QID1213990040-2']
                    q19_choice = random.choice(q19_neg_opt)
                    q19_button = driver.find_element(By.ID, q19_choice)
                    q20_neg_opt = ['mc-choice-input-QID1213990045-1', 'mc-choice-input-QID1213990045-2']
                    q20_choice = random.choice(q20_neg_opt)
                    q20_button = driver.find_element(By.ID, q20_choice)
                    q21_neg_opt = ['mc-choice-input-QID1213990047-1', 'mc-choice-input-QID1213990047-2']
                    q21_choice = random.choice(q21_neg_opt)
                    q21_button = driver.find_element(By.ID, q21_choice)

                    q22_comment = driver.find_element(By.XPATH, '//*[@id="question-QID40"]/div/div/div/div/div/div[2]/textarea')
                    q23_comment = driver.find_element(By.XPATH, '//*[@id="question-QID41"]/div/div/div/div/div/div[2]/textarea')


                # Action Block
                pg1_submit = driver.find_element(By.ID, 'next-button')
                pg1_actions = ActionChains(driver)
                pg1_actions.move_to_element(q1_button)
                pg1_actions.click(q1_button)
                pg1_actions.move_to_element(q2_button)
                pg1_actions.click(q2_button)
                pg1_actions.move_to_element(q3_button)
                pg1_actions.click(q3_button)
                pg1_actions.move_to_element(q4_button)
                pg1_actions.click(q4_button)
                pg1_actions.move_to_element(q5_button)
                pg1_actions.click(q5_button)
                pg1_actions.move_to_element(q6_button)
                pg1_actions.click(q6_button)
                pg1_actions.move_to_element(q7_button)
                pg1_actions.click(q7_button)
                pg1_actions.move_to_element(q8_button)
                pg1_actions.click(q8_button)
                pg1_actions.move_to_element(q9_button)
                pg1_actions.click(q9_button)
                pg1_actions.move_to_element(q10_button)
                pg1_actions.click(q10_button)                
                pg1_actions.move_to_element(q11_button)
                pg1_actions.click(q11_button)
                pg1_actions.move_to_element(q12_button)
                pg1_actions.click(q12_button)                
                pg1_actions.move_to_element(q13_button)
                pg1_actions.click(q13_button)
                pg1_actions.move_to_element(q14_button)
                pg1_actions.click(q14_button)
                pg1_actions.move_to_element(q15_button)
                pg1_actions.click(q15_button)
                pg1_actions.move_to_element(q16_button)
                pg1_actions.click(q16_button)
                pg1_actions.move_to_element(q17_button)
                pg1_actions.click(q17_button)
                pg1_actions.move_to_element(q18_button)
                pg1_actions.click(q18_button)
                pg1_actions.move_to_element(q19_button)
                pg1_actions.click(q19_button)
                pg1_actions.move_to_element(q20_button)
                pg1_actions.click(q20_button)
                pg1_actions.move_to_element(q21_button)
                pg1_actions.click(q21_button)

                # Open text elements
                pg1_actions.move_to_element(q22_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q22_comment.send_keys(random.choice(exEmpExpPos))
                elif respSent == 'Neutral':
                    q22_comment.send_keys(random.choice(exEmpExpNeu))
                else:
                    q22_comment.send_keys(random.choice(exEmpExpNeg))

                pg1_actions.move_to_element(q23_comment)
                time.sleep(1)
                if respSent == 'Positive':
                    q23_comment.send_keys(random.choice(exEmpExpPos))
                elif respSent == 'Neutral':
                    q23_comment.send_keys(random.choice(exEmpExpNeu))
                else:
                    q23_comment.send_keys(random.choice(exEmpExpNeg))

                # Submit response
                pg1_actions.move_to_element(pg1_submit)
                pg1_actions.click(pg1_submit)
                pg1_actions.perform()

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

        respGenCount = ex_can_xp(respGenCount, respSent, respGen)

        # Scaling the generation of responses via threading
        def gen_loop (respGen, respGenCount):
            #threads = [] 
            while respGen > respGenCount:
                t1 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t1.start()
                respGenCount +=1
                t2 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t2.start()
                respGenCount +=1
                t3 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t3.start()
                respGenCount +=1
                t4 = threading.Thread(target=ex_can_xp, args=(respGenCount, respSent, respGen))
                t4.start()
                respGenCount +=1
                
                ex_can_xp(respGenCount, respSent, respGen)
                respGenCount +=1

        gen_loop(respGen, respGenCount)

        print('Job complete!')


if __name__ == "__main__":
    main()
