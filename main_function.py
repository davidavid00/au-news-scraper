import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from sqlite3 import Error
import os
# from pygooglenews import GoogleNews

# gn = GoogleNews(lang = 'en', country = 'AU')

import schedule
import time

#######################################
# DATABASE CHECK/SETUP
#######################################

database_name = 'news_entries.db'
table_name = 'articles'

# Check if the database exists
def database_exists():
    if os.path.isfile(database_name):
        return True
    else:
        print("nothin exists")
        return False


# Create a database and table
def create_database():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    # Create the articles table
    c.execute(f'''CREATE TABLE {table_name} (
                    site TEXT,
                    headline TEXT,
                    desc TEXT,
                    url TEXT
                  )''')
    print("created")
    conn.commit()
    conn.close()

# Check if the database exists, and create it if necessary
if not database_exists():
    create_database()
    print(f"The database '{database_name}' and table '{table_name}' have been created.")
else:
    print(f"The database '{database_name}' already exists.")


#######################################
# Initiate Scrape
#######################################
keywords = ['Queensland']

def news_scrape():
    # List of target news sites
    news_sites = [
        {'name': 'ABC News', 'url': 'https://www.abc.net.au/news/justin'},
        {'name': '7 News', 'url': 'https://7news.com.au/news/vic'},
        {'name': '9 News', 'url': 'https://www.9news.com.au/just-in'},
        {'name': 'Weekly Times Now', 'url': 'https://www.weeklytimesnow.com.au/news/breaking-news'},
        {'name': 'The Land', 'url': 'https://www.theland.com.au/news/'},
        {'name': 'The Riverine Grazier', 'url': 'https://www.thegrazier.com.au/news'},
        {'name': 'Stock Journal', 'url': 'https://www.stockjournal.com.au/news/'}
        # Add more news sites as needed
    ]

    matching_articles = []

    for site in news_sites:
        try:
            response = requests.get(site['url'])
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find relevant HTML elements containing news articles
            abc_div = soup.find_all('div', class_='CardLayout_content__bev76')
            seven_div = soup.find_all('div', class_='css-1n26x9e-StyledBauhausCard')
            nine_div = soup.find_all('div', class_='story__wrapper')
            weeklytimes = soup.find_all('article', class_='storyblock')
            land_div = soup.find_all('div', class_='w-full py-5.5')
            grazier = soup.find_all('article', class_='blog-basic-grid--container')

            if abc_div:
                for article in abc_div:
                    headline_element = article.find('a')
                    description_element = article.find('div', class_='Typography_base__k7c9F GenericCard_synopsis__iPZsQ Typography_sizeMobile14__2WyUY Typography_lineHeightMobile24__xwyV0 Typography_regular__Aqp4p Typography_colourInherit__xnbjy')

                    if headline_element:
                        
                        headline = headline_element.get_text()
                        description = description_element.get_text()
                        article_url = article.find('a')['href']

                        # print(headline)
                        # print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url})
            elif seven_div:
                for article in seven_div:
                    headline_element = article.find('span', class_='css-e1a8nq-StyledHeadlineText')
                    # description_element = article.find('div', class_='Typography_base__k7c9F GenericCard_synopsis__iPZsQ Typography_sizeMobile14__2WyUY Typography_lineHeightMobile24__xwyV0 Typography_regular__Aqp4p Typography_colourInherit__xnbjy')

                    if headline_element:
                        
                        headline = headline_element.get_text()
                        description = description_element.get_text()
                        article_url = article.find('a')['href']

                        # print(headline)
                        # print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url})
            elif nine_div:
                for article in nine_div:
                    headline_element = article.find('span', class_='story__headline__text')
                    description_element = article.find('div', class_='story__abstract')
                    # print(description_element)
                    if headline_element:
                        
                        headline = headline_element.get_text()
                        description = description_element.get_text()
                        article_url = article.find('a')['href']

                        # print(headline)
                        # print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url})
            elif weeklytimes:
                for article in weeklytimes:
                    headline_element = article.find('h4', class_='storyblock_title')
                    description_element = article.find('p', class_='storyblock_standfirst g_font-body-s')
                    # print(description_element)
                    if headline_element:
                        
                        headline = headline_element.get_text()
                        description = description_element.get_text()
                        article_url = article.find('a')['href']

                        # print(headline)
                        # print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url})
            elif land_div:
                for article in land_div:
                    headline_element = article.find('a')
                    # description_element = article.find('p', class_='storyblock_standfirst g_font-body-s')
                    # print(description_element)
                    if headline_element:
                        
                        headline = headline_element.get_text()
                        # description = description_element.get_text()
                        article_url = article.find('a')['href']

                        # print(headline)
                        # print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':"n/a", 'url': article_url})
            elif grazier:
                for article in grazier:
                    headline_element = article.find('h1')
                    description_element = article.find('div', class_='blog-excerpt-wrapper')
                    # print(description_element)
                    if headline_element:
                        # print(headline_element)
                        headline = headline_element.get_text().replace("\n","").strip()
                        description = description_element.get_text()
                        article_url = article.find('a')['href']

                        # print(headline)
                        # print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url}) 


        except Exception as e:
            print(f"Error scraping {site['name']}: {str(e)}")
    
    if matching_articles:
        print(matching_articles)
        database_update(matching_articles)
        # send_email_notification(matching_articles)

#######################################
# SEARCH THE DATABASE FOR EXISTING
#######################################

def database_update (articles):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    # check if url exists
    existing_urls = set()
    c.execute("SELECT url FROM articles")
    rows = c.fetchall()
    for row in rows:
        existing_urls.add(row[0])


    for article in articles:
        if article['url'] not in existing_urls:
            c.execute("INSERT INTO articles (site, headline, desc, url) VALUES (?, ?, ?, ?)",
                      (article['site'], article['headline'], article['desc'], article['url']))
            send_email_notification(article)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    

# def search_google():
#     tnc = gn.search('"The Nature Conservancy"', when = '1h')
#     print(tnc)

# search_google()

#######################################
# SEND AN EMAIL
#######################################

def send_email_notification(article):

     # Add email credentials from the credentials.txt file
    with open('credentials.txt', 'r') as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split('=')
            credentials[key] = value

    username = credentials['username']
    password = credentials['password']
    recipient_email = credentials['to']
    server = credentials['smtp']
    port = credentials['port']



    # Compose email 
    body = f"{article['site']} - {article['headline']}\n URL: {article['url']}"
    subject = f"News Articles from {article['site']}"

    # Create email message
    message = MIMEMultipart()
    message['From'] = username
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SMTP server and send email
        server = smtplib.SMTP(server, port)
        server.starttls()
        server.login(username, password)
        server.send_message(message)
        server.quit()

        print("Email notification sent successfully!")

    except Exception as e:
        print(f"Error sending email notification: {str(e)}")

#######################################
# INITIATE AND SCHEDULE
#######################################

news_scrape()
# Schedule the script to run every hour
schedule.every().hour.do(news_scrape)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
