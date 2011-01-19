%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

Name: perl-AptPkg
Version: 0.1.24
Release: %mkrel 1
Summary: Perl interface to libapt-pkg
License: GPL
Group: Development/Perl
URL: http://packages.debian.org/unstable/perl/libapt-pkg-perl
Source: libapt-pkg-perl_%{version}.tar.gz
Source1: etc-apt.tgz
BuildRequires: gcc-c++ perl-devel apt-mdv-devel

%description
A Perl interface to APT's libapt-pkg which provides modules
for configuration file/command line parsing, version comparison,
inspection of the binary package cache and source package details.

%prep
%setup -q -n libapt-pkg-perl-%{version}
tar -xz -C t/cache/etc/ -f %SOURCE1 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/ INC=-I%_includedir/rpm
make INC=-I%_includedir/rpm

#%check
#make test

%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README debian/changelog examples
%doc AptPkg/*.pod

%{perlvendorlib}/*
%{_mandir}/man3/*

%changelog
