# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SVN
%define	pnam	Mirror
Summary:	SVN::Mirror - Mirror Remote Subversion Repository to local
Summary(pl):	SVN::Mirror - lokalne mirrorowane zdalnych repozytoriów Subversion
Name:		perl-SVN-Mirror
Version:	0.41
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3544933deebbe5fdf25677d0be21e6db
BuildRequires:	perl-Data-UUID
%{?with_tests:BuildRequires:	perl-SVN-Simple}
BuildRequires:	perl-VCP
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-subversion >= 1.0.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mirror Remote Subversion Repository to local.

%description -l pl
Lokalne mirrorowane zdalnych repozytoriów Subversion.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "n" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:echo "n" | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

echo "n" | %{__make} install \
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
