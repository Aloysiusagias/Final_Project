from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
from Pre2 import Preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from svm import svm
import json
from selenium.webdriver.firefox.options import Options

def userNulll(driver, urut):
    penulis = ''
    while(penulis == ''):
        joinn = False
        balas = ''
        penulis = ''
        last = penulis
        pesan2 = [""]
        jam = ''
        pesan2 = []
        pesan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(urut)+"]")
        driver.execute_script("arguments[0].scrollIntoView(true);", pesan)
        urut -= 1
        if (len(pesan.find_elements_by_xpath(".//a[@class='im_message_photo_thumb']")) > 0) :
            # print('ini adalah foto')
            penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
        elif (len(pesan.find_elements_by_xpath(".//span[@ng-switch-when='messageActionChatJoined']")) > 0):
            # print('seseorang join')
            penulis = ''
        elif (len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_split_text']")) > 0):
            if((len(pesan.find_elements_by_xpath(".//div[@class='im_message_date_split im_service_message_wrap' and @style='display: none;']")) > 0)):
                if(len(pesan.find_elements_by_xpath(".//div[@class='im_message_text']"))>0):
                    # print('Ini juga sebenernya pesan biasa')
                    penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
            elif(len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_text nocopy']"))>0) :
                # print("ini adalah tanggal")
                penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
            else :
                # print('seseorang join')
                penulis = 'join'
        elif(len(pesan.find_elements_by_xpath(".//span[@ng-bind='::historyMessage.date | time']"))>0 or len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_text nocopy']"))>0) :
            # print('ini adalah pesan biasa')
            penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
        else :
            # print('seseorang join')
            penulis = 'join'
    return penulis