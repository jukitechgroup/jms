from bokeh.io import curdoc
from bokeh.models.widgets import Panel, Tabs, Div, Button, DataTable, TableColumn
from bokeh.layouts import row, gridplot, widgetbox, layout, gridplot 
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
import pandas as pd
from pandas import DataFrame, read_csv
import json


# --------- Check selected sensors -------------------

with open('/home/jms/JMS/data/sensor_enabled.json', 'r') as f:
    json_data = json.load(f)
    
#------------------------------------------------------------------

# ----------------- Create CSV Paths  --------------------

file1 = r'/home/jms/JMS/data/out1.csv'
file2 = r'/home/jms/JMS/data/out2.csv'
file3 = r'/home/jms/JMS/data/out3.csv'
file4 = r'/home/jms/JMS/data/out4.csv'
file5 = r'/home/jms/JMS/data/out5.csv'
file6 = r'/home/jms/JMS/data/out6.csv'
file7 = r'/home/jms/JMS/data/out7.csv'
file8 = r'/home/jms/JMS/data/out8.csv'
#-------------------------------------------------------------------

# ----------------- Create Pandas datatables ---------------------

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)
data3 = pd.read_csv(file3)
data4 = pd.read_csv(file4)
data5 = pd.read_csv(file5)
data6 = pd.read_csv(file6)
data7 = pd.read_csv(file7)
data8 = pd.read_csv(file8)
#------------------------------------------------------------------

# ----------------- Remove Empty sines and NaNs ---------

data1 = data1.dropna()
data2 = data2.dropna()
data3 = data3.dropna()
data4 = data4.dropna()
data5 = data5.dropna()
data6 = data6.dropna()
data7 = data7.dropna()
data8 = data8.dropna()
#-----------------------------------------------------------------

# --------------------Change dates to datetime objects ---

data1['aika'] = pd.to_datetime(data1['aika'])
data2['aika'] = pd.to_datetime(data2['aika'])
data3['aika'] = pd.to_datetime(data3['aika'])
data4['aika'] = pd.to_datetime(data4['aika'])
data5['aika'] = pd.to_datetime(data5['aika'])
data6['aika'] = pd.to_datetime(data6['aika'])
data7['aika'] = pd.to_datetime(data7['aika'])
data8['aika'] = pd.to_datetime(data8['aika'])
#-----------------------------------------------------------------

# ------------------- Data smooth ---------------------------------


data1['smoothed'] = data1['arvo'].rolling(5).mean()
data2['smoothed'] = data2['arvo'].rolling(5).mean()
data3['smoothed'] = data3['arvo'].rolling(5).mean()
data4['smoothed'] = data4['arvo'].rolling(5).mean()
data5['smoothed'] = data5['arvo'].rolling(5).mean()
data6['smoothed'] = data6['arvo'].rolling(5).mean()
data7['smoothed'] = data7['arvo'].rolling(5).mean()
data8['smoothed'] = data8['arvo'].rolling(5).mean()

#------------------------------------------------------------------

# ----------------------Specs from tables -----------------------

data1['mean'] =  data1['arvo'].mean()
data2['mean'] =  data2['arvo'].mean()
data3['mean'] =  data3['arvo'].mean()
data4['mean'] =  data4['arvo'].mean()
data5['mean'] =  data5['arvo'].mean()
data6['mean'] =  data6['arvo'].mean()
data7['mean'] =  data7['arvo'].mean()
data8['mean'] =  data8['arvo'].mean()

data1['max'] =  data1['arvo'].max()
data2['max'] =  data2['arvo'].max()
data3['max'] =  data3['arvo'].max()
data4['max'] =  data4['arvo'].max()
data5['max'] =  data5['arvo'].max()
data6['max'] =  data6['arvo'].max()
data7['max'] =  data7['arvo'].max()
data8['max'] =  data8['arvo'].max()

