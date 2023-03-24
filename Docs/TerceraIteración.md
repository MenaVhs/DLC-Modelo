3060 Ti
### Creación del Dataset
```deeplabcut.generate_training_dataset.trainingsetmanipulation.create_training_dataset(config_path, num_shuffles=1, Shuffles=None, net_type='resnet_50', augmenter_type='imgaug')```
### Entrenamiento
```deeplabcut.pose_estimation_tensorflow.training.train_network(config_path, shuffle=1, trainingsetindex=0, gputouse=0, max_snapshots_to_keep=200000, autotune=True, displayiters=1000, saveiters=1000, maxiters=213000, allow_growth=True, keepdeconvweights=True)```
Hora de inicio: 1:07 p.m

### Exportación de modelo
```deeplabcut.export_model(config_path, iteration=1, shuffle=1, trainingsetindex=0, snapshotindex='all', TFGPUinference=True, overwrite=True, make_tar=True)```