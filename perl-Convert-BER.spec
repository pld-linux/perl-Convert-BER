%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	BER
Summary:	Convert::BER perl module
Summary(pl):	Modu� perla Convert::BER
Name:		perl-Convert-BER
Version:	1.3101
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Math-BigInteger
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::BER provides an OO interface to encoding and decoding data
into packets using the ASN.1 Basic Encoding Rules (BER)

%description -l pl
Convert::BER udost�pnia obiektowy interfejs kodowania i dekodowania
danych przy wykorzystaniu BER (ASN.1 Basic Encoding Rules).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

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
