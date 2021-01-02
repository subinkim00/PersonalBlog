# Personal Blog
By Subin Kim

## Overview
This project is a personal blog page built with Django!

## How to run:
1. pip install all necessary packages
2. Run 'python manage.py runserver' in the terminal
3. Open up the local server link found in the terminal

## Routes and Description
- **admin/** : allows for administrative management of webapp
- **/** : (implicit slash) splash page with an introduction and an overview of all blog posts
- **post/** : routes user to page showing the blog post specified by the request.GET "id". If the id specified by the user does not exist, the user is redirected to the splash page

## Attributions:
I used a free online responsive HTML5 template from templated.co for the page design.