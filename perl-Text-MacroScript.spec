%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	MacroScript
Summary:	Text::MacroScript - A macro pre-processor with embedded perl capability
Summary(pl):	Text::MacroScript - preprocesor makr z mo¿liwo¶ci± wbudowywania Perla
Name:		perl-Text-MacroScript
Version:	1.37
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Define macros, scripts and variables in macro files or directly in
text files.

%description -l pl
Modu³ ten pozwala na definiowanie makr, skryptów i zmiennych w plikach
makr lub bezpo¶rednio w plikach tekstowych.

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
