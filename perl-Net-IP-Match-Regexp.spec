
%define module	Net-IP-Match-Regexp
%define name	perl-%{module}
%define version	0.94
%define rel	3

Summary:	Efficiently match IP addresses against IP ranges via regexp
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch
%define _requires_exceptions perl(re)

%description
This module allows you to check an IP address against one or more IP
ranges.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/Net
%{_mandir}/man3/*
