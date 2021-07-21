# excel_generator
from excel_generator.generator import Generator

json_file = "producs.weight.json"
excel_file = "producs.weight.xls"
generator = Generator(json_file=json_file, excel_file=excel_file)
generator.generate()