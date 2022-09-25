from gi.repository import Nautilus, GObject
from typing import List
import os


class TestExtension(GObject.GObject, Nautilus.MenuProvider):
    """'Open in Sublime Text' menu entries for Nautilus"""

    def launch_sublime(
        self,
        menu: Nautilus.MenuItem,
        file: Nautilus.FileInfo,
    ) -> None:
        """Launch single file / directory in Sublime Text"""
        launch_cmd = f'subl "{file.get_location().get_path()}"'
        os.system(launch_cmd)

    # when right clicking with some objects selected
    def get_file_items(self, files: List[Nautilus.FileInfo]):

        file = files[0]

        if file.is_directory():
            item_label = "/%s/" % file.get_name()
        else:
            item_label = file.get_name()

        item = Nautilus.MenuItem(
            name="Open in SublimeText",
            label="Open in ST: %s" % item_label,
            tip="Opens %s in SublimeText." % item_label,
        )
        item.connect("activate", self.launch_sublime, file)

        return [
            item,
        ]

    # when right clicking on the empty space
    def get_background_items(self, *args):
        file = args[-1]

        item = Nautilus.MenuItem(
            name="Open in SublimeText",
            label="Open in ST: /%s/" % file.get_name(),
            tip="Opens /%s/ in SublimeText." % file.get_name(),
        )
        item.connect("activate", self.launch_sublime, file)

        return [
            item,
        ]
