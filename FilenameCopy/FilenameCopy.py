import sublime
import sublime_plugin
import os


class FilenameCopyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sublime.set_clipboard(os.path.basename(self.view.file_name()))
        print(os.path.basename(self.view.file_name()))


class ListOpenFilesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        views = window.views()
        fileNames = ''
        for view in views:
            if view and view.file_name():
                fileNames += os.path.basename(view.file_name()) + '\n'
        window.new_file().insert(
            edit, 0, "List of open files:\n\n" + fileNames)
