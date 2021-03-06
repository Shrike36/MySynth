# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledODXDtv.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import time

import numpy as np
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PyQt5.QtWidgets import *

import pyqtgraph as pg

import rtmidi

from Controller.Controller import Controller
from Modifiers.Detune import Detune, ModulatedDetune
from Modifiers.WaveAdder import WaveAdder as wa, WaveAdder
from Modifiers.Panner import StereoPanner as sp, StereoPanner, ModulatedPanner
from Modulation.ParamsModulation import LFOModulation, ModulationType
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.ModulatedOscillator import ModulatedOscillator
from Oscillators.Oscillator import Oscillator, Type
from Oscillators.WaveGenerator import WaveGenerator
from Synth.Parameters import SynthParams
from Synth.Synth import Synth


class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1522, 945)
        self.actionSample_Rate = QAction(MainWindow)
        self.actionSample_Rate.setObjectName(u"actionSample_Rate")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 111, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 110, 231, 101))
        self.osc_1_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.osc_1_layout.setObjectName(u"osc_1_layout")
        self.osc_1_layout.setContentsMargins(0, 0, 0, 0)
        font1 = QFont()
        font1.setPointSize(12)
        self.osc_1_sine_radioButton = QRadioButton(self.centralwidget)
        self.osc_1_sine_radioButton.setObjectName(u"1")
        self.osc_1_sine_radioButton.setGeometry(QRect(10, 240, 80, 21))
        self.osc_1_sine_radioButton.setFont(font1)
        self.osc_1_sine_radioButton.setChecked(True)
        self.osc_1_sine_radioButton.setAutoExclusive(False)
        self.osc_1_square_radioButton = QRadioButton(self.centralwidget)
        self.osc_1_square_radioButton.setObjectName(u"osc_1_square_radioButton")
        self.osc_1_square_radioButton.setGeometry(QRect(10, 270, 80, 21))
        self.osc_1_square_radioButton.setFont(font1)
        self.osc_1_square_radioButton.setAutoExclusive(False)
        self.osc_1_sawtooth_radioButton = QRadioButton(self.centralwidget)
        self.osc_1_sawtooth_radioButton.setObjectName(u"osc_1_sawtooth_radioButton")
        self.osc_1_sawtooth_radioButton.setGeometry(QRect(130, 240, 121, 21))
        self.osc_1_sawtooth_radioButton.setFont(font1)
        self.osc_1_sawtooth_radioButton.setAutoExclusive(False)
        self.osc_1_triangle_radioButton = QRadioButton(self.centralwidget)
        self.osc_1_triangle_radioButton.setObjectName(u"osc_1_triangle_radioButton")
        self.osc_1_triangle_radioButton.setGeometry(QRect(130, 270, 101, 21))
        self.osc_1_triangle_radioButton.setFont(font1)
        self.osc_1_triangle_radioButton.setAutoExclusive(False)
        self.osc_1_type_rbtnGroup =  QButtonGroup()
        self.osc_1_type_rbtnGroup.addButton(self.osc_1_sine_radioButton)
        self.osc_1_type_rbtnGroup.addButton(self.osc_1_square_radioButton)
        self.osc_1_type_rbtnGroup.addButton(self.osc_1_sawtooth_radioButton)
        self.osc_1_type_rbtnGroup.addButton(self.osc_1_triangle_radioButton)
        self.osc_1_type_rbtnGroup.setExclusive(True)
        self.osc_1_sine_radioButton.toggled.connect(self.osc_1_sine_radioButton_clicked)
        self.osc_1_square_radioButton.toggled.connect(self.osc_1_square_radioButton_clicked)
        self.osc_1_sawtooth_radioButton.toggled.connect(self.osc_1_sawtooth_radioButton_clicked)
        self.osc_1_triangle_radioButton.toggled.connect(self.osc_1_triangle_radioButton_clicked)
        self.osc_1_off_radioButton = QRadioButton(self.centralwidget)
        self.osc_1_off_radioButton.setObjectName(u"osc_1_off_radioButton")
        self.osc_1_off_radioButton.setGeometry(QRect(10, 60, 80, 21))
        self.osc_1_off_radioButton.setFont(font1)
        self.osc_1_off_radioButton.setAutoExclusive(False)
        self.osc_1_off_radioButton.toggled.connect(self.osc_1_off_radioButton_clicked)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 20, 111, 16))
        self.label_2.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(320, 110, 231, 101))
        self.lfo_1_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.lfo_1_layout.setObjectName(u"lfo_1_layout")
        self.lfo_1_layout.setContentsMargins(0, 0, 0, 0)
        self.lfo_1_off_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_off_radioButton.setObjectName(u"lfo_1_off_radioButton")
        self.lfo_1_off_radioButton.setGeometry(QRect(320, 60, 80, 21))
        self.lfo_1_off_radioButton.setFont(font1)
        self.lfo_1_off_radioButton.setAutoExclusive(False)
        self.lfo_1_off_radioButton.toggled.connect(self.lfo_1_off_radioButton_clicked)
        self.lfo_1_AM_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_AM_radioButton.setObjectName(u"lfo_1_AM_radioButton")
        self.lfo_1_AM_radioButton.setGeometry(QRect(320, 320, 80, 21))
        self.lfo_1_AM_radioButton.setFont(font1)
        self.lfo_1_AM_radioButton.setAutoExclusive(False)
        self.lfo_1_AM_radioButton.setChecked(True)
        self.lfo_1_FM_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_FM_radioButton.setObjectName(u"lfo_1_FM_radioButton")
        self.lfo_1_FM_radioButton.setGeometry(QRect(420, 320, 61, 21))
        self.lfo_1_FM_radioButton.setFont(font1)
        self.lfo_1_FM_radioButton.setAutoExclusive(False)
        self.lfo_1_PM_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_PM_radioButton.setObjectName(u"lfo_1_PM_radioButton")
        self.lfo_1_PM_radioButton.setGeometry(QRect(500, 320, 51, 21))
        self.lfo_1_PM_radioButton.setFont(font1)
        self.lfo_1_PM_radioButton.setAutoExclusive(False)

        self.mod_1_type_rbtnGroup =  QButtonGroup()
        self.mod_1_type_rbtnGroup.addButton(self.lfo_1_AM_radioButton)
        self.mod_1_type_rbtnGroup.addButton(self.lfo_1_FM_radioButton)
        self.mod_1_type_rbtnGroup.addButton(self.lfo_1_PM_radioButton)
        self.mod_1_type_rbtnGroup.setExclusive(True)
        self.lfo_1_AM_radioButton.toggled.connect(self.lfo_1_AM_radioButton_clicked)
        self.lfo_1_FM_radioButton.toggled.connect(self.lfo_1_FM_radioButton_clicked)
        self.lfo_1_PM_radioButton.toggled.connect(self.lfo_1_PM_radioButton_clicked)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(630, 20, 111, 16))
        self.label_3.setFont(font)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(630, 110, 231, 101))
        self.adsr_1_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.adsr_1_layout.setObjectName(u"adsr_1_layout")
        self.adsr_1_layout.setContentsMargins(0, 0, 0, 0)
        self.adsr_1_off_radioButton = QRadioButton(self.centralwidget)
        self.adsr_1_off_radioButton.setObjectName(u"adsr_1_off_radioButton")
        self.adsr_1_off_radioButton.setGeometry(QRect(630, 60, 80, 21))
        self.adsr_1_off_radioButton.setFont(font1)
        self.adsr_1_off_radioButton.setAutoExclusive(False)
        self.adsr_1_off_radioButton.toggled.connect(self.adsr_1_off_radioButton_clicked)
        self.lfo_1_rate_dial = QDial(self.centralwidget)
        self.lfo_1_rate_dial.setObjectName(u"lfo_1_rate_dial")
        self.lfo_1_rate_dial.setGeometry(QRect(310, 380, 50, 64))
        self.lfo_1_rate_dial.setNotchesVisible(True)
        self.lfo_1_rate_dial.valueChanged.connect(self.lfo_1_rate_dial_moved)
        # self.lfo_1_rate_dial.setNotchTarget(10)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 370, 47, 14))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 370, 61, 16))
        self.label_5.setFont(font1)
        self.lfo_1_amount_dial = QDial(self.centralwidget)
        self.lfo_1_amount_dial.setObjectName(u"lfo_1_amount_dial")
        self.lfo_1_amount_dial.setGeometry(QRect(390, 380, 50, 64))
        self.lfo_1_amount_dial.setNotchesVisible(True)
        self.lfo_1_amount_dial.valueChanged.connect(self.lfo_1_amount_dial_moved)
        self.adsr_1_att_slider = QSlider(self.centralwidget)
        self.adsr_1_att_slider.setObjectName(u"adsr_1_att_slider")
        self.adsr_1_att_slider.setGeometry(QRect(700, 240, 160, 16))
        self.adsr_1_att_slider.setMaximum(99)
        self.adsr_1_att_slider.setSingleStep(1)
        self.adsr_1_att_slider.setValue(10)
        self.adsr_1_att_slider.setOrientation(Qt.Horizontal)
        self.adsr_1_dec_slider = QSlider(self.centralwidget)
        self.adsr_1_dec_slider.setObjectName(u"adsr_1_dec_slider")
        self.adsr_1_dec_slider.setGeometry(QRect(700, 280, 160, 16))
        self.adsr_1_dec_slider.setValue(10)
        self.adsr_1_dec_slider.setOrientation(Qt.Horizontal)
        self.adsr_1_sus_slider = QSlider(self.centralwidget)
        self.adsr_1_sus_slider.setObjectName(u"adsr_1_sus_slider")
        self.adsr_1_sus_slider.setGeometry(QRect(700, 320, 160, 16))
        self.adsr_1_sus_slider.setValue(10)
        self.adsr_1_sus_slider.setOrientation(Qt.Horizontal)
        self.adsr_1_rel_slider = QSlider(self.centralwidget)
        self.adsr_1_rel_slider.setObjectName(u"adsr_1_rel_slider")
        self.adsr_1_rel_slider.setGeometry(QRect(700, 360, 160, 16))
        self.adsr_1_rel_slider.setValue(10)
        self.adsr_1_rel_slider.setOrientation(Qt.Horizontal)
        self.adsr_1_att_slider.valueChanged.connect(self.adsr_1_att_slider_moved)
        self.adsr_1_dec_slider.valueChanged.connect(self.adsr_1_dec_slider_moved)
        self.adsr_1_sus_slider.valueChanged.connect(self.adsr_1_sus_slider_moved)
        self.adsr_1_rel_slider.valueChanged.connect(self.adsr_1_rel_slider_moved)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(630, 240, 47, 14))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(630, 280, 47, 14))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(630, 320, 61, 16))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(630, 360, 61, 16))
        self.label_9.setFont(font1)
        self.lfo_2_off_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_off_radioButton.setObjectName(u"lfo_2_off_radioButton")
        self.lfo_2_off_radioButton.setGeometry(QRect(320, 520, 80, 21))
        self.lfo_2_off_radioButton.setFont(font1)
        self.lfo_2_off_radioButton.setAutoExclusive(False)
        self.lfo_2_off_radioButton.toggled.connect(self.lfo_2_off_radioButton_clicked)
        self.adsr_2_off_radioButton = QRadioButton(self.centralwidget)
        self.adsr_2_off_radioButton.setObjectName(u"adsr_2_off_radioButton")
        self.adsr_2_off_radioButton.setGeometry(QRect(630, 520, 80, 21))
        self.adsr_2_off_radioButton.setFont(font1)
        self.adsr_2_off_radioButton.setAutoExclusive(False)
        self.adsr_2_off_radioButton.toggled.connect(self.adsr_2_off_radioButton_clicked)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(630, 820, 61, 16))
        self.label_10.setFont(font1)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 480, 111, 16))
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(320, 480, 111, 16))
        self.label_12.setFont(font)
        self.lfo_2_amount_dial = QDial(self.centralwidget)
        self.lfo_2_amount_dial.setObjectName(u"lfo_2_amount_dial")
        self.lfo_2_amount_dial.setGeometry(QRect(390, 840, 50, 64))
        self.lfo_2_amount_dial.setNotchesVisible(True)
        self.lfo_2_amount_dial.valueChanged.connect(self.lfo_2_amount_dial_moved)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(320, 830, 47, 14))
        self.label_13.setFont(font1)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(630, 570, 231, 101))
        self.adsr_2_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.adsr_2_layout.setObjectName(u"adsr_2_layout")
        self.adsr_2_layout.setContentsMargins(0, 0, 0, 0)
        self.adsr_2_sus_slider = QSlider(self.centralwidget)
        self.adsr_2_sus_slider.setObjectName(u"adsr_2_sus_slider")
        self.adsr_2_sus_slider.setGeometry(QRect(700, 780, 160, 16))
        self.adsr_2_sus_slider.setValue(10)
        self.adsr_2_sus_slider.setOrientation(Qt.Horizontal)
        self.lfo_2_square_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_square_radioButton.setObjectName(u"lfo_2_square_radioButton")
        self.lfo_2_square_radioButton.setGeometry(QRect(320, 730, 80, 21))
        self.lfo_2_square_radioButton.setFont(font1)
        self.lfo_2_square_radioButton.setAutoExclusive(False)
        self.osc_2_triangle_radioButton = QRadioButton(self.centralwidget)
        self.osc_2_triangle_radioButton.setObjectName(u"osc_2_triangle_radioButton")
        self.osc_2_triangle_radioButton.setGeometry(QRect(130, 730, 101, 21))
        self.osc_2_triangle_radioButton.setFont(font1)
        self.osc_2_triangle_radioButton.setAutoExclusive(False)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(320, 570, 231, 101))
        self.lfo_2_layout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.lfo_2_layout.setObjectName(u"lfo_2_layout")
        self.lfo_2_layout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(630, 740, 47, 14))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(630, 780, 61, 16))
        self.label_15.setFont(font1)
        self.osc_2_off_radioButton = QRadioButton(self.centralwidget)
        self.osc_2_off_radioButton.setObjectName(u"osc_2_off_radioButton")
        self.osc_2_off_radioButton.setGeometry(QRect(10, 520, 80, 21))
        self.osc_2_off_radioButton.setFont(font1)
        self.osc_2_off_radioButton.setAutoExclusive(False)
        self.osc_2_off_radioButton.toggled.connect(self.osc_2_off_radioButton_clicked)
        self.lfo_2_rate_dial = QDial(self.centralwidget)
        self.lfo_2_rate_dial.setObjectName(u"lfo_2_rate_dial")
        self.lfo_2_rate_dial.setGeometry(QRect(310, 840, 50, 64))
        self.lfo_2_rate_dial.setNotchesVisible(True)
        self.lfo_2_rate_dial.valueChanged.connect(self.lfo_2_rate_dial_moved)
        self.osc_2_sawtooth_radioButton = QRadioButton(self.centralwidget)
        self.osc_2_sawtooth_radioButton.setObjectName(u"osc_2_sawtooth_radioButton")
        self.osc_2_sawtooth_radioButton.setGeometry(QRect(130, 700, 121, 21))
        self.osc_2_sawtooth_radioButton.setFont(font1)
        self.osc_2_sawtooth_radioButton.setAutoExclusive(False)
        self.adsr_2_rel_slider = QSlider(self.centralwidget)
        self.adsr_2_rel_slider.setObjectName(u"adsr_2_rel_slider")
        self.adsr_2_rel_slider.setGeometry(QRect(700, 820, 160, 16))
        self.adsr_2_rel_slider.setValue(10)
        self.adsr_2_rel_slider.setOrientation(Qt.Horizontal)
        self.lfo_2_sine_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_sine_radioButton.setObjectName(u"lfo_2_sine_radioButton")
        self.lfo_2_sine_radioButton.setGeometry(QRect(320, 700, 80, 21))
        self.lfo_2_sine_radioButton.setFont(font1)
        self.lfo_2_sine_radioButton.setChecked(True)
        self.lfo_2_sine_radioButton.setAutoExclusive(False)
        self.lfo_2_PM_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_PM_radioButton.setObjectName(u"lfo_2_PM_radioButton")
        self.lfo_2_PM_radioButton.setGeometry(QRect(500, 780, 51, 21))
        self.lfo_2_PM_radioButton.setFont(font1)
        self.lfo_2_PM_radioButton.setAutoExclusive(False)
        self.lfo_2_sawtooth_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_sawtooth_radioButton.setObjectName(u"lfo_2_sawtooth_radioButton")
        self.lfo_2_sawtooth_radioButton.setGeometry(QRect(440, 700, 121, 21))
        self.lfo_2_sawtooth_radioButton.setFont(font1)
        self.lfo_2_sawtooth_radioButton.setAutoExclusive(False)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(630, 480, 111, 16))
        self.label_16.setFont(font)
        self.lfo_2_FM_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_FM_radioButton.setObjectName(u"lfo_2_FM_radioButton")
        self.lfo_2_FM_radioButton.setGeometry(QRect(420, 780, 61, 21))
        self.lfo_2_FM_radioButton.setFont(font1)
        self.lfo_2_FM_radioButton.setAutoExclusive(False)
        self.osc_2_square_radioButton = QRadioButton(self.centralwidget)
        self.osc_2_square_radioButton.setObjectName(u"osc_2_square_radioButton")
        self.osc_2_square_radioButton.setGeometry(QRect(10, 730, 80, 21))
        self.osc_2_square_radioButton.setFont(font1)
        self.osc_2_square_radioButton.setAutoExclusive(False)
        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 570, 231, 101))
        self.osc_2_layout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.osc_2_layout.setObjectName(u"osc_2_layout")
        self.osc_2_layout.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(390, 830, 61, 16))
        self.label_17.setFont(font1)
        self.osc_2_sine_radioButton = QRadioButton(self.centralwidget)
        self.osc_2_sine_radioButton.setObjectName(u"osc_2_sine_radioButton")
        self.osc_2_sine_radioButton.setGeometry(QRect(10, 700, 80, 21))
        self.osc_2_sine_radioButton.setFont(font1)
        self.osc_2_sine_radioButton.setChecked(True)
        self.osc_2_sine_radioButton.setAutoExclusive(False)

        self.osc_2_type_rbtnGroup =  QButtonGroup()
        self.osc_2_type_rbtnGroup.addButton(self.osc_2_sine_radioButton)
        self.osc_2_type_rbtnGroup.addButton(self.osc_2_square_radioButton)
        self.osc_2_type_rbtnGroup.addButton(self.osc_2_sawtooth_radioButton)
        self.osc_2_type_rbtnGroup.addButton(self.osc_2_triangle_radioButton)
        self.osc_2_type_rbtnGroup.setExclusive(True)
        self.osc_2_sine_radioButton.toggled.connect(self.osc_2_sine_radioButton_clicked)
        self.osc_2_square_radioButton.toggled.connect(self.osc_2_square_radioButton_clicked)
        self.osc_2_sawtooth_radioButton.toggled.connect(self.osc_2_sawtooth_radioButton_clicked)
        self.osc_2_triangle_radioButton.toggled.connect(self.osc_2_triangle_radioButton_clicked)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(630, 700, 47, 14))
        self.label_18.setFont(font1)
        self.lfo_2_triangle_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_triangle_radioButton.setObjectName(u"lfo_2_triangle_radioButton")
        self.lfo_2_triangle_radioButton.setGeometry(QRect(440, 730, 101, 21))
        self.lfo_2_triangle_radioButton.setFont(font1)
        self.lfo_2_triangle_radioButton.setAutoExclusive(False)

        self.lfo_2_type_rbtnGroup =  QButtonGroup()
        self.lfo_2_type_rbtnGroup.addButton(self.lfo_2_sine_radioButton)
        self.lfo_2_type_rbtnGroup.addButton(self.lfo_2_square_radioButton)
        self.lfo_2_type_rbtnGroup.addButton(self.lfo_2_sawtooth_radioButton)
        self.lfo_2_type_rbtnGroup.addButton(self.lfo_2_triangle_radioButton)
        self.lfo_2_type_rbtnGroup.setExclusive(True)
        self.lfo_2_sine_radioButton.toggled.connect(self.lfo_2_sine_radioButton_clicked)
        self.lfo_2_square_radioButton.toggled.connect(self.lfo_2_square_radioButton_clicked)
        self.lfo_2_sawtooth_radioButton.toggled.connect(self.lfo_2_sawtooth_radioButton_clicked)
        self.lfo_2_triangle_radioButton.toggled.connect(self.lfo_2_triangle_radioButton_clicked)

        self.lfo_2_AM_radioButton = QRadioButton(self.centralwidget)
        self.lfo_2_AM_radioButton.setObjectName(u"lfo_2_AM_radioButton")
        self.lfo_2_AM_radioButton.setGeometry(QRect(320, 780, 80, 21))
        self.lfo_2_AM_radioButton.setFont(font1)
        self.lfo_2_AM_radioButton.setAutoExclusive(False)
        self.lfo_2_AM_radioButton.setChecked(True)

        self.mod_2_type_rbtnGroup =  QButtonGroup()
        self.mod_2_type_rbtnGroup.addButton(self.lfo_2_AM_radioButton)
        self.mod_2_type_rbtnGroup.addButton(self.lfo_2_FM_radioButton)
        self.mod_2_type_rbtnGroup.addButton(self.lfo_2_PM_radioButton)
        self.mod_2_type_rbtnGroup.setExclusive(True)
        self.lfo_2_AM_radioButton.toggled.connect(self.lfo_2_AM_radioButton_clicked)
        self.lfo_2_FM_radioButton.toggled.connect(self.lfo_2_FM_radioButton_clicked)
        self.lfo_2_PM_radioButton.toggled.connect(self.lfo_2_PM_radioButton_clicked)

        self.adsr_2_att_slider = QSlider(self.centralwidget)
        self.adsr_2_att_slider.setObjectName(u"adsr_2_att_slider")
        self.adsr_2_att_slider.setGeometry(QRect(700, 700, 160, 16))
        self.adsr_2_att_slider.setValue(10)
        self.adsr_2_att_slider.setOrientation(Qt.Horizontal)
        self.adsr_2_dec_slider = QSlider(self.centralwidget)
        self.adsr_2_dec_slider.setObjectName(u"adsr_2_dec_slider")
        self.adsr_2_dec_slider.setGeometry(QRect(700, 740, 160, 16))
        self.adsr_2_dec_slider.setValue(10)
        self.adsr_2_dec_slider.setOrientation(Qt.Horizontal)
        self.adsr_2_att_slider.valueChanged.connect(self.adsr_2_att_slider_moved)
        self.adsr_2_dec_slider.valueChanged.connect(self.adsr_2_dec_slider_moved)
        self.adsr_2_sus_slider.valueChanged.connect(self.adsr_2_sus_slider_moved)
        self.adsr_2_rel_slider.valueChanged.connect(self.adsr_2_rel_slider_moved)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 450, 1521, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.line.setFont(font2)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(270, 0, 20, 901))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(580, 0, 20, 901))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(890, 0, 20, 901))
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(940, 20, 111, 16))
        self.label_19.setFont(font)
        self.detune_off_radioButton = QRadioButton(self.centralwidget)
        self.detune_off_radioButton.setObjectName(u"detune_off_radioButton")
        self.detune_off_radioButton.setGeometry(QRect(940, 60, 80, 21))
        self.detune_off_radioButton.setFont(font1)
        self.detune_off_radioButton.setAutoExclusive(False)
        self.detune_off_radioButton.toggled.connect(self.detune_off_radioButton_clicked)
        self.detune_value_dial = QDial(self.centralwidget)
        self.detune_value_dial.setObjectName(u"detune_value_dial")
        self.detune_value_dial.setGeometry(QRect(930, 110, 111, 101))
        self.detune_value_dial.setOrientation(Qt.Horizontal)
        self.detune_value_dial.setWrapping(False)
        self.detune_value_dial.setNotchesVisible(True)
        self.detune_value_dial.valueChanged.connect(self.detune_value_dial_moved)
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(940, 480, 111, 16))
        self.label_21.setFont(font)
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(940, 740, 81, 16))
        self.label_22.setFont(font1)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(940, 700, 91, 16))
        self.label_23.setFont(font1)
        self.osc_1_value_slider = QSlider(self.centralwidget)
        self.osc_1_value_slider.setObjectName(u"osc_1_value_slider")
        self.osc_1_value_slider.setGeometry(QRect(1040, 700, 131, 16))
        self.osc_1_value_slider.setValue(99)
        self.osc_1_value_slider.setOrientation(Qt.Horizontal)
        self.osc_2_value_slider = QSlider(self.centralwidget)
        self.osc_2_value_slider.setObjectName(u"osc_2_value_slider")
        self.osc_2_value_slider.setGeometry(QRect(1040, 740, 131, 16))
        self.osc_2_value_slider.setValue(99)
        self.osc_2_value_slider.setOrientation(Qt.Horizontal)
        self.osc_1_value_slider.valueChanged.connect(self.osc_1_value_dial_moved)
        self.osc_2_value_slider.valueChanged.connect(self.osc_2_value_dial_moved)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(1200, 0, 20, 901))
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(940, 570, 231, 101))
        self.adder_layot = QVBoxLayout(self.verticalLayoutWidget_7)
        self.adder_layot.setObjectName(u"adder_layot")
        self.adder_layot.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(1250, 20, 111, 16))
        self.label_24.setFont(font)
        self.panner_lfo_sine_radioButton = QRadioButton(self.centralwidget)
        self.panner_lfo_sine_radioButton.setObjectName(u"panner_lfo_sine_radioButton")
        self.panner_lfo_sine_radioButton.setGeometry(QRect(1250, 290, 80, 21))
        self.panner_lfo_sine_radioButton.setFont(font1)
        self.panner_lfo_sine_radioButton.setChecked(True)
        self.panner_lfo_sine_radioButton.setAutoExclusive(False)
        self.panner_modulated_radioButton = QRadioButton(self.centralwidget)
        self.panner_modulated_radioButton.setObjectName(u"panner_modulated_radioButton")
        self.panner_modulated_radioButton.setGeometry(QRect(1250, 240, 111, 21))
        self.panner_modulated_radioButton.setFont(font1)
        self.panner_modulated_radioButton.setAutoExclusive(False)
        self.panner_modulated_radioButton.toggled.connect(self.panner_modulated_radioButton_clicked)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(1250, 370, 47, 14))
        self.label_25.setFont(font1)
        self.panner_lfo_square_radioButton = QRadioButton(self.centralwidget)
        self.panner_lfo_square_radioButton.setObjectName(u"panner_lfo_square_radioButton")
        self.panner_lfo_square_radioButton.setGeometry(QRect(1250, 320, 80, 21))
        self.panner_lfo_square_radioButton.setFont(font1)
        self.panner_lfo_square_radioButton.setAutoExclusive(False)
        self.panner_off_radioButton = QRadioButton(self.centralwidget)
        self.panner_off_radioButton.setObjectName(u"panner_off_radioButton")
        self.panner_off_radioButton.setGeometry(QRect(1250, 60, 80, 21))
        self.panner_off_radioButton.setFont(font1)
        self.panner_off_radioButton.setAutoExclusive(False)
        self.panner_off_radioButton.toggled.connect(self.panner_off_radioButton_clicked)
        self.panner_rate_dial = QDial(self.centralwidget)
        self.panner_rate_dial.setObjectName(u"panner_rate_dial")
        self.panner_rate_dial.setGeometry(QRect(1240, 380, 50, 64))
        self.panner_rate_dial.setNotchTarget(3.700000000000000)
        self.panner_rate_dial.setNotchesVisible(True)
        self.panner_rate_dial.valueChanged.connect(self.panner_rate_dial_moved)
        self.panner_lfo_triangle_radioButton = QRadioButton(self.centralwidget)
        self.panner_lfo_triangle_radioButton.setObjectName(u"panner_lfo_triangle_radioButton")
        self.panner_lfo_triangle_radioButton.setGeometry(QRect(1370, 320, 101, 21))
        self.panner_lfo_triangle_radioButton.setFont(font1)
        self.panner_lfo_triangle_radioButton.setAutoExclusive(False)
        self.panner_lfo_sawtooth_radioButton = QRadioButton(self.centralwidget)
        self.panner_lfo_sawtooth_radioButton.setObjectName(u"panner_lfo_sawtooth_radioButton")
        self.panner_lfo_sawtooth_radioButton.setGeometry(QRect(1370, 290, 121, 21))
        self.panner_lfo_sawtooth_radioButton.setFont(font1)
        self.panner_lfo_sawtooth_radioButton.setAutoExclusive(False)

        self.panner_lfo_type_rbtnGroup =  QButtonGroup()
        self.panner_lfo_type_rbtnGroup.addButton(self.panner_lfo_sine_radioButton)
        self.panner_lfo_type_rbtnGroup.addButton(self.panner_lfo_square_radioButton)
        self.panner_lfo_type_rbtnGroup.addButton(self.panner_lfo_sawtooth_radioButton)
        self.panner_lfo_type_rbtnGroup.addButton(self.panner_lfo_triangle_radioButton)
        self.panner_lfo_type_rbtnGroup.setExclusive(True)
        self.panner_lfo_sine_radioButton.toggled.connect(self.panner_lfo_sine_radioButton_clicked)
        self.panner_lfo_square_radioButton.toggled.connect(self.panner_lfo_square_radioButton_clicked)
        self.panner_lfo_sawtooth_radioButton.toggled.connect(self.panner_lfo_sawtooth_radioButton_clicked)
        self.panner_lfo_triangle_radioButton.toggled.connect(self.panner_lfo_triangle_radioButton_clicked)

        self.panner_value_dial = QDial(self.centralwidget)
        self.panner_value_dial.setObjectName(u"panner_value_dial")
        self.panner_value_dial.setGeometry(QRect(1240, 110, 111, 101))
        self.panner_value_dial.setNotchesVisible(True)
        self.panner_value_dial.valueChanged.connect(self.panner_value_dial_moved)
        self.lfo_1_sine_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_sine_radioButton.setObjectName(u"lfo_1_sine_radioButton")
        self.lfo_1_sine_radioButton.setGeometry(QRect(320, 240, 80, 21))
        self.lfo_1_sine_radioButton.setFont(font1)
        self.lfo_1_sine_radioButton.setChecked(True)
        self.lfo_1_sine_radioButton.setAutoExclusive(False)
        self.lfo_1_triangle_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_triangle_radioButton.setObjectName(u"lfo_1_triangle_radioButton")
        self.lfo_1_triangle_radioButton.setGeometry(QRect(440, 270, 101, 21))
        self.lfo_1_triangle_radioButton.setFont(font1)
        self.lfo_1_triangle_radioButton.setAutoExclusive(False)
        self.lfo_1_square_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_square_radioButton.setObjectName(u"lfo_1_square_radioButton")
        self.lfo_1_square_radioButton.setGeometry(QRect(320, 270, 80, 21))
        self.lfo_1_square_radioButton.setFont(font1)
        self.lfo_1_square_radioButton.setAutoExclusive(False)
        self.lfo_1_sawtooth_radioButton = QRadioButton(self.centralwidget)
        self.lfo_1_sawtooth_radioButton.setObjectName(u"lfo_1_sawtooth_radioButton")
        self.lfo_1_sawtooth_radioButton.setGeometry(QRect(440, 240, 121, 21))
        self.lfo_1_sawtooth_radioButton.setFont(font1)
        self.lfo_1_sawtooth_radioButton.setAutoExclusive(False)

        self.lfo_1_type_rbtnGroup =  QButtonGroup()
        self.lfo_1_type_rbtnGroup.addButton(self.lfo_1_sine_radioButton)
        self.lfo_1_type_rbtnGroup.addButton(self.lfo_1_square_radioButton)
        self.lfo_1_type_rbtnGroup.addButton(self.lfo_1_sawtooth_radioButton)
        self.lfo_1_type_rbtnGroup.addButton(self.lfo_1_triangle_radioButton)
        self.lfo_1_type_rbtnGroup.setExclusive(True)
        self.lfo_1_sine_radioButton.toggled.connect(self.lfo_1_sine_radioButton_clicked)
        self.lfo_1_square_radioButton.toggled.connect(self.lfo_1_square_radioButton_clicked)
        self.lfo_1_sawtooth_radioButton.toggled.connect(self.lfo_1_sawtooth_radioButton_clicked)
        self.lfo_1_triangle_radioButton.toggled.connect(self.lfo_1_triangle_radioButton_clicked)

        self.master_dial = QDial(self.centralwidget)
        self.master_dial.setObjectName(u"detune_value_dial_2")
        self.master_dial.setGeometry(QRect(1240, 570, 111, 101))
        self.master_dial.setOrientation(Qt.Horizontal)
        self.master_dial.setWrapping(False)
        self.master_dial.setNotchesVisible(True)
        self.master_dial.valueChanged.connect(self.master_dial_moved)
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(1250, 480, 111, 16))
        self.label_26.setFont(font)
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(630, 390, 61, 51))
        self.label_20.setFont(font1)
        self.adsr_1_level_slider = QSlider(self.centralwidget)
        self.adsr_1_level_slider.setObjectName(u"adsr_1_level_slider")
        self.adsr_1_level_slider.setGeometry(QRect(700, 410, 160, 16))
        self.adsr_1_level_slider.setValue(10)
        self.adsr_1_level_slider.setOrientation(Qt.Horizontal)
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(630, 850, 61, 51))
        self.label_27.setFont(font1)
        self.adsr_2_level_slider = QSlider(self.centralwidget)
        self.adsr_2_level_slider.setObjectName(u"adsr_2_level_slider")
        self.adsr_2_level_slider.setGeometry(QRect(700, 870, 160, 16))
        self.adsr_2_level_slider.setValue(10)
        self.adsr_2_level_slider.setOrientation(Qt.Horizontal)
        self.adsr_1_level_slider.valueChanged.connect(self.adsr_1_level_slider_moved)
        self.adsr_2_level_slider.valueChanged.connect(self.adsr_2_level_slider_moved)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1522, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionSample_Rate)
        # self.pen = pg.mkPen(color=(255, 0, 0), width=5)
        # self.pen_1 = pg.mkPen(color=(0, 255, 0), width=5)
        # self.wave_gen = WaveGenerator(20000)
        # self.envelope_1_a = Envelope(0.3, 0.2, 3.8, 0.9, 0.8, 20000)
        # self.envelope_2_a = Envelope(0.5, 0.5, 2, 5.9, 0.5, 20000)
        #
        # self.osc_1_view = pg.PlotWidget()
        # self.osc_1_view.setBackground('w')
        # self.osc_1_view.setXRange(0, 20000, padding=0)
        # self.osc_1_view.setYRange(-1.2, 1.2, padding=0)
        # self.osc_1_view.hideAxis('bottom')
        # self.osc_1_view.hideAxis('left')
        # self.osc_1_layout.addWidget(self.osc_1_view)
        # self.osc_1_view.plot(self.wave_gen.sine_wave,pen=self.pen)
        #
        # self.osc_2_view = pg.PlotWidget()
        # self.osc_2_view.setBackground('w')
        # self.osc_2_view.setXRange(-2, 20002, padding=0)
        # self.osc_2_view.setYRange(-1.2, 1.2, padding=0)
        # self.osc_2_view.hideAxis('bottom')
        # self.osc_2_view.hideAxis('left')
        # self.osc_2_layout.addWidget(self.osc_2_view)
        # self.osc_2_view.plot(self.wave_gen.sawtooth_wave,pen=self.pen_1)
        #
        # self.lfo_1_view = pg.PlotWidget()
        # self.lfo_1_view.enableMouse(False)
        # self.lfo_1_view.setBackground('w')
        # self.lfo_1_view.setXRange(0, 20000, padding=0)
        # self.lfo_1_view.setYRange(-1.2, 1.2, padding=0)
        # self.lfo_1_view.hideAxis('bottom')
        # self.lfo_1_view.hideAxis('left')
        # self.lfo_1_layout.addWidget(self.lfo_1_view)
        # self.lfo_1_view.plot(self.wave_gen.square_wave,pen=self.pen)
        #
        # self.lfo_2_view = pg.PlotWidget()
        # self.lfo_2_view.setBackground('w')
        # self.lfo_2_view.setXRange(0, 20000, padding=0)
        # self.lfo_2_view.setYRange(-1.2, 1.2, padding=0)
        # self.lfo_2_view.hideAxis('bottom')
        # self.lfo_2_view.hideAxis('left')
        # self.lfo_2_layout.addWidget(self.lfo_2_view)
        # self.lfo_2_view.plot(self.wave_gen.triangle_wave,pen=self.pen_1)
        #
        # self.adsr_1_view = pg.PlotWidget()
        # self.adsr_1_view.setBackground('w')
        # self.adsr_1_view.setXRange(0, 10*20000, padding=0)
        # self.adsr_1_view.setYRange(-0.2, 1.2, padding=0)
        # self.adsr_1_view.hideAxis('bottom')
        # self.adsr_1_view.hideAxis('left')
        # self.adsr_1_layout.addWidget(self.adsr_1_view)
        # self.adsr_1_view.plot(self.envelope_1_a.values, pen=self.pen)
        #
        # self.adsr_2_view = pg.PlotWidget()
        # self.adsr_2_view.setBackground('w')
        # self.adsr_2_view.setXRange(0, 10*20000, padding=0)
        # self.adsr_2_view.setYRange(-0.2, 1.2, padding=0)
        # self.adsr_2_view.hideAxis('bottom')
        # self.adsr_2_view.hideAxis('left')
        # self.adsr_2_layout.addWidget(self.adsr_2_view)
        # self.adsr_2_view.plot(self.envelope_2_a.values, pen=self.pen_1)

        self.render_rate = 44100

        # t1 = time.time()
        self.wave_generator = WaveGenerator(self.render_rate)
        # print(" Total time taken is :", time.time() - t1)

        self.lfo_1 = LFO(Oscillator(Type.sine,self.wave_generator,self.render_rate))

        self.envelope_1 = Envelope(0.1,0.2,3.8,0.9,0.9,self.render_rate)

        self.modulation_1 = LFOModulation(ModulationType.fm)

        self.detune_1 = Detune(0)
        self.detune_2 = ModulatedDetune(1/4,self.lfo_1,2)

        self.wave_adder_1 = WaveAdder(1,1,0.5)

        self.panner_1 = StereoPanner(0.3)
        self.panner_2 = ModulatedPanner(0.2,self.lfo_1,4)

        self.base_oscillator_1 = Oscillator(Type.sawtooth,self.wave_generator,self.render_rate)
        self.base_oscillator_2 = Oscillator(Type.sine,self.wave_generator,self.render_rate)
        self.modulated_oscillator = ModulatedOscillator(Type.sine,self.wave_generator,self.lfo_1,3,self.envelope_1,
                                                        self.modulation_1,1,self.render_rate)

        self.params = SynthParams()

        self.synth = Synth(self.base_oscillator_2,self.base_oscillator_2,
                           detune=self.detune_1,
                           wave_adder=self.wave_adder_1,
                           stereo_panner=self.panner_1,
                           params=self.params,
                           render_rate=self.render_rate,
                           stereo=False)

        self.synth.get_next_sample_with_numba(1,1,0,256,self.render_rate)

        self.midi_in = rtmidi.MidiIn()
        #
        # port = None
        # while not isinstance(port, int):
        #     self.midi_info()
        #     port = input()
        #     try:
        #         port = int(port)
        #     except ValueError:
        #         print("Port need to be a number!\n")

        self.controller = Controller(synth=self.synth,sample_rate=self.render_rate)
        self.controller.change_midi_port(0, self.midi_in.get_port_count())
        self.controller.toggle()

        self.count = 0

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def osc_1_off_radioButton_clicked(self):
        self.synth.params.osc_1_is_working = not self.sender().isChecked()
    def osc_1_sine_radioButton_clicked(self):
        self.synth.params.osc_1_type = 0
    def osc_1_square_radioButton_clicked(self):
        self.synth.params.osc_1_type = 1
    def osc_1_sawtooth_radioButton_clicked(self):
        self.synth.params.osc_1_type = 2
    def osc_1_triangle_radioButton_clicked(self):
        self.synth.params.osc_1_type = 3

    def osc_2_off_radioButton_clicked(self):
        self.synth.params.osc_2_is_working = not self.sender().isChecked()
    def osc_2_sine_radioButton_clicked(self):
        self.synth.params.osc_2_type = 0
    def osc_2_square_radioButton_clicked(self):
        self.synth.params.osc_2_type = 1
    def osc_2_sawtooth_radioButton_clicked(self):
        self.synth.params.osc_2_type = 2
    def osc_2_triangle_radioButton_clicked(self):
        self.synth.params.osc_2_type = 3

    def lfo_1_off_radioButton_clicked(self):
        self.synth.params.mod_1_is_working = not self.sender().isChecked()
    def lfo_1_sine_radioButton_clicked(self):
        self.synth.params.lfo_1_type = 0
    def lfo_1_square_radioButton_clicked(self):
        self.synth.params.lfo_1_type = 1
    def lfo_1_sawtooth_radioButton_clicked(self):
        self.synth.params.lfo_1_type = 2
    def lfo_1_triangle_radioButton_clicked(self):
        self.synth.params.lfo_1_type = 3
    def lfo_1_AM_radioButton_clicked(self):
        self.synth.params.mod_1_type = 0
    def lfo_1_FM_radioButton_clicked(self):
        self.synth.params.mod_1_type = 1
    def lfo_1_PM_radioButton_clicked(self):
        self.synth.params.mod_1_type = 2
    def lfo_1_rate_dial_moved(self):
        self.synth.params.lfo_1_frequency = 0.19*self.lfo_1_rate_dial.value() + 1
    def lfo_1_amount_dial_moved(self):
        self.synth.params.mod_1_index = 1/11*self.lfo_1_amount_dial.value() + 1

    def lfo_2_off_radioButton_clicked(self):
        self.synth.params.mod_2_is_working = not self.sender().isChecked()
    def lfo_2_sine_radioButton_clicked(self):
        self.synth.params.lfo_2_type = 0
    def lfo_2_square_radioButton_clicked(self):
        self.synth.params.lfo_2_type = 1
    def lfo_2_sawtooth_radioButton_clicked(self):
        self.synth.params.lfo_2_type = 2
    def lfo_2_triangle_radioButton_clicked(self):
        self.synth.params.lfo_2_type = 3
    def lfo_2_AM_radioButton_clicked(self):
        self.synth.params.mod_2_type = 0
    def lfo_2_FM_radioButton_clicked(self):
        self.synth.params.mod_2_type = 1
    def lfo_2_PM_radioButton_clicked(self):
        self.synth.params.mod_2_type = 2
    def lfo_2_rate_dial_moved(self):
        self.synth.params.lfo_2_frequency = 0.19*self.lfo_2_rate_dial.value() + 1
    def lfo_2_amount_dial_moved(self):
        self.synth.params.mod_2_index = 1/11*self.lfo_2_amount_dial.value() + 1

    def adsr_1_off_radioButton_clicked(self):
        self.synth.params.adsr_1_is_working = not self.sender().isChecked()
    def adsr_1_att_slider_moved(self):
        self.synth.params.adsr_1[0] = 499/9900*self.adsr_1_att_slider.value()+0.01
    def adsr_1_dec_slider_moved(self):
        self.synth.params.adsr_1[1] = 499/9900*self.adsr_1_dec_slider.value()+0.01
    def adsr_1_sus_slider_moved(self):
        self.synth.params.adsr_1[2] = 499/9900*self.adsr_1_sus_slider.value()+0.01
    def adsr_1_rel_slider_moved(self):
        self.synth.params.adsr_1[3] = 499/9900*self.adsr_1_rel_slider.value()+0.01
    def adsr_1_level_slider_moved(self):
        self.synth.params.adsr_1[4] = 1/99*self.adsr_1_level_slider.value()

    def adsr_2_off_radioButton_clicked(self):
        self.synth.params.adsr_2_is_working = not self.sender().isChecked()
    def adsr_2_att_slider_moved(self):
        self.synth.params.adsr_2[0] = 499/9900*self.adsr_2_att_slider.value()+0.01
    def adsr_2_dec_slider_moved(self):
        self.synth.params.adsr_2[1] = 499/9900*self.adsr_2_dec_slider.value()+0.01
    def adsr_2_sus_slider_moved(self):
        self.synth.params.adsr_2[2] = 499/9900*self.adsr_2_sus_slider.value()+0.01
    def adsr_2_rel_slider_moved(self):
        self.synth.params.adsr_2[3] = 499/9900*self.adsr_2_rel_slider.value()+0.01
    def adsr_2_level_slider_moved(self):
        self.synth.params.adsr_2[4] = 1/99*self.adsr_2_level_slider.value()

    def panner_rate_dial_moved(self):
            self.synth.params.lfo_panner_frequency = 0.19*self.panner_rate_dial.value() + 1
    def panner_value_dial_moved(self):
        if not self.synth.params.panner_modulation_is_working:
            self.synth.params.panner_index = 1/99*self.panner_value_dial.value()
        else:
            self.synth.params.panner_index = 1/198*self.panner_value_dial.value()
    def panner_off_radioButton_clicked(self):
        self.synth.params.panner_is_working = not self.sender().isChecked()
    def panner_modulated_radioButton_clicked(self):
        self.synth.params.panner_modulation_is_working = not self.sender().isChecked()
    def panner_lfo_sine_radioButton_clicked(self):
        self.synth.params.lfo_panner_type = 0
    def panner_lfo_square_radioButton_clicked(self):
        self.synth.params.lfo_panner_type = 1
    def panner_lfo_sawtooth_radioButton_clicked(self):
        self.synth.params.lfo_panner_type = 2
    def panner_lfo_triangle_radioButton_clicked(self):
        self.synth.params.lfo_panner_type = 3

    def detune_value_dial_moved(self):
        self.synth.params.detune_index = 1/297*self.detune_value_dial.value()
    def detune_off_radioButton_clicked(self):
        self.synth.params.detune_is_working = not self.sender().isChecked()

    def osc_1_value_dial_moved(self):
        self.synth.params.osc_1_adder_index = 1/99*self.osc_1_value_slider.value()
    def osc_2_value_dial_moved(self):
        self.synth.params.osc_2_adder_index = 1/99*self.osc_2_value_slider.value()

    def master_dial_moved(self):
        self.synth.params.master = 2/99*self.master_dial.value()

    def midi_info(self):
        print("Available MIDI ports:\n")
        available_ports = self.midi_in.get_ports()
        for i in range(len(available_ports)):
            print("[", i, "]", available_ports[i])
        print("\nPlease select port of a MIDI device:")

    def run_synth_no_gui(self,synth):
        port = None
        while not isinstance(port, int):
            self.midi_info()
            port = input()
            try:
                port = int(port)
            except ValueError:
                print("Port need to be a number!\n")

        controller = Controller(synth=synth,sample_rate=self.render_rate)
        controller.change_midi_port(port, self.midi_in.get_port_count())
        controller.toggle()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSample_Rate.setText(QCoreApplication.translate("MainWindow", u"Sample Rate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Oscillator 1", None))
        self.osc_1_sine_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.osc_1_square_radioButton.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.osc_1_sawtooth_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sawtooth", None))
        self.osc_1_triangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.osc_1_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LFO 1", None))
        self.lfo_1_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.lfo_1_AM_radioButton.setText(QCoreApplication.translate("MainWindow", u"AM", None))
        self.lfo_1_FM_radioButton.setText(QCoreApplication.translate("MainWindow", u"FM", None))
        self.lfo_1_PM_radioButton.setText(QCoreApplication.translate("MainWindow", u"PM", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ADSR 1", None))
        self.adsr_1_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Decay", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sustain", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.lfo_2_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.adsr_2_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Oscillator 2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"LFO 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.lfo_2_square_radioButton.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.osc_2_triangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Decay", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sustain", None))
        self.osc_2_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.osc_2_sawtooth_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sawtooth", None))
        self.lfo_2_sine_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.lfo_2_PM_radioButton.setText(QCoreApplication.translate("MainWindow", u"PM", None))
        self.lfo_2_sawtooth_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sawtooth", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ADSR 2", None))
        self.lfo_2_FM_radioButton.setText(QCoreApplication.translate("MainWindow", u"FM", None))
        self.osc_2_square_radioButton.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.osc_2_sine_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.lfo_2_triangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.lfo_2_AM_radioButton.setText(QCoreApplication.translate("MainWindow", u"AM", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Detune", None))
        self.detune_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Adder", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Oscillator 2", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Oscillator 1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Panner", None))
        self.panner_lfo_sine_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.panner_modulated_radioButton.setText(QCoreApplication.translate("MainWindow", u"Modulated", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.panner_lfo_square_radioButton.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.panner_off_radioButton.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.panner_lfo_triangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.panner_lfo_sawtooth_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sawtooth", None))
        self.lfo_1_sine_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.lfo_1_triangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.lfo_1_square_radioButton.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.lfo_1_sawtooth_radioButton.setText(QCoreApplication.translate("MainWindow", u"Sawtooth", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Master", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Sustain\n"
                                                                       "level", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Sustain\n"
                                                                       "level", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi
