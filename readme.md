# vintedApi

A web scraper that gets new items from the vinted catalog

## Installation

- install redis
- Download the zip file with all of the scripts
- Extract all of the files
- Optional: find vpn extensions and download them with [crx downloader](https://crxextractor.com/)
- Optional: put the .crx files in ./vpns folder
- If no vpns => only one browser and refrech for new data every 4 seconds if new data => 4 seconds * number of items (getting all the data from those items)

- paste the api url for the filter in vintedApi.py
- paste your discord token in discordBot.py at the bottom
- paste the channel id in discordBot.py

## Usage

**Vpn is optional but recommended!**

- run scraper.py
- setup the vpn extensions in the browser
- press enter to get Authentication for each browser
- press enter when done 

- run discordBot.py 

## TODO

- add config file for channel id and discord token, search url
- add option for multiple search filters and also in diffrent channels

- being able to change settings while scraper is running such as (new urls)
- change setting with discord
- add new browsers and delete browsers while running

- check if vpn is still working => out of order alert

- translate the title and description to own language

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

MIT License

Copyright (c) [2023] [Sem5262]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
