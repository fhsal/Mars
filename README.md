# Mars

CWRU Data Analytics Module Ten Challenge


## Overview of Project

The project involved scraping data from several internet sites regarding the planet Mars, storing that data using Mongo and then displaying that data on a web page.  

### Summary

The effort involved using Chrome developer tools to inspect pages and identify elements to scrape using Beautiful Soup to scrape.  The elements captured included news headings, article summaries, featured images and images of the different hemispheres of the Red Planet.  The data was stored in a Mongo database and the pages were rendered using Splinter and Flask with css from Bootstrap - plus I added my own local css for further customization.  

## Major components of the work:

* Deliverable 1: using a jupyter notebook to step-wise scrape news title, article summary and featured image  

* Deliverable 2: exporting the jupyter notebook to a py file and updating it to create functions to automate scraping through the web sites and looping through the html to grab hemisphere images from an additional site, storing that image information and metadata in Mongo.  That data was then read from Mongo and displayed on a page rendered using Flask  

* Deliverable 3: adding Bootstrap formatting to the page, including changing the styling of the scrape button, jumbotron and turning the hemisphere images into a single row similar to thumbnails. 

## Rendered page and Mongo database images

# Page header with jumbotron and button styled using style.scc

![img](https://github.com/fhsal/Mars/blob/main/images/jumbotron.png)


# Page body with news summary, main image and table of facts

![img](https://github.com/fhsal/Mars/blob/main/images/mid-page.png)


# Hemisphere images shown in a single row using Bootstrap

![img](https://github.com/fhsal/Mars/blob/main/images/hemispheres.png)


# Mongo database with stored hemisphere information

![img](https://github.com/fhsal/Mars/blob/main/images/mongo.png)

