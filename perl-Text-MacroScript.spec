%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	MacroScript
Summary:	Text-MacroScript perl module
Summary(pl):	Modu³ perla Text-MacroScript
Name:		perl-Text-MacroScript
Version:	1.37
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-MacroScript perl module.

%description -l pl
Modu³ perla Text-MacroScript.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz macro
%{perl_sitelib}/Text/MacroScript.pm
%{_mandir}/man3/*
