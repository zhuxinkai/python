#coding=utf8
#导入模块，其中最重要的是itchat模块
import itchat, time
#调用itchat进行登录，会出现一个二维码，扫描二维码，登录网页微信。
itchat.auto_login(True)
# 将需要的祝福词放在字符串中，%s为占位符，用后面的  displayname ,或者  NICKNAME ,UserName进行替换。
SINCERE_WISH = u'值此新年佳节之际，朱鑫凯携家人祝%s您新年快乐！万事顺意！'
# 利用itchat获取好友信息，并更新好友列表。 将其存入 friendlist数组， 1: 为数组的截取方式，从数组编号1开始截取。
friendList = itchat.get_friends(update=True)[1:]
count = 0
#利用for循环进行数组的遍历。
for friend in friendList:
#itchat.send 发送，不是太理解‘%’在其中的语法内容。
    itchat.send( SINCERE_WISH % (friend['DisplayName']
                                 or friend['NickName']), friend['UserName'])
#隔5秒发送一个好友。
    time.sleep(5)
print("----end----")
