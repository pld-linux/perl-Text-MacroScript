%include	/usr/lib/rpm/macros.perl
Summary:	Text-MacroScript perl module
Summary(pl):	Modu� perla Text-MacroScript
Name:		perl-Text-MacroScript
Version:	1.34
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-MacroScript-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-MacroScript perl module.

%description -l pl
Modu� perla Text-MacroScript.

%prep
%setup -q -n Text-MacroScript-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/MacroScript
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz macro

%{perl_sitelib}/Text/MacroScript.pm
%{perl_sitearch}/auto/Text/MacroScript

%{_mandir}/man3/*
