
## Brief Summary

This program takes an input text file customers.txt and outputs a list of invitees. 

Ouput all customer within 100 km of Intercom's Dublin office.

Formula calculate distance- https://en.wikipedia.org/wiki/Great-circle_distance.

## Prerequisites
Python 2.7
Flake8 Linting

## Command

For running tests
```
make tests
```

For running linter
```
make lint
```

## List files

For running install requirements:
```
pip install -r requirements.txt
```

For running intercom and give output:
```
./bin/intercom
```


## How to run it using docker
I provide Dockerfile for python 2.7.
You need to have Docker installed on your local machine

Step:
```
1. Install Docker
2. ./run.sh
3. docker exec -it {container_id} bin/bash
4. cd opt/intercom/
5.  ./bin/intercom
```

## Design Structure
### Models
- Customer
    - Customer has name userid and location (Point)
- Point
    - Point for hold latitude and longitude
### Decoder
- CustomerDecoder
    - For decode string json to customer object
### Service
- InviteeService
    - Calculate distance and get all customer less than 100km sorted by user id 
### Core
- Parsing
    - Validation parsing for json file
- DistanceStrategy
    - Manager using strategy pattern for selecting which strategy we will use for estimate distance 
- GlobalCircleDistance
    - Estimate Distance using Global Circle Distance formula
- FormatterOutput
    - Create file output.txt for list user being invited


Philip Moniaga philip.moniaga@gmail.com
