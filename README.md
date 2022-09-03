# Post- SeeeQueuehuhe, SeQuEl, Sqruierul
Simple project to apply data modelling with Postgres and build somewhat an
ETL pipeline using Python.

## The scenario is as follow;

The fresh and revolutionizing startup, SparkiFy, wants to convert and store
their collected .json data files to a relational database, e.g. Postgres.

They want this to be done in a modern manner, so the purpose is to build a
local ETL pipeline and host the Postgres database in docker.

---

# Dataset
The .json data set are provided in the `data/` folder.

Sample record:
```python
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, \
"artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud",\
"song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", \
"duration": 152.92036, "year": 0}
```

Any new sample data that wish to be added needs to be manually added in the
`data/` folder and then execute order 66.

---
