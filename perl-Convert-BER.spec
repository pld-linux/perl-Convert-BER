%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	BER
Summary:	Convert::BER perl module
Summary(pl):	Modu³ perla Convert::BER
Name:		perl-Convert-BER
Version:	1.31
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Math-BigInteger
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::BER provides an OO interface to encoding and decoding data
into packets using the ASN.1 Basic Encoding Rules (BER)

%description -l pl
Convert::BER udostêpnia obiektowy interfejs kodowania i dekodowania
danych przy wykorzystaniu BER (ASN.1 Basic Encoding Rules).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Convert/BER.pm
%{_mandir}/man3/*
