from bts7960 import rpi_JGB37545 
mt = rpi_JGB37545.motor(hall_sensor=17, 
           bts_L_EN=13, 
           bts_R_EN=19, 
           bts_L_PWM=6, 
           bts_R_PWM=12, 
           wheel_diameter = 0.1)