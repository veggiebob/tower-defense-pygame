import yaml
towers_config = yaml.load(open("../../config/entities/towers.yaml").read(), Loader=yaml.FullLoader)
print(yaml.dump(towers_config))
print('basic tower range: %d'%towers_config['advanced_tower']['range'])
