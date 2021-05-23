# DRAGONHACK 2020

## Team `New_folder`
- Boshko Koloski
- Gojko Hajduković
- Ferdi Jajai
- Ilija Tavcioski

## Short descritpion
This project addresses the problem of forest fires and the consequences of the environment.
In order to do so we manually constructed dataset of wildfires, described by location features, duration features, how much area was impacted, what were the consequences to the nature.
Furthermore we employ NLP techniques to construct a Knowledge Graph where facts and entities of causes and relations are collected by automatically scraping and analyzing top N google articles, which we later visualize.
To see the impact on a broader scale, we also collect and visualize satellite images before and after the fire disaster and analyze the sentiment of the public throught NLP sentiment analysis.
Finally with the taken parameters we suggest how much reforestation should be done and how big the damage was by some conventional and nonconventional compartment metrics.

## Project organization

- [Knowledge graphs, language analysis](./src/back/nlp)
- [Image acquisition and processing](./src/back/maps)
- [Data](./data) <- Scraped and serialized data 
- [UI/UX Mockup](./mockups)     

## Setup

The backend code is developed with Python 3. To install the dependencies needed for reproduction of results run the following line.

```bash
pip3 install -r requirments.txt
pipenv install
```

## Usage 
Open the UI/UX mockup located  [here](./mockups).

## Earth Observation Hack
We use SINERGIZE's satellite imagery with a custom script for visualizing wildfires in order to collect the images before, during and after the incident has occured.
For a given event, we scan the coordinates with a bounding box in order to collect the imagery in the interval of [start_day-10, end_day+30] and obtain a collection of unique satellite images of the specific wildfire.
Additionaly, while acquiring the images, we scan for the satellite data on the available and non-cloudy dates in order to obtain high-quality images. 

## BEST UX

## BEST CARBON FOOTPRINT REDUCTION 
## MOST USEFUL HACK
![Alt text](data/knowledge_graphs/diagram_readme.png?raw=true "Title")