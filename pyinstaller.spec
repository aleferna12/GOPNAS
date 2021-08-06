# -*- mode: python ; coding: utf-8 -*-
# Esse script serve para criar o executável com o seguinte comando: "py -m PyInstaller pyinstaller.spec"
# Não faça isso se não souber o que está fazendo!
import PyInstaller.config
PyInstaller.config.CONF['distpath'] = "."
from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          [],
          name='GOPNAS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='./Resources/app_icon.ico'
          )
