from splinter import Browser
from bs4 import BeautifulSoup
import time 
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:\Chromesafe\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def mars_news():

    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('div', class_='content_title').text
    para = soup.find('div', class_='article_teaser_body').text
 
    News_dict = {"Headline": title,"Details": para}
    return News_dict


def featured_image():

    browser = init_browser()

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)

    # Moving through the pages
    time.sleep(10)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get featured image
    results = soup.find('article')
    extension = results.find('figure', 'lede').a['href']
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension
    featured_Image_dict = {"image": featured_image_url}

    return featured_Image_dict

def Weather_tweet():
    
    browser = init_browser()
    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tweet_url)



    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweeter = soup.find('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = tweeter.text
    mars_weather_dict = {"mars_weather": mars_weather }

    return mars_weather_dict

def Mars_Facts_table():
    
    browser = init_browser()

    df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

    df_Mars_Facts = df_Mars_Facts[0]

    df_Mars_Facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    df_Mars_table = df_Mars_Facts.to_html("Mars_Facts_Table.html")



    df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_table}



    return df_Mars_Facts_dict

def hemisphere_images():
    image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    full_hemisphere_dict = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

    return full_hemisphere_dict