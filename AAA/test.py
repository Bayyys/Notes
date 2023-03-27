from PyQt5.QtWidgets import QFrame, QGridLayout
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTextEdit, QApplication, QLineEdit, QHBoxLayout
import sys
import time
import serial


str1 = '3a2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003efdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f0fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44002afeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bbfdffff6e124400ffffffffffffffff0d3b2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003ffdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400edfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440027feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c0fdffff6e124400ffffffffffffffff0e3c2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440039fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bdfdffff6e124400ffffffffffffffff073d2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003efdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400effdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440023feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bdfdffff6e124400ffffffffffffffff0a'

str2 = '2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440040fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b3fdffff6e124400ffffffffffffffffd20b2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003cfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f0fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440024feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b6fdffff6e124400ffffffffffffffffd10c2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440042fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001cfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c4fdffff6e124400ffffffffffffffffdf0d2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440041fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001ffeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bcfdffff6e124400ffffffffffffffffda0e2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440047fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440021feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bafdffff6e124400ffffffffffffffffe10f2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440048fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440019feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c2fdffff6e124400ffffffffffffffffe5102a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003dfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e9fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c4fdffff6e124400ffffffffffffffffda112a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003cfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e6fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400befdffff6e124400ffffffffffffffffd3122a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440039fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001bfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c5fdffff6e124400ffffffffffffffffdc132a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440041fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001afeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b0fdffff6e124400ffffffffffffffffd1142a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440034fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e7fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400affdffff6e124400ffffffffffffffffc0152a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003ffdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400ecfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b5fdffff6e124400ffffffffffffffffd7162a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440035fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e6fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001efeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c2fdffff6e124400ffffffffffffffffd1172a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440032fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440025feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b9fdffff6e124400ffffffffffffffffca182a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440038fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400ebfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001dfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b9fdffff6e124400ffffffffffffffffd1192a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440039fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400eafdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001ffeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c2fdffff6e124400ffffffffffffffffdd1a2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003ffdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400ebfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440021feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c4fdffff6e124400ffffffffffffffffe91b2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003efdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400eefdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440023feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c6fdffff6e124400fffffffffffffffff01c2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003cfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f6fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bbfdffff6e124400ffffffffffffffffe91d2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003afdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f5fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b9fdffff6e124400ffffffffffffffffe71e2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003efdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400eafdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c2fdffff6e124400ffffffffffffffffea1f2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44004ffdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e4fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440018feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b2fdffff6e124400ffffffffffffffffdc202a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440042fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001efeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bffdffff6e124400fffffffffffffffff0212a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440040fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e8fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001dfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400befdffff6e124400ffffffffffffffffe4222a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440040fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400eafdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400aefdffff6e124400ffffffffffffffffda232a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440041fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f2fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44002bfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b5fdffff6e124400fffffffffffffffff6242a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440040fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e7fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bbfdffff6e124400ffffffffffffffffe6252a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003cfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e6fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440017feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b7fdffff6e124400ffffffffffffffffd5262a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440040fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f2fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001efeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bdfdffff6e124400fffffffffffffffff3272a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440031fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440022feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b9fdffff6e124400ffffffffffffffffe6282a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440037fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400eefdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440028feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bdfdffff6e124400fffffffffffffffff2292a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003ffdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e9fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440026feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bcfdffff6e124400fffffffffffffffff32a2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440047fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b9fdffff6e124400fffffffffffffffffd2b2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440045fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f0fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440027feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b6fdffff6e124400fffffffffffffffffd2c2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440038fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e4fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440025feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bdfdffff6e124400ffffffffffffffffea2d2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440034fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e7fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440019feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b2fdffff6e124400ffffffffffffffffd32e2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003afdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400eafdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440016feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400befdffff6e124400ffffffffffffffffe62f2a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440042fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e3fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440018feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c5fdffff6e124400fffffffffffffffff1302a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440037fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e4fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001cfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c6fdffff6e124400ffffffffffffffffed312a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440038fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e6fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001dfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400c5fdffff6e124400fffffffffffffffff1322a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440042fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e7fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001efeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bffdffff6e124400fffffffffffffffff8332a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440046fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e9fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bdfdffff6e124400ffffffffffffffffff342a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440035fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f5fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001cfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bafdffff6e124400fffffffffffffffff4352a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440037fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440023feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bafdffff6e124400fffffffffffffffffa362a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003efdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f2fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440020feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b3fdffff6e124400fffffffffffffffff9372a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003cfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f4fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001bfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b2fdffff6e124400fffffffffffffffff4382a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b44003dfdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f0fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001dfeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400b5fdffff6e124400fffffffffffffffff7392a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440039fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400effdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44002afeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bffdffff6e124400ffffffffffffffff0a'

