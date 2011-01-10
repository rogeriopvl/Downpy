# Downpy

## Info

Downpy is a tool written in python that downloads every specified filetype or file extension contained in a given web page. This tool was built to use along with [Filebuster](http://rogeriopvl.com/filebuster).

## Install

You can install Downpy using `pip` or `easy_install`:
	
	sudo pip install downpy
or
	sudo easy_install downpy

An executable file will be copied to your `/usr/local/bin` folder.

## Usage

If you installed the package with `pip` or `easy_install`, you should be able to run Downpy from the command line with:

	down [options] <url>

If you opted not to install Downpy, you can just clone the git repo and execute the `down` script:

	./down [options] <url>

### Options
* -e / --extension - specifies only one file extension (without the dot) to download
* -f / --filetype - scecifies a filetype (audio, video, doc)
* -s / --search - downloads only links containing the given string
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

	down -e ogg http://example.com/

Download all video files in a web page:

	down -f video http://example.com/

Download all doc files and save it on the ~/Documents folder

	down -e doc -o ~/Documents/ http://example.com/
