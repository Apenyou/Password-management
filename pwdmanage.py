"""
@Author: your name
@Date: 2020-04-19 21:05:47
@LastEditTime: 2020-04-20 15:42:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Password-management\pwdmanage.py
"""
import click
import pwdproduce
import sqlitelib
import base64lib

print('input root password：')
root = input()


# @click.command()
# @click.option('--rootpwd', prompt='Your root password', help='Must remember the password.')


@click.command()
@click.option('--model', prompt='1.seek 2.add 3.del', help='Select operation mode.')
def manage(model):
    """Generate passwords and manage them."""
    if model == '1': manage_seek()
    if model == '2': manage_add()
    if model == '3': manage_del()


@click.command()
@click.option('--appid', prompt='appid', help='The user name of the application.')
@click.option('--software', prompt='software name', help='software name.')
def manage_add(appid, software):
    pwd = base64lib.base64encode(pwdproduce.pwdproduce(root, appid) + root)
    sql = 'INSERT INTO pwdlist (appid, software, pwd) VALUES ("' + appid + '", "' + software + '", "' + pwd + '")'
    sqlitelib.sqlitelib('sqlite3-key.db', sql)
    print('password produce succeed : ' + base64lib.base64decode(pwd)[:13])


@click.command()
@click.option('--software', prompt='software name', help='software name.')
def manage_seek(software):
    # TODO:添加查询密吗root校验
    sql = 'select appid, pwd, id from pwdlist where "' + software + '" like software'
    # print(sql)
    idandpwd = sqlitelib.sqlitelib('sqlite3-key.db', sql)
    print('appid : ' + idandpwd[0][0])
    print('password : ' + base64lib.base64decode(idandpwd[0][1])[:13])
    print('pwdID : ' + str(idandpwd[0][2]))


@click.command()
@click.option('--pwdid', prompt='pwd ID', help='Delete by pwdlistID')
def manage_del(pwdid):
    sql = 'DELETE FROM pwdlist WHERE ID = ' + pwdid + ''
    result = sqlitelib.sqlitelib('sqlite3-key.db', sql)
    print('delete succeed !!')


if __name__ == '__main__':
    while 1:
        manage()
