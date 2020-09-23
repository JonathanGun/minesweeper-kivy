pyi-makespec --name minesweeper --icon=resource/icon.ico --add-data resource/*;. --onefile --noconsole main.py
python editspec.py -f=minesweeper.spec
pyinstaller --clean --noconfirm minesweeper.spec
pause