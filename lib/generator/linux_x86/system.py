#!/usr/bin/env python
'''
OWASP ZSC | ZCR Shellcoder
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
https://github.com/Ali-Razmjoo/OWASP-ZSC
http://api.z3r0d4y.com/
https://lists.owasp.org/mailman/listinfo/owasp-zsc-tool-project [ owasp-zsc-tool-project[at]lists[dot]owasp[dot]org ]
'''
from core import stack
from core import template
def run(command):
	command = command.replace('[space]',' ')
	if int(len(command)) < 5:
		command = str(command) + '[space]&&[space]echo[space]1[space]>[space]/dev/null' #bypass a bug in here, fix later
	#bug in line 12 & 13, check later 
	return template.sys(stack.generate(command.replace('[space]',' '),'%ecx','string'))
