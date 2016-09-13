#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dconf
Version  : 0.26.0
Release  : 1
URL      : https://download.gnome.org/core/3.21/3.21.4/sources/dconf-0.26.0.tar.xz
Source0  : https://download.gnome.org/core/3.21/3.21.4/sources/dconf-0.26.0.tar.xz
Summary  : dconf client library
Group    : Development/Tools
License  : LGPL-2.1
Requires: dconf-bin
Requires: dconf-lib
Requires: dconf-data
Requires: dconf-doc
BuildRequires : dbus-extras
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glibc-staticdev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)

%description
dconf is a simple key/value storage system that is heavily optimised for
reading.  This makes it an ideal system for storing user preferences
(which are read 1000s of times for each time the user changes one).  It
was created with this usecase in mind.

%package bin
Summary: bin components for the dconf package.
Group: Binaries
Requires: dconf-data

%description bin
bin components for the dconf package.


%package data
Summary: data components for the dconf package.
Group: Data

%description data
data components for the dconf package.


%package dev
Summary: dev components for the dconf package.
Group: Development
Requires: dconf-lib
Requires: dconf-bin
Requires: dconf-data
Provides: dconf-devel

%description dev
dev components for the dconf package.


%package doc
Summary: doc components for the dconf package.
Group: Documentation

%description doc
doc components for the dconf package.


%package lib
Summary: lib components for the dconf package.
Group: Libraries
Requires: dconf-data

%description lib
lib components for the dconf package.


%prep
%setup -q -n dconf-0.26.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dconf
/usr/libexec/dconf-service

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/dconf
/usr/share/dbus-1/services/ca.desrt.dconf.service
/usr/share/vala/vapi/dconf.deps
/usr/share/vala/vapi/dconf.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/dconf/client/dconf-client.h
/usr/include/dconf/common/dconf-changeset.h
/usr/include/dconf/common/dconf-enums.h
/usr/include/dconf/common/dconf-paths.h
/usr/include/dconf/dconf.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
/usr/share/gtk-doc/html/dconf/DConfClient.html
/usr/share/gtk-doc/html/dconf/annotation-glossary.html
/usr/share/gtk-doc/html/dconf/api-index-0.16.html
/usr/share/gtk-doc/html/dconf/api-index-0.18.html
/usr/share/gtk-doc/html/dconf/api-index-0.20.html
/usr/share/gtk-doc/html/dconf/api-index-0.26.html
/usr/share/gtk-doc/html/dconf/api-index-full.html
/usr/share/gtk-doc/html/dconf/ch01.html
/usr/share/gtk-doc/html/dconf/dconf-DConfChangeset.html
/usr/share/gtk-doc/html/dconf/dconf-DConfError.html
/usr/share/gtk-doc/html/dconf/dconf-dconf-Paths.html
/usr/share/gtk-doc/html/dconf/dconf-overview.html
/usr/share/gtk-doc/html/dconf/dconf-service.html
/usr/share/gtk-doc/html/dconf/dconf-tool.html
/usr/share/gtk-doc/html/dconf/dconf.devhelp2
/usr/share/gtk-doc/html/dconf/home.png
/usr/share/gtk-doc/html/dconf/index.html
/usr/share/gtk-doc/html/dconf/index.sgml
/usr/share/gtk-doc/html/dconf/left-insensitive.png
/usr/share/gtk-doc/html/dconf/left.png
/usr/share/gtk-doc/html/dconf/object-tree.html
/usr/share/gtk-doc/html/dconf/programs.html
/usr/share/gtk-doc/html/dconf/right-insensitive.png
/usr/share/gtk-doc/html/dconf/right.png
/usr/share/gtk-doc/html/dconf/style.css
/usr/share/gtk-doc/html/dconf/up-insensitive.png
/usr/share/gtk-doc/html/dconf/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/gio/modules/libdconfsettings.so
