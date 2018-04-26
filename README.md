# Cisco Live US - Devnet workshop 2897
This file will provide you with instructions around how to create JavaScript, HTML and python code to create a 
port automation web user interface on top of Cisco ACI

## Use case

A company is implementing ACI in its data center. They think the user interface that comes with the solution is great, 
however they would like to implement the following process:

![picture alt](images/port_Workflow_Diagram.png "Port deployment workflow")

## Solution

In order to support this workflow, a simplified web user interface that abstract all the objects that 
we saw before can be made with the comprehensive set of APIs that ACI provides. 

In this solution, an operator can simply select the port type, switch-port and VLAN, and the solution will create all 
the needed configuration in ACI.

For your reference, we are going to use the following frameworks

* django Web Framework - https://www.djangoproject.com/
* Angular JS Framework - https://angularjs.org/ 
* Cisco UI Framework - https://developer.cisco.com/site/uiux/ 

[Get Started!]
 
[Get Started!]: lab/step1.md
