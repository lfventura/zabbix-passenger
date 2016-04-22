Zabbix Passenger monitoring utility
===================================

This small utility parses the output of passenger-status and produces values
that can be used with the accompanying zabbix template (zabbix-template.xml).

Copy the binary to /usr/local/bin and put the userparameter_passenger.conf file
to the correct location to be included in your agent configuration.

The helper binary looks for passenger-status in the path or a RVM wrapper for
the default Ruby.



HOW TO COMPILE
=============

mkdir ~/work/src/lucas/user/zabbix-passenger
cp *.go src/lucas/user/zabbix-passenger/

export GOPATH=$HOME/work
export PATH=$PATH:/usr/local/go/bin

go get golang.org/x/net/html/charset
go get gopkg.in/alecthomas/kingpin.v2
go get launchpad.net/xmlpath

go install lucas/user/zabbix-passenger

Copy the binary to the desired system
