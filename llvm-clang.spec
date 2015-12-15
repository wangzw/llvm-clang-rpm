%define name llvm-clang
%define release 1%{?dist}

Name: %{name}
Version: %{version}
Release: %{release}
Summary: The Low Level Virtual Machine
Group: Development/Libraries
Source0: llvm-clang-%{version}.tar.gz

License: NCSA
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gcc-c++
Requires: glibc-devel glibc-headers kernel-headers libstdc++-devel libgcc glibc glibc-common gcc gcc-c++

%description
LLVM is a compiler infrastructure designed for compile-time,
link-time, runtime, and idle-time optimization of programs from
arbitrary programming languages.  The compiler infrastructure includes
mirror sets of programming tools as well as libraries with equivalent
functionality.

%build
cd %{_topdir} && %{__make} build-llvm

%install
cd %{_topdir} && %{__make} install-llvm

%clean
cd %{_topdir} && %{__make} clean

%files
%defattr(-,root,root,-)
%{_prefix}/bin/*
%{_prefix}/include/*
%{_prefix}/lib/*
%{_prefix}/share/*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Mon Dec 14 2015 Zhanwei Wang <wangzw@wangzw.org> - %{version}-1
- Initial RPM release
