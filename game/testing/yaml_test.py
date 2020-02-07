import yaml

from game.common.yaml_parsing import YAMLInstancer


class testClass:
    REQ_ATTRS = ['health'] # notice, __init__ is defaulted to empty
    def __str__ (self):
        # prints all the properties of a an instance of this class
        return 'instance of testClass: {\n%s\n}'%('\n'.join(["%s: %s"%(k,v) for k,v in vars(self).items()]))

example_test = open("./test.yaml").read() # read the yaml file

# test #1
object_dictionary = YAMLInstancer.instance_multiple_to_dict(example_test, testClass)
print(object_dictionary['instance1'])

# test #2
YAMLInstancer.get_variables(globals(), example_test, testClass) # put the objects out into global scope
print(instance1.property1)
print(instance2.property4['hi'])
"""
    this is WEIRD, because INSTANCE1 was declared nowhere...
    but since it was handed the global scope variables
    it was able to create 'instance1' outside this scope, using the class testClass
    
    TL;DR instance1 is an instance of testClass but it thinks it's an error
    python is scary
    
    also haven't decided on whether or not this is the way to go, 
    or whether instances should be read from a dictionary instead (see test#1)
    
    thinking of having REQ_ATTRS be a static attribute of all classes that can be instanced from yaml, without requiring an __init__ method
    
    also we can constsrain TYPES of REQ_ATTRS . . . what do you think?
"""