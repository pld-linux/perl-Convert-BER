%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	BER
Summary:	Convert::BER Perl module - ASN.1 Basic Encoding Rules
Summary(pl):	Modu� Perla Convert::BER - podstawowe regu�y kodowania ASN.1
Name:		perl-Convert-BER
Version:	1.3101
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	00fd5e5a98d4194da0e980186cba6292
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Math-BigInteger
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::BER provides an object oriented interface to encoding and
decoding data into packets using the ASN.1 Basic Encoding Rules (BER)

%description -l pl
Convert::BER udost�pnia obiektowy interfejs kodowania i dekodowania
danych przy wykorzystaniu ASN.1 BER (podstawowych regu� kodowania -
Basic Encoding Rules).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Convert/BER.pm
%{_mandir}/man3/*
