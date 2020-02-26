## Using our YAML
#### 1. Import the `YAMLInstancer` from yaml_parsing.py
```python
from game.common.yaml_parsing import YAMLInstancer
```
#### 2. Read the yaml file you want
   - for example, a file in the same directory should be
   - `file_content = open('test_file.yaml').read()`
   - this gives you a **str** of the file
   - you could also do it in plain string format
   - ```python
     """
     object:
         property1: value
         property2: value
     """
     ```
#### 3. Get the Object
   - pass the **string** and **class** of object you want into one of two methods like so:
      - `YAMLInstancer.get_single(file_content, class) -> object` returns first object in yaml file
      - `YAMLInstancer.get_multiple(file_content, class) -> dict<object>` returns all objects in yaml file, in a dictionary
         - `class` is your **YAML-compatible class**

## YAML - compatible classes
#### Needs
  * static attributes:
     - `REQ_ATTRS`: a **list** of **string** names of required properties from yaml
       - example: `REQ_ATTRS = ['name', 'id', 'child']`
       - <span style="color:red">note: if you add *name* as a required attribute, it can be automatically set by the *key* of the value in yaml</span>
     - `TYPE_ATTRS`: a **dict** of **key-value** pairs (**name-type**, respectively) that specifies object types of properties
       - example: `TYPE_ATTRS = {'id': int, 'child':Enemy}`
       - this is used to recursively serialize objects without specifying types in the yaml
       - this also replaces the `class` attribute, which should *not* be used but is supported just in case
#### Optional / case-by-case
  * static attributes:
     - `DEFAULT_ATTRS`: a **dict** of **key-value** pairs (**name-value**, respectively) that specifies default attributes
  * methods:
     - `yaml_init`: a method that is called *after* an object is initialized, if it exists
     - for example:
    ```yaml
    # enemy_test.yaml
    enemy1:
        health: 100
        speed: 20
        difficulty: 10000
    ```
    ```python
    from game.common.yaml_parsing import YAMLInstancer
    class Enemy:
        ...
        def yaml_init(self):
            self.original_health = self.health
        ...
    enemy1 = YAMLInstancer.get_single(open('enemy_test.yaml', 'r').read(), Enemy)
    print(enemy1.original_health) # prints '100'
    ```
    