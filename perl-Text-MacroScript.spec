%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	MacroScript
Summary:	Text::MacroScript - a macro pre-processor with embedded perl capability
Summary(pl):	Text::MacroScript - preprocesor makr z mo�liwo�ci� wbudowywania Perla
Name:		perl-Text-MacroScript
Version:	1.38
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6cc43c181801aaef875b8b4ed22f198c
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Define macros, scripts and variables in macro files or directly in
text files.

%description -l pl
Modu� ten pozwala na definiowanie makr, skrypt�w i zmiennych w plikach
makr lub bezpo�rednio w plikach tekstowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README macro
%{perl_vendorlib}/Text/MacroScript.pm
%{_mandir}/man3/*
