# Python2 控制台文字颜色 pip install colored
from colored import fg, bg, attr
print '%s%s Hello World !!! %s' % (fg(1), bg(7), attr(0))
print '%s This is Res %s' % (fg('red'), attr('reset'))
print '{} This is Yellow bg {}'.format(fg('green'), attr('reset'))
print '%s Hello World !!! %s' % (fg('#C0C0C0') + bg('#00005f'), attr('reset'))

# Python2 控制台颜色2
import colored
print colored.attr('reset'),
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;30mGray like Ghost\033[1;m'
print '\033[1;31mRed like Radish\033[1;m'
print '\033[1;32mGreen like Grass\033[1;m'
print '\033[1;33mYellow like Yolk\033[1;m'
print '\033[1;34mBlue like Blood\033[1;m'
print '\033[1;35mMagenta like Mimosa\033[1;m'
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;37mWhite like Whipped Cream\033[1;m'
print '\033[1;38mCrimson like Chianti\033[1;m'
print '\033[1;41mHighlighted Red like Radish\033[1;m'
print '\033[1;42mHighlighted Green like Grass\033[1;m'
print '\033[1;43mHighlighted Brown like Bear\033[1;m'
print '\033[1;44mHighlighted Blue like Blood\033[1;m'
print '\033[1;45mHighlighted Magenta like Mimosa\033[1;m'
print '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
print '\033[1;47mHighlighted Gray like Ghost\033[1;m'
print '\033[1;48mHighlighted Crimson like Chianti\033[1;m'

# 复制文本
import pyperclip
pyperclip.copy('abc')

# Cython配置
pip install cython
# file: hello.pyx
def say_hello_to(name):
    print("Hello %s!" % name)
# file: setup.py
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize("hello.pyx"))
python setup.py build_ext --inplace # Linux中生成hello.so，Windows中生成hello.pyd
>>> import hello
>>> hello.say_hello_to('Sir')
Windows中要安装VCForPython27，并对msvc9compiler.py与msvccompiler.py更改get_build_version：9.0，find_vcvarsall：r'C:\Users\xxx\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat'
详情见https://www.cnblogs.com/lazyboy/p/4017567.html

# 语法
lst[::n] # list中每隔n取1个，-1即反转
a, b, c = 1, 2, 3

# 经验
re的反向界定只能使用定长文本，不定长的可用regex
安装pycrypto-2.6.win32-py2.7后要将C:\Python27\Lib\site-packages\crypto改为Crypto
sys.path.append(r'D:\code\myproj')，就可以from file import class了
3.6中安装pyqt5：pip3 install pyqt5 -i https://pypi.douban.com/simple

# Pyinstaller
打包 pyinstaller test.py -F -i test.ico
解包 python pyinstxtractor.py test.exe # https://sourceforge.net/projects/pyinstallerextractor/
再用 uncompyle2 或 EasyPythonDecompiler 解 pyc
保护 将引用的 py 编译为 pyd

# 操作
Notepad++缩进：设置 > 首选项 > 语言 > Python > Python > 替换为空格 # 不要出现tab
Pycharm 代码折叠 Ctrl+Alt+T，Ctrl+Alt+L 自动排版，错误定位 F2

# Windows中虚拟环境
pip install virtualenv
pip install virtualenvwrapper
venv\scripts\activate deactivate

# 已有2.7后安装3.6
将 3.6 的 python.exe 改为 python3.exe，删除其 scripts/pip.exe，之后分别执行的是 python3 与 pip3
创建对应虚拟环境 virtualenv -p python3 36
Pycharm: File > Settings > Project xxx > Project Interpreter > 选择对应版本
打包exe：pip3 install pyinstaller -i https://pypi.douban.com/simple, python3 -m PyInstaller qt.py -F -w -i app.ico # 注意大小写PyInstaller
