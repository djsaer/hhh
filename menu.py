import digital_display
import Big
import turtle
import text_exam
import Hash_Function
import processing

Manu_Number = 7

def menu():
    print("------------MENU------------")
    option = eval(input("1.数码显示\n2.哈希函数\n3.绘制‘大’字\n4.进度条\n5.字符检测\n6.检查语法错误\n7.运行爬虫程序\n8.退出\n请选择:"))
    if option <= Manu_Number and option!=0:
        try:
            nextmenu(option)
        except Exception as erro:
            print(erro)
    elif option == 8:
        return 0
    else:
        raise Exception('请选择菜单内数字！')


def nextmenu(op):
    if op == 1:
        idx = eval(input('\n------------MENU1------------\n1.显示自定义数字\n2.显示自定义时间\n3.显示当前时间\n4.返回上级菜单\n请选择:'))
        if idx <=3 and idx!=0:
            digital_display.main(idx)
            turtle.Turtle._screen = None
            turtle.TurtleScreen._RUNNING = True
            nextmenu(op)
        elif idx ==4:
            menu()
        else:
            raise Exception('请选择菜单内数字')
    elif op == 2:
        idx = eval(input('\n------------MENU2------------\n1.运行哈希函数\n2.返回上级菜单\n请选择:'))
        if idx <=1 and idx !=0:
            Hash_Function.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字')
    elif op == 3:
        idx = eval(input('\n------------MENU3------------\n1.选择大字的颜色与大小\n2.返回上级菜单\n请选择:'))
        if idx == 1:
            Big.main()
            turtle.Turtle._screen = None
            turtle.TurtleScreen._RUNNING = True
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字')
    elif op == 4:
        idx = eval(input('\n------------MENU4------------\n1.展示进度条\n2.返回主菜单\n请选择:'))
        if idx == 1:
            processing.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字')
    elif op == 5:
        idx = eval(input('\n------------MENU5------------\n1.开始文件字符检测\n2.返回主菜单\n请选择：'))
        if idx == 1:
            text_exam.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字')
    elif op == 6:
        idx = eval(input('\n------------MENU6------------\n1.开始检查文件语法错误\n2.返回主菜单\n请选择：'))
        if idx == 1:
            grammer_checker.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字')
    elif op == 7:
        idx = eval(input('\n------------MENU7------------\n1.开始运行爬虫程序\n2.返回主菜单\n请选择：'))
        if idx == 1:
            pc.main()
            nextmenu(op)
        elif idx == 2:
            menu()
        else:
            raise Exception('请选择菜单内数字')


try:
    menu()
except Exception as err:
    print(err)
