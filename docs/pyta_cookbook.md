
## Dictionaries

### Use `get()` method on dicts

```python
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

>>> greeting(382)
"Hi Alice!"

>>> greeting(333333)
"Hi there!"
```

When "get()" is called it checks if the given key exists in the dict. If it does exist, the value for that key is returned. If it does not exist then the value of the default argument is returned instead.

### Merge two dictionaries

```python
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)
{'c': 4, 'a': 1, 'b': 3}
```

Note that Python merges dictionary keys in the order listed in the expression, overwriting duplicates from left to right.
### `pprint` Alternative for Dictionaries


... (as an alternative to the "pprint" module)

# The standard string repr for dicts is hard to read:
>>> my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
>>> import json
>>> print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
>>> json.dumps({all: 'yup'})
TypeError: keys must be a string
In most cases I'd stick to the built-in "pprint" module though :-)


### Sort a Python dict by value (== get a representation sorted by value)

```python
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator
sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```
## Pandas

### CSV to/from Dataframe

To save a dataframe to CSV without indices:

```python
df.to_csv('file_name.csv',index=False)
```

To read from a dataframe without the indices:

```python
df_new = pd.read_csv('file_name.csv').drop(['unnamed 0'],axis=1)
```

### Plotting a Dataframe

For most plotting do not rely on the Pandas wrappers to matplotlib. Instead, just use matplotlib directly:

```python
import matplotlib.pyplot as plt

plt.scatter(df['col_name_1'], df['col_name_2'])
plt.show() # Depending on whether you use IPython or interactive mode, etc.
```

and remember that you can access a NumPy array of the column's values with `df.col_name_1.values` for example.


## Tuples

# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
>>> from collections import namedtuple
>>> Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
>>> my_car = Car('red', 3812.4)
>>> my_car.color
'red'
>>> my_car.mileage
3812.4

# We get a nice string repr for free:
>>> my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
>>> my_car.color = 'blue'
AttributeError: "can't set attribute"
