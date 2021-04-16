# Final_Project

This is My Final Project as Student at Telkom University with Computer Engineering major

My Final Project is about "ONLINE NEWS TEXT ANALYSIS ON STOCK MOVEMENT USING SUPPORT VECTOR MACHINE ALGORITHM" (Indonesian Stock Only)
My data is from "The Traders" Telegram Groups, so the goal is the program will listen to the group and will classifie the sentiment (Positive or Negative)

I am using Selenium to scrape my data through telegram chat, the file is "scrap_tele_sehari.py".
if you want to use the scraping code, you have to change the firefox profile in "myprofile" variable, geckodriver path in "PATH" variable.
and you have to change the link to your telegram group in line 20
The scraping code will scrape chat per day, so in variable "target" you have to set the how many day you want to scrape the chat.

And the process of the algorithm is in folder "komplit2"
