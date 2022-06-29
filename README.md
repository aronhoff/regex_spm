# regex_spm

Enable Structural Pattern Matching ([PEP-634](https://peps.python.org/pep-0634/)) for Python 
regular expressions

The string goes in the place of the subject, wrapped by a `regex_spm` function.<br>
The various possible regex patterns go after the `case`s.

### Simple example

```python
import regex_spm

match regex_spm.fullmatch_in("abracadabra"):
  case r"\d+": print("It's all digits")
  case r"\D+": print("There are no digits in the search string")
  case _: print("It's something else")
```

`regex_spm` provides 3 functions, which correspond to `re` search functions:
- `re.search` → `regex_spm.search_in`
- `re.match` → `regex_spm.match_in`
- `re.fullmatch` → `regex_spm.fullmatch_in`

### Accessing the match object
To access the matched groups or the entire `re.Match` object, simply capture the pattern:
```python
match regex_spm.fullmatch_in("123,45"):
  case r"(\d+),(?P<second>\d+)" as m:
    print("Notice the `as m` at the end of the line above")
    print(f"The first group is {m[1]}")
    print(f"The second group is {m['second']}")
    print(f"The full `re.Match` object is available as {m.match}")
```

### Pattern caveats (workaround below)

**#1:** Due to the mechanics of Python SPM, it is not possible to use case blocks like `case 
re.compile(r"my-regex"): ...`. Python would try to use `re.compile` as a class name, which does not
exist.

**#2:** It is also not possible to save patterns to simple local variables like:
```python
pattern1 = r"my-first-pattern"
pattern2 = re.compile(r"my-second-pattern")
match regex_spm.search_in(my_string):
  case pattern1: print("This does not work, it matches any string. Python interprets `pattern1` "
                       "as simply a new capture variable name, hiding its previous value.")
  case pattern2: print("This does not work either")
```

### Using patterns from variables (caveat workaround)
Python requires "value patterns" to use a "dotted name", i.e. there must be a `.` in tha name used 
to reach the stored pattern. 

Putting stored patterns in a class like below is sufficient.

```python
class PageRegexes:
  index = re.compile(r"example\.com/index.html")
  shopping_cart = r"example\.com/shopping_cart.html"

match regex_spm.search_in(my_url):
  case PageRegexes.index: print("It's the index page")
  case PageRegexes.shopping_cart: print("It's the shopping cart page")
  case r"example\.com/about.html": print("You can even mix and match")
```

## Install
Requires Python 3.10+ of course
```bash
pip install regex_spm
```