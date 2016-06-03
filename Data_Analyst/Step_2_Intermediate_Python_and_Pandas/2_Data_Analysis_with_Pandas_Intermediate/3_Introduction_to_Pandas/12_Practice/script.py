import pandas as pandas_Pandas_Module


class Script:

	@staticmethod
	def main():
		food_info = pandas_Pandas_Module.read_csv("../food_info.csv")
		columns = food_info.columns.tolist()
		gram_columns = list()
		_g = 0
		while (_g < len(columns)):
			column = (columns[_g] if _g >= 0 and _g < len(columns) else None)
			_g = (_g + 1)
			if (column.find("(g)") != -1):
				gram_columns.append(column)
		gram_df = food_info[gram_columns]
		print(str(gram_df.head()))


class python_internal_ArrayImpl:

	@staticmethod
	def _get(x,idx):
		if ((idx > -1) and ((idx < len(x)))):
			return x[idx]
		else:
			return None



Script.main()