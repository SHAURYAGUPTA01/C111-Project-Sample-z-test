import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot( [data] ,["reading time"] ,show_hist = False)
#fig.show()

mean =st.mean(data)
std = st.stdev(data)
print(f"mean and standard deviation of data is : {mean,std}")

def random_mean(number):
    data_set = []
    for i in range(0,number):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = st.mean(data_set)
    return mean

mean_list = []
for i in range(0,100):
    sample_mean = random_mean(30)
    mean_list.append(sample_mean)

mean =st.mean(mean_list)
std = st.stdev(mean_list)
print(f"mean and standard deviation of sample data is : {mean,std}")
fig = ff.create_distplot( [mean_list] ,["reading_time"] ,show_hist = False)
#fig.show()

first_stdstart,first_stdend = mean-std, mean+std
second_stdstart,second_stdend = mean-(std*2), mean+(std*2)
third_stdstart,third_stdend = mean-(std*3), mean+(std*3)

df= pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean_sample1 = st.mean(data)
fig = ff.create_distplot( [data] ,["reading_time"] ,show_hist = False)
fig.add_trace(go.Scatter( x = [mean,mean] , y = [0,0.17] , mode = "lines", name = "mean"))

fig.add_trace(go.Scatter( x = [first_stdend,first_stdend] , y = [0,0.17] , mode = "lines", name = "first std end"))

fig.add_trace(go.Scatter( x = [second_stdend,second_stdend] , y = [0,0.17] , mode = "lines", name = "second std end"))

fig.add_trace(go.Scatter( x = [third_stdend,third_stdend] , y = [0,0.17] , mode = "lines", name = "third std end"))
fig.show()

#zScore = (New Sample Mean - Sampling Distribution Mean) / standard deviation

zscore = (mean_sample1-mean) / std
print(f"zscore of first intervention : {zscore}")