Name:           xcb-util
Version:        0.3.9
Release:        0
License:        MIT
Summary:        utility libraries for X C Binding
Url:            http://xcb.freedesktop.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  gperf
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  m4
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
Description: %{summary}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package 	devel
Summary:        Development and header files for xcb-util
Group:          System Environment/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description	devel
Development files for xcb-util.

%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%remove_docs

%files
%defattr(-,root,root,-)
%{_libdir}/libxcb-util.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h
