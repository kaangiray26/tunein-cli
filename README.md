# tunein-cli

## Overview
tunein-cli allows you to browse TUNEIN streams from your command line and listen to them.

## Features
-Open streams directly from your terminal using mplayer
-Download streams as .pls files
-Printout stream url source
-Open streams in browser
-Add streams to favourites
-Add custom streams using urls to favourites
-Play stations from favourites

## Requirements
- untangle
- requests
- mplayer
  - ```apt-get install mplayer``` or ```brew install mplayer``` or ```sudo pacman -S mplayer```

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
- Linux
- macOS
- Windows(**without coloring and mplayer function**)
