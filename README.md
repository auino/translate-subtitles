# translate-subtitles

Easily translate subtitles files.

### Description ###

This program allows you to translate [srt subtitles 
files](https://docs.fileformat.com/video/srt/) by using [Google 
Translate](https://translate.google.com).

### Installation ###

1. Clone the repository:

```
git clone https://github.com/auino/translate-subtitles.git
```

2. `cd` into the download folder

3. Install [Python](https://www.python.org) requirements:

```
pip install -r requirements.txt
```

5. You are ready to run the tool

### Usage ###

Simply run the following command

```
python translate-subtitles.py -i <inputfile> -il <inputfile_language> -o 
<outputfile> -ol <outputfile_language>
```

where:
* `inputfile` identifies the input `srt` file to be processed
* `inputfile_language` identifies the language of the input `srt` file (e.g. `en`, `it`, `es`, etc.)
* `outputfile` identifies the output `srt` file to be generated
* `outputfile_language` identifies the language of the output `srt` file (e.g. `en`, `it`, `es`, etc.)

### Contacts ###

You can find me on Twitter as [@auino](https://twitter.com/auino).
