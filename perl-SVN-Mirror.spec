# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SVN
%define		pnam	Mirror
Summary:	SVN::Mirror - mirror remote subversion repository to local
Summary(pl.UTF-8):	SVN::Mirror - lokalne mirrorowane zdalnych repozytoriów subversion
Name:		perl-SVN-Mirror
Version:	0.73
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CL/CLKAO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	170e067de85916f8d0b6a508194fbba3
%if %{with tests}
BuildRequires:	perl-BSD-Resource
BuildRequires:	perl-SVN-Simple
BuildRequires:	subversion
%endif
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Data-UUID
BuildRequires:	perl-File-chdir
BuildRequires:	perl-URI
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-VCP
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-subversion >= 1.0.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(SVK::.*)'

%description
Mirror remote subversion repository to local.

%description -l pl.UTF-8
Lokalne mirrorowane zdalnych repozytoriów subversion.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes | tr y n | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
yes | tr y n | %{__make}

%{?with_tests:yes | tr y n | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

yes | tr y n | %{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE*
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SVN/Mirror
%{perl_vendorlib}/SVN/Mirror.pm
%{_mandir}/man[13]/*
