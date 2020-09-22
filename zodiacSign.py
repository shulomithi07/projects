import requests #importing requests
import bs4      #importing beautifulSoup4

# Getting the site content and storing it in the rquest
rquest = requests.get('https://www.astrology.com/horoscope/daily.html')

# Converting request class to beautifulSoup4 class)
soup = bs4.BeautifulSoup(rquest.text,'lxml')

# declaring an empty list to store links
links = []

# Find the data from the site by telling bs4 where to search i.e; in the div of class signs
for data in soup.find_all('div', class_='signs'):
    
    # getting all the anchor tags
    for a in data.find_all('a'):
    
        # appending the href attributes in the links list
        links.append(a.get('href')) #for getting link

# looping the content for the repeatation of the task
user_input = True
while user_input == True:
    print('\n')
    print("Choose your sign:\n")

    print('''
    1.aries
    2.taurus
    3.gemini
    4.cancer
    5.leo
    6.virgo
    7.libra
    8.scorpio
    9.sagittarius
    10.capricorn
    11.aquarius
    12.pisces''')

    print('\n')
    n = int(input('Enter your sign\'s number: ' ))

    print('\n')

    # # Defining a function for the process of printing the desired output
    def zodiac(n):
        '''The site which i used for crawling updates its daily content a bit slower '''
        output = []

        # by taking the user input again requesting the links of the particular signs
        if n == 1:
            res = requests.get(links[0])

        elif n == 2:
            res = requests.get(links[1])

        elif n == 3:
            res = requests.get(links[2])

        elif n == 4:
            res = requests.get(links[3])
        
        elif n == 5:
            res = requests.get(links[4])
        
        elif n == 6:
            res = requests.get(links[5])
            
        elif n == 7:
            res = requests.get(links[6])
            
        elif n == 8:
            res = requests.get(links[7])
            
        elif n == 9:
            res = requests.get(links[8])
        
        elif n == 10:
            res = requests.get(links[9])
        
        elif n == 11:
            res = requests.get(links[10])

        elif n == 12:
            res = requests.get(links[11])
        
        else:
            return  f'i guess you entered a wrong number'
        
        soup = bs4.BeautifulSoup(res.text,'lxml')

        # getting the horoscope from the below mentioned class
        
        for data in soup.find_all('div',class_ = 'horoscope-main grid grid-right-sidebar primis-rr'):
        
            # getting all the p tags
        
            for text in data.find_all('p'):
        
                # Getting the text from p tag and appending it to the output
        
                output.append(text.getText())
                break    
        return output[0] #returning the text 
        
    print(zodiac(n))

    # Taking the input from user to try once again 
    user_input = True if(input("\nDo you want to Try again ? (yes/no)\n")) == 'yes' else False
