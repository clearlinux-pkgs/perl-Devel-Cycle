#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Cycle
Version  : 1.12
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/L/LD/LDS/Devel-Cycle-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LD/LDS/Devel-Cycle-1.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdevel-cycle-perl/libdevel-cycle-perl_1.12-1.debian.tar.xz
Summary  : 'Find memory cycles in objects'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Devel-Cycle-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Perl Module Devel::Cycle
========================
This module can be used to find memory cycles in objects and other
references.  Here is the synopsis:

%package dev
Summary: dev components for the perl-Devel-Cycle package.
Group: Development
Provides: perl-Devel-Cycle-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-Cycle package.


%package license
Summary: license components for the perl-Devel-Cycle package.
Group: Default

%description license
license components for the perl-Devel-Cycle package.


%prep
%setup -q -n Devel-Cycle-1.12
cd ..
%setup -q -T -D -n Devel-Cycle-1.12 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Devel-Cycle-1.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-Cycle
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Devel-Cycle/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Devel/Cycle.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Cycle.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-Cycle/deblicense_copyright
