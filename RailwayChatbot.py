import random
import re
import requests
import json

from pip._vendor.distlib.compat import raw_input

#-----------------------------------ALL THE MESSAGES---------------------------------

greetings = ['hello', 'hi', 'hey', 'hey!','hola','hello','namaste']
random_greetings = random.choice(greetings)

question1 = ['how are you?','how are you','how do you do','how do you do?','how are you feeling']
reply = ['i am fine, how are you','I am good, how are you?','I am great, how are you?']
random_reply = random.choice(reply)

how = ['i am great','i feel good','i am nice']
howreply=['That is great to know!','Glad you feel that way!']
randomhowreply=random.choice(howreply)

question2 = ['what is your name ?','what is your name','your name please','your name']
intro = ['I am Hazard','My name is Hazard']
random_intro = random.choice(intro)

question3 = ['what is your job?','who are you','who are you?','your job','your work','your job?','your work?','what do you do']
working = ['I am a railway reservation chatbot','I am a chatbot and I give details regarding trains']
random_working = random.choice(working)

question4 = ['check live station']
responses = ['Sure!','As you say']
random_response = random.choice(responses)

question5=['what can you do']
           
question6 = ['trains travelling through the station','find trains through the station','trains between']

question7= ['search for station','station information','information on station']

question8 = ['station on map','where is this station on the map']

question9=['trains cancelled','what all trains were cancelled']

question10=['coach layout','show me the coach layout']

thanks=['thank you','thank you so much','good job']
thanksresponse=['you are most welcome, any other help?','My pleasure, can i help you with something else']
randomthanks=random.choice(thanksresponse)

compliment = ['You are welcome']
random_compliment = random.choice(compliment)

bye=['bye','bye bye']

#----------------------------------------------------------------------------------------


#api key: 22c585f486f96802e627b345f5646ffa
    
        
print()
print("Hello i am Hazard, Manan's chatbot")
while True:
    print()
    userInput = input(">> ")
    userInput=userInput.lower()
    if userInput in greetings:
        print(random_greetings)
        
    elif userInput in how:
        
        print(randomhowreply)
        
    elif userInput in question1:
        print(random_reply)
        
    elif userInput in question2:
        print(random_intro)
        
    elif userInput in question3:
        print(random_working)
        
    elif userInput in question4:
        print(random_response)
        code=input("Enter station code: ")
        hours=input("Within how many hours: ")
        r1=requests.get('https://indianrailapi.com/api/v2/LiveStation/apikey/22c585f486f96802e627b345f5646ffa/StationCode/'+code+'/hours/'+hours)
        data1=r1.json()
        message=data1['Message']
        print(message)
        trains=data1['Trains']
        print("These were")
        if(trains==None):
            print("No Train")
        else:
            for x in trains:
                print(x['Number']+' '+ x['Name'])
        
  
        
    elif userInput in question5:
        print("I can do the following\n 1.Check live stations\n 2.Search for a station and give details\n 3.Show where the station is on the map\n 4.Return all the cancelled trains on a date\n 5.Check Trains Passing through a station\n 6.Check coach layout")
        
    
        
    elif userInput in question6:
        code=input("Enter station code: ")
        r2 = requests.get('http://indianrailapi.com/api/v2/AllTrainOnStation/apikey/22c585f486f96802e627b345f5646ffa/StationCode/'+code)         
        data2 = r2.json()
        ListOfTrains = data2['Trains']
        for x in ListOfTrains:
          print('The train '+x['TrainName']+ ' ' +x['TrainNo'])
            
    elif userInput in question7:
        print("Sure! Please enter your station code which you want to search for")
        code=input("Enter station code: ")
        r1=requests.get("https://indianrailapi.com/api/v2/AutoCompleteStation/apikey/22c585f486f96802e627b345f5646ffa/StationCodeOrName/"+code)
        data1 = r1.json()
        stationinfo=data1['Station']
        print(stationinfo)
        
    elif userInput in question8:
         print("Staion on map")
         code=input("Please enter station code")
         r1=requests.get("https://indianrailapi.com/api/v2/StationLocationOnMap/apikey/22c585f486f96802e627b345f5646ffa/StationCode/"+code)
         data1=r1.json()
         mapstation=data1["URL"]
         print(mapstation)
        
    elif userInput in question9:
        print("You can search for cancelled trains")
        date=input("Please enter date to see cancelled trains: ")
        r1=requests.get("https://indianrailapi.com/api/v2/CancelledTrains/apikey/22c585f486f96802e627b345f5646ffa/Date/"+date)
        data1=r1.json()
        cancelledtrains=data1["Trains"]
        for x in cancelledtrains:
            print('The train '+x['TrainName']+' and number' +x['TrainNumber']+ ' was cancelled')
        
    elif userInput in question10:
        print("You can see the coach layout")
        number=input("Enter Train number please: ")
        r1=requests.get("https://indianrailapi.com/api/v2/CoachLayout/apikey/22c585f486f96802e627b345f5646ffa/TrainNumber/"+number)
        data1=r1.json()
        print("The coach layout for the train", number, "is: ")
        coach=data1["Coaches"]
        for x in coach:
            print(x['SerialNo']+' '+ x['Name']+' '+ x['Number'])
            
    elif userInput in thanks:
        print(randomthanks)
        
    elif userInput in bye:
        print("Thank you, Looking forward to seeing you again")
        exit()
    
    
        
    
    else:
      print("I did not understand what you said, can you please repeat")


#NDLS=New Delhi
#SBC=bangalore
#GZB=Ghaziabhad

