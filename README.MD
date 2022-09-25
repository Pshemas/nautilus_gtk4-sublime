# "Open in Sublime Text" menu entries for Nautilus, GTK4

Since Nautilus in Gnome 43 has been upgraded to GTK4 it was time to rewrite this simple extension.

![Open in Sublime sample](open_in_st.png)

It provides "Open in ST:" right-click menu entries for folders and files. Current limitation is that it opens single file / directory - when multiple are selected last one is used (as most of the times I need to open a single folder with this menu this hasn't been an issue for me so far).

## Installation

Just copy/move nautilusgtk4-sublime.py to one of the Nautilus extension folders, for example: ~/.local/share/nautilus-python/extensions/ .After Gnome restart it should be working - just right click and see whether extra entries appear.
## Developement Ideas

First of all - by adding a simple loop it should be possible to handle  opening multiple files. Would be nice to do it with some nice styling of the menu entries (for example by adding "..." to mark that multiple files will be opened).

Secondly - handling of opening either in new window or in the last used one could be added (by passing -wm option to command that launches Sublime).

Lastly - even at this super cobbled together stage it is obvious that a small refactor to eliminate code duplication wouldn't hurt ;) .