Name: libX11
Summary: Core X11 protocol client library
Version: 1.8.1
Release: 1
License: MIT
URL: http://www.x.org
Source0: %{name}-%{version}.tar.zst
BuildRequires: libtool
BuildRequires: xorg-x11-util-macros
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(xproto) >= 7.0.25
BuildRequires: pkgconfig(xcb) >= 1.11.1

%description
%{summary}.

%package common
Summary: Common data for libX11
BuildArch: noarch

%description common
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-xcb = %{version}-%{release}

%description devel
X.Org X11 libX11 development package.

%package xcb
Summary: XCB interop for libX11
Conflicts: %{name} < %{version}-%{release}

%description xcb
libX11/libxcb interoperability library.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%reconfigure
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/X11/Xcms.txt
rm -rf %{buildroot}%{_datadir}/doc
rm -rf %{buildroot}%{_mandir}

%files
%{_libdir}/libX11.so.6
%{_libdir}/libX11.so.6.4.0

%files xcb
%{_libdir}/libX11-xcb.so.1
%{_libdir}/libX11-xcb.so.1.0.0

%files common
%doc AUTHORS COPYING README.md NEWS
%{_datadir}/X11/locale/
%{_datadir}/X11/XErrorDB

%files devel
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/XKBlib.h
%{_includedir}/X11/Xcms.h
%{_includedir}/X11/Xlib.h
%{_includedir}/X11/XlibConf.h
%{_includedir}/X11/Xlibint.h
%{_includedir}/X11/Xlib-xcb.h
%{_includedir}/X11/Xlocale.h
%{_includedir}/X11/Xregion.h
%{_includedir}/X11/Xresource.h
%{_includedir}/X11/Xutil.h
%{_includedir}/X11/cursorfont.h
%{_includedir}/X11/extensions/XKBgeom.h
%{_libdir}/libX11.so
%{_libdir}/libX11-xcb.so
%{_libdir}/pkgconfig/x11.pc
%{_libdir}/pkgconfig/x11-xcb.pc
