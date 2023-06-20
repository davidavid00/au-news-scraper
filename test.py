import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from pygooglenews import GoogleNews

# gn = GoogleNews(lang = 'en', country = 'AU')



# import schedule
# import time

def scrape_and_send_email():
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

    # Keywords to search for
    keywords = ['Father']

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
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url})
            elif grazier:
                for article in grazier:
                    headline_element = article.find('h1')
                    description_element = article.find('div', class_='blog-excerpt-wrapper')
                    # print(description_element)
                    if headline_element:
                        
                        headline = headline_element.get_text()
                        description = description_element.get_text()
                        article_url = article.find('a')['href']

                        print(headline)
                        print(description)
                        # Check if any keyword matches the headline
                        if any(keyword.lower() in headline.lower() for keyword in keywords):
                            matching_articles.append({'site': site['name'], 'headline': headline, 'desc':description, 'url': article_url})
            

            # if articles:
            #     for article in articles:
            #         headline_element = article.find('h3', class_='title')

            #         if headline_element:
            #             headline = headline_element.get_text()
            #             article_url = headline_element.find('a')['href']

            #             # Check if any keyword matches the headline
            #             if any(keyword.lower() in headline.lower() for keyword in keywords):
            #                 matching_articles.append({'site': site['name'], 'headline': headline, 'url': article_url})
            # else:
                # section for ABC articles
                
                
            

        except Exception as e:
            print(f"Error scraping {site['name']}: {str(e)}")
    
    if matching_articles:
        print(matching_articles)

        # send_email_notification(matching_articles)
scrape_and_send_email()
# def search_google():
#     tnc = gn.search('"The Nature Conservancy"', when = '1h')
#     print(tnc)

# search_google()


# def send_email_notification(articles):
#     # Email configuration
#     sender_email = 'your_email@example.com'
#     sender_password = 'your_password'
#     recipient_email = 'recipient_email@example.com'

#     subject = 'News Articles Matching Keywords'

#     # Compose email body
#     body = ''
#     for article in articles:
#         body += f"{article['site']} - {article['headline']}\n"
#         body += f"URL: {article['url']}\n\n"

#     # Create email message
#     message = MIMEMultipart()
#     message['From'] = sender_email
#     message['To'] = recipient_email
#     message['Subject'] = subject
#     message.attach(MIMEText(body, 'plain'))

#     try:
#         # Connect to SMTP server and send email
#         server = smtplib.SMTP('smtp.example.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.send_message(message)
#         server.quit()

#         print("Email notification sent successfully!")

#     except Exception as e:
#         print(f"Error sending email notification: {str(e)}")


# # Schedule the script to run every hour
# schedule.every().hour.do(scrape_and_send_email)

# # Run the scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(1)