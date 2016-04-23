# Do not create a package with debugging info
%define  debug_package %{nil}
Name:		zabbix-passenger	
Version:	1.0
Release:	1%{?dist}
Summary:	Passenger monitoring for Zabbix Agent

Group:		Networking/Admin	
License:	none

Source:		%{name}.tar.gz

Requires:	zabbix-agent

%description
This package provides a tool to convert the passenger-status output to something that Zabbix can handle and monitor

%prep
%setup -q -n %{name}


%build
export GOPATH=$RPM_BUILD_DIR/%{name}/work
export PATH=$PATH:/usr/local/go/bin
mkdir -p $RPM_BUILD_DIR/%{name}/work/src
pwd
#mv ../zabbix-passenger $RPM_BUILD_DIR/%{name}/work/src/

go get golang.org/x/net/html/charset
go get gopkg.in/alecthomas/kingpin.v2
go get launchpad.net/xmlpath

go install zabbix-passenger

%install
echo "aqui"
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/
mkdir -p $RPM_BUILD_ROOT/etc/sudoers.d/
cp -a $RPM_BUILD_DIR/%{name}/work/bin/zabbix-passenger $RPM_BUILD_ROOT/usr/local/bin/
install -m 644 $RPM_BUILD_DIR/%{name}/work/src/%{name}/userparameter_passenger.conf $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/
install -m 440 $RPM_BUILD_DIR/%{name}/work/src/%{name}/zabbix-passenger-sudo $RPM_BUILD_ROOT/etc/sudoers.d/

%post

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR

%files
%defattr(-,root,root)
/usr/local/bin/zabbix-passenger
/etc/zabbix/zabbix_agentd.d/userparameter_passenger.conf
/etc/sudoers.d/zabbix-passenger-sudo

%changelog
* Fri Apr 22 2016 Lucas Ventura
- Initial build
