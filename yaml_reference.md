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
**To see specifics, see <a href="https://github.com/veggiebob/tower-defense-pygame/projects/1">the yaml card in our project base</a>**
```python
# example
class Tower:
    # these are name-specific keys that 
    # specify certain ways to read the YAML
    REQ_ATTRS = ['health', 'reload_rate', 'projectile_type']
    DEFAULT_ATTRS = {
        'health': 50,
        'reload_rate': 20,
        'projectile_type': Projectile
    }
    TYPE_REQ = {
        'health': int
    }
    def get_hit (self):
        self.health -= 50 # self.health is a guaranteed property
```
Yaml encoding:
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
