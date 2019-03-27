JMS

JMS comes from Jukitech Measurement System made by Jukitech Group Oy<br>

This project is about making Raspberry Pi as data collector and also live display to sensors. <br><br>

Used packages/Libraries : <br>

memcache  --  http://memcached.org/ <br>
MinimalModbus  --  https://pypi.org/project/MinimalModbus/ <br>
sqlite3  --   https://docs.python.org/2/library/sqlite3.html <br> 
Flask  --  http://flask.pocoo.org/ <br>
Supervisord  --  http://supervisord.org/ <br>
Bokeh  --  https://bokeh.pydata.org/en/latest/ <br>
Pandas  --  https://pandas.pydata.org/ <br>
nginx  --  https://www.nginx.com/<br>
uWSGI  --  https://uwsgi-docs.readthedocs.io/en/latest/ <br>
Hostapd  --  https://wiki.gentoo.org/wiki/Hostapd <br>
dnsmasq  --  http://www.thekelleys.org.uk/dnsmasq/doc.html

<br><br>
Rasberry Pi operating system is Minibian  --  https://minibianpi.wordpress.com/ <br>

Supervisord is monitoring all necessary services ; Flask, Bokeh and background script that collects data from sensors<br><br>

Scripts : <br><br>

db.py   --  Collects data from sensors and put them to database <br>
live_graph.py  --  Generates graphs to live view <br>
history_graph.py  -- Generates graphs to history view <br>


Screenshots : https://jukitech.fi/pics/index.php?twg_album=JMS-Software&twg_show=x <br><br>

Used Hardware :<br>
Raspberry Pi 3+  --  https://www.raspberrypi.org/products/raspberry-pi-3-model-b/ <br>
RTC-Module  --  https://thepihut.com/products/mini-rtc-module-for-raspberry-pi  <br>
RS485 <--> Serial Converter  --  https://www.aliexpress.com/item/TTL-to-RS485-Converter-Module-3-3V-5-0V-Hardware-Auto-Control-for-Arduino-AVR/32837392872.html <br>

