Summary:	A C language extension library for TCL
Name:		tcl-more
Version:	0.7
Release:	0.1
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

%prep
%setup -q -n tclmore_%{version}b1

%build
%configure \
	--enable-threads \
	--enable-shared \
	--enable-64bit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/more*
%attr(755,root,root) %{_libdir}/more*/libmore*.so
%{_libdir}/more*/*.tcl
%{_mandir}/man*/more*
