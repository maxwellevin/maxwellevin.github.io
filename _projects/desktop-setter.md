---
title: Desktop Setter
subtitle: An automated desktop setting application for MacOS
featured_image: /images/projects/desktop-setter/desktop-setter.png
date: 12-11-2019
layout: project
---

One of the things that I really enjoy about my desktop computer running Windows is that my login-screen changes to a different stunning nature photo every day. I enjoy the nature theme and I like that it happens without any intervention on my part. It's a feature that slightly improves my PC experience. 

My (Macbook) laptop doesn't have anything like that built-in, and I thought it would be simple enough to code instead of paying for an existing product, so I made [desktop-setter](https://github.com/maxwellevin/desktop-setter) to help me improve and fluidly change my background on my own timescale. 

**Desktop-setter** can be configured to run using either a local folder containing pictures or by querying the [Unsplash API](https://unsplash.com/developers). Recently I've been using my program to change my background every few hours to some winter-themed mountain photo from Unsplash. You can see an example of this below:

![](/images/projects/desktop-setter/desktop-setter.png)

I'm still working on improving the CLI, but for now the unsplash.py python script can be run in the following way:

```
watch -n time_interval_in_seconds python3 unsplash.py query=whatever_you_want_to_see
```

I wrote a separate script to set the background to local images in a folder. You can run it like this:

```
python3 local.py /path/to/folder/ time_interval_in_minutes
```

#### There are still a few things left to do...
1. Simplify CLI and other UI improvements
2. Unify unsplash.py and local.py scripts
3. Adapt code to work for windows devices
4. Adapt code to work for linux devices
5. Add more MacOS implementations (touchbar, siri)?