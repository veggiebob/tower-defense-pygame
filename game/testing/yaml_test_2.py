# this is a more detailed testing of yaml, hopefully with nested classes as anonymous instances
from game.common.yaml_parsing import YAMLInstancer
def print_all_attributes (obj):
    return 'instance of %s: {\n%s\n}' % (obj.__ if hasattr(obj, '__') else obj.__class__, '\n'.join(["%s: %s" % (k, v) for k, v in vars(obj).items() if k!="__"]))

# open and read test yaml file
test_yaml = open('./test_2.yaml').read()

# get the first (or only) object from the yaml file
o = YAMLInstancer.get_single(test_yaml)
print(print_all_attributes(o))

print('--------------------------------')

# get multiple objects from yaml file, as a dict like {object1name: value1, object2name: value2, . . . }
o = YAMLInstancer.get_multiple(test_yaml)
for k, v in o.items():
    print(print_all_attributes(v))