data1['min'] =  data1['arvo'].min()
data2['min'] =  data2['arvo'].min()
data3['min'] =  data3['arvo'].min()
data4['min'] =  data4['arvo'].min()
data5['min'] =  data5['arvo'].min()
data6['min'] =  data6['arvo'].min()
data7['min'] =  data7['arvo'].min()
data8['min'] =  data8['arvo'].min()

data1.shape[0]
data2.shape[0]
data3.shape[0]
data4.shape[0]
data5.shape[0]
data6.shape[0]
data7.shape[0]
data8.shape[0]

if (data1.shape[0] > 0 and json_data["sensor1"]):
    data_11 = data1.iloc[[1], [3,4,5]]
    data_11['row_count'] = data1.shape[0]
    data_11['sensor_nro'] = "Sensor1"
else:
    data_11 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_11['sensor_nro'] = 'sensor1'
    pass
    
if (data2.shape[0] > 0 and json_data["sensor2"]):
    data_12 = data2.iloc[[1], [3,4,5]]
    data_12['row_count'] = data2.shape[0]
    data_12['sensor_nro'] = "Sensor2"
else:
    data_12 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_12['sensor_nro'] = 'sensor2'
    pass
    
if (data3.shape[0] > 0 and json_data["sensor3"]):
    data_13 = data3.iloc[[1], [3,4,5]]
    data_13['row_count'] = data3.shape[0]
    data_13['sensor_nro'] = "Sensor3"
else:
    data_13 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_13['sensor_nro'] = 'sensor3'
    pass
    
if (data4.shape[0] > 0 and json_data["sensor4"]):
    data_14 = data4.iloc[[1], [3,4,5]]
    data_14['row_count'] = data4.shape[0]
    data_14['sensor_nro'] = "Sensor4"
else:
    data_14 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_14['sensor_nro'] = 'sensor4'
    pass

if (data5.shape[0] > 0 and json_data["sensor5"]):
    data_15 = data5.iloc[[1], [3,4,5]]
    data_15['row_count'] = data5.shape[0]
    data_15['sensor_nro'] = "Sensor5"
else:
    data_15 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_15['sensor_nro'] = 'sensor5'
    pass

if (data6.shape[0] > 0 and json_data["sensor6"]):
    data_16 = data6.iloc[[1], [3,4,5]]
    data_16['row_count'] = data6.shape[0]
    data_16['sensor_nro'] = "Sensor6"
else:
    data_16 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_16['sensor_nro'] = 'sensor6'
    pass

if (data7.shape[0] > 0 and json_data["sensor7"]):
    data_17 = data7.iloc[[1], [3,4,5]]
    data_17['row_count'] = data7.shape[0]
    data_17['sensor_nro'] = "Sensor7"
else:
    data_17 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_17['sensor_nro'] = 'sensor7'
    pass

if (data8.shape[0] > 0 and json_data["sensor8"]):
    data_18 = data8.iloc[[1], [3,4,5]]
    data_18['row_count'] = data8.shape[0]
    data_18['sensor_nro'] = "Sensor8"
else:
    data_18 = pd.DataFrame(columns=['mean', 'max', 'min', 'row_count'])
    data_18['sensor_nro'] = 'sensor8'
    pass

concatenate = [data_11, data_12, data_13, data_14, data_15, data_16, data_17, data_18]
final_specs = pd.concat(concatenate).reset_index(drop=True)
#final_specs.index.name= 'sensor_nro'

print (final_specs)

# -----------------------------------------------------------------

# ------- Change data to ColumnDataSourceksi for Bokeh--

source_data1 = ColumnDataSource(data1)
source_data2 = ColumnDataSource(data2)
source_data3 = ColumnDataSource(data3)
source_data4 = ColumnDataSource(data4)
source_data5 = ColumnDataSource(data5)
source_data6 = ColumnDataSource(data6)
source_data7 = ColumnDataSource(data7)
source_data8 = ColumnDataSource(data8)

