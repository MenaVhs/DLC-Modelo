# Segunda iteración 
## Segundo entrenamiento del modelo

Esta segunda iteración se ocuparon los mismos videos y frames etiquetados que en la primera iteración. Lo cual, sólo se canbió por un *1* en el fichero *config.yaml*.

### Creación del training dataset
Cuando se trabaja con Tensorpack, las imágenes de entrada se procesan en lotes para mejorar la eficiencia del procesamiento. El tamaño del lote se puede ajustar para ajustarse a las limitaciones de memoria del sistema y maximizar el rendimiento. Sin embargo, a diferencia de ImgAug, Tensorpack no permite lotes de tamaño mayor que 1. Esto significa que Tensorpack procesará cada imagen de manera individual en lugar de procesar varias imágenes simultáneamente en un lote. <br>

En consecuencia, ImgAug puede ser más eficiente en el procesamiento de grandes conjuntos de datos de imágenes que Tensorpack, ya que permite lotes de tamaño mayor que 1, lo que puede mejorar significativamente la velocidad de procesamiento en sistemas con múltiples núcleos de CPU. Sin embargo, esto también dependerá de la cantidad de memoria disponible en el sistema y de la complejidad de las transformaciones de imagen que se están aplicando. 
<br>
La ruta del proyecto es: ```config_path = 'D:\DLC\CV-Mena-2023-02-26\config.yaml'```
Por defecto <br>
```deeplabcut.create_training_dataset(config_path, augmenter_type='imgaug')``` <br>
Se aplicó: <br>
```deeplabcut.generate_training_dataset.trainingsetmanipulation.create_training_dataset(config_path, num_shuffles=1, Shuffles=None, net_type='resnet_50', augmenter_type='imgaug')```<br>

[Información](https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html#f-create-training-dataset-s)

### Entrenamiento de la red
Nuevos: 
1. keepdeconvweights: bool, opcional, por defecto=True. También restaura los pesos de las capas de deconvolución (y la columna vertebral) cuando se entrena a partir de una instantánea. Tenga en cuenta que si cambia el número de partes del cuerpo, debe establecerlo en false para volver a entrenar. <br>
Hora en la que inició a entrenar: 11:29 A.M. <br>
A las 3:41 P.M. terminó en 205000<br>
```deeplabcut.pose_estimation_tensorflow.training.train_network(config_path, shuffle=1, trainingsetindex=0, gputouse=0, max_snapshots_to_keep=200000, autotune=True, displayiters=100, saveiters=1000, maxiters=250000, allow_growth=True, keepdeconvweights=True)```

<!-- 
Se continuó a las 3:55 P.M. con 
init_weights: 'D:\DLC\CV-Mena-2023-02-26\dlc-models\iteration-1\CVFeb26-trainset95shuffle1\train\snapshot-205000' 
Se detivo a las 4:49 P.M hasta la iteración 251000-->

La iteración con menor pérdida fue: <br>
Iter: 213000, Loss: 0.179%, Learning Rate: 0.5%, precisión del: 99.821%


### Exportar modelo

deeplabcut.export_model(config_path, iteration=1, shuffle=1, trainingsetindex=0, snapshotindex='all', TFGPUinference=True, overwrite=True, make_tar=True)
'D:\DLC\CV-Mena-2023-02-26\dlc-models\iteration-1\CVFeb26-trainset95shuffle1\train'
### Evaluación

Es importante evaluar el rendimiento de la red entrenada. Este rendimiento se mide calculando el error euclidiano medio (MAE; que es proporcional al error cuadrático medio medio) entre las etiquetas manuales y las predichas por DeepLabCut. El MAE se guarda en un archivo separado por comas y se muestra para todos los pares y sólo para los pares probables (>p-cutoff). Esto ayuda a excluir, por ejemplo, partes del cuerpo ocluidas. Uno de los puntos fuertes de DeepLabCut es que, debido a la salida probabilística del mapa de puntuación, puede, si está suficientemente entrenado, informar también de forma fiable si una parte del cuerpo es visible en un fotograma determinado. (véanse las discusiones sobre las puntas de los dedos al alcanzar y las patas de Drosophila durante el comportamiento 3D en [Mathis et al, 2018]). <br>
Los resultados de la evaluación se computan tecleando: <br>
```deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True, gputouse=0, trainingsetindex='all')```
deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True)


