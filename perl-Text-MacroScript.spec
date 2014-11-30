#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	MacroScript
%include	/usr/lib/rpm/macros.perl
Summary:	Text::MacroScript - a macro pre-processor with embedded perl capability
Summary(pl.UTF-8):	Text::MacroScript - preprocesor makr z możliwością wbudowywania Perla
Name:		perl-Text-MacroScript
Version:	1.40
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d4959e2c7d1bb43dda0d0a18d8e71fc3
URL:		http://search.cpan.org/dist/Text-MacroScript/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Define macros, scripts and variables in macro files or directly in
text files.

%description -l pl.UTF-8
Moduł ten pozwala na definiowanie makr, skryptów i zmiennych w plikach
makr lub bezpośrednio w plikach tekstowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README macro
%{perl_vendorlib}/Text/MacroScript.pm
%{_mandir}/man3/*
