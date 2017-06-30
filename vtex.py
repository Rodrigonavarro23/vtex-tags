# Sublime text 3 plugin for Vtex tags
# Copyright Rodrigo Navarro 2017
# MIT LICENSE

import sublime
import sublime_plugin
import json
import os


class VtexCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		current_file = view.file_name()
		completions = []
		html_file = os.path.dirname(__file__) + '/completions.json'
		file_name, file_extension = os.path.splitext(current_file)
		html_extensions = [
			'.html',
			'.hbs',
			'.jsx'
		]
		if file_extension in html_extensions:
			return (self.getCompletions(html_file))
		else:
			return None

	def getCompletions(self, file):
		with open(file) as json_data:
		    completionList = json.load(json_data)["completions"]
		    completions = []
		    for current in completionList:
		    	tmp = [current["trigger"], current["contents"]]
		    	completions.append(tmp)

		    completions.sort()
		    return completions