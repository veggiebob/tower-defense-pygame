import yaml, importlib
class YAMLInstancer:
    KEYS = ['REQ_ATTRS', 'DEFAULT_ATTRS', 'TYPE_ATTRS']
    LITERAL = '_literal_'
    @staticmethod
    def is_yaml_value_type (T):
        return T == int or T == float or T == str or T == bool
    @staticmethod
    def get_dict (yaml_string):
        return yaml.load(yaml_string, Loader=yaml.FullLoader)

    @staticmethod
    def get_class (module_name, class_name):
        m = importlib.import_module(module_name)
        return getattr(m, class_name)

    @staticmethod
    def get_yaml_string_class (class_string:str):
        # todo: search for classes recursively, using os (if the module isn't specified)
        separator = class_string.index('@')
        module_name = class_string[:separator]
        class_name = class_string[separator + 1:]
        y = YAMLInstancer.get_class(module_name, class_name)
        # print('found class %s in module %s'%(class_name, module_name))
        return y

    @staticmethod
    def require (requirements, object_dict):
        for r in requirements:
            try:
                foo = object_dict[r]
            except:
                raise Exception("you need attribute %s"%r)
        return True

    # @staticmethod
    # def check_type (type_requirements, object_dict):
    #     for k,v in type_requirements:
    #         if type(object_dict[k])


    @staticmethod
    def get_object (object_name, current_object, inferred_class:type=None):
        # todo: test literal expression evaluation using key _literal_ or something
        # todo: make a property 'init' that allows user to do method calls from a list?
        # recursive simple parsing stuff
        object_type = type(current_object)
        if YAMLInstancer.is_yaml_value_type(object_type):
            if object_type == str:
                try:
                    index = current_object.index(YAMLInstancer.LITERAL)
                    if index >= 0:
                        print('is a literal')
                        code = current_object[index + len(YAMLInstancer.LITERAL):]
                        return eval(code)
                except: pass
            return current_object
        if object_type == list:
            # print('%s is a list'%object_name)
            output = []
            for o in current_object:
                output.append(YAMLInstancer.get_object(object_name, o))
            return output
        if object_type != dict:
            raise Exception("%s is not an int, str, list or dict. What's wrong with you?"%current_object)

        is_in_parent = len(list(current_object.items())) == 1 # if it's an anonymous object like {'panel': { keys and values . . . } } that only has one object inside
        if is_in_parent:
            child = list(current_object.items())[0] # tuple with key, value
            return YAMLInstancer.get_object(child[0], child[1])

        # if it's a dict, then we've got some parsing to do
        object_class = inferred_class
        if inferred_class is None:
            try:
                object_class = YAMLInstancer.get_yaml_string_class(current_object['class'])
            except:
                raise Exception("unable to get class of object %s"%object_name)

        has_reqs = True
        has_defaults = True
        has_types = True
        try:
            requirements = getattr(object_class, YAMLInstancer.KEYS[0])
        except:
            has_reqs = False
        try:
            defaults = getattr(object_class, YAMLInstancer.KEYS[1])
        except:
            has_defaults = False
        try:
            types = getattr(object_class, YAMLInstancer.KEYS[2])
        except:
            has_types = False

        output_object = object_class()
        output_object.__ = object_name # used to be useful for handling objects but not needed anymore

        # special 'names'
        try:
            if requirements.index('name') >= 0:
                try:
                    output_object.name = current_object['name']
                except:
                    output_object.name = object_name
        except: pass

        # fill out defaults first
        if has_defaults:
            for k,v in defaults.items():
                setattr(output_object, k, v)

        # set attributes recursively
        for k,v in current_object.items():
            if k=='class': continue
            infer_type = None
            if has_types:
                try:
                    infer_type = types[k]
                except: pass

            if has_types and infer_type is not None:
                setattr(output_object, k, YAMLInstancer.get_object(k, v, infer_type))
            else:
                setattr(output_object, k, YAMLInstancer.get_object(k, v))

        # do requirement and type checks
        if has_reqs:
            for r in requirements:
                try:
                    getattr(output_object, r)
                except:
                    raise Exception('%s of class %s requires property %s' % (object_name, object_class, r))

        if has_types:
            for k,v in types.items():
                o_type = type(getattr(output_object, k))
                if o_type != v:
                    raise Exception('property %s needs to be of type %s, but is currently of type %s'%(k, v, o_type))

        # Yay! Your object has navigated the deadly twists of recursion
        # and the dangerous winding path of requirements and type checks.
        # Your object is now free to go
        return output_object

    @staticmethod
    def get_single (yaml_string:str):
        d = YAMLInstancer.get_dict(yaml_string)
        name = list(d.items())[0][0]
        o = YAMLInstancer.get_object(name, d[name])
        return o

    @staticmethod
    def get_multiple (yaml_string:str):
        d = YAMLInstancer.get_dict(yaml_string)
        objects = {}
        for k,v in d.items():
            objects[k] = YAMLInstancer.get_object(k, v)
        return objects

    @staticmethod
    # this method is old, stale and nasty. please don't use it
    def instance_yaml (_yaml, object_class_type):
        if type(object_class_type)!=type:
            raise Exception('you need to input a class to instantiate an object')
        if type(_yaml) != dict:
            yobj = YAMLInstancer.get_dict(_yaml)
        else:
            yobj = _yaml

        object_name = list(yobj.keys())[0]
        yobj = yobj[object_name]  # dictionary from yaml
        properties = list(yobj.items())

        object_class = object_class_type # for now
        try:
            user_class_string = yobj['class']
            print('class found %s'%user_class_string)
            user_class = YAMLInstancer.get_yaml_string_class(user_class_string)
            print('found user class %s'%user_class)
            object_class = user_class
        except:
            print('could not find class')

        iobj = object_class() # instance of the class
        iobj._ = object_name # set the _ of the instance
        if object_class.REQ_ATTRS.index('name') >= 0: # set the name if it's needed
            try:
                iobj.name = yobj['name']
                print('had property "name"=%s, put in object'%iobj.name)
                properties.remove(('name', yobj['name']))
                print('removed name property')
            except:
                iobj.name = object_name
                print('arbitrarily added name object')

        # if it specifies default attributes, then put them in
        if hasattr(object_class, YAMLInstancer.KEYS[1]): # default attributes
            for k,v in getattr(object_class, YAMLInstancer.KEYS[1]).items():
                try:
                    t = getattr(iobj, k) # check if it exists
                except: # if not . . .
                    setattr(iobj, k, v)


        # make sure that it has all the required attributes
        YAMLInstancer.require(getattr(object_class, YAMLInstancer.KEYS[0]), yobj)

        # if it has types specified, make sure that they are the right types
        # if hasattr(object_class, YAMLInstancer.KEYS[2]):
        #     for k,v in getattr(object_class, YAMLInstancer.KEYS[2]):
        #         if not type(getattr(iobj, k)) is v:
        #             raise Exception('you need the attribute %s have the type %s'%(k, v))

        # finally, add in the properties
        for k,v in properties:
            # print('key, value is %s, %s'%(k, v))
            if k=='class': continue
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