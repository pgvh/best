import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def tasks():

    ####Task1


    """
    #2
    nominal:bluetooth,screen,wifi
    ordinal:gen,cores,speed,sim

    """
    #1
    data = pd.read_csv("mobile_price_1.csv")
    #3
    data["resolution"] = data["px_height"]*data["px_width"]
    #4
    data["DPI_w"]= np.where(data['sc_w'] == 0, np.nan ,data["px_width"]/(data["sc_w"]*0.393701))
    #5
    data["call_ratio"] = data["battery_power"] / data["talk_time"]
    #6
    data["memory"]= data["memory"]/1024
    #7
    desc = data.describe()
    #8
    plt.xlabel("mobile phone prices")
    plt.ylabel("number of mobile phones")
    plt.title("histogram of mobile phone prices:")
    plt.hist(data["price"],rwidth=0.95,color='steelblue', edgecolor='navy')
    #plt.show()



    #####Task2


    corr = data.corr()
    plt.figure(figsize=(16, 16))
    sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, cmap='coolwarm', annot=True,linewidths=1)
    #plt.show()
    ##2
    # battery_power, resolution ,ram,gen .
    #
    ##3
    # yes,
    # bluetooth,cores,speed,sim,screen,wifi also May affect the price.
    #
    #4

    data.plot.scatter(x='battery_power', y='price',color='hotpink' )
    data.plot.scatter(x='ram', y='price',color='hotpink')
    data.plot.scatter(x='gen', y='price',color='hotpink')
    data.plot.scatter(x='resolution', y='price',color='hotpink')

    #plt.show()

    # 5


    table = pd.DataFrame()
    table['resolution'] = pd.qcut(data['resolution'], q=4)
    table['ram'] = pd.qcut(data['ram'], q=4)
    table['price'] = data['price']
    table['gen'] = data['gen']

    table = pd.pivot_table(table, values='price', index=['resolution', 'ram'], columns=['gen'])

    print(table)

    #####task3

    #1
    ordinal_list = ['cores', 'speed', 'sim']
    for i in ordinal_list:
        if i == 'cores':
            ordered_cores = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
            temp = []
            for j in list(data[i]):
                temp.append(ordered_cores.index(j) + 1)
            data['cores_ord'] = temp
        elif i == 'speed':
            ordered_speed = ['low', 'medium', 'high']
            temp = []
            for j in list(data[i]):
                temp.append(ordered_speed.index(j) + 1)
            data['speed_ord'] = temp
        elif i == 'sim':
            ordered_speed = ['Single', 'Dual']
            temp = []
            for j in list(data[i]):
                temp.append(ordered_speed.index(j) + 1)
            data['sim_ord'] = temp

    #print(data.head())

    # 2

    data = pd.concat([data, pd.get_dummies(data['wifi'], prefix='wifi')], axis=1)

    nominal_list = ['bluetooth', 'screen']
    for i in nominal_list:
        if i == 'bluetooth':
            ordered_cores = ['No', 'Yes']
            temp = []
            for j in list(data[i]):
                temp.append(ordered_cores.index(j))
            data['bluetooth_bin'] = temp
        elif i == 'screen':
            ordered_speed = ['LCD', 'Touch']
            temp = []
            for j in list(data[i]):
                temp.append(ordered_speed.index(j))
            data['screen_bin'] = temp

    #print(data.head())

    # 3
    corr = data.corr()
    plt.figure(figsize=(18, 18))
    sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, cmap='coolwarm',linewidths=1)
    #plt.show()

    # 4
    data.to_csv("mobile_prices_converted.csv", index=False)



    #####task4



    #1
    pg = sns.PairGrid(data, vars=['price', 'gen', 'ram', 'resolution'], palette='RdBu_r')
    pg.map_diag(sns.histplot,color=".3")
    pg.map_offdiag(sns.scatterplot , color="m")
    #plt.show()

    #2

    sorted_c = sorted(data.cores.unique())

    c_cat = pd.Categorical(data['cores'], ordered=True, categories=sorted_c)

    plt.figure()
    plt.scatter(data['px_width'], data['px_height'], c=c_cat.codes, s=data['price'] / 10., alpha=0.3,
                cmap='jet')
    plt.xlabel('Pixel width')
    plt.ylabel('Pixel height')
    plt.colorbar()
    #plt.show()



    #3
    plt.close()
    data2 = pd.read_csv("mobile_price_2.csv")
    data["price_ratio"] = data2["price_2"] / data["price"]
    new_corr = data.corr()
    print(new_corr["price_ratio"])
    data.plot.scatter(x="price_ratio", y="camera", title= "Scatter plot - camera and price ratio", color='lime');

    #plt.show()


if __name__ == '__main__':
    tasks()

