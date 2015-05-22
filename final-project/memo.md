# Hewlett-Packard contract explorer

Yes, the contracts are back. Obviously I can't make something on the whole data set, so I just want to take one company and plot all of its contracts in an app. 

## Quick Pitch

Maps, graphs, some analysis and a list of contracts given to Hewlett-Packard over the last 15 years

## The Old Way

1. Go to USAspending.gov
2. Query 'Hewlett-Packard'
3. Pick a specific year
4. Receive a partial set of data (< 30 fields) 
5. Download that data as an xls (repeat steps 5 and 6 if you want more than one year of data)
6. Use a set of tools like Excel, Tableau etc. to analyze and visualize that data

A different picture of the data can be retrieved by making an API query, but a persona can only get a complete picture of the data by doing a bulk data download.

If using the API, the data comes in xml form, so it would likely require an extra step to turn it into something usable by conventional programs.

## The New Way

1. Go to my site
3. Query 'Hewlett-Packard'
4. Receive summary (visual) and listed results for your query that can be downloaded or embedded directly

## Data details

### Where does the data come from? How is it collected?

The data comes from USAspending.gov. Right now I am using API queries to download the data, though API queries only return a few fields. I will have to work with that for now until I am able to bulk download the entire data set.

### What data-cleaning/processing needs to be done?

Little data cleaning needs to be done, but I will need to geocode two locations for every contract -- place of performance and location of recipient. 

I will need to convert the data from xml to a form better suited to a Flask app -- either JSON or csv.

I will also want to run some calculations on the data to find summary facts -- number of contracts by year, value of contracts by year, percent of contracts given to each agency (Army, Navy etc.).

## Implementation details

### Describe the public-facing endpoints

For right now I intend for there to be one main summary page that takes all the data and dynamically generates some useful numbers. Then by clicking into different parts of the application you can dig deeper into the data. We'll see how far I get with that

### How will the data be stored?

The data will likely be in a json on my computer -- possibly a csv

# Who else has done it and how is your attempt better?

- [Find The Best](http://www.findthebest.com/) - a research site which is not specific to government contracting data. It's basically USAspending with slightly better queryability and nicer graphic design. My project will be specific to one contractor, and do analysis on their data instead of just displaying it with better margins and padding.

- [FedSpending.org](http://www.fedspending.org/) - Clearly an early attempt at what I want to do eventually, but hasn't been updated since 2012, and looks like it's from 2005. The visuals are very basic and it doesn't allow users to drill down to the actual contract level. My project will do better than just show a brief overview, it will allow people to view down to the contract level.

# Pre-mortem

- **Really slow load times:** With so many elements on a page and so much data, the page will probably load painfully slow

- **Too much data:** Fifteen years worth of HP data is a lot for a simple app like this. Will have to work on the best way to deal with it on a series of pages.

