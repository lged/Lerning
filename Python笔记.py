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
