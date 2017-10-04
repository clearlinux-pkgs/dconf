#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dconf
Version  : 0.26.1
Release  : 9
URL      : https://download.gnome.org/sources/dconf/0.26/dconf-0.26.1.tar.xz
Source0  : https://download.gnome.org/sources/dconf/0.26/dconf-0.26.1.tar.xz
Summary  : dconf client library
Group    : Development/Tools
License  : LGPL-2.1
Requires: dconf-bin
Requires: dconf-lib
Requires: dconf-data
Requires: dconf-doc
BuildRequires : dbus-extras
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32gio-unix-2.0)
BuildRequires : pkgconfig(32glib-2.0)
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


%package dev32
Summary: dev32 components for the dconf package.
Group: Default
Requires: dconf-lib32
Requires: dconf-bin
Requires: dconf-data
Requires: dconf-dev

%description dev32
dev32 components for the dconf package.


%package doc
Summary: doc components for the dconf package.
Group: Documentation

%description doc
doc components for the dconf package.


%package extras
Summary: extras components for the dconf package.
Group: Default

%description extras
extras components for the dconf package.


%package lib
Summary: lib components for the dconf package.
Group: Libraries
Requires: dconf-data

%description lib
lib components for the dconf package.


%package lib32
Summary: lib32 components for the dconf package.
Group: Default
Requires: dconf-data

%description lib32
lib32 components for the dconf package.


%prep
%setup -q -n dconf-0.26.1
pushd ..
cp -a dconf-0.26.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507153015
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1507153015
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
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
/usr/lib64/libdconf.so
/usr/lib64/pkgconfig/dconf.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libdconf.so
/usr/lib32/pkgconfig/32dconf.pc
/usr/lib32/pkgconfig/dconf.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
/usr/share/gtk-doc/html/dconf/DConfClient.html
/usr/share/gtk-doc/html/dconf/annotation-glossary.html
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
/usr/share/gtk-doc/html/dconf/left-insensitive.png
/usr/share/gtk-doc/html/dconf/left.png
/usr/share/gtk-doc/html/dconf/object-tree.html
/usr/share/gtk-doc/html/dconf/programs.html
/usr/share/gtk-doc/html/dconf/right-insensitive.png
/usr/share/gtk-doc/html/dconf/right.png
/usr/share/gtk-doc/html/dconf/style.css
/usr/share/gtk-doc/html/dconf/up-insensitive.png
/usr/share/gtk-doc/html/dconf/up.png

%files extras
%defattr(-,root,root,-)
/usr/lib32/gio/modules/libdconfsettings.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/gio/modules/libdconfsettings.so
/usr/lib64/libdconf.so.1
/usr/lib64/libdconf.so.1.0.0

%files lib32
%defattr(-,root,root,-)
%exclude /usr/lib32/gio/modules/libdconfsettings.so
/usr/lib32/libdconf.so.1
/usr/lib32/libdconf.so.1.0.0
