# Government data scraper

## Context
This repository contains code that will allow you to download files from a website containing a download click button.
When starting this project, the initial use case was for a government website, which is why the title still stands.
Despite, the title, you should be able to use this code for any website.


## Useful info
- Ideally have Chrome installed on your machine.
- Follow the folder structure in this repository to make it easier to set your preferred download folder.
- Technical dependencies as per `requirements.txt`.
- Be familiar with xpaths and feel confident enough to get the desired xpath (I'd recommend Chrome for this).

## Example command
python3 ./src/main.py "https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/householddisposableincomeandinequality" "/html/body/main/div[4]/div/div[1]/section[2]/div[1]/div[2]/div/div/a" <preferred_download_dir>

## Considerations
- If the website in the example command changes its structure, the example command might crash.
- Although outside the scope of this project, it might be useful to add some logic to rename the file once downloaded.