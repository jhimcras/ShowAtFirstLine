import sublime
import sublime_plugin

class ShowAtFirstLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cur_point = self.view.sel()[0].begin()
		cur_line_first_point = self.view.line(cur_point).begin()
		cur_layout = self.view.text_to_layout(cur_line_first_point)
		self.view.set_viewport_position(cur_layout)
