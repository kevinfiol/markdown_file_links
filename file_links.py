import sublime
import sublime_plugin
import re
import os

REGEX = r'^\[\[([^\s]+?)\]\]$'

class OpenFileLink(sublime_plugin.TextCommand):
    def __init__(self, view):
        sublime_plugin.TextCommand.__init__(self, view)

    def get_word(self, event):
        cursor_point = self.view.window_to_text((event["x"], event["y"]))
        region = self.view.extract_scope(cursor_point)
        word = self.view.substr(region)
        match = re.match(REGEX, word)

        if not match:
            return None
        return match.group(1)

    def want_event(self):
        return True

    def is_enabled(self):
        return True

    def is_visible(self, event):
        word = self.get_word(event)
        if word == None:
            return False
        return True

    def run(self, _edit, event):
        word = self.get_word(event)
        directory = os.path.dirname(self.view.file_name())
        file_path = os.path.join(directory, word)
        normalized_path = os.path.abspath(file_path) # account for relative paths `../foo.md`
        if not os.path.isfile(normalized_path):
            print('Markdown Link: is not real path: ' + normalized_path)
            return
        window = sublime.active_window()
        window.open_file(normalized_path)
