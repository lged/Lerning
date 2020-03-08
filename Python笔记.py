#Python2 控制台文字颜色
from colored import fg, bg, attr
print '%s%s Hello World !!! %s' % (fg(1), bg(7), attr(0))
print '%s This is Res %s' % (fg('red'), attr('reset'))
print '{} This is Yellow bg {}'.format(fg('green'), attr('reset'))
raw_input()
