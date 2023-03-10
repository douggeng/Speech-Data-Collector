# Speech Data Collector

A speech transcriber that iterates through the transcript and everytime you say a key word it gets added into a SQL database

## Description

This program is a simulation of when businesses get access to the mic in your device, This is how they accuartly target you for advertising.

## Getting Started

### Video Demo (Click image)
[![Video Demo](https://img.youtube.com/vi/UtbnAN2j2vQ/0.jpg)](https://www.youtube.com/watch?v=UtbnAN2j2vQ)


### Libraries

* Pyaudio
* Json
* Websockets
* Asyncio
* Base64
* Mysql.connector
* Datetime
* String

### Instructions

* Register an account on https://www.assemblyai.com/ (cost $5 for 5 hours of use) and get the api key.
* Create a database and table in SQL
* Plug in your info into the variables under db.
* Insert your api key in api_key
* Now run main.py and talk into the mic mentioning my keywords or add your own:
```
python main.py
```
* Once finished talking "ctr c".
* Now run:
```
python userdata.py
```
* All the times you said the keyword should now be in SQL with the date.



## What I learned

* Working with websockets
* Utilizing audio libraries
* How to remove punctuation from strings


## What I want to improve/add

* Creating a seperate app to replicate exactly how these companies work.
* Adding a second table to include user_ids to seperate individual data from others.
* Implement different classes for more companies
* Add exact time of word said
