
#1
import re
pattern = r'ab*'
test_strings = ["a", "ab", "abb", "b", "abc", "aabb", ""]
for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")
#2
import re
pattern = r'ab{2,3}'
test_strings = ["abb", "abbb", "a", "ab", "abbbb", "abc", "aabb"]
for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")
#3
import re
pattern = r'[a-z]+_[a-z]+'
test_strings = ["hello_world","test_case","Python_program","helloWorld","abc_def_ghi","no_underscore"]
for string in test_strings:
    if re.search(pattern, string):
        print(f"'{string}' contains a match")
    else:
        print(f"'{string}' does not match")
#4
import re
pattern = r'[A-Z][a-z]+'
test_strings = ["Hello", "World", "Python", "UPPER", "lower", "CamelCase", "A", "Zebra"]
for string in test_strings:
    if re.search(pattern, string):
        print(f"'{string}' contains a match")
    else:
        print(f"'{string}' does not match")
#5
import re
pattern = r'a.*b$'
test_strings = ["ab", "a123b", "axb", "a_b", "abc", "bca", "aanythingb"]
for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match")
#6
import re
pattern = r'[ ,.]'
replacement = ':'
text = "Hello, world. This is a test string."
result = re.sub(pattern, replacement, text)
print(result)
#7
import re
def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_str)
snake_case = "hello_world_example"
camel_case = snake_to_camel(snake_case)
print(camel_case)
#8
import re
text = "HelloWorldExample"
result = re.split(r'(?=[A-Z])', text)
print(result)
#9
import re
text = "InsertSpacesBetweenWordsStartingWithCapitals"
result = re.sub(r'([A-Z])', r' \1', text).strip()
print(result)
#10
import re
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower()
camel_case = "ConvertCamelCaseToSnakeCase"
snake_case = camel_to_snake(camel_case)
print(snake_case)