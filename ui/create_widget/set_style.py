
"""UI 스타일 설정 모듈입니다.
테마별 색상, 폰트, 스타일시트를 정의합니다."""

from PyQt5.QtGui import QFont, QColor
from utility.settings.setting_user import load_settings

dict_set, _ = load_settings()
if dict_set.__class__ != dict:
    dict_set = {'테마': '다크레드'}

qfont12 = QFont()
qfont12.setFamily('나눔고딕')
qfont12.setPixelSize(12)

qfont13 = QFont()
qfont13.setFamily('나눔고딕')
qfont13.setPixelSize(13)

qfont14 = QFont()
qfont14.setFamily('나눔고딕')
qfont14.setPixelSize(14)

# 테마용 공통 색상
color_cs_hr = QColor(255, 255, 255)
color_ct_hg = QColor(255, 255, 0)
color_fg_rt = QColor(160, 255, 160)
color_bt_yl = QColor(255, 255, 160)

color_pluss = QColor(200, 50, 50)
color_minus = QColor(50, 50, 200)

style_bc_by = '''
    QPushButton{background-color: rgb(150, 100, 100);border-style: solid;border-width: 1px;border-color: rgb(150, 100, 100);}
    QPushButton:hover{background-color: rgb(170, 120, 120);}'''
style_bc_sl = '''
    QPushButton{background-color: rgb(100, 100, 150);border-style: solid;border-width: 1px;border-color: rgb(100, 100, 150);}
    QPushButton:hover{background-color: rgb(120, 120, 170);}'''
style_bc_bs = '''
    QPushButton{background-color: rgb(80, 130, 80);border-style: solid;border-width: 1px;border-color: rgb(80, 130, 80);}
    QPushButton:hover{background-color: rgb(100, 150, 100);}'''
style_bc_bd = '''
    QPushButton{background-color: rgb(30, 80, 30);border-style: solid;border-width: 1px;border-color: rgb(30, 80, 30);}
    QPushButton:hover{background-color: rgb(50, 100, 50);}'''
style_ck_bx = ''''
    QCheckBox::indicator {width: 15px; height: 15px;}
    QCheckBox::indicator::unchecked {image: url(ui/_icon/unchecked.png);}
    QCheckBox::indicator::checked {image: url(ui/_icon/checked.png);}'''

style_st_ss = '''
    QPushButton{background-color: rgb(60, 60, 80);border-style: solid;border-width: 1px;border-color: rgb(60, 60, 80);}
    QPushButton:hover{background-color: rgb(80, 80, 100);}'''
style_st_su = '''
    QPushButton{background-color: rgb(70, 70, 90);border-style: solid;border-width: 1px;border-color: rgb(70, 70, 90);}
    QPushButton:hover{background-color: rgb(90, 90, 110);}'''
style_st_cf = '''
    QPushButton{background-color: rgb(90, 90, 100);border-style: solid;border-width: 1px;border-color: rgb(90, 90, 100);}
    QPushButton:hover{background-color: rgb(110, 110, 120);}'''
style_st_sf = '''
    QPushButton{background-color: rgb(70, 70, 80);border-style: solid;border-width: 1px;border-color: rgb(70, 70, 80);}
    QPushButton:hover{background-color: rgb(90, 90, 100);}'''
style_st_mf = '''
    QPushButton{background-color: rgb(50, 50, 60);border-style: solid;border-width: 1px;border-color: rgb(50, 50, 60);}
    QPushButton:hover{background-color: rgb(70, 70, 80);}'''
style_st_sp = '''
    QPushButton{background-color: rgb(80, 100, 80);border-style: solid;border-width: 1px;border-color: rgb(80, 100, 80);}
    QPushButton:hover{background-color: rgb(100, 120, 100);}'''
style_st_ct = '''
    QPushButton{background-color: rgb(80, 80, 100);border-style: solid;border-width: 1px;border-color: rgb(80, 80, 100);}
    QPushButton:hover{background-color: rgb(100, 100, 120);}'''
style_st_ks = '''
    QPushButton{background-color: rgb(100, 100, 80);border-style: solid;border-width: 1px;border-color: rgb(100, 100, 80);}
    QPushButton:hover{background-color: rgb(120, 120, 100);}'''

