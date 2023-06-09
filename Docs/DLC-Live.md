# Instalación de DLC-Live y DeepLabCut-Live GUI

[Información oficial de DLC-Live](https://github.com/DeepLabCut/DeepLabCut-live) <br>
[Información oficial de DLC-Live GUI](https://github.com/DeepLabCut/DeepLabCut-live-GUI)

🔥🔥🔥 Note :: alone, this object does not record video or capture images from a camera. This must be done separately.🔥🔥🔥


El proyecto de DLC-Live se encuentra en el directorio: <br>
```DLC-Live```

## [1. Instalación de DLC-Live](https://github.com/DeepLabCut/DeepLabCut-live/blob/master/docs/install_desktop.md?plain=1)
### Crear entorno virtual en Anaconda para dlc-live (Windows/Ubuntu)<br>
~~~
conda create -n dlc-live python=3.7 tensorflow-gpu==1.13.1 # if using GPU
conda create -n dlc-live python=3.7 tensorflow==1.13.1 # if not using GPU
~~~
### Instalar entorno virtual en dlc-live
~~~
conda activate dlc-live
pip install deeplabcut-live
dlc-live-test
~~~

## [2. Instalación de DLC-Live GUI](https://github.com/DeepLabCut/DeepLabCut-live-GUI/blob/master/docs/install.md?plain=1)
~~~ 
conda activate dlc-live
pip install deeplabcut-live-gui
~~~

## 3. Corre el deeplabcut-live-gui
~~~
conda activate dlc-live
dlclivegui
~~~


## [Instalación de OpenCV, Cmake, VStudio 2019 con VScode ](https://www.youtube.com/watch?v=-GY2gT2umpk&ab_channel=NicolaiNielsen-ComputerVision%26AI)
Al final de todos los pasos del video, en cmd: <br>
```cmake --build "C:\build" --target INSTALL --config Release``` <br>

## Tener instalado
Instalar: <br>
- Visual Studio 2019
- Cmake
- OpenCV 4.5.x
- CUDA 11.2 (si no está instalado)
- cuDNN (si no está instalado)
- Arduino: Arduino IDE, Arduino, C/C++, Arduino-Snippets y Arduino de Moozyk
[Para configutaciones de Arduino en VScode](https://www.youtube.com/watch?v=f7gFt7vDeLw&ab_channel=Proyectosdetecnolog%C3%ADaconarduino)