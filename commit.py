'''
Created on 2016年12月16日

@author: gzq
'''
import os
import time
import getopt
import sys
import pexpect

SSH_NEWKEY = r'Are you sure you want to continue connecting \(yes/no\)\?'


def auto_run(cmd, passwd='tdq$abc123'):
    os.system(cmd)
    return
    child = pexpect.spawn(cmd)
    child.logfile_read = sys.stdout.buffer
    i = child.expect([pexpect.TIMEOUT, SSH_NEWKEY, '[Pp]assword: '])
    if i == 0:  # Timeout
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        sys.exit(1)
    if i == 1:  # SSH does not have the public key. Just accept it.
        child.sendline('yes')
        child.expect('[Pp]assword: ')
    child.sendline(passwd)
    child.expect(pexpect.EOF)


def git_pull():
    auto_run('git fetch origin master')
    os.system('git merge origin/master')


def git_commit():
    os.system('git add *')
    os.system('git commit -m \'%s\'' % time.strftime('%Y-%m-%d-%X',
                                                     time.localtime()))
    auto_run('git push origin master')
    print('COMMIT COMPLETE !!!')


if __name__ == '__main__':
    commit = 1
    force = False
    scp = None
    # 获取输入参数 -c commit
    opts, args = getopt.getopt(sys.argv[1:], "hpfs:", ['help', 'pull', 'force', 'scp='])
    for op, value in opts:
        if op in ("-p", "--pull"):
            commit = 0
        elif op in ("-f", "--force"):
            commit = 0
            force = True
        elif op in ("-s", "--scp"):
            scp = value
        elif op in ("-h", "--help"):
            print('-h     : print this help message and exit (also --help)')
            print('-p     : git pull  (also --pull)')
            print('-f     : git pull force  (also --force)')
            print('-s     : scp  (also --scp)')
            sys.exit()
    if scp:
        # command = 'scp yunshu.py yunshu2.py yunzhi.py yuntu.py auto.py base.py yunzhi_test.py yuntu_test.py yunshu_test.py gzq@172.16.10.11:/home/tdqs/code4f/pmg-%s/code' % scp
        # print(command)
        # auto_run(command, 'tdq$abc456')
        if scp == '1.0.5':
            cmd = 'cp yunshu.py yunshu2.py yunzhi.py yuntu.py auto.py base.py yunzhi_test.py yuntu_test.py yunshu_test.py myredis.py ../qs_yun/pmg-1.0.5/'
        else:
            cmd = 'cp 1.0.3/yunshu.py 1.0.3/yunzhi.py 1.0.3/yuntu.py 1.0.3/auto.py 1.0.3/base.py ../qs_yun/pmg-1.0.4/'
        os.chdir('../qs_yun')
        git_pull()
        os.chdir('../gzq')
        os.system(cmd)
        os.chdir('../qs_yun')
        git_commit()
    elif commit:
        git_commit()
    else:
        if force:
            os.system('git fetch --all')
            os.system('git reset --hard origin/master')
            os.system('git pull')
        else:
            auto_run('git fetch origin master')
            os.system('git merge origin/master')
        print('UPDATE COMPLETE !!!')
