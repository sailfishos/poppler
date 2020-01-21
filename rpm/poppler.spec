Name:           poppler
Version:        0.74.0
Release:        1
License:        (GPLv2 or GPLv3) and GPLv2+ and LGPLv2+ and MIT
Summary:        PDF rendering library
Url:            http://poppler.freedesktop.org/
Source0:        http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
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

%description
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package contains the shared library.

%package qt5
Summary:        PDF rendering library (Qt 5 based shared library)
Requires:       poppler = %{version}
Obsoletes:      poppler-qt

%description qt5
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides the Qt 5 based shared library for applications
using the Qt 5 interface to Poppler.

%package qt5-devel
Summary:        PDF rendering library (Qt 5 interface development files)
Requires:       qt5-qtcore-devel qt5-qtgui-devel qt5-qttest-devel qt5-qtwidgets-devel qt5-qtxml-devel
Requires:       poppler-devel = %{version}-%{release}
Requires:       poppler-qt5 = %{version}-%{release}
Obsoletes:      poppler-qt-devel

%description qt5-devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides a Qt 5 style interface to Poppler.

%package devel
Summary:        PDF rendering library (development files)
Requires:       libjpeg-devel
Requires:       pkgconfig
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
%setup -q -n %{name}-%{version}/upstream

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib .
make %{?_smp_mflags}

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT
rm -f %{buildroot}%{_libdir}/*.la
%if 0%{?build_with_qt5}
cd %{buildroot}
find . -type f -o -type l | grep -v qt | xargs rm -v
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post qt5 -p /sbin/ldconfig
%postun qt5 -p /sbin/ldconfig

%post glib -p /sbin/ldconfig
%postun glib -p /sbin/ldconfig

%files qt5
%defattr(-,root,root,-)
%{_libdir}/libpoppler-qt5.so.*

%files qt5-devel
%defattr(-,root,root,-)
%{_libdir}/libpoppler-qt5.so
%{_libdir}/pkgconfig/poppler-qt5.pc
%{_includedir}/poppler/qt5/

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libpoppler-cpp.so.*
%{_libdir}/libpoppler.so.*

%files devel
%defattr(-,root,root,-)
%doc README
%{_libdir}/pkgconfig/poppler.pc
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_libdir}/pkgconfig/poppler-splash.pc
%{_libdir}/libpoppler.so
%{_libdir}/libpoppler-cpp.so
%{_includedir}/poppler/

%files glib
%defattr(-,root,root,-)
%{_libdir}/libpoppler-glib.so.*
%{_libdir}/girepository-1.0/Poppler-*.typelib

%files glib-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/pkgconfig/poppler-cairo.pc
%{_libdir}/libpoppler-glib.so
%{_datadir}/gir-1.0/Poppler-*.gir

%files utils
%defattr(-,root,root,-)
%{_bindir}/pdffonts
%{_bindir}/pdfimages
%{_bindir}/pdfinfo
%{_bindir}/pdftohtml
%{_bindir}/pdftoppm
%{_bindir}/pdftops
%{_bindir}/pdftotext
%{_bindir}/pdfdetach
%{_bindir}/pdfseparate
%{_bindir}/pdftocairo
%{_bindir}/pdfunite
%{_bindir}/pdfsig
%{_mandir}/man1/pdffonts.*
%{_mandir}/man1/pdfimages.*
%{_mandir}/man1/pdfinfo.*
%{_mandir}/man1/pdftohtml.*
%{_mandir}/man1/pdftoppm.*
%{_mandir}/man1/pdftops.*
%{_mandir}/man1/pdftotext.*
%{_mandir}/man1/pdfdetach.1.gz
%{_mandir}/man1/pdfseparate.1.gz
%{_mandir}/man1/pdftocairo.1.gz
%{_mandir}/man1/pdfunite.1.gz
%{_mandir}/man1/pdfsig.1.gz
