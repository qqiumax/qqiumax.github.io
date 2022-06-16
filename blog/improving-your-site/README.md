# Part05: Improving Your Blog Site&SEO
## In the [last class](https://qqiumax.github.io/blog/adding-directories) you should already have a bunch of folders like this: 
![image01](https://qqiumax.github.io/blog/improving-your-site/improve1.png)
## Today will be about how to improve your own website!
## **1.Customize a 404 page**
## 1. create a .md file called 404.md in your **root** path, not anywhere else.
## 2. Write whatever you want to write in markdown.
## 3. And you are done!
## **2.Setting up google analytics**
## 1. Go to <https://analytics.google.com> and sign up with your google account, you might need a VPN or Proxy if you are in a censored country.
## 2. Follow the directions, but **click "advanced settings" and choose Universal analytics** Ignore the warnings
## 3. get your tracking code, should be like UA-xxxxxxxxx-x
## 4. Open your _config.yml file with notepad, and add a line called <code>google_analytics: UA-xxxxxxxxx-x</code>, replace the UA-xxxxxxxxx-x with your own tracking code.
## 5. And you are done!
## **3.improve your _config.yml file**
## 1. add a line called <code>description: xxx</code> replace xxx with a fluent, summurative, keyword-rich description of your whole website.
## 2. add a line called <code>author: xxx</code> replace xxx with your name.
## 3. And you are done!
## **4.add a sitemap**
## 1. Use xml format, create a thing called sitemap.xml, open it with wordpad.
## 2. follow the format below:
![image02](https://qqiumax.github.io/blog/improving-your-site/improve2.png)
## 3. Go [here](https://www.sitemaps.org/) for more information.
## **5.Add a robots.txt**
## 1. create a file called robots.txt
## 2. if you want to block a site from crawl: use 

    User-Agent: *
    Disallow: site_URL_you_wanna_block

## 3. Add a line called: <code>Sitemap: sitemap_URL_you_just_created</code>
## 4. And you are done!

## **After you have done everything, open git bash, type:**

    git add *
    git commit -a (add an another -S here in you have gpg key) -m "a-note-for-change"
    git push origin main

## **And you are done!**
## Next class we are going to learn to publish your site on search engines like google and bing!

[back](https://qqiumax.github.io/blog/)


###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright Max Qiu 2022. All Rights Reserved.