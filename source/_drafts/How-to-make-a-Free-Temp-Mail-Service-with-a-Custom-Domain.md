---
title: How to make a Free Temp Mail Service with a Custom Domain
tags:
- Mail
- Custom Domain
- Free
categories: 
- Tutorials
---

## 1. Create Free Domain

Goto [Freenom](https://www.freenom.com/en/index.html?lang=en) to create a Free Domain
{% asset_img msedge_9118U8Eiuy.png Freenom Homepage %}

In here enter the Domain you like without the [TLD](https://de.wikipedia.org/wiki/Top-Level-Domain), I'll use `bloginator`
`.tk, .ml, .ga, .cf` are available and for free.
Because I like `.tk` the most I choose it, but you can choose whatever you like.
To get the Domain click on "Get it now!". Then click on the green Button "Checkout"
{% asset_img msedge_sb0CMVOPzk.png Cart%}
Select Period "12 Months @ FREE" and press "Continue"
You have to create an account for this, you can either use another Tempmail Service or login with Google or Facebook. I'll use another Tempmail Service called [Temp Mail](https://temp-mail.org/en/) the problem with such Tempmail Services is that their domains are often banned, which with a Custom Domain wont be happening.
I entered my Email Address and pressed "Click to Verify" Now I got a Email, where I have to click on a link.
Now they ask for personal details, but because I want to be unknown, I'll use a [Fake Name Generator](https://en.fakenamegenerator.com/).

### IMPORTANT: You aren't safe be using a Fake Name Generator, use a Tor Browser, VPN and Security Addons to really hide yourself

I just copy the Details from the Generator into the Form. As Country and State I just use anything. And Lastly I choose a Password, Agree to the Terms and press on "Complete Order"

Now I have to [sign in](https://my.freenom.com/clientarea.php) again.
Goto "Services","My Domains" to modify your domain
{% asset_img msedge_TONiwO850H.png My Domains%}

Now you see your Domain, to edit its DNS Records click on "Manage Domain" and "Manage Freenom DNS"

## 2. DNS Records

Leave "Name" empty
For "Type" choose `MX`
For "TTL" choose `86400`
For "Target" enter `emailfake.com`
For "Priority" enter `1`

Click on "Save Changes"

## 3. Fake Email

Goto `https://emailfake.com/<your-domain>`
Mine would be `https://emailfake.com/bloginator.tk`

If you see
{% asset_img msedge_mR8JPcGtf5.png Address is not valid %}
wait for a couple minutes or hours and enter the your URL again

After a few minutes there is "Address is valid (uptime 96 days)"

Now you can copy your Email Address and use it for any service you like

## 4. Get Emails

To get Emails press this button:

{% asset_img msedge_8fX3mCp8It.png Button %}

## Extra: Website

You know could also use e.g. [000webhost](https://www.000webhost.com/) to create a Free Website and use your Domains to access it.
You can also use Cloudflare DNS for Caching and better Interface
