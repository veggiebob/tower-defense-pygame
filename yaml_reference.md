#### A Brief Guide to YAML

The fundamental primitive in YAML is the key-value pair.
Everything is either a key, or a value.

```yaml
key: value
```

Every YAML document is comprised of a tree structure: one or more
nodes at the top level, one value for every leaf.

```yaml
key:
  value: ...
  othervalue: ...
otherkey:
  value3: ...
lastkey: ...
```

```
            key                  otherkey      lastkey
           /   \                    |
        value  othervalue         value3
```


Values can be one of several different types.
```yaml
key:
  integerValue: 0
  doubleValue: 0.1
  stringValue: "Hello!"
  stringValue2: Hello! #not recommended, but will still parse
  listValue:
    - 0
    - 1
    - 2
  arrayValue: [1, 1, 2, 3, 5]
  keyPairValue:
    integerValue: 1
    doubleValue: 0.2
```

There is additional, shorter syntax for key-value pairs

```yaml
    whatever: { key: value, key2: value2, key3: { a: b, c: 0 } }
```
is equivalent to 
```yaml
    whatever:
      key: value
      key2: value2
      key3:
        a: b
        c: 0
```

In our codebase, we will frequently use YAML key-value pairs to represent
objects.

```python
# example
# also please don't structure your code like this
# this is a BAD example
class Tower:
    def __init__ (self, config):
        self.speed = config['speed']
        self.reload_rate = config['reload_rate']
        self.bullet_type = config['bullet_type']
```
```yaml
    basic_tower:
      speed: 20
      reload_rate: 100
      bullet_type: "basic_bullet"
```
Using a combination of these structures allows us to easily create instances of game objects without doing them in code, so we can avoid
```python
basic_tower = Tower()
basic_tower.speed = 120
basic_tower.reload_rate = 100
basic_tower.bullet_type = "basic_bullet"
```

<a href="https://yaml.org/refcard.html">YAML Reference Card</a>
