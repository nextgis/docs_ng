Генерация сетки в метрах
========================

.. figure:: _static/grids-demo.png
   :align: center
   :width: 16cm

   Сгенерированные сетки
   
Инструмент осуществляет генерацию сетки в границах объектов из векторного слоя. Размер сетки задаётся в метрах. Объекты могут быть в любом месте Эемли.

На входе:

*  Мультиполигональный слой с одним или несколькими объектами. Принимается формат Geopackage
*  Шаг сетки в метрах
*  Режим: points (точки), rect (квадраты).
*  Алгоритм обрезки сетки по границам: all (оставлять все квадраты в охвате объекта), touches (оставлять все квадраты касающиеся объекта), intersection (обрезать квадраты по границе объекта).

.. figure:: _static/grid-1000-rect-all.png
   :align: center
   :width: 16cm

   all
   
   
.. figure:: _static/grid-1000-rect-touches.png
   :align: center
   :width: 16cm

   touches
   
   
.. figure:: _static/grid-1000-rect-intersection.png
   :align: center
   :width: 16cm

   intersection
   
   
.. figure:: _static/grid-1000-point-all.png
   :align: center
   :width: 16cm

   all для точек
   
   
.. figure:: _static/grid-1000-point-intersection.png
   :align: center
   :width: 16cm

   touches и intersection для точек

   
.. figure:: _static/grid-planet.png
   :align: center
   :width: 16cm

   Сгенерированные сетки для нескольких полигонов в разных местах глобуса
   

На выходе:

* Geopackage

`Видео <https://youtu.be/v5WXJ7fhS9k?si=SrYXZERbxCcApcif>`_

Запуск инструмента: https://toolbox.nextgis.com/operation/grid

**Попробуйте инструмент в действии, скачав наш пример:**

`Набор исходных данных <https://nextgis.ru/data/toolbox/grid/grid_inputs_ru.zip>`_ для проверки работы инструмента. Внутри архива пошаговая инструкция.

`Пример результата <https://nextgis.ru/data/toolbox/grid/grid_outputs_ru.zip>`_ работы инструмента.