str3 = 'feffffa59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400,\
        bcfdffff 6e124400 ffffffff ffffffff\
        2b0a840100 a55a0000 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400,\
        4a,\
        fdffff a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400,\
        ee,\
        fdffff a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400,\
        24'

string = 'f1 322a0200 a55a0000 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 42fdffff a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 e7fdffff a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 1efeffff a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 a59b4400 bffdffff 6e124400 ffffffff ffffffff'

str4 = '322a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440042fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400e7fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b44001efeffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bffdffff6e124400ffffffffffffffff'

print(len(str1))
print(len(str2))
print(len(str3))
print("str4\t" + str(len(str4)))
print((4+4+4*32+8)*2)
all = ""

# 导入QApplication和相关类


# )
# every_time = time.strftime('%Y-%m-%d %H:%M:%S')# 时间戳
# data = ''

# print(ser)
from time import sleep

class myThread(QThread):
    sig = pyqtSignal(bytes)
    flag = False
    ser = serial.Serial(  # 下面这些参数根据情况修改
        port='COM3',  # 串口
        baudrate=4608000,  # 波特率
        stopbits=1,
        bytesize=8,
        parity='N',
        )
    count = 0
    rest = b''

    def go(self):
        self.flag = True
        self.ser.flushInput()
        print("start")

    def stop(self):
        self.flag = False
        self.ser.flushInput()
        print("stop")

    def run(self):
        self.ser.flushInput()
        while True:
            # print(self.flag)
            if self.flag and self.ser.in_waiting:
                data = self.ser.read(self.ser.in_waiting)
                self.sig.emit(data)
                print("--------------------")
                self.bytesSplit(data)
                # self.count += 1
                print('count' + str(self.count))
                sleep(0.000125)

    def bytesSplit(self, data):
        if len(self.rest) > 0:
            data = self.rest + data
        while len(data) > 144:
            if data.find(b'\xa5Z') != -1:
                index_s = data.find(b'\xa5Z') - 4
                index_e = index_s + 24
                get = data[index_s: index_e]
                print(get)
                self.count += 1
                print(len(get))
                self.rest = data[index_e:]
                data = data[index_e:]
            else:
                break
        print(self.rest)

    def bytesSplit2(self, data):
        if len(self.rest) > 0:
            data = self.rest + data
        while len(data) > 24:
            find = data.find(b'\xa5Z')
            if find != -1 and len(data) > find + 24:
                index_s = data.find(b'\xa5Z') + 4
                index_e = index_s + 10
                get = data[index_s: index_e]
                # print(get)
                self.count += 1
            else:
                break


