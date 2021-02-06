# Bellows
---

* **Author**: devoxel (discord: devoxel#8493), casualchameleon (discord: casualchameleon#6618), temportalflux (discord: temportalflux#3142)
* **Version**: 0.3.3
* **Foundry VTT Compatibility**: Tested on 0.6.6 and 0.7.5
* **System Compatibility (If applicable)**: n/a
* **Module Requirement(s)**: n/a
* **Module Conflicts**: no known conflicts, but its plausible that any modules change the playlist or ambient sound data could conflict
* **Translation Support**: Playlist import is localised at the moment, but nothing else.

## Link(s) to Module
* https://github.com/casualchameleon/Bellows
* https://raw.githubusercontent.com/casualchameleon/Bellows/master/module.json

## Description

This is a fork of casualchameleon's [fork](https://github.com/temportalflux/MusicAssist) of 
temportalflux's [MusicAssist](https://github.com/temportalflux/MusicAssist).

A few desired features for this fork:
- Youtube Playlist through a secondary service (the old playlist import is a bit hacky)

## Installation

In order to gain something by using this fork you need to run a web service for playlist import.
This is not simple, and for best results requires you to run a little webserver for playlists.
If this is merged upstream this will be an optional step, for now don't use this fork unless you
have a vague idea what you're doing.

### nginx block for this service

```
server {
        server_name SERVER_NAME_HERE;
        listen 80;
        client_max_body_size 1M;

        location / {
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_pass http://localhost:30069;
        }
}
```

Import the [module.json](https://raw.githubusercontent.com/casualchameleon/Bellows/master/module.json) as
you would any other module. The contents of the module directory should look similar to this github repository's root.

## Features

The current feature set includes:
- Playlist tracks can be imported from a youtube url such as `https://www.youtube.com/watch?v=_2xHCZSqpi4`
- Ambient Sound objects can be marked as streaming sounds with the same functionality as streamed playlist tracks (these are unable to fade however)
- YouTube Playlist imports

## Demonstration
Many thanks to [Sunamon](https://github.com/Sunamon) and [OrbitalBliss](https://github.com/OrbitalBliss) for
putting together a demonstration of Bellows' basic features.

[![Bellows Demonstration](https://img.youtube.com/vi/Z9A0Hq6BR8Y/0.jpg)](https://youtu.be/Z9A0Hq6BR8Y)

## Known Issues
- In Firefox, audio may not play in certain scenarios due to autoplay restrictions.
  You can fix this by clicking the autoplay button in the url bar and allowing it for your Foundry VTT site.
  Each player using Firefox will need to do this for it to work. Chromium based browsers don't have this issue.

![image](https://user-images.githubusercontent.com/1485053/97107921-03e8ff80-16c2-11eb-8695-59da5c368a19.png)
