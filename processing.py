import time
def main(): #添加进度条
    scale = 50
    print("执行开始".center(25,'-'))
    start = time.perf_counter()
    for i in range(scale+1):
        a = '*'* i
        b = '.' * (scale - i)
        c = (i/scale)*100
        t = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,t),end = "")
        time.sleep(0.05)
    print("\n"+"执行结束".center(scale//2,'-'))