class mainWin(QWidget):
    mes = [[[0xaa, 0x08, 0x01], [0xaa, 0x08, 0x02]],    # 0连接方式：0-usb串口，1-wifi
               [[0xaa, 0x03, 0x01, 0x96], [0xaa, 0x03, 0x01, 0x95], [0xaa, 0x03, 0x01, 0x94], [0xaa, 0x03, 0x01, 0x93], [0xaa, 0x03, 0x01, 0x92], [0xaa, 0x03, 0x01, 0x91], [0xaa, 0x03, 0x01, 0x90]],  # 1采样率：0-250，1-500，2-1k，3-2k，4-4k，5-8k，6-16k
               [[0xaa, 0x07, 0x20], [0xaa, 0x07, 0x02]],    # 2通道数：0-32，1-2
               [[0xaa, 0x06, 0x00], [0xaa, 0x06, 0x01]]]    # 3启停：0-停止，1-启动
    message = {'usb':[0xaa, 0x08, 0x01], 'wifi':[0xaa, 0x08, 0x02],
           250:[0xaa, 0x03, 0x01, 0x96], 500:[0xaa, 0x03, 0x01, 0x95], 1000:[0xaa, 0x03, 0x01, 0x94], 2000:[0xaa, 0x03, 0x01, 0x93], 4000:[0xaa, 0x03, 0x01, 0x92], 8000:[0xaa, 0x03, 0x01, 0x91], 16000:[0xaa, 0x03, 0x01, 0x90],
           32:[0xaa, 0x07, 0x20], 2:[0xaa, 0x07, 0x02],
           'stop':[0xaa, 0x06, 0x00], 'start':[0xaa, 0x06, 0x01]}
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False

    def initUI(self):
        self.resize(400, 300)
        self.setWindowTitle('test')
        layout = QVBoxLayout()
        self.btn_start = QPushButton('start', self)
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.btn_stop = QPushButton('stop', self)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)
        self.text = QTextEdit(self)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.text)
        layout.addWidget(self.btn_stop)
        self.btn_send_start = QPushButton('send start', self)
        self.btn_send_start.clicked.connect(self.btn_send_start_clicked)
        self.btn_send_stop = QPushButton('send stop', self)
        self.btn_send_stop.clicked.connect(self.btn_send_stop_clicked)
        self.sendFrame = QFrame(self)
        self.sendLayout  = QGridLayout()

        self.et_send = QLineEdit(self)
        self.btn_send = QPushButton('send', self)
        self.btn_send.clicked.connect(self.btn_send_clicked)
        layout.addWidget(self.btn_send_start)
        layout.addWidget(self.btn_send_stop)
        self.sendLayout.addWidget(self.et_send, 1, 0, 1, 2)
        self.sendLayout.addWidget(self.btn_send, 2, 0, 1, 2)
        self.sendFrame.setLayout(self.sendLayout)
        layout.addWidget(self.sendFrame)
        self.setLayout(layout)
        self.mythread = myThread()
        self.mythread.sig.connect(self.textAppend)
        self.mythread.start()
    
    def sendMessage(self, state, connect='usb', sample_rate=1000, channel=32):
        self.mythread.ser.flushInput()
        self.mythread.ser.flushOutput()
        if state == 'start':
            self.mythread.ser.write(self.message[connect])
            sleep(0.05)
            self.mythread.ser.write(self.message[sample_rate])
            sleep(0.05)
            self.mythread.ser.write(self.message[channel])
            sleep(0.05)
            self.mythread.ser.write(self.message['start'])
            sleep(0.05)
        elif state == 'stop':
            for i in range(3):
                self.mythread.ser.write(self.message['stop'])
                sleep(0.05)

    def startMessage(self, rate, channel):
        self.mythread.ser.flushInput()
        self.mythread.ser.flushOutput()
        self.mythread.ser.write(self.message[0][0])
        sleep(0.1)
        self.mythread.ser.write(self.message[1][rate])
        sleep(0.1)
        self.mythread.ser.write(self.message[2][channel])
        sleep(0.1)
        self.mythread.ser.write(self.message[3][1])
        sleep(0.1)
    
    def stopMessage(self):
        self.mythread.ser.flushInput()
        self.mythread.ser.flushOutput()
        for i in range(3):
            self.mythread.ser.write(self.message[3][0])
            sleep(0.05)

    def btn_send_clicked(self):
        massage = self.et_send.text()
        # send = bytearray()
        send = []
        for mas in massage.split(' '):
            send.append(int(mas, 16))
        print(send)
        self.mythread.ser.flushInput()
        self.mythread.ser.flushOutput()
        self.mythread.ser.write(send)


    def btn_send_start_clicked(self):
        self.mythread.ser.flushInput()
        self.mythread.ser.flushOutput()
        self.sendMessage('start', 'usb', 8000, 2)
        print("write 0x AA 06 01")
        print("start")
    
    def btn_send_stop_clicked(self):
        self.mythread.ser.flushInput()
        self.mythread.ser.flushOutput()
        self.sendMessage('stop')
        print("write 0x AA 06 00")
        print("stop")

    def btn_start_clicked(self):
        self.flag = True
        self.mythread.go()

    def btn_stop_clicked(self):
        self.flag = False
        self.mythread.stop()

    def textAppend(self, data):
        if self.flag:
            self.text.append(str(data))
            self.text.append("-----------------")
            ...
    
    def closeEvent(self, event):
        self.mythread.ser.close()
        self.mythread.quit()
        print("close")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = mainWin()
    test = []
    test.append(1)
    test.append([1, 2, 3])
    win.show()
    sys.exit(app.exec_())

    # ser = serial.Serial(port='COM3', baudrate=4608000)
    # i = 0
    # time1 = time.time()
    # while(i<10000):
    #     data = ser.readline(ser.in_waiting)
    #     print(data)
    #     i += 1
    #     print("count:\t", i)
    
    # print(time.time() - time1)
    # ser.close()



# # while False:
# while True:
#     data = ser.readline().hex() # 读取数据
#     print(data)
#     print('-----------------')
#     all += data
