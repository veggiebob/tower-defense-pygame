import yaml
class YAMLInstancer:
    KEYS = ['REQ_ATTRS', 'DEFAULT_ATTRS', 'TYPE_ATTRS']
    @staticmethod
    def get_dict (yaml_string):
        return yaml.load(yaml_string, Loader=yaml.FullLoader)

    @staticmethod
    def instance_yaml (_yaml, object_class_type):
        # todo: class declaration using eval(class string) and recursive instancing, class as
        if type(object_class_type)!=type:
            raise Exception('you need to input a class to instantiate an object')
        if type(_yaml) != dict:
            yobj = YAMLInstancer.get_dict(_yaml)
        else:
            yobj = _yaml

        object_name = list(yobj.keys())[0]

        yobj = yobj[object_name]  # dictionary from yaml

        object_class = object_class_type # for now
        # print('dictionary is %s'%yobj)
        # try: # https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
        #     print('tries setting class to %s'%eval(yobj['class']))
        #     object_class = eval(yobj['class']) # if it has a class type, make this class that class type
        #     print('successful')
        #     yobj.remove(yobj['class'])
        # except:
        #     object_class = object_class_type
        #     print('could not find/use attribute "class" of %s'%object_name)


        iobj = object_class() # instance of the class
        iobj._ = object_name # set the _ of the instance

        # if it specifies default attributes, then put them in
        if hasattr(object_class, YAMLInstancer.KEYS[1]): # default attributes
            for k,v in getattr(object_class, YAMLInstancer.KEYS[1]).items():
                try:
                    t = getattr(iobj, k) # check if it exists
                except: # if not . . .
                    setattr(iobj, k, v)


        # make sure that it has all the required attributes
        for r in getattr(object_class, YAMLInstancer.KEYS[0]):
            try:
                foo = yobj[r]
            except:
                raise Exception('you need the attribute %s in the instance %s'%(r, iobj._))

        # if it has types specified, make sure that they are the right types
        if hasattr(object_class, YAMLInstancer.KEYS[2]):
            for k,v in getattr(object_class, YAMLInstancer.KEYS[2]):
                if not type(getattr(iobj, k)) is v:
                    raise Exception('you need the attribute %s have the type %s'%(k, v))

        # finally, add in the properties
        for k,v in yobj.items():
            # print('key, value is %s, %s'%(k, v))
            setattr(iobj, k, v)
        return iobj

    @staticmethod
    def instance_multiple_to_list (yaml_string, object_class):
        d = YAMLInstancer.get_dict(yaml_string).items()
        return [YAMLInstancer.instance_yaml({k:v}, object_class) for k,v in d]

    @staticmethod
    def instance_multiple_to_dict (yaml_string, object_class):
        d = YAMLInstancer.get_dict(yaml_string).items()
        new_dict = {}
        for k,v in d:
            new_dict[k] = YAMLInstancer.instance_yaml({k:v}, object_class)
        return new_dict

    @staticmethod
    def get_variables (globs, yaml_string, object_class):
        objs = YAMLInstancer.instance_multiple_to_list(yaml_string, object_class)
        for o in objs:
            globs[o._] = o