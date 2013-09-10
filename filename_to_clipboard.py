# This command is already built-in to Sublime text, in the right-click menu for any open file
# But I wanted to practice making a sublime text plugin.
# This plugin adds the command, and the menu file adds the command to the menu.
import sublime, sublime_plugin

class Filename_to_clipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_clipboard(self.view.file_name())
    sublime.message_dialog("The full file path was copied to the clipboard")
