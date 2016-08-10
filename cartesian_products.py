import subprocess
import itertools
import unittest


def flatten_string_to_list(string):
  this_list_of_sets = []
  i = 0
  while i < len(string):
    this_set = []
    if string[i].isalpha():
      this_set.append("")
      while i < (len(string)) and string[i].isalpha():
        this_set[0] += string[i]
        i += 1
    elif string[i] == "{":
      this_bracket_content = get_string_of_bracket(string[i:])
      i += len(this_bracket_content)
      this_set = flatten_set_to_list(this_bracket_content[1:-1])
    this_list_of_sets.append(this_set)
  return combine_sets(this_list_of_sets)

def combine_sets(lists):
  new_list, pretty_list = [], []
  for element in itertools.product(*lists):
    new_list.append(element)
  for element in new_list:
    complete_string = ""
    for el in element:
      complete_string += "".join(str(e) for e in el)
    pretty_list.append(complete_string)
  return pretty_list

def flatten_set_to_list(string):
  this_list = []
  i = 0
  while i < len(string):
    next_string = ""
    while i < len(string) and string[i] != ",":
      next_string += string[i]
      i +=1
      if i < len(string) and string[i] == "{":
        this_bracket = get_string_of_bracket(string[i:])
        i += len(this_bracket)
        next_string += this_bracket
    this_list.extend(flatten_string_to_list(next_string))
    i += 1
  return this_list

def get_string_of_bracket(string):
  i, open, close = 0, 0, 0
  while i < len(string):
    if string[i]== "{": open += 1 
    if string[i] == "}": close += 1 
    i += 1
    if open == close:
      return string[ : i]

class MyTest(unittest.TestCase):
  def test_simple(self):
    test_cases = '{a,b}{c,d}', 'a{b,c}d{e,f,g}hi', 'a{b,c{d,e,f}g,h}ij{k,l}', 'a{b,c}d{e,f,g{h,i{j,k}}}'
    for test_set in test_cases:
      self.assertEqual(" ".join(flatten_string_to_list(test_set)), subprocess.check_output('echo '+ test_set, shell=True)[:-1] )

if __name__ == '__main__':
    unittest.main()
