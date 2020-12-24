# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/Entry_Record_System-PU/ERS.py'],
             pathex=['D:\\Entry_Record_System-PU'],
             binaries=[],
             datas=[('D:/Entry_Record_System-PU/excel_export.py', '.'), ('D:/Entry_Record_System-PU/picture', 'picture/')],
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
          [],
          name='ERS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\Entry_Record_System-PU\\logo.ico')
