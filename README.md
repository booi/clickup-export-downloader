# ClickUp Export Downloader

This script takes in a Clickup export file and downloads all the attachments into the specified directory. As of writing, clickup does not require a validated session to download attachments so this script does not require any authentication to work.

This does not check to see if you've already downloaded the attachment and will overwrite any file it finds.

## Requirements

* A clickup export file
* Python 3
* poetry

## Usage

```bash
poetry env use
python clickup_export_downloader.py [EXPORT_FILE.csv] [ATTACHMENTS_DIRECTORY]
```

## Warranty

None.
