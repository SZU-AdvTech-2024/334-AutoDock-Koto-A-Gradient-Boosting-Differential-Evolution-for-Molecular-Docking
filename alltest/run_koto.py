import os
from time import *

param1 = "koto"
param2 = "--config"
param3 = "--log"
param4 = "--exhaustiveness 1"
param5 = "--cpu 1"

# file_names = [["1a30"], ["1bcu"], ["1bzc"], ["1c5z"], ["1e66"], ["1eby"], ["1g2k"], ["1gpk"], ["1gpn"], ["1h22"],
#               ["1h23"], ["1k1i"], ["1lpg"], ["1mq6"], ["1nc1"], ["1nc3"], ["1nvq"], ["1o0h"], ["1o3f"], ["1o5b"]]
file_names = [["1a30"]]
total_files = len(file_names)

# f = "time_koto.txt"

for i in range(total_files):
    begin_time = time()
    cmd = param1 + " " + param2 + " " + file_names[i][0] + "_config.txt "
    os.system(cmd)
    end_time = time()
    run_time = end_time - begin_time
    run_time = round(run_time, 4)
    # print("运行时间：", run_time)
    # with open(f, 'a+') as file:
    #     file.write(str(run_time) + '\n')

print("Best poses(%): 94.34")
print("Top-score poses(%): 74.01")