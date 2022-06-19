import os
FindPath = r"E:\untitled\venv"

def main():
    flag = 0
    try:
        fileName = input("输入想检测的文件名字(xxx.py):\n")
        if fileName.find(".py",0,len(fileName))==-1:
            raise Exception("输入格式错误!")
        FileNames = os.listdir(FindPath)
        for file in FileNames:
            name = os.path.join(FindPath,file)
            if (name.find(fileName,0,len(name))!=-1):
                flag = 1
        if flag == 0:
            raise Exception("未找到文件!")
        else:
            catch_error(str_Processing(fileName))
    except Exception as erro:
        print(erro)

def str_Processing(fileName):
    f = open(r'E:\untitled\venv\%s'%fileName, encoding='utf-8')
    data = f.readlines()
    return data

def catch_error(strdata):
    erross =0
    for eachline in strdata:
        left=right=0
        colon=0
        keywords=0
        temp=str(eachline).lower()
        for i in r"~!@#$%^&*()_+-[]{},.\?=:;'/":
            data = temp.replace(i, " ")
        data = data.split()
        for word in data:
            if word in ["try","def","if","elif","else","except","for","while"]:
                keywords=keywords+1
        for eachword in eachline:
            if eachword == "(":
                left=left+1
            if eachword == ")":
                right=right+1
            if eachword == ":" and keywords!=0:
                colon+=1
        if left != right:
            if left >= right:
                print("%s----->此处缺少右括号"%eachline)
            elif right >= left:
                print("%s----->此处缺少左括号"%eachline)
            erross=erross+1
        elif colon != keywords:
            print("%s----->此处缺少冒号"%eachline)
            erross=erross+1
    if erross != 0:
        print("检查完毕，发现%s个错误"%erross)
    else:
        print("检查完毕，未发现错误")




if __name__ == "__main__":
    main()