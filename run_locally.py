import os
import platform
assert platform.system() == "Windows", "本脚本仅支持在windows上运行"
os.system("python -m venv venv")
commands = [R".\venv\Scripts\activate.bat",
            "python -m pip install --upgrade pip",
            "pip install -r requirements.txt --upgrade",
            "python main.py",
            ]
os.system(" & ".join(commands))
