Summary: nethserver-zabbix-mysql-epel sets up the monitoring system
%define name nethserver-zabbix-mysql-epel
Name: %{name}
%define version 0.0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: nethserver-mysql,zabbix30-server-mysql,zabbix30-web-mysql,zabbix30-agent,net-snmp-utils,nethserver-net-snmp,php-mysql
Conflicts: nethserver-zabbix22, nethserver-zabbix
BuildRequires: nethserver-devtools net-snmp-utils nethserver-net-snmp
BuildArch: noarch

%description
NethServer Zabbix mysql configuration

%changelog

#%pre
#getent passwd zabbix >/dev/null || useradd -m -d /var/lib/zabbix -s /bin/bash zabbix
#exit 0

%prep
%setup

%build
perl createlinks
mkdir -p root/var/lib/nethserver/zabbix/backup

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
