import os


class SqlFetcher:
	def __init__(self, sql_folder: str) -> None:
		self.sql = {}
		self.sql_folder = sql_folder

	def __getitem__(self, file_name: str):
		if file_name in self.sql:
			return self.sql[file_name]
		self.sql[file_name] = open(self.__sql_path(file_name), "r").read()
		return self.sql[file_name]

	def __sql_path(self, file):
		return os.path.join(self.sql_folder, file)