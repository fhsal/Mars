#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[28]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[29]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[30]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[31]:


slide_elem.find('div', class_='content_title')


# In[32]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[33]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[34]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[35]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[36]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[37]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[38]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[39]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[40]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[41]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[42]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[43]:


# Parse the data
hemi_html = browser.html
hemi_soup = soup(hemi_html, 'html.parser')

# Retrieve all items for hemispheres information
items = hemi_soup.find_all('div', class_='item')


# In[46]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

main_url = 'https://marshemispheres.com/'

for image in items:
        hemisphere = {}
        titles = image.find('h3').text
    # link for full image
        link_ref = image.find('a', class_='itemLink product-item')['href']
    # Use the base URL to create an absolute URL
        browser.visit(main_url + link_ref)
    # parse the data
        image_html = browser.html
        image_soup = soup(image_html, 'html.parser')
        download = image_soup.find('div', class_= 'downloads')
        img_url = main_url + download.find('a')['href']
    
        print(titles)
        print(img_url)
    
    # add to list
        hemisphere['img_url'] = img_url
        hemisphere['title'] = titles
        hemisphere_image_urls.append(hemisphere)
        browser.back()


# In[ ]:





# In[47]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[48]:


# 5. Quit the browser
browser.quit()


# In[ ]:




