# tunein-cli

## Overview
tunein-cli allows you to browse TUNEIN streams from your command line and listen to them.

## Requirements
- untangle
  - ```pip install untangle```
- curses
- requests
- mplayer
  - ```apt-get install mplayer``` or ```brew install mplayer```

## Installation
```
   $ git clone "https://github.com/Kaanthegmr/tunein-cli"
   $ cd tunein-cli-master
   $ python tunein.py
   ```
## Usage
Once you start the program you will see this line 
> Do you want to open stream(y/n):  

If you answer with *y*,stream will be opened with mplayer automatically.  
Answering with *n* results in a creation of a .pls file that can be imported into a media player to open the stream.

After that you can use the numbers on the screen to navigate through pages.

## Compability
- Linux
- macOS
- Windows(**without coloring and mplayer function**)
