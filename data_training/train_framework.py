from pylearn2.config import yaml_parse

layer1_yaml = open('Layer1.yaml', 'r').read()
hyper_params_l1 = {'features' :'train_features.npy',
                   'labels' :'train_labels.npy',
                   'start' :0,
                   'stop' :8000,
                   'nvis' :600,
                   'nhid' :250,
                   'batch_size' :100,
                   'monitoring_batches' :5,
                   'max_epochs' :500,
                   'save_path' :'.'}
layer1_yaml = layer1_yaml % (hyper_params_l1)
print layer1_yaml
train = yaml_parse.load(layer1_yaml)
train.main_loop()

layer2_yaml = open('Layer2.yaml','r').read()
hyper_params_l2 = {'features' :'train_features.npy',
                   'labels' :'train_labels.npy',
                   'start' :0,
                   'stop' :8000,
                   'nvis' :hyper_params_l1['nhid'],
                   'nhid' :250,
                   'batch_size' :100,
                   'monitoring_batches' :5,
                   'max_epochs' :500,
                   'save_path' :'.'}
layer2_yaml = layer2_yaml % (hyper_params_l2)
print layer2_yaml
train = yaml_parse.load(layer2_yaml)
train.main_loop()

mlp_yaml = open('Layer3.yaml', 'r').read()
hyper_params_mlp = {'features' :'train_features.npy',
                    'labels' :'train_labels.npy',
                    'start' :0,
                    'stop' :8000,
                    'test_start' :0,
                    'test_stop' :2000,
                    'n_class' :2,
                    'batch_size' :100,
                    'max_epochs' :1000,
                    'nvis' :600,
                    'save_path' :'.'}
mlp_yaml = mlp_yaml % (hyper_params_mlp)
print mlp_yaml
train = yaml_parse.load(mlp_yaml)
train.main_loop()
