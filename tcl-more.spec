%bcond_without	test
Summary:	A C language extension library for TCL
Name:		tcl-more
Version:	0.7
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://download.gna.org/tclmore/0.7/tclmore_%{version}b1_src.tar.gz
# Source0-md5:	0b93449da47f7b558d8af6329ac8c192
URL:		http://download.gna.org/tclmore/0.7/tclmore.html
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C language extension library for TCL. It provides additional
commands to a TCL interpreter and a set of C API functions accessible
through the stub mechanism.

%package devel
Summary:	Header files and develpment documentation for tcl-more
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do tcl-more
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for tcl-more.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumetacja do tcl-more.

%prep
%setup -q -n tclmore_%{version}b1

sed -i -e 's#/home/devel/src/C/tcl/tclmore/main--0.7/##g' Makefile*

%build
%configure \
	--enable-threads \
	--enable-shared \
	--enable-64bit
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT="$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel     -p      /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel   -p      /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc BUGS README TODO
%dir %{_libdir}/tclmore*
%attr(755,root,root) %{_libdir}/libtclmore[0-9].[0-9].[0-9].so
%{_libdir}/tclmore*/*.tcl
%attr(755,root,root) %{_libdir}/tclmore*/tclcommand.*
%{_infodir}/tclmore.info*

%files devel
%defattr(644,root,root,755)
%{_aclocaldir}/*.m4
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libtclmore[0-9].[0-9].so
%attr(755,root,root) %{_libdir}/libtclmore[0-9].so
%{_libdir}/libtclmore*.a
