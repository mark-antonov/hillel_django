from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail as django_send_mail

import requests

from .models import Author, Quote


@shared_task()
def no_quotes_send_email(subject, message, from_email, recipient_list):
    """ Sending a message about the absence of new quotes. """
    django_send_mail(subject, message, from_email, recipient_list)


@shared_task()
def scraping_quotes():
    """
    Parsing function https://quotes.toscrape.com to add quotes and their authors to the database (5 quotes at a time).
    If there are no new quotes, an email will be sent. Call no_quotes_send_email().
    """
    url = 'https://quotes.toscrape.com'  # URL for scraping
    number_of_quotes = 5  # Number of quotes at once
    current_number_of_page = 1  # Number of page to start

    while number_of_quotes != 0:
        r = requests.get(f'{url}/page/{str(current_number_of_page)}/')
        soup = BeautifulSoup(r.content, features='xml')
        quotes = soup.findAll('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text

            # Check if quote exist in our base.
            if not Quote.objects.filter(text=text).exists():
                # Get the author of quote url
                author_url_end = quote.find('small', class_='author').find_next_sibling('a').get('href')
                author_url = f'{url}/{author_url_end}'

                author_r = requests.get(author_url)
                author_soup = BeautifulSoup(author_r.content, features='xml')
                author_block = author_soup.find('div', class_='author-details')

                # Get the author of quote title
                name = author_block.find('h3', class_='author-title').text

                # Check if author exist in our base.
                if not Author.objects.filter(name=name).exists():
                    born_date = author_block.find('span', class_='author-born-date').text
                    born_location = author_block.find('span', class_='author-born-location').text
                    description = author_block.find('div', class_='author-description').text

                    # Add author in our base and save.
                    author = Author.objects.create(name=name, born_date=born_date, born_location=born_location,
                                                   description=description)
                else:
                    author = Author.objects.get(name=name)

                # Add quote in our base and save.
                quote = Quote.objects.create(text=text, author=author)
                quote.save()

                # Decrease the number of quotes by 1
                number_of_quotes -= 1

            # If there are no new quotes - send message
            if number_of_quotes != 0 and quote == quotes[-1] and not soup.find('li', class_='next'):
                no_quotes_send_email.delay(subject='Information about quotes',
                                           message='Quotes are over',
                                           from_email='antonov@gmail.com',
                                           recipient_list=['admin@example.com'])
                number_of_quotes = 0
                break

        current_number_of_page += 1
