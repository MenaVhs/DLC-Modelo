# General
Este documento es una guía de cómo configurar el DeepLabCut (DLC) para entrenamiento de 
modelos utilizando una o más GPU en Windows 10 u 11 versión 2.3.0.<br>
Páginas oficiales de DLC:
- General: http://www.mackenziemathislab.org/deeplabcut 
- Documentación: https://deeplabcut.github.io/DeepLabCut/docs/UseOverviewGuide.html 
- Repositorio: https://github.com/DeepLabCut/DeepLabCut 
- Artículo de investigación de DLC: https://www.nature.com/articles/s41593-018-0209-y

Fecha de creación 26/Febrero/2023<br>
Autor: Mena


## Versiones y hardware utilizados para el presente proyeto

1. DLC: 2.3.0
2. Tensorflow = 2.10.0
3. Tensorflow-gpu = 2.10
4. CUDA: 11.2
5. cuDNN: 8.1
6. Visual Studio Code 1.75.1
7. Python = 3.8.16
8. Anaconda 2022.10
9. Sistema operativo: Windows 11

Hardware:<br>
GPU: NVIDIA GeFore RTX 3060 Ti 16 Gb

## Instalación

[Leer documento oficial de instalación](https://deeplabcut.github.io/DeepLabCut/docs/installation.html )

Es importante seguir el orden:
1. Anaconda
2. Visual Studio Code, active el autoguardado
    Ver apartado de OPCIONAL si prefiere trabajar con el entorno de DEEPLABCUT desde su VScode<br>
3. Python (verificar que se genere el PATH)
2. Git (opcional, si quiere clonar el repositorio sino, sólo con descargar el ZIP)<br>
  2.1. Clonar repositorio de DLC en GitHub
  2.2. Suponiendo que quiere clonar en escritorio, dar click derecho y click en "Abrir Terminal"
  2.3. Escribir: git clone https://github.com/DeepLabCut/DeepLabCut
3. Abrir el promt de Anaconda como administrador
4. Para entrar a carpeta de proyecto, copiar la dirección donde se encuentra nuestro proyecto de DLC, por ejemplo:<br>
  ```cd C:\Users\Name\Desktop\DeepLabCut\conda-environments```
5. Para crear el entorno virtual de DEEPLABCUT, pegar:<br>
  ```conda env create -f DEEPLABCUT.yaml```
6. Instalar Tensorflow dentro de entorno virtual DEEPLABCUT: <br>  
  ```pip install tensorflow = 2.10.0``` 
  **IMPORTANTE** Si quiere instalar otra versión de tensorflow, ver [compatibilidad](https://www.tensorflow.org/install/source?hl=es-419#gpu )  
7. Instalar Tensorflow-gpu
  ```pip install tensorflow-gpu = 2.10.0```
8. Instalar Drivers de acuerdo a la GPU instalada. <br>  Importante, leer instrucciones de DLC sobre la GPU<br>
   Para saber el modelo de GPU
   a) CTRL + r
   b) escribir: dxdiag
   c) segunda pestaña, en español "Pantalla"
   Si es NVIDIA: https://www.nvidia.com/download/index.aspx 
9. Instalación de CUDA 11.2: https://developer.nvidia.com/cuda-11.2.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal 
10. Para descargar cuDNN 8.1 debe tener cuenta de NVIDIA: https://developer.nvidia.com/rdp/cudnn-archive 
11. Ver instrucciones para instalar cuDNN en CUDA: https://www.youtube.com/watch?v=C1en3qSs39g&t=38s&ab_channel=CarlosPerales%2CPhD 
12. Comprobar que CUDA detecta su GPU NVIDIA
    Abrir Windows PowerShell y escribir: <br>  ```nvcc --version```<br>
    Si aparece la versión 11.2, está del otro lado<br>
    Sino, siga estos pasos: https://www.youtube.com/watch?v=keOjesFzwW8&ab_channel=DIEGOLITTLELION <br>
    Elimite el CUDA de otra versión desde panel de control y aplicación.<br>
    Repetir pasos 8 y 12


## Opcional
Si lo prefiere, puede trabajar el proyecto desde la IDE de VScode, junto con la terminal de Anaconda<br>
Una forma es tener un archivo Python para llevar los siguientes pasos. <br>
Puede abrir cualquier archivo de python dentro de este proyecto
1. Para entrar al entorno virtual desde VScode, click en la esquina inferior donde dice *Python <<versión de python instalada>>*
2. Se desplegará en la barra superior los entornos virtuales que tiene
3. Seleccione el entorno de DEEPLABCUT con Pyhton 3.8.16
4. CTRL + ñ para abrir terminal dentro de VScode
5. Observe que al inicio del la ruta dice "(DEEPLABCUT)"<br>

# Guía completa de ejecución de un proyecto

## Crear o cargar proyecto en GUI de DLC
Dentro del promt de Aanconda como administrador
1. Entrar al entorno virtual de DEEPLABCUT <br>
    ```activate DEEPLABCUT```
2. ```ipython```
3. ```import deeplabcut```
4. ```deeplabcut.launch_dlc()```  para abrir la GUI
5. New project
6. Ingrese datos
7. De preferencia, dar click en "Copy videos to project folder"
8. Click en "create"
Nota: revise la dirección donde se guardó su projecto
Si ya tiene un proyecto generado:
1. Click en "Load project"
2. Seleccionar archivo config.yaml

## Extraer, etiquetar frames  crear dataset de entranmiento

