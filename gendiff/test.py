import gendiff_parse
import gendiff_engine

print(gendiff_engine.generate_diff(*gendiff_parse.generate_parse('file3.json', 'file4.json')))
