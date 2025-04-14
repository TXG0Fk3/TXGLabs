# Application.py
#
# Copyright 2025 TXG0Fk3
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw

CREDITS = dict(
    artists=(

    ),
    designers=(

    ),
    developers=(
        'Leoverton Xavier (TXG0Fk3)',
    ),
    translators=(
        'Leoverton Xavier (Brazilian Portuguese)',
    ),
    supporters=(

    ),
)



class Application(Adw.Application):
    application_id = None

    def __init__(self):
        super().__init__(application_id='com.txg0kf3.TXGLabs',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ApplicationWindow(application=self, title='TXGLabs', icon_name=self.application_id)
        win.present()


@Gtk.Template(resource_path='/com/txg0fk3/TXGLabs/ui/main_window.ui')
class ApplicationWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ApplicationWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.application = kwargs['application']

        self.add_actions()

    def add_actions(self):
        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.on_about_menu_clicked)
        self.application.add_action(about_action)

        preferences_action = Gio.SimpleAction.new('preferences', None)
        preferences_action.connect('activate', self.on_preferences_menu_clicked)
        self.application.add_action(preferences_action)

        shortcuts_action = Gio.SimpleAction.new('shortcuts', None)
        shortcuts_action.connect('activate', self.on_shortcuts_menu_clicked)
        self.application.add_action(shortcuts_action)

        quit_action = Gio.SimpleAction.new('quit', None)
        quit_action.connect('activate', lambda *_: self.quit())
        self.application.add_action(quit_action)

    def on_about_menu_clicked(self, _action, _param):
        builder = Gtk.Builder.new_from_resource('/com/txg0fk3/TXGLabs/ui/about_window.ui')
        window = builder.get_object('about_window')

        window.set_artists(CREDITS['artists'])
        window.set_designers(CREDITS['designers'])
        window.set_developers(CREDITS['developers'])
        window.set_translator_credits('\n'.join(CREDITS['translators']))
        window.add_acknowledgement_section(_('Supporters'), CREDITS['supporters'])

        window.set_release_notes("""
            <ul>
                <li>[Reader] Nothing</li>
            </ul>
        """)

        window.set_transient_for(self)
        window.present()


    def on_shortcuts_menu_clicked(self, _action, _param):
        builder = Gtk.Builder()
        builder.add_from_resource('/com/txg0fk3/TXGLabs/ui/shortcuts_overview.ui')

        shortcuts_overview = builder.get_object('shortcuts_overview')
        shortcuts_overview.set_modal(True)
        shortcuts_overview.set_transient_for(self)
        shortcuts_overview.present()

    def on_preferences_menu_clicked(self, _action, _param):
        print("Preferences menu clicked")
        

def main(version):
    app = Application()
    return app.run(sys.argv)
