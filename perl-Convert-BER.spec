%include	/usr/lib/rpm/macros.perl
Summary:	Convert-BER perl module
Summary(pl):	Modu³ perla Convert-BER
Name:		perl-Convert-BER
Version:	1.26
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-BER-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Math-BigInteger
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-BER provides an OO interface to encoding and decoding data
into packets using the ASN.1 Basic Encoding Rules (BER)

%description -l pl
Convert-BER udostêpnia obiektowy interfejs kodowania i dekodowania
danych przy wykorzystaniu BER (ASN.1 Basic Encoding Rules).

%prep
%setup -q -n Convert-BER-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Convert/BER
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Convert/BER.pm
%{perl_sitearch}/auto/Convert/BER

%{_mandir}/man3/*
