# minelib/server is a collection of minecraft server utilities
# Copyright (C) 2020  Manuel Quarneti

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import path
import requests
from . import server


class MinecraftServer(server.MinecraftServer):
    def download(self):
        response = requests.get(
            "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        )
        version_list = response.json()["versions"]
        version = next(
            filter(lambda version: version["id"] == self.vanilla_version, version_list)
        )

        response = requests.get(version["url"])
        server = response.json()["downloads"]["server"]

        response = requests.get(server["url"])
        open(
            path.join(self.directory, f"/minecraft_server.{self.vanilla_version}.jar"),
            "wb",
        ).write(response.content)
