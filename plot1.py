# -*- coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # CSVのロード
    data = np.genfromtxt('tests2.csv',delimiter=',', dtype='float')
       
    #z行のXを含む列
    r = np.where(data[:,3] == 0)
    
    print(r)
    
    #ｒ列を取出し
    data[np.array(r)]
    #data[r]
    
    print(data)
    

     # 2次元配列を分割（経過時間t, x座標, y座標の1次元配列)
    x = data[:,1]
    y = data[:,2]
    z = data[:,3]
    
    
    # グラフにプロット
    plt.rcParams["font.family"] = "Times New Roman" # フォントの種類
    #plt.scatter(x, y)
    plt.plot(x, y, color='red')
    plt.show()
    plt.savefig("plot.svg", format="svg",dpi=1200)


if __name__ == "__main__":
    main()