import yaml
class YAMLInstancer:
    @staticmethod
    def get_dict (yaml_string):
        return yaml.load(yaml_string, Loader=yaml.FullLoader)

    @staticmethod
    def instance_yaml (_yaml, object_class):
        if type(object_class)!=type:
            print('you need to input a class to instantiate an object')
            return
        if type(_yaml) != dict:
            yobj = YAMLInstancer.get_dict(_yaml)
        else:
            yobj = _yaml
        iobj = object_class()
        iobj.name = list(yobj.keys())[0]
        yobj = yobj[iobj.name]
        for r in object_class.REQ_ATTRS:
            try:
                foo = yobj[r]
            except:
                print('you need the attribute %s in the instance %s'%(r,iobj.name))
                return
        if type(yobj) == dict: # must be a dict, not a list
            for (k,v) in yobj.items():
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
            globs[o.name] = o