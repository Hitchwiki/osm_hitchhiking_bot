# osm_hitchhiking_bot
Automated edits on openstreetmap.org to improve hitchhiking related content.

## Unification of official hitchhiking spot tagging
Discussed in [OSM Wiki](https://wiki.openstreetmap.org/wiki/Mechanical_Edits/TillWenke/moving_hitchhiking_stops_to_%27highway%3Dhitchhiking%27_(mainly_in_Europe/Germany))


### Setup

Copy `secret.json.example` to `secret.json`.

Read https://github.com/matkoniecz/osm_bot_abstraction_layer and https://wiki.openstreetmap.org/wiki/OAuth to set the secrets. In the OAuth application set "Redirect URIs" to "urn:ietf:wg:oauth:2.0:oob". If you run one of the editing scripts the first time you will be prompted (how) to set the uncommented lines in `secret.json`.

Install a pyvenv from `requirements.txt` with Python 3.12.6.

### Performing the edits
First get a feeling for the edit using `manual_testing.ipynb`. Once you are confident that you found a script to perform the large scale edit, use a dedicated `.py` file.