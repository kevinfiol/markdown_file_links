import sublime
import sublime_plugin
import re
import os

REGEX = r'^\[\[([^\s]+?)\]\]$'

class OpenFileLink(sublime_plugin.TextCommand):
    def __init__(self, view):
        sublime_plugin.TextCommand.__init__(self, view)

    def is_markdown_file(self):
        _file, ext = os.path.splitext(self.view.file_name())
        return ext == '.md' or ext == '.mdx'

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
        if not self.is_markdown_file():
            return False

        word = self.get_word(event)
        if word == None:
            return False
        return True

    def run(self, _edit, event):
        if not self.is_markdown_file():
            return

        word = self.get_word(event)
        if word == None:
            return

        directory = os.path.dirname(self.view.file_name())
        file_path = os.path.join(directory, word)
        normalized_path = os.path.abspath(file_path) # account for relative paths `../foo.md`

        # check extension
        _file, ext = os.path.splitext(normalized_path)
        if ext == '':
            # default to markdown
            normalized_path += '.md'

        if not os.path.isfile(normalized_path):
            print('sublime_file_links: is not real path: ' + normalized_path)
            return
        window = sublime.active_window()
        window.open_file(normalized_path)
        window.run_command('reveal_in_side_bar')
