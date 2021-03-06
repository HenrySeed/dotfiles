# hyper-transparent [![Build Status](https://travis-ci.org/codealchemist/hyper-transparent.svg?branch=master)](https://travis-ci.org/codealchemist/hyper-transparent)
[Hyper](https://hyper.is) plugin to easily set window transparency and vibrancy.

Also allows you to easily set vibrancy on OSX.

![screenshot](https://cldup.com/lBSydSyCwc.gif)


## Install

Open Hyper config, find `plugins` and add `'hyper-transparent'` there:

```
plugins: [
  'hyper-transparent'
],
```

You'll find up to date plugin install instructions in the official [Hyper](https://hyper.is) site.


## Change background color

Open **Hyper** config and change `backgroundColor` at config root level.

Input any HEX color you like.

**HyperTransparent** will remember this color and apply transparency to it.


## Set default config

You can also persist a default config for **HyperTransparent** so your preferred settings are kept even after upgrading or reinstalling it.

Add the following config to **Hyper**'s config:

```
hyperTransparent: {
  backgroundColor: '#4b4',
  opacity: 0.2,
  vibrancy: '' // ['', 'dark', 'medium-light', 'ultra-dark']
}
```

This config will be preferred, so every time you reload the app it will always
be loaded.



## About Hyper
Hyper is a terminal app written with web technologies using [Electron](http://electron.atom.io).

Cool stuff huh? ;)
