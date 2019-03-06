#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
##from PyQt5.QtQuick import *
from PyQt5.uic import *
##from PyQt5.QtQml import *
from PyQt5.QtChart import *
import psutil
import random



#-------------------------------------------------
    
__author__ = '__Bill__'



class _Window_(QMainWindow):
    """
    -------------------(_Example_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)




        
#-----------------------drop shadow ---------------o

        self.effect = QGraphicsDropShadowEffect()
        
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(10)
        self.effect.setXOffset(5)
        self.effect.setYOffset(-5)
        self.effect.setColor(Qt.black)

#-------------timer-----------------

        self.window2 = QMainWindow()

        self.cpu_percentage = psutil.cpu_percent(interval=0.05)
        self.cpu_cores = psutil.cpu_percent(interval=0.05, percpu=True)
        print(self.cpu_cores[0])
        print(self.cpu_cores[1])
        
        self.switch_functions = (False)
        #print('x',self.switch_functions)
        
       
        self.timer  = QTimer()
        self.timer.timeout.connect(self.update_bar__)
        self.timer.start(750)
        
        
        self.blank_tick = (0)


#------------cpu core 0 values-----------------o
        
        self.tick_cpu0_0 = (0)
        self.tick_cpu0_1 = (0)
        self.tick_cpu0_2 = (0)
        self.tick_cpu0_3 = (0)
        self.tick_cpu0_4 = (0)
        self.tick_cpu0_5 = (0)
        self.tick_cpu0_6 = (0)
        self.tick_cpu0_7 = (0)


#------------cpu core 1 values-----------------o

        self.tick_cpu1_0 = (0)
        self.tick_cpu1_1 = (0)
        self.tick_cpu1_2 = (0)
        self.tick_cpu1_3 = (0)
        self.tick_cpu1_4 = (0)
        self.tick_cpu1_5 = (0)
        self.tick_cpu1_6 = (0)
        self.tick_cpu1_7 = (0)
        
 
#---------------create lines for graph-----------------o
        
        self.series_bottom = QLineSeries()
        self.series_cpu0 = QLineSeries()
        self.series_cpu1 = QLineSeries()

        self.series_bottom << QPointF(0, 0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(7,0);


        #self.series_cpu0 << QPointF(0,self.tick_cpu0_0) << QPointF(1, self.tick_1) << QPointF(2, self.tick_2) << QPointF(3,self.tick_3) << QPointF(4,self.tick_4) << QPointF(5,self.tick_5) << QPointF(6,self.tick_6) << QPointF(7,self.tick_7);      


#--------------add values for cpu-1 to chart-----------------------o
        
        self.series_cpu0.append(0, self.tick_cpu0_0);
        self.series_cpu0.append(0, self.tick_cpu0_1);
        self.series_cpu0.append(0, self.tick_cpu0_2);
        self.series_cpu0.append(0, self.tick_cpu0_3);
        self.series_cpu0.append(0, self.tick_cpu0_4);
        self.series_cpu0.append(0, self.tick_cpu0_5);
        self.series_cpu0.append(0, self.tick_cpu0_6);
        self.series_cpu0.append(0, self.tick_cpu0_7);


#--------------add values for cpu-2 to chart-----------------------o
        
        self.series_cpu1.append(0, self.tick_cpu1_0);
        self.series_cpu1.append(0, self.tick_cpu1_1);
        self.series_cpu1.append(0, self.tick_cpu1_2);
        self.series_cpu1.append(0, self.tick_cpu1_3);
        self.series_cpu1.append(0, self.tick_cpu1_4);
        self.series_cpu1.append(0, self.tick_cpu1_5);
        self.series_cpu1.append(0, self.tick_cpu1_6);
        self.series_cpu1.append(0, self.tick_cpu1_7);



      
        self.series = QAreaSeries(self.series_bottom, self.series_cpu0)
        self.series_2 = QAreaSeries(self.series_bottom, self.series_cpu1)
        
        self.series.setName("Batman")
        self.series.setBorderColor(QColor.fromRgb(25,25,25, 5)) #color for center line
        self.series_2.setBorderColor(QColor.fromRgb(25,25,25, 5))
        #self.series.setColor(QColor.fromRgb(55,205,155, 90))


        

#-----------background-chart---------------------

        self.chart = QChart()
        self.chart_2 = QChart()
        
        self.chart.addSeries(self.series);
        self.chart_2.addSeries(self.series_2)
        
        
        self.chart.setTitle("cpu cores");
        self.chart_2.setTitle("cpu cores")
        #self.chart.createDefaultAxes()
        

        self.chart.axisX = QValueAxis()
        self.chart_2.axisX = QValueAxis()
        #self.chart.axisX.setRange(0,1);
        #self.chart.axisX.setTickCount(0);

        self.chart.setAxisX(self.chart.axisX)
        self.chart_2.setAxisX(self.chart_2.axisX)

        self.chart.addAxis(self.chart.axisX, Qt.AlignBottom);
        self.chart_2.addAxis(self.chart_2.axisX, Qt.AlignBottom);

        #self.chart.axisX.setShadesBrush(QColor.fromRgb(25,225,25, 80))        
        #self.chart.axisX.setShadesColor(QColor.fromRgb(125,25,125, 80))
        #self.chart.axisX.setShadesVisible(False)#color for grid squares
        
        self.chart.axisY = QValueAxis()
        self.chart_2.axisY = QValueAxis()
        #self.chart.axisY.setRange(0, 100);
        #self.chart.axisY.setTickCount(0);

        self.chart.setAxisY(self.chart.axisY)
        self.chart_2.setAxisY(self.chart_2.axisY)

        self.chart.addAxis(self.chart.axisY, Qt.AlignRight);
        self.chart_2.addAxis(self.chart_2.axisY, Qt.AlignRight);

        #self.chart.axisY.setShadesBrush(QColor.fromRgb(25,225,25, 80))
        #self.chart.axisX.setShadesColor(QColor.fromRgb(25,225,25, 80))
        #self.chart.axisY.setShadesVisible(False)#color for grid squares


        #self.chart.setAnimationOptions(QChart.GridAxisAnimations)
        self.chart.setBackgroundBrush(QColor.fromRgb(25,25,25, 0))# transparent background
        #total transparency for 2nd graph background
        self.chart_2.setBackgroundBrush(QColor.fromRgb(25,25,25, 0))
        
        self.chart.legend().setVisible(False);#turn off graph legend
        self.chart_2.legend().setVisible(False);
       
##        self.chart.setDropShadowEnabled(True) #shadow under window
##        self.chart_2.setDropShadowEnabled(False)
        
        self.chart.setPlotAreaBackgroundVisible(False)
        self.chart_2.setPlotAreaBackgroundVisible(False)
        

        
#------------chart view---------------------
  
        self.chartView = QChartView(self.chart);
        self.chartView_2 = QChartView(self.chart_2);

        self.chartView.setRenderHint(QPainter.Antialiasing);
        self.chartView_2.setRenderHint(QPainter.Antialiasing);
    
        self.chartView.setChart(self.chart)
        self.chartView_2.setChart(self.chart_2)

        self.initGUI()

        



        
    def update_bar__(self):
        #print('update_bar__')

        self.cpu_percentage = psutil.cpu_percent(interval=0.25)
        self.cpu_cores = psutil.cpu_percent(interval=0.05, percpu=True)
##        print(self.cpu_cores[0])
##        print(self.cpu_cores[1])

        self.chart.removeAllSeries() #clear graph readout before next data entry
        self.chart_2.removeAllSeries()




        
        self.cpu_percentage_core0 = self.cpu_cores[0]#cpu core 0
        self.tick_cpu0_7 = self.cpu_percentage_core0
        print('self.tick_cpu0_7 ', self.tick_cpu0_7)
        self.cpu_percentage_core1 = self.cpu_cores[1]#cpu core 1
        self.tick_cpu1_7 = self.cpu_percentage_core1
        print('self.tick_cpu1_7 ', self.tick_cpu1_7)





        
        self.tick_cpu0_0 = self.tick_cpu0_1#sequence values
        self.tick_cpu0_1 = self.tick_cpu0_2
        self.tick_cpu0_2 = self.tick_cpu0_3
        self.tick_cpu0_3 = self.tick_cpu0_4
        self.tick_cpu0_4 = self.tick_cpu0_5
        self.tick_cpu0_5 = self.tick_cpu0_6
        self.tick_cpu0_6 = self.tick_cpu0_7

        self.tick_cpu1_0 = self.tick_cpu1_1#sequence values
        self.tick_cpu1_1 = self.tick_cpu1_2
        self.tick_cpu1_2 = self.tick_cpu1_3
        self.tick_cpu1_3 = self.tick_cpu1_4
        self.tick_cpu1_4 = self.tick_cpu1_5
        self.tick_cpu1_5 = self.tick_cpu1_6
        self.tick_cpu1_6 = self.tick_cpu1_7


        self.series_bottom = QLineSeries()
        self.series_cpu0 = QLineSeries()
        self.series_cpu1 = QLineSeries()


#--------------bottom line on graph-----------------------o

        self.series_bottom.append(0, self.blank_tick);
        self.series_bottom.append(1, self.blank_tick);
        self.series_bottom.append(2, self.blank_tick);
        self.series_bottom.append(3, self.blank_tick);
        self.series_bottom.append(4, self.blank_tick);
        self.series_bottom.append(5, self.blank_tick);
        self.series_bottom.append(6, self.blank_tick);
        self.series_bottom.append(7, self.blank_tick);

        #self.series_bottom << QPointF(0, 0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(7,0);
        #self.series_cpu0 << QPointF(0,self.tick_cpu0_0) << QPointF(1, self.tick_1) << QPointF(2, self.tick_2) << QPointF(3, self.tick_3) << QPointF(4, self.tick_4) << QPointF(5,self.tick_5);      


#--------------add values for cpu-0 to chart-----------------------o

        self.series_cpu0.append(0, self.tick_cpu0_0);#load values
        self.series_cpu0.append(1, self.tick_cpu0_1);
        self.series_cpu0.append(2, self.tick_cpu0_2);
        self.series_cpu0.append(3, self.tick_cpu0_3);
        self.series_cpu0.append(4, self.tick_cpu0_4);
        self.series_cpu0.append(5, self.tick_cpu0_5);
        self.series_cpu0.append(6, self.tick_cpu0_6);
        self.series_cpu0.append(7, self.tick_cpu0_7);

#--------------add values for cpu-1 to chart-----------------------o
        
        self.series_cpu1.append(0, self.tick_cpu1_0);
        self.series_cpu1.append(1, self.tick_cpu1_1);
        self.series_cpu1.append(2, self.tick_cpu1_2);
        self.series_cpu1.append(3, self.tick_cpu1_3);
        self.series_cpu1.append(4, self.tick_cpu1_4);
        self.series_cpu1.append(5, self.tick_cpu1_5);
        self.series_cpu1.append(6, self.tick_cpu1_6);
        self.series_cpu1.append(7, self.tick_cpu1_7);



        self.series = QAreaSeries(self.series_bottom, self.series_cpu0)
        self.series_2 = QAreaSeries(self.series_bottom, self.series_cpu1)

        self.series.setColor(QColor.fromRgb(255, 255, 102, 90))#set color for graph readout
        self.series_2.setColor(QColor.fromRgb(255, 153, 0, 90))

        self.chart.addSeries(self.series)
        self.chart_2.addSeries(self.series_2)

  
        

    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls
                              | Qt.Tool)
                        #| Qt.WindowStaysOnTopHint

        self.window2.setWindowFlags(Qt.FramelessWindowHint # hides the window controls
                             | Qt.SplashScreen
                             | Qt.NoDropShadowWindowHint#
                             |  Qt.Tool)
                        # | Qt.WindowStaysOnTopHint

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.window2.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setCentralWidget(self.chartView)
        self.window2.setCentralWidget(self.chartView_2)

        #self.setGeometry(500,200, 100,20)
        #self.window2.setGeometry(500,200, 100,20)
        
        self.resize(250, 150);
        self.window2.resize(250, 150);

        self.move(1700,600)
        self.window2.move(1700,600)

        self.setGraphicsEffect(self.effect)
        #self.window2.setGraphicsEffect(self.effect)

##        self.setWindowTitle('My Window')
##        self.window2.setWindowTitle('My Window 2')

        self.show()
        self.window2.show()


if __name__ == '__main__':
    app = QApplication([])
    _Win_ = _Window_()
    app.exec_()
