# Desktop App

## Running python app

Install python virtual env:

```shell
sudo pip install virtualenv
```

Browse to project folder.

Start virtual env and activate:

```shell
virtualenv venv
source venv/bin/activate
```

Install packages:

```shell
pip install -r requirements.txt
```

## Run project:

### GUI
```shell
flet run main.py -d
```

The UI will be appeared:

![img.png](img.png)

### Cli

It can also be run from the command line

```shell
# python csv_hasher.py <csv_file_path> <has_type>

python csv_hasher.py ./test_data/CSV-1-short.csv sha1

```
## Creating desktop app

```shell
flet pack main.py
```

For more details check [flet.dev docs](https://flet.dev/docs/guides/python/packaging-desktop-app)