source_data99 = ColumnDataSource(final_specs)
#------------------------------------------------------------------






# -------- Lets make Graph-----------------------------------------

plot = figure(x_axis_type='datetime' ,plot_height=400, plot_width=800, title="History", logo = None) 
plot.add_tools(HoverTool(tooltips=[('Aika',  '@aika{%F %H-%M-%S}'),('Arvo', '$y')],formatters={'aika'      : 'datetime'}))

plot2 = figure(x_axis_type='datetime' ,plot_height=400, plot_width=800, title="History", logo = None) 
plot2.add_tools(HoverTool(tooltips=[('Aika',  '@aika{%F %H-%M-%S}'),('smoothed', '$y')],formatters={'aika'      : 'datetime'}))

datatable_columns = [
                         TableColumn(field="sensor_nro", title="Sensor Number"), 
                         TableColumn(field="mean", title="Average"),
                         TableColumn(field="max", title="Max"),
                         TableColumn(field="min", title="Min"),
                         TableColumn(field="row_count", title="Values Count"),
                         ]
data_table = DataTable(source=source_data99, columns=datatable_columns, width=800, height=400)
    #div1 = Div(text="""{data1}""", width=800, height=400)
tab3 = Panel(child=data_table, title="DataSpecs")

if (json_data["sensor1"]):
    plot.line(line_width=1, source = source_data1, x='aika', y='arvo',  legend="Sensori1", line_color="blue")
    tab1 = Panel(child=plot, title="Original")
    plot2.line(line_width=1, source = source_data1, x='aika', y='smoothed',  legend="Sensori1", line_color="blue")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor2"]):
    plot.line(line_width=1, source = source_data2, x='aika', y='arvo',  legend="Sensori2", line_color="orange")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data2, x='aika', y='smoothed',  legend="Sensori2", line_color="orange")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor3"]):  
    plot.line(line_width=1, source = source_data3, x='aika', y='arvo',  legend="Sensori3", line_color="purple")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data3, x='aika', y='smoothed',  legend="Sensori3", line_color="purple")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor4"]):
    plot.line(line_width=1, source = source_data4, x='aika', y='arvo',  legend="Sensori4", line_color="red")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data4, x='aika', y='smoothed',  legend="Sensori4", line_color="red")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor5"]):
    plot.line(line_width=1, source = source_data5, x='aika', y='arvo',  legend="Sensori5", line_color="black")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data5, x='aika', y='smoothed',  legend="Sensori5", line_color="black")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor6"]):
    plot.line(line_width=1, source = source_data6, x='aika', y='arvo',  legend="Sensori6", line_color="pink")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data6, x='aika', y='smoothed',  legend="Sensori6", line_color="pink")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor7"]):
    plot.line(line_width=1, source = source_data7, x='aika', y='arvo',  legend="Sensori7", line_color="green")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data7, x='aika', y='smoothed',  legend="Sensori7", line_color="green")
    tab2 = Panel(child=plot2, title="Smoothed")
if (json_data["sensor8"]):
    plot.line(line_width=1, source = source_data8, x='aika', y='arvo',  legend="Sensori8", line_color="magenta")
    tab1 = Panel(child=plot, title="original")
    plot2.line(line_width=1, source = source_data8, x='aika', y='smoothed',  legend="Sensori8", line_color="magenta")
    tab2 = Panel(child=plot2, title="Smoothed")
plot.xaxis.axis_label = "Aika"
plot.yaxis.axis_label = "Arvo"
plot2.xaxis.axis_label = "Aika"
plot2.yaxis.axis_label = "Arvo"



tabs = Tabs(tabs=[ tab2, tab1, tab3 ])

#layout_history = gridplot([[None, tabs]], logo = None, toolbar_location="right", sizing_mode='fixed', plot_width=1000, plot_height=1000)

curdoc().add_root(row(tabs, width=800))
curdoc().title = "history"
#-----------------------------------------------------------------------
