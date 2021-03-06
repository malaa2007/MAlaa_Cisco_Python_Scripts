#########################################################################################################	
##      Author = Mohamed Alaa                                                                          ##	
##      Purpose = Simple SSH session to a Cisco router that executes the 'show ip int brief' command.  ##
##      Uses = netmiko, ConnectHandler, datetime                                                       ##
##      Created on 2-10-2017                                                                           ##
##      Version 1.0                                                                                    ##
#########################################################################################################

## First, I must import the ConnectHandler factory function from Netmiko. 
## This factory function selects the correct Netmiko class based upon the device_type
 
from netmiko import ConnectHandler

## using datetime to calculate total time

from datetime import datetime

## Request your inputs

IP = raw_input("Enter Device IP Add: ")
USERNAME = raw_input("Enter your Username: ")
PASSWORD = raw_input("Enter your Password: ")
ENABLEPASS = raw_input("Enter your enable password: ")

## Save start date and time in variable start_time and print it.

start_time = datetime.now()
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "Program started at:", start_time
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

## Now in order to connect, all I need to do is call the "ConnectHandler" netmiko factory function directly
## The supported device_type's are cisco_ios, cisco_xe, cisco_asa, cisco_nxos, cisco_xr, cisco_wlc_ssh, arista_eos, 
## hp_procurve, hp_comware, huawei, f5_ltm, juniper, and brocade_vdx.

net_connect = ConnectHandler(device_type='cisco_ios', ip=IP, username=USERNAME, password=PASSWORD) 

## Now at this point we have an SSH connection. I can verify this by executing the .find_prompt() method

net_connect.find_prompt()

## I can also send commands down the SSH channel and receive the output back. 
## Here, I use the .send_command() method to send the 'show ip int brief' command:

output = net_connect.send_command("show ip int brief")

## Print the output of the command

print output

## Save end date and time in variable end_time and print it.

end_time = datetime.now()
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "Program finished at:", end_time


## Save total time in variable total_time

total_time = end_time - start_time

## Print the total time

print 
print "Program took almost:", total_time
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
