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

