# HacknRoll: Autoshelf

<img width="500" alt="Capture" src="https://user-images.githubusercontent.com/45474952/72673726-7e3c8180-3aa9-11ea-9c42-19015f10bfff.PNG">


## Inspiration
Exactly like what the elevator pitch describes. As the world becomes more interconnected, with retail becoming increasingly digital, there are local businesses suffering. These old shops tend to sell their goods at reasonable prices, with some even carrying deadstock which may prove to be more valuable. The biggest problem that they face is the lack of awareness, which is certainly not helped by the tendency to carry non-branded goods (such as shoes & bags) with poorly updated inventories.

We are strong believers that help starts at our doorstep- if these shops were to be given the opportunity to display their inventory online, they will stand a chance at competing with other online businesses. It was from this firm belief that Autoshelf was born. Autoshelf seeks to automate the process of allowing these shops to put them up online, hopefully giving them a second chance at being owned. We felt ReNew could solve this problem through image analytics & automation.

# What it does
All the shop owner has to do is to 
1. fix their phone onto the selfie stick 
2. place any item on to the turntable 
3. open the app.

When an item is detected on the turntable, photos of the object is taken at multiple angles. These photos will then make up the listing with 3 main features that will be identified & auto-filled by the app: 
1. What the object is?
2. What colour is the object?
3. What are the dimensions of the object?
 
The process is repeated with another object and at the end, the shop owner may review the items he has and decide the cost of what each item should be, adding further descriptions if necessary. This enables potential customers to have an idea of what exactly the shop sells, with brief descriptions and a 360 degree view of the object.

## How we built it
We split this solution into 3 parts. 
1. The physical model of the cataloguer 
2. The front end of the app
3. The back end of the app. 

Samuel was in charge of the hardware (1), Aaron managed the app development (2) while Benjamin handled the image processing(3). Splitting the work enabled us to work quickly independently, although we each faced many problems.

## Challenges we ran into
1. Working with the limited hardware available to create something reliable.
2. We were not familiar with languages in the field of app development (e.g. Java).
3. There was a lack of a large-scale, open source data set. This limited the precision of the app, so it was hard to follow conventional ways of content-based image retrieval. 

## Accomplishments that we're proud of
1. Having a working physical prototype of the cataloguer
2. Getting Firebase to work on the app (albeit local not cloud image processing)
3. Managing to improvise our design and trying our best continuously in the 24 hours
4. (not an accomplishment but) this is Samuel's first hackathon and he thoroughly enjoyed the food (and the hacking of course!)
 
## What we learned
1. #joinhacknroll2021
2. app development is not easy
3. Poor circuitry can be solved by good coding (sometimes)
4. google lens is too good, we should've known that they wouldn't reveal their api 

## What's next for automatic cataloguer
We hope that you could give us some feedback regarding the feasibility of our idea because we understand that our prototype might not be 100% or even 80% accurate but we truly hope to address this problem!
