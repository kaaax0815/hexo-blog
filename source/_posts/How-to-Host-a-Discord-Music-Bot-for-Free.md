---
title: How to Host a Discord Music Bot for Free
date: 2021-03-08 17:26:10
tags:
- Discord
- Hosting
- Free
categories: 
- Tutorials
---
[comment]: <> (Make "PRO Section", where you can change Bot Image and stay online)

Today, I'll show you how to Host a Discord Music Bot for Free. Its 100% Free, requires minimal coding experience and doesn't take long.

## 1. Hosting

The easiest way is to use Repl.it, because its simple and completely free. If you want you could use Heroku or Glitch.

Create Account on [repl.it](https://repl.it/signup)

The easiest way is to use a Social Media Login. Github, Google or Facebook. I will use Google
{% asset_img msedge_uaeH0Qkayy.png.webp Repl.it Installation %}
Press Enter on the first one to keep the current one or edit it as you like
Press "yes" if the email address is the one you want to use
The other things don't matter. Select what I use or whatever you want

## 2. Create Discord Bot

You will need a TOKEN from Discord to set up the Bot
Go to the [Discord Developer Portal](https://discord.com/developers/applications/)
Click in the Right Corner on "New Application"
{% asset_img msedge_pvgz9b6miE.png.webp Discord Application %}
Now Enter a Name for the Bot

### IMPORTANT! This is the Name everybody will see on the Server. Choose something like `yourname`Bot. I named mine "berndMusicBot"

Click on "Create".
Under Client ID click on "Copy" and write it down somewhere. You'll need it for later
Now click on "Bot" on the left side and click "Add Bot" and confirm with "Yes, do it!"
To get the TOKEN click on "Click to Reveal Token"
{% asset_img msedge_LTbfXYDwE9.png.webp Discord Token %}
Click on "Copy" and write it down somewhere safe. Alternatively you could leave to Tab open. You'll need it for later

### IMPORTANT! This is the Token where if somebody has it can control your bot completely. So dont share it!

## 3. Configure Music Bot

The best Music Bot which you can easily host is [SudhanPlayz/Discord-MusicBot](https://github.com/SudhanPlayz/Discord-MusicBot)
![](ezgif-4-9ee9b32578c2.webp)

If you want a [Youtube Video](https://link.kaaaxcreators.de/9jo8Ha) by the Author himself you can watch it [here](https://link.kaaaxcreators.de/9jo8Ha)
I will use a modified version, better for 24/7 and without ads
Click here to run it on Repl: [![Run on Repl.it](https://repl.it/badge/github/kaaaxcreators/discordjs)](https://repl.it/github/kaaaxcreators/discordjs)

After clicking on the Button, the Github Repo will be cloned to Repl.it. After a while you should see something like this:
{% asset_img msedge_xjvlu1XLvf.png.webp Repl.it Repl %}

We will create a file called ".env". This is where we put our Token. The Prefix is a String which needs to be before every command. For PREFIX="!" you would call the Bot with !play, For PREFIX="lol" you would call the Bot with lolplay

Create a file
{% asset_img msedge_j2KaM5ZA9o.png.webp Create File %}
Now type `.env`

Copy and Insert the Following Code
```ini
TOKEN="<yourtoken>"
PREFIX="<yourprefix>"
```
In my Case it is:
```ini
TOKEN="ODE4NTI1MDU5NDU0MzM3MDY1.YEZU3Q.GQ4YO-ai9IXrOqkQLrUG0A2iOPA"
PREFIX="="
```
Now you simply press:
{% asset_img msedge_2PyzEy6e6N.png.webp Run %}

This might take a while for the first time, because it needs to download and install many packages

When it is done you should see "[API] Logged in as `your bot name`"

If not type in the Console `npm i`. If this doesn't fix it, leave a Comment or write me on any Social Media

## 4. Add Bot to Server
I assume that you have a Discord Server
Copy the URL and insert it into a new TAB. Replace %CLIENTID% with your Bot ID from earlier
https://discord.com/oauth2/authorize?client_id=%CLIENTID%&scope=bot&permissions=2146954879
In my case it is:
https://discord.com/oauth2/authorize?client_id=818525059454337065&scope=bot&permissions=2146954879

{% asset_img msedge_Tb1SryfxxT.png.webp Add Bot to Server %}

Select Server in Dropdown and Click "Continue"
Scroll down and Click "Authorize"
Pass the Captcha and you are done with Configuration

Go into the Discord Server and type `yourprefix`help
Now you will see all commands and how to use theme
To play a song join a Voice Channel and type `yourprefix`play `search request`
Example: =play rick astly never gonna
If you don't want to hear any more, simply type `yourprefix`leave and your bot will leave the Voice Channel

## 5. Personalize
Open Folder "events" and open File "ready.js"
Replace:
```javascript
await client.user.setActivity("kaaaxcreators.de | §help", {
```
With:
```javascript
await client.user.setActivity("%YOUR PRESENCE%", {
```
Replace %YOUR PRESENCE% with what you want under your bot to show
{% asset_img Discord_x5KbKxdDuP.png.webp Discord Presence %}

## 6. Stay Online 24/7
On the right you'll see something like this
{% asset_img msedge_lKfca36uNK.png.webp Repl Online %}
Copy the URL you'll need it for later
Repls sleeps usually after 30 minutes
To keep the awake we will use something called cronjobs. It will simulate a Person going to the URL so the Bot stays online forever
For this we will create an account on [cron-job.org](https://cron-job.org/en/signup/)
Enter the Fields, Only Password and Email matters.
If you want to use a Temp-Mail you can use my [Temp-Mail Service](https://emailfake.com/kaaaxcreators.tk)
Activate your Account through the URL in the Mail you received
Now Press [log in](https://cron-job.org/en/members/)
Enter Email and Password from the Registration
Click on "[Cronjobs](https://cron-job.org/en/members/jobs/)" and click on "Create cronjob" on the right

Title: `<anything>`
URL: `<url from repl.it>` my case: `https://discordjs.berndi33hdoders.repl.co`
Leave everything else as Default
Scroll down and click on "Create cronjob"
Now every 15 Minutes your Repl receives a request and stays awake

## Optional: Change Avatar

If you want a different Avatar then the default
Go to the [Discord Developer Portal](https://discord.com/developers/applications)
Click on your Bot
Click on "Bot" on the right
Under "Icon" click the Image, now you can choose from any Image on your PC
Now my Bot has a different avatar
{% asset_img Discord_8nk1hvE1cN.png.webp New Avatar %}

## Extra: SoundCloud
Coming Soon
Doesn't currently work because SoundCloud doesn't accept new Applications