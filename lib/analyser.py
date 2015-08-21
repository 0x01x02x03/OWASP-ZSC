#!/usr/bin/env python
'''
OWASP ZSC | ZCR Shellcoder

ZeroDay Cyber Research
Z3r0D4y.Com
Ali Razmjoo
'''
import encode
import sys
import os
from core import color
from core import done
from core import start
def chmod_spliter(cont):
	cont = cont.replace('chmod(\'','')
	cont = cont.replace('\',\'','\x90\x90\x90')
	cont = cont.replace('\')','')
	cont = cont.rsplit('\x90\x90\x90')
	return cont[0] + '\x90\x90\x90' + cont[1]
def dir_creator(cont):
	cont = cont.replace('dir_create(\'','')
	cont = cont.replace('\',\'','')
	cont = cont.replace('\')','')
	return cont
def download_spliter(cont):
	cont = cont.replace('download(\'','')
	cont = cont.replace('\',\'','\x90\x90\x90')
	cont = cont.replace('\')','')
	cont = cont.rsplit('\x90\x90\x90')
	return cont[0] + '\x90\x90\x90' + cont[1]
def download_exec_spliter(cont):
	cont = cont.replace('download_execute(\'','')
	cont = cont.replace('\',\'','\x90\x90\x90')
	cont = cont.replace('\')','')
	cont = cont.rsplit('\x90\x90\x90')
	return cont[0] + '\x90\x90\x90' + cont[1]+ '\x90\x90\x90' + cont[2]
def executor(cont):
	cont = cont.replace('exec(\'','')
	cont = cont.replace('\',\'','')
	cont = cont.replace('\')','')
	return cont
def file_creator(cont):
	cont = cont.replace('file_create(\'','')
	cont = cont.replace('\',\'','\x90\x90\x90')
	cont = cont.replace('\')','')
	cont = cont.rsplit('\x90\x90\x90')
	return cont[0] + '\x90\x90\x90' + cont[1]
def script_exec(cont):
	cont = cont.replace('script_executor(\'','')
	cont = cont.replace('\',\'','\x90\x90\x90')
	cont = cont.replace('\')','')
	cont = cont.rsplit('\x90\x90\x90')
	return cont[0] + '\x90\x90\x90' + cont[1]+ '\x90\x90\x90' + cont[2]
def syst(cont):
	cont = cont.replace('system(\'','')
	cont = cont.replace('\',\'','')
	cont = cont.replace('\')','')
	return cont
def file_writer(cont):
	cont = cont.replace('write(\'','')
	cont = cont.replace('\',\'','\x90\x90\x90')
	cont = cont.replace('\')','')
	cont = cont.rsplit('\x90\x90\x90')
	return cont[0] + '\x90\x90\x90' + cont[1]
