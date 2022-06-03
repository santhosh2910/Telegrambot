#Import the libraries.
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import xlrd

#Create lists to store the scraped data
authors=[]
quotes=[]
#Createafunction to scrape the website
def scrape_website(page_number):
  page_num = str(page_number)
  URL='https://www.goodreads.com/quotes/tag/inspirational?page='+page_num
  webpage=requests.get(URL) #Makearequest to the website
  soup=BeautifulSoup(webpage.text,'html.parser') #Parse the text from the website
  quoteText=soup.find_all('div',attrs={'class':'quoteText'})

  for i in quoteText:
    quote = i.text.strip().split('\n')[0] #Get the quotes
    author = i.find('span',attrs={'class':'authorOrTitle'}).text.strip() #Get the author
    quotes.append(quote)
    authors.append(author)

#Loop through'n'pages and scrape the data
n = 5
for num in range(0,n):
  scrape_website(num)

#Combine the lists
combine_list=[]
#Loop through the quotes list and combine it with the authors list
for i in range(len(quotes)):
  combine_list.append(quotes[1]+'-'+authors[i])

print(combine_list)

# df = pd.DataFrame({'Quotes':quotes}) 
# df.to_csv('Quotes.csv', index=False, encoding='utf-8') 
