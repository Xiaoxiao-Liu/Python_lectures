# 第一题
#创建一个舍友列表roomates，存放你的所有舍友

#从roomates列表中随机输出一个舍友名字，变量名为roomate，\
# 用randint()函数得到随机数，范围是0-len(roomates)，\
# 用这个数字做下标，获得随机舍友名字

#第二题
#根据表格中的提示，完成访客周报模板设计,以下方法任选其一。
##方法一
variables = []




print('您的人气指数比上周提升%d人次，\
获得%s称号！您的人气排名%s，\
您的空间人气打败了%f%%的好友，要继续保持哦！%d月%d日%s，\
%s马不停蹄最早来看您！%s是本周访问您最多次的朋友！' % (variables[0],variables[1],
                                variables[2],variables[3],variables[4],variables[5],
                                variables[6],variables[7],variables[8]))

##方法二
variables = {}


print('您的人气指数比上周提升%d人次，\
获得%s称号！您的人气排名%s，\
您的空间人气打败了%f%%的好友，要继续保持哦！%d月%d日%s，\
%s马不停蹄最早来看您！%s是本周访问您最多次的朋友！' % (variables['人气提升指数'],variables['人气标签'],
                                variables['人气提升情况'],variables['人气提升比例'],variables['月份'],
                                variables['日期'],variables['时间'],variables['好友1'],variables['好友2']))

#方法三

