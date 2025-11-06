Name:           poppler
Version:        25.11.0
Release:        1
License:        (GPLv2 or GPLv3) and GPLv2+ and LGPLv2+ and MIT
Summary:        PDF rendering library
Url:            https://github.com/sailfishos/poppler
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  boost-devel >= 1.71.0

Patch1: 0001-Revert-Require-the-newer-qt5-provided-by-the-new-bas.patch
Patch2: 0002-Don-t-build-qt5-demos-tests.patch
Patch3: 0003-Revert-Remove-QT_VERSION_CHECK-that-are-always-true.patch

%description
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package contains the shared library.

%package qt5
Summary:        PDF rendering library (Qt 5 based shared library)
Requires:       poppler = %{version}

%description qt5
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides the Qt 5 based shared library for applications
using the Qt 5 interface to Poppler.

%package qt5-devel
Summary:        PDF rendering library (Qt 5 interface development files)
Requires:       qt5-qtcore-devel qt5-qtgui-devel qt5-qttest-devel qt5-qtwidgets-devel qt5-qtxml-devel
Requires:       poppler-devel = %{version}-%{release}
Requires:       poppler-qt5 = %{version}-%{release}

%description qt5-devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides a Qt 5 style interface to Poppler.

%package devel
Summary:        PDF rendering library (development files)
Requires:       poppler = %{version}-%{release}

%description devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package contains the headers and development libraries needed to
build applications using Poppler.

%package glib
Summary:        PDF rendering library (GLib-based shared library)
Requires:       poppler = %{version}-%{release}

%description glib
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides the GLib-based shared library for applications
using the GLib interface to Poppler.

%package glib-devel
Summary:        PDF rendering library (GLib interface development files)
Requires:       glib2-devel
Requires:       poppler-devel = %{version}-%{release}
Requires:       poppler-glib = %{version}-%{release}

%description glib-devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides a GLib-style interface to Poppler.

%package utils
Summary:        PDF utilitites (based on libpoppler)
Requires:       poppler >= %{version}

%description utils
This package contains pdftops (PDF to PostScript converter), pdfinfo
(PDF document information extractor), pdfimages (PDF image extractor),
pdftohtml (PDF to HTML converter), pdftotext (PDF to text converter),
and pdffonts (PDF font analyzer).

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake . -G Ninja -DENABLE_BOOST=ON -DENABLE_GPGME=off -DENABLE_QT6=off -DENABLE_LCMS=off \
   -DENABLE_UNSTABLE_API_ABI_HEADERS=ON
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post qt5 -p /sbin/ldconfig
%postun qt5 -p /sbin/ldconfig

%post glib -p /sbin/ldconfig
%postun glib -p /sbin/ldconfig

%files qt5
%{_libdir}/libpoppler-qt5.so.*

%files qt5-devel
%{_libdir}/libpoppler-qt5.so
%{_libdir}/pkgconfig/poppler-qt5.pc
%{_includedir}/poppler/qt5/

%files
%license COPYING
%{_libdir}/libpoppler-cpp.so.*
%{_libdir}/libpoppler.so.*

%files devel
%{_libdir}/pkgconfig/poppler.pc
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_libdir}/libpoppler.so
%{_libdir}/libpoppler-cpp.so
%{_includedir}/poppler/
%exclude %{_includedir}/poppler/qt5
%exclude %{_includedir}/poppler/glib

%files glib
%{_libdir}/libpoppler-glib.so.*
%{_libdir}/girepository-1.0/Poppler-*.typelib

%files glib-devel
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/libpoppler-glib.so
%{_datadir}/gir-1.0/Poppler-*.gir
%{_includedir}/poppler/glib/

%files utils
%{_bindir}/pdf*
%{_mandir}/man1/*

%exclude %{_datarootdir}/locale/ca/LC_MESSAGES/pdfsig.mo

