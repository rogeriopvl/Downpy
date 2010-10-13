# Downpy

## Info

Downpy is a tool written in python that downloads every specified filetype or file extension contained in a given web page. This tool was built to use along with [Filebuster](http://rogeriopvl.com/filebuster).

## Usage

	python downpy.py [options] <url>

### Options
* -e / --extension - specifies only one file extension (without the dot) to download
* -f / --filetype - scecifies a filetype (audio, video, doc)
* -o / --output - specifies an output directory

If you don't pass any options to downpy it will run with `-f audio` by default.

Too know more about available options:
	
	python downpy.py --help

### Available extensions:
* audio: .mp3, .ogg, .mp4a, .wma, .aac
* video: .avi, .mp4, .wmv, .flv
* doc: .doc, .docx, .txt, .rtf, .pdf, .epub, .chm

If you wan't more extensions you can edit the code or open an issue in github project page.

### Examples
Download all ogg files in a web page:

	python downpy.py -e ogg http://example.com/

Download all video files in a web page:

	python downpy.py -f video http://example.com/

Download all doc files and save it on the ~/Documents folder

	python downpy.py -e doc -o ~/Documents/ http://example.com/

## Roadmap

###To do:

- Python egg package
- Loading bar in text-mode while downloading
- Full GUI