if dict_set['테마'] == '다크블루':
    color_fg_bt = QColor(230, 230, 240)
    color_fg_bc = QColor(190, 190, 200)
    color_fg_hl = QColor(175, 175, 185)
    color_fg_dk = QColor(150, 150, 160)
    color_bf_bt = QColor(110, 110, 120)
    color_bf_bb = QColor(90, 90, 100)
    color_bf_dk = QColor(70, 70, 80)
    color_bg_bl = QColor(60, 60, 70)
    color_hv_bt = QColor(53, 53, 63)
    color_bg_bt = QColor(50, 50, 60)
    color_bg_ld = (50, 50, 60, 150)
    color_bg_bc = QColor(40, 40, 50)
    color_bg_dk = QColor(30, 30, 40)
    color_bg_ct = QColor(25, 25, 40)
    color_bg_bk = QColor(20, 20, 30)
elif dict_set['테마'] == '다크브라운':
    color_fg_bt = QColor(240, 230, 230)
    color_fg_bc = QColor(200, 190, 190)
    color_fg_hl = QColor(185, 175, 175)
    color_fg_dk = QColor(160, 150, 150)
    color_bf_bt = QColor(120, 110, 110)
    color_bf_bb = QColor(100, 90, 90)
    color_bf_dk = QColor(80, 70, 70)
    color_bg_bl = QColor(70, 60, 60)
    color_hv_bt = QColor(63, 53, 53)
    color_bg_bt = QColor(60, 50, 50)
    color_bg_ld = (60, 50, 50, 150)
    color_bg_bc = QColor(50, 40, 40)
    color_bg_dk = QColor(40, 30, 30)
    color_bg_ct = QColor(40, 25, 25)
    color_bg_bk = QColor(30, 20, 20)
elif dict_set['테마'] == '다크그린':
    color_fg_bt = QColor(230, 240, 230)
    color_fg_hl = QColor(175, 185, 175)
    color_fg_bc = QColor(190, 200, 190)
    color_fg_dk = QColor(150, 160, 150)
    color_bf_bt = QColor(110, 120, 110)
    color_bf_bb = QColor(90, 100, 90)
    color_bf_dk = QColor(70, 80, 70)
    color_bg_bl = QColor(60, 70, 60)
    color_hv_bt = QColor(53, 63, 53)
    color_bg_bt = QColor(50, 60, 50)
    color_bg_ld = (50, 60, 50, 150)
    color_bg_bc = QColor(40, 50, 40)
    color_bg_dk = QColor(30, 40, 30)
    color_bg_ct = QColor(25, 40, 25)
    color_bg_bk = QColor(20, 30, 20)
elif dict_set['테마'] == '다크옐로':
    color_fg_bt = QColor(240, 240, 230)
    color_fg_bc = QColor(200, 200, 190)
    color_fg_hl = QColor(185, 185, 175)
    color_fg_dk = QColor(160, 160, 150)
    color_bf_bt = QColor(120, 120, 110)
    color_bf_bb = QColor(100, 100, 90)
    color_bf_dk = QColor(80, 80, 70)
    color_bg_bl = QColor(70, 70, 60)
    color_hv_bt = QColor(63, 63, 53)
    color_bg_bt = QColor(60, 60, 50)
    color_bg_ld = (60, 60, 50, 150)
    color_bg_bc = QColor(50, 50, 40)
    color_bg_dk = QColor(40, 40, 30)
    color_bg_ct = QColor(40, 40, 25)
    color_bg_bk = QColor(30, 30, 20)
elif dict_set['테마'] == '다크라임':
    color_fg_bt = QColor(230, 240, 240)
    color_fg_bc = QColor(190, 200, 200)
    color_fg_hl = QColor(175, 185, 185)
    color_fg_dk = QColor(150, 160, 160)
    color_bf_bt = QColor(110, 120, 120)
    color_bf_bb = QColor(110, 120, 120)
    color_bf_dk = QColor(70, 80, 80)
    color_bg_bl = QColor(60, 70, 70)
    color_hv_bt = QColor(53, 63, 63)
    color_bg_bt = QColor(50, 60, 60)
    color_bg_ld = (50, 60, 60, 150)
    color_bg_bc = QColor(40, 50, 50)
    color_bg_dk = QColor(30, 40, 40)
    color_bg_ct = QColor(25, 40, 40)
    color_bg_bk = QColor(20, 30, 30)
elif dict_set['테마'] == '다크퍼플':
    color_fg_bt = QColor(240, 230, 240)
    color_fg_bc = QColor(200, 190, 200)
    color_fg_hl = QColor(185, 175, 185)
    color_fg_dk = QColor(160, 150, 160)
    color_bf_bt = QColor(120, 110, 120)
    color_bf_bb = QColor(120, 110, 120)
    color_bf_dk = QColor(80, 70, 80)
    color_bg_bl = QColor(70, 60, 60)
    color_hv_bt = QColor(63, 53, 63)
    color_bg_bt = QColor(60, 50, 60)
    color_bg_ld = (60, 50, 60, 150)
    color_bg_bc = QColor(50, 40, 50)
    color_bg_dk = QColor(40, 30, 40)
    color_bg_ct = QColor(40, 25, 40)
    color_bg_bk = QColor(30, 20, 30)
elif dict_set['테마'] == '다크레드':
    color_fg_bt = QColor(250, 220, 220)
    color_fg_bc = QColor(210, 180, 180)
    color_fg_hl = QColor(195, 165, 165)
    color_fg_dk = QColor(170, 140, 140)
    color_bf_bt = QColor(130, 100, 100)
    color_bf_bb = QColor(110, 70, 70)
    color_bf_dk = QColor(90, 60, 60)
    color_bg_bl = QColor(80, 55, 55)
    color_bg_bt = QColor(70, 45, 45)
    color_bg_ld = (70, 45, 45, 150)
    color_bg_bc = QColor(55, 35, 35)
    color_bg_dk = QColor(45, 28, 28)
    color_bg_ct = QColor(40, 22, 22)
    color_bg_bk = QColor(32, 18, 18)
elif dict_set['테마'] == '다크오렌지':
    color_fg_bt = QColor(250, 230, 210)
    color_fg_bc = QColor(210, 190, 170)
    color_fg_hl = QColor(195, 175, 155)
    color_fg_dk = QColor(170, 150, 130)
    color_bf_bt = QColor(130, 110, 90)
    color_bf_bb = QColor(110, 85, 65)
    color_bf_dk = QColor(90, 70, 55)
    color_bg_bl = QColor(80, 55, 50)
    color_hv_bt = QColor(73, 58, 43)
    color_bg_bt = QColor(70, 55, 40)
    color_bg_ld = (70, 55, 40, 150)
    color_bg_bc = QColor(55, 42, 30)
    color_bg_dk = QColor(45, 33, 22)
    color_bg_ct = QColor(40, 28, 18)
    color_bg_bk = QColor(32, 22, 14)
elif dict_set['테마'] == '다크핑크':
    color_fg_bt = QColor(250, 220, 230)
    color_fg_bc = QColor(210, 180, 190)
    color_fg_hl = QColor(195, 165, 175)
    color_fg_dk = QColor(170, 140, 150)
    color_bf_bt = QColor(130, 100, 110)
    color_bf_bb = QColor(110, 80, 90)
    color_bf_dk = QColor(90, 70, 80)
    color_bg_bl = QColor(80, 60, 68)
    color_hv_bt = QColor(73, 53, 61)
    color_bg_bt = QColor(70, 50, 58)
    color_bg_ld = (70, 50, 58, 150)
    color_bg_bc = QColor(55, 40, 47)
    color_bg_dk = QColor(45, 32, 38)
    color_bg_ct = QColor(40, 26, 32)
    color_bg_bk = QColor(32, 22, 27)
elif dict_set['테마'] == '다크그레이':
    color_fg_bt = QColor(230, 230, 230)
    color_fg_hl = QColor(175, 175, 175)
    color_fg_bc = QColor(190, 190, 190)
    color_fg_dk = QColor(150, 150, 150)
    color_bf_bt = QColor(110, 110, 110)
    color_bf_bb = QColor(85, 85, 85)
    color_bf_dk = QColor(70, 70, 70)
    color_bg_bl = QColor(65, 65, 65)
    color_hv_bt = QColor(58, 58, 58)
    color_bg_bt = QColor(55, 55, 55)
    color_bg_ld = (55, 55, 55, 150)
    color_bg_bc = QColor(45, 45, 45)
    color_bg_dk = QColor(35, 35, 35)
    color_bg_ct = QColor(30, 30, 30)
    color_bg_bk = QColor(22, 22, 22)
else:
    color_fg_bt = QColor(220, 230, 250)
    color_fg_bc = QColor(180, 190, 210)
    color_fg_hl = QColor(165, 175, 195)
    color_fg_dk = QColor(140, 150, 170)
    color_bf_bt = QColor(100, 110, 130)
    color_bf_bb = QColor(90, 100, 120)
    color_bf_dk = QColor(60, 70, 85)
    color_bg_bl = QColor(55, 60, 75)
    color_hv_bt = QColor(48, 53, 68)
    color_bg_bt = QColor(45, 50, 65)
    color_bg_ld = (45, 50, 65, 150)
    color_bg_bc = QColor(35, 40, 52)
    color_bg_dk = QColor(28, 32, 42)
    color_bg_ct = QColor(22, 26, 36)
    color_bg_bk = QColor(16, 20, 28)

rgb_fg_bt = f'rgb({color_fg_bt.red()}, {color_fg_bt.green()}, {color_fg_bt.blue()})'
rgb_fg_dk = f'rgb({color_fg_dk.red()}, {color_fg_dk.green()}, {color_fg_dk.blue()})'
rgb_bf_bt = f'rgb({color_bf_bt.red()}, {color_bf_bt.green()}, {color_bf_bt.blue()})'
rgb_bf_bb = f'rgb({color_bf_bb.red()}, {color_bf_bb.green()}, {color_bf_bb.blue()})'
rgb_bf_dk = f'rgb({color_bf_dk.red()}, {color_bf_dk.green()}, {color_bf_dk.blue()})'
rgb_bg_bl = f'rgb({color_bg_bl.red()}, {color_bg_bl.green()}, {color_bg_bl.blue()})'
rgb_bg_bt = f'rgb({color_bg_bt.red()}, {color_bg_bt.green()}, {color_bg_bt.blue()})'
rgb_bg_bc = f'rgb({color_bg_bc.red()}, {color_bg_bc.green()}, {color_bg_bc.blue()})'
rgb_bg_dk = f'rgb({color_bg_dk.red()}, {color_bg_dk.green()}, {color_bg_dk.blue()})'
rgb_bg_ct = f'rgb({color_bg_ct.red()}, {color_bg_ct.green()}, {color_bg_ct.blue()})'

style_fc_bt = f'QLineEdit {{color: {rgb_fg_bt};}}'
style_fc_dk = f'QFrame {{color: {rgb_fg_dk};}}'
style_bc_st = f'''
    QPushButton {{background-color: {rgb_bf_bb};border-style: solid;border-width: 1px;border-color: {rgb_bf_bb};}}
    QPushButton:hover {{background-color: {rgb_bf_bt};}}'''
style_bc_bt = f'''
    QPushButton {{background-color: {rgb_bf_dk};border-style: solid;border-width: 1px;border-color: {rgb_bf_dk};}}
    QPushButton:hover {{background-color: {rgb_bf_bb};}}'''
style_bc_bb = f'''
    QPushButton {{background-color: {rgb_bg_bc};border-style: solid;border-width: 1px;border-color: {rgb_bg_bc};}}
    QPushButton:hover {{background-color: {rgb_bg_bl};}}'''
style_bc_dk = f'''
    QPushButton, QTextEdit, QLineEdit, QCheckBox
    {{background-color: {rgb_bg_dk};border-style: solid;border-width: 1px;border-color: {rgb_bg_dk};}}
    QPushButton:hover {{background-color: {rgb_bg_bt};}}'''
style_pgbar = f'QProgressBar {{background-color: {rgb_bg_dk};}} QProgressBar::chunk {{background-color: {rgb_bf_bb};}}'
style_ht_gb = f'QGroupBox {{background-color: {rgb_bg_ct}; border: 2px solid {rgb_bg_ct};}}'
style_ht_pb = f'QPushButton {{background-color: {rgb_bg_ct}; border: 2px solid {rgb_bg_ct};}}'
