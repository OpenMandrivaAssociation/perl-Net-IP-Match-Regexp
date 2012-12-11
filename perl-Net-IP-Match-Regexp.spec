%define upstream_name	 Net-IP-Match-Regexp
%define upstream_version 1.01

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(re\\)'
%else
%define _requires_exceptions perl(re)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Efficiently match IP addresses against IP ranges via regexp
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module allows you to check an IP address against one or more IP
ranges.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/Net
%{_mandir}/man3/*


%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 410095
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.1
+ Revision: 292261
- update to new version 1.01

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.00-1mdv2008.1
+ Revision: 136304
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 1.00-1mdv2008.0
+ Revision: 81920
- 1.00

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 0.94-3mdv2008.0
+ Revision: 34872
- annual rebuild


* Sun May 28 2006 Anssi Hannula <anssi@mandriva.org> 0.94-2mdv2007.0
- _requires_exception perl(re)

* Sun May 28 2006 Anssi Hannula <anssi@mandriva.org> 0.94-1mdv2007.0
- initial Mandriva package

