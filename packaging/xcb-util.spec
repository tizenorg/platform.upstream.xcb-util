Name:           xcb-util
Version:        0.3.9
Release:        0
License:        MIT
Summary:        Utility libraries for X C Binding
Url:            http://xcb.freedesktop.org/
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  gperf
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  m4
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-util
Summary:        XCB utility modules
Group:          Graphics/X Window System

%description -n libxcb-util
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

Included in this package are:

- atom: Standard core X atom constants and atom caching.
- aux: Convenient access to connection setup and some core requests.
- event: Callback X event handling.

%package 	devel
Summary:        Development and header files for xcb-util
Group:          Development/Libraries
Requires:       libxcb-util = %{version}
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

%remove_docs

%post -n libxcb-util -p /sbin/ldconfig

%postun -n libxcb-util -p /sbin/ldconfig


%files -n libxcb-util
%defattr(-,root,root,-)
%{_libdir}/libxcb-util.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h
