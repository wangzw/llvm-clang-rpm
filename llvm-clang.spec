%define name llvm
%define release 1%{?dist}

Name: %{name}
Version: %{version}
Release: %{release}
Summary: The Low Level Virtual Machine
Group: Development/Libraries
Source0: llvm-clang-%{version}.tar.gz

License: NCSA
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
LLVM is a compiler infrastructure designed for compile-time,
link-time, runtime, and idle-time optimization of programs from
arbitrary programming languages.  The compiler infrastructure includes
mirror sets of programming tools as well as libraries with equivalent
functionality.

%package devel
Summary: The Low Level Virtual Machine
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
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
%{_prefix}/usr/lib/clang/*
%{_prefix}/usr/share/doc/*
%{_prefix}/usr/share/man/*
%{_prefix}/usr/share/llvm

%files devel
%defattr(-,root,root,-)
%{_prefix}/include/*
%{_prefix}/lib/*
%{_prefix}/usr/share/llvm/*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Mon Dec 14 2015 Zhanwei Wang <wangzw@wangzw.org> - %{version}-1
- Initial RPM release