def do(cont):
	content = cont.rsplit('\x90\x90\x90')
	os_name,filename,encode_type,job = content[0],content[1],content[2],content[3]
	shellcode = None
	if 'freebsd_x64' in os_name:
		if 'chmod(' in job:
			from generator.freebsd_x64 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.freebsd_x64 import dir_create
			shellcode = dir_create.run(dir_creator(job))
		if 'download(' in job:
			from generator.freebsd_x64 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.freebsd_x64 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.freebsd_x64 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.freebsd_x64 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.freebsd_x64 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.freebsd_x64 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.freebsd_x64 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'freebsd_x86' in os_name:
		if 'chmod(' in job:
			from generator.freebsd_x86 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.freebsd_x86 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.freebsd_x86 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.freebsd_x86 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.freebsd_x86 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.freebsd_x86 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.freebsd_x86 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.freebsd_x86 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.freebsd_x86 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'linux_arm' in os_name: 
		if 'chmod(' in job:
			from generator.linux_arm import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.linux_arm import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.linux_arm import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.linux_arm import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.linux_arm import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.linux_arm import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.linux_arm import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.linux_arm import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.linux_arm import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'linux_mips' in os_name:
		if 'chmod(' in job:
			from generator.linux_mips import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.linux_mips import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.linux_mips import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.linux_mips import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.linux_mips import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.linux_mips import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.linux_mips import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.linux_mips import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.linux_mips import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'linux_x64' in os_name:
		if 'chmod(' in job:
			from generator.linux_x64 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.linux_x64 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.linux_x64 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.linux_x64 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.linux_x64 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.linux_x64 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.linux_x64 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.linux_x64 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.linux_x64 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'linux_x86' in os_name:
		if 'chmod(' in job:
			from generator.linux_x86 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.linux_x86 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.linux_x86 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.linux_x86 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.linux_x86 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.linux_x86 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.linux_x86 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.linux_x86 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.linux_x86 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'osx' in os_name:
		if 'chmod(' in job:
			from generator.osx import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.osx import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.osx import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.osx import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.osx import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.osx import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.osx import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.osx import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.osx import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'solaris_x64' in os_name:
		if 'chmod(' in job:
			from generator.solaris_x64 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.solaris_x64 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.solaris_x64 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.solaris_x64 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.solaris_x64 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.solaris_x64 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.solaris_x64 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.solaris_x64 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.solaris_x64 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'solaris_x86' in os_name:
		if 'chmod(' in job:
			from generator.solaris_x86 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.solaris_x86 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.solaris_x86 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.solaris_x86 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.solaris_x86 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.solaris_x86 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.solaris_x86 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.solaris_x86 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.solaris_x86 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'windows_x64' in os_name:
		if 'chmod(' in job:
			from generator.windows_x64 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.windows_x64 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.windows_x64 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.windows_x64 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.windows_x64 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.windows_x64 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.windows_x64 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.windows_x64 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.windows_x64 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if 'windows_x86' in os_name:
		if 'chmod(' in job:
			from generator.windows_x86 import chmod
			values = chmod_spliter(job).rsplit('\x90\x90\x90')
			shellcode = chmod.run(values[0],values[1])
		if 'dir_create(' in job:
			from generator.windows_x86 import dir_create
			value = dir_creator(job)
			shellcode = dir_create.run(value)
		if 'download(' in job:
			from generator.windows_x86 import download
			values = download_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download.run(values[0],values[1])
		if 'download_execute(' in job:
			from generator.windows_x86 import download_execute
			values = download_exec_spliter(job).rsplit('\x90\x90\x90')
			shellcode = download_execute.run(values[0],values[1],values[2])
		if 'exec(' in job:
			from generator.windows_x86 import exc
			shellcode = exc.run(executor(job))
		if 'file_create(' in job:
			from generator.windows_x86 import file_create
			values = file_creator(job).rsplit('\x90\x90\x90')
			shellcode = file_create.run(values[0],values[1])
		if 'script_executor(' in job:
			from generator.windows_x86 import script_executor
			values = script_exec(job).rsplit('\x90\x90\x90')
			shellcode = script_executor.run(values[0],values[1],values[2])
		if 'system(' in job:
			from generator.windows_x86 import system
			shellcode = system.run(syst(job))
		if 'write(' in job: 
			from generator.windows_x86 import write
			values = file_writer(job).rsplit('\x90\x90\x90')
			shellcode = write.run(values[0],values[1])
	if shellcode == 'N':
		done.disable(os_name,job)
		return 0
	old_encode_type = ''
	if shellcode is not None:
		shellcode = encode.process(encode_type,shellcode,os_name,job).replace('\n\n','\n').replace('\n\n','\n')
		NE = False
		if shellcode[0] == 'N':
			shellcode = shellcode[1:]
			NE = True
			old_encode_type = encode_type
			encode_type = 'none'
	tmpname = '.tmp.'+filename
	save = open(tmpname,'w')
	save.write(shellcode)
	save.close()
	tmp = os.popen('as %s -o %s.o > .tmp2.%s'%(tmpname,tmpname,tmpname)).read()
	comment = os.popen('objdump -D %s.o'%(tmpname)).read()
	comment = comment.replace('.tmp.'+filename+'.o',filename).replace('\n\n','\n')
	res = os.popen('''objdump -D %s.o |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g' '''%(tmpname)).read()
	res = res.replace('x','\\x').rsplit()[0]
	null = os.system('rm -rf %s %s.o .tmp2.%s'%(tmpname,tmpname,tmpname))
	PASS = True
	if str(len(res)/4) == '0':
		PASS = False
	shellcode = done.c_style(job,os_name,encode_type,str(len(res)/4),comment,str(filename.rsplit('.')[0])+'_compiled',str(filename),res)
	os.system('clear')
	done.res(PASS,shellcode,filename,os_name,job,encode_type,str(len(res)/4),old_encode_type,NE)
