import sublime, sublime_plugin

class Filename_to_clipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_clipboard(self.view.file_name())
    sublime.message_dialog("The full file path was copied to the clipboard")
