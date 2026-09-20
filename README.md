# My personal page

### Site for showcase of my projects, resume, etc.

![image of my site](showcase.png)

## [try me](https://danb1551.cz/)

## Features

 - Showcase of my projects
 - My resume
 - Services that I can provide
 - How to contact me information
 - at /lookup endpoint returning number of visitors (only that visited / (root) endpoint)

## Dependencies

 - docker
 - compose plugin installed in docker

## How to run

###### well, that page is with information of me so you must change the text in HTML

```bash
docker compose run
```

the page will be available at adress that is shown in the terminal

## How it works

I used flask librar in python, because flask is simple to use and it can render Jinja templates. Thanks to Jinja rendering I don't need to edit HTML that is used in header in every single HTML file but I just edit base.html file and the change will be visible everywhere