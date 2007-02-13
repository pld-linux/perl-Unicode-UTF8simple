#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	UTF8simple
Summary:	Unicode::UTF8simple - Conversions to/from UTF-8 from/to character sets
Summary(pl.UTF-8):	Unicode::UTF8simple - konwersje do/z UTF-8 z/do różnych zestawów znaków
Name:		perl-Unicode-UTF8simple
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1d90907170ed41690a572a2d6ed6e7da
URL:		http://search.cpan.org/dist/Unicode-UTF8simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides UTF-8 conversion for Perl versions from 5.00 and up.
It was mainly written for use with Perl 5.00 to 5.6.0 because
those Perl versions do not support Unicode::MapUTF8 or Encode.

Unicode::UTF8simple is written in plain Perl (no C code) and will
work with any Perl 5 version. It is just slightly slower than
Encode.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcję do konwersji UTF-8 dla wersji Perla
począwszy od 5.00. Został napisany głównie do używania z perlem od
5.00 do 5.6.0, jako że te wersje Perla nie obsługują Unicode::MapUTF8
i Encode.

Unicode::UTF8simple jest napisany w czystym Perlu (bez kodu w C) i
będzie działać z dowolną wersją Perla 5. Jest tylko trochę wolniejszy
niż Encode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Unicode/*.pm
%{_mandir}/man3/*