### Extraer
1. Seleccione la pestaña de "Extract frames"
2. Configure las variables de acuerdo a la documentación. Consejo, elija **k-means**
3. En Frame cropping seleccione GUI (si necesita recortar para que extraiga un área específica)
3. Click en "Extract frames"
4. Seleccionar áreas para recorte (si es necesario)
5. Puede observar los frames dentro del directorio "labeled-data" por cada video

### Etiquetar
1. Configure dentro del archivo config.yaml los bodyparts y el skeleton de acuerdo a los puntos que quiere etiquetar
2. Seleccione "Labels frame"
3. Selecionar carpeta por carpeta donde se contienen los frames
4. Se abrirá la GUI de Napari para su debido etiquetado
5. Se recomienda ir guardando cada cierto tiempo de etiquetado hasta terminar con la última carpeta <br>
   ```File > Save Selected Layer(s)...```

### Dataset
1. Dar click en "Create training dataset"
2. Configurar los parámentros (Ojo, estos deben coincidir con los datos de entrenamiento)
3. Click en "Create training dataset" para crear

**NOTA:** Si usted quiere hacer más iteraciones
1. Abra archivo config.yaml
2. Cambie el número de la iteracipon en la opción "iteration"
3. Repita el paso del dataset
4. Revise si se generó otra carpata llamada **iteration <<número de la iteración nueva>>**


## Entrenamiento del modelo

Para tener una mejor configuración del entrenamiento, puede regresar a la terminal de Anaconda.
En el caso de este proyecto, se configuró dentro del entorno virtual del promt de Anaconda.

1. Guarde la ruta de su proyecto en una variable, por ejemplo:
```config_path = 'C:\Users\Name\Desktop\Proyecto-Mena-2023-02-26\config.yaml' ```
2. ```import deeplabcut```
3. ```deeplabcut.train_network(config_path, shuffle=1, trainingsetindex=0, gputouse=0, max_snapshots_to_keep=200000, autotune=False, displayiters=100, saveiters=100, maxiters=200000, allow_growth=True)```<br>
Información de la API https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html#g-train-the-network 
4. Al finalizar el entrenamiento se generarán los archivos snapshots. 

## Exportar el modelo entrenado
### (el último)
Esta función permite exportar un modelo animal único bien entrenado para aplicaciones en tiempo real, etc. Esta función es parte de Kane et al, 2020 eLife.<br>

```deeplabcut.export_model(config_path, iteration=None, shuffle=1, trainingsetindex=0,snapshotindex='all', TFGPUinference=True, overwrite=False, make_tar=True)```<br>
Información: https://deeplabcut.github.io/DeepLabCut/docs/HelperFunctions.html?highlight=export_model 

## Evaluar la red entrenada

Los resultados de la evaluación se calculan escribiendo:
Establecer plotting a ```True``` muestra todos los fotogramas de prueba y entrenamiento con las etiquetas manuales y predichas. 
Comprobar visualmente las imágenes etiquetadas de prueba (y entrenamiento) que se crean en el directorio 'evaluation-results'. <br>

```deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True, gputouse=0, trainingsetindex='all')``` <br>
Información oficial: https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html#h-evaluate-the-trained-network 

Notas:
Tomar en cuenta el almacenamiento, debido a que la función de evaluciación inicia desde el primer snapshot si quieres volver a correr la ejecución checando si existencia de snapshot's. 
Si detecta existencia, pasa al siguiente snapshot. Sin embargo, todo debe estar dentro de la misma carpeta para porder continuar desde el punto donde se quedó.

## Análisis de videos nuevos
La red entrenada puede utilizarse para analizar nuevos vídeos. El usuario debe elegir primero un punto de control con los mejores resultados de evaluación para analizar los vídeos. En este caso, el usuario puede introducir el índice correspondiente del punto de control en la variable snapshotindex del archivo config.yaml. Por defecto, se utiliza el punto de control más reciente (es decir, el último) para analizar el vídeo. Los vídeos nuevos NO tienen que estar en el archivo config. Puede analizar nuevos vídeos en cualquier momento simplemente utilizando la siguiente línea de código: <br>
Si usted quiere analizar videos que están en otro directorio <br>
```deeplabcut.analyze_videos(config_path, ['fullpath/analysis/project/videos/reachingvideo1.avi'], save_as_csv=True)``` <br> 

video_path =  ['D:\DLC\VideosParaTracking\grupo 2\R4\Grupo2R4S1\Grupo2R4S1.mp4']
El que se utilizó para este proyecto fue:
```deeplabcut.analyze_videos(config_path, video_path , videotype='mp4', shuffle=1, trainingsetindex=0, gputouse=0, save_as_csv=True, destfolder=None, dynamic=(True, .5, 10))```<br>

Recorte dinámico de vídeos:
Si tiene fotogramas grandes y el animal/objeto ocupa una fracción menor, puede recortar alrededor del animal/objeto para acelerar la velocidad de procesamiento. Por ejemplo, si tiene un experimento de campo abierto grande pero sólo rastrea el ratón, esto acelerará su análisis **(también útil para aplicaciones en tiempo real)**. <br>
Para usar esto simplemente añada ```dynamic=(True,.5,10)``` cuando llame a **analyze_videos*. <br>

Más información: https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html#i-novel-video-analysis  

## Filtrado
```deeplabcut.filterpredictions(config_path, video_path, shuffle=1, trainingsetindex=0, filtertype='arima', p_bound=0.01, ARdegree=3, MAdegree=1, alpha=0.01)```
API: https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html?highlight=plot#j-filter-pose-data-data-recommended <br>

## Gráficar 
```deeplabcut.plot_trajectories(config_path, video_path,  videotype='mp4', shuffle=1)```
API: https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html?highlight=plot#k-plot-trajectories

~~~
código 
de bloque 
~~~