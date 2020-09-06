# window.py
#
# Copyright 2020 rmflynn
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/org/rmflynn/nixvox/window.ui')
class NixvoxWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'NixvoxWindow'

    book_button = Gtk.Template.Child()
    book_menu = Gtk.Template.Child()
    note_book = Gtk.Template.Child()
    book_title = Gtk.Template.Child()
    lists_box = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
