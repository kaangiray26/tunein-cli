# tunein-cli :radio:

## Overview
__tunein-cli__ allows you to browse TUNEIN streams from your command line and listen to them by parsing xml from **http://opml.radiotime.com/** to gather stations information.

## Features
- _Open streams directly from your terminal using mplayer_  
- _Download streams as .pls files_  
- _Printout stream url source_  
- _Open streams in browser_  
- _Add streams to favourites_  
- _Add custom streams using urls to favourites_  
- _Play stations from favourites_  

## Requirements
- inquirer (__v2.6.3__)
- untangle (__v1.1.1__)
- requests (__v2.23.0__)
- mplayer
  - ```apt-get install mplayer``` or ```brew install mplayer``` or ```sudo pacman -S mplayer```  
  - for windows download from the [website](https://oss.netfarm.it/mplayer/).

## Installation
```
   $ git clone "https://github.com/Kaanthegmr/tunein-cli"
   $ cd tunein-cli-master
   $ pip install -r requirements.txt
   $ python tunein.py
   ```
## Usage
Once you start the program you will see the following output:
Use your keyboard navigate through options.
>   [?] Select Option::  
>   [1]: Open Stream  
>   [2]: Download Stream  
>   [3]: Show Stream Source  
>   [4]: Open In Browser  
>   [5]: Add to Favourites  
>   [6]: Add custom station  
>   [7]: Favourites  
>   [8]: Exit  

## Compability
- Linux :heavy_check_mark:  
- macOS :heavy_check_mark:  
- Windows :heavy_multiplication_x: (**without coloring and mplayer function**)

## Troubleshoot
If you're on a Linux system, consider doing the following changes:
```
   $ sudo touch /etc/mplayer/mplayer.conf
   $ sudo echo "nolirc=yes" > /etc/mplayer/mplayer.conf
   $ sudo echo "ao=alsa" > /etc/mplayer/mplayer.conf
```
