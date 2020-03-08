# Python2 控制台文字颜色 pip install colored
from colored import fg, bg, attr
print '%s%s Hello World !!! %s' % (fg(1), bg(7), attr(0))
print '%s This is Res %s' % (fg('red'), attr('reset'))
print '{} This is Yellow bg {}'.format(fg('green'), attr('reset'))
print '%s Hello World !!! %s' % (fg('#C0C0C0') + bg('#00005f'), attr('reset'))

# Python2 原生控制台颜色2
from colored attr
print attr('reset'),
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;31mRed like Radish\033[1;m'
print '\033[1;41mHighlighted Red like Radish\033[1;m'
print '\033[1;42mHighlighted Green like Grass\033[1;m'
