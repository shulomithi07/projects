import requests  # importing requests
import bs4  # importing beautifulSoup4

def get_data():
    # Getting the site content and storing it in the rquest
    rquest = requests.get('https://www.astrology.com/horoscope/daily.html')

    # Converting request class to beautifulSoup4 class)
    soup = bs4.BeautifulSoup(rquest.text, 'lxml')

    # declaring an empty list to store links
    links = []

    # Find the data from the site by telling bs4 where to search i.e; in the div of class signs
    for data in soup.find_all('div', class_='signs'):

        # getting all the anchor tags
        for a in data.find_all('a'):

            # appending the href attributes in the links list
            links.append(a.get('href'))  # for getting link
    return links

# Getting the Zodiac Data
def zodiac(n):
    '''The site which i used for crawling updates its daily content a bit slower '''
    output = []
    links = get_data()

    # Requesting the links of the particular signs with given user input.
    if (n not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
        return f'i guess you entered a wrong number'
    else:
        n -= 1
        for i in range(0, 13):
            if n == i:
                res = requests.get(links[i])
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    # getting the horoscope from the below mentioned id
    for data in soup.find_all('div', id='content'):
        # getting all the p tags
        for text in data.find_all('p'):
            # Getting the text from p tag and appending it to the output
            output.append(text.getText())
            break
    return output[0]  # returning the text

# Defining a function for the process of printing the desired output
def print_data(user_input):
    # looping the content for the repeatation of the task
    while user_input == True:
        print('\n')
        print("Choose your sign:\n")

        for i in ["1.aries", "2.taurus", "3.gemini", "4.cancer", "5.leo", 
                  "6.virgo", "7.libra", "8.scorpio", "9.sagittarius", 
                  "10.capricorn", "11.aquarius", "12.pisces"]:
            print(i)
            
        print('\n')
        n = int(input('Enter your sign\'s number: '))
        print('\n')
        print(zodiac(n))

        # Taking the input from user to try once again
        user_input = True if(
            input("\nDo you want to Try again ? (yes/no)\n")) == 'yes' else False


print_data(True)
