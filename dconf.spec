#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dconf
Version  : 0.40.0
Release  : 25
URL      : https://download.gnome.org/sources/dconf/0.40/dconf-0.40.0.tar.xz
Source0  : https://download.gnome.org/sources/dconf/0.40/dconf-0.40.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: dconf-bin = %{version}-%{release}
Requires: dconf-data = %{version}-%{release}
Requires: dconf-lib = %{version}-%{release}
Requires: dconf-libexec = %{version}-%{release}
Requires: dconf-license = %{version}-%{release}
Requires: dconf-man = %{version}-%{release}
Requires: dconf-services = %{version}-%{release}
BuildRequires : bash-completion-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus-extras
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(vapigen)
BuildRequires : vala

%description
dconf is a simple key/value storage system that is heavily optimised for
reading.  This makes it an ideal system for storing user preferences
(which are read 1000s of times for each time the user changes one).  It
was created with this usecase in mind.

%package bin
Summary: bin components for the dconf package.
Group: Binaries
Requires: dconf-data = %{version}-%{release}
Requires: dconf-libexec = %{version}-%{release}
Requires: dconf-license = %{version}-%{release}
Requires: dconf-services = %{version}-%{release}

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
Requires: dconf-lib = %{version}-%{release}
Requires: dconf-bin = %{version}-%{release}
Requires: dconf-data = %{version}-%{release}
Provides: dconf-devel = %{version}-%{release}
Requires: dconf = %{version}-%{release}

%description dev
dev components for the dconf package.


%package dev32
Summary: dev32 components for the dconf package.
Group: Default
Requires: dconf-lib32 = %{version}-%{release}
Requires: dconf-bin = %{version}-%{release}
Requires: dconf-data = %{version}-%{release}
Requires: dconf-dev = %{version}-%{release}

%description dev32
dev32 components for the dconf package.


%package extras
Summary: extras components for the dconf package.
Group: Default

%description extras
extras components for the dconf package.


%package lib
Summary: lib components for the dconf package.
Group: Libraries
Requires: dconf-data = %{version}-%{release}
Requires: dconf-libexec = %{version}-%{release}
Requires: dconf-license = %{version}-%{release}

%description lib
lib components for the dconf package.


%package lib32
Summary: lib32 components for the dconf package.
Group: Default
Requires: dconf-data = %{version}-%{release}
Requires: dconf-license = %{version}-%{release}

%description lib32
lib32 components for the dconf package.


%package libexec
Summary: libexec components for the dconf package.
Group: Default
Requires: dconf-license = %{version}-%{release}

%description libexec
libexec components for the dconf package.


%package license
Summary: license components for the dconf package.
Group: Default

%description license
license components for the dconf package.


%package man
Summary: man components for the dconf package.
Group: Default

%description man
man components for the dconf package.


%package services
Summary: services components for the dconf package.
Group: Systemd services

%description services
services components for the dconf package.


%prep
%setup -q -n dconf-0.40.0
cd %{_builddir}/dconf-0.40.0
pushd ..
cp -a dconf-0.40.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615911520
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :
cd ../build32;
meson test -C builddir || : || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/dconf
cp %{_builddir}/dconf-0.40.0/COPYING %{buildroot}/usr/share/package-licenses/dconf/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dconf

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
/usr/lib32/libdconf.so.1
/usr/lib32/libdconf.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dconf-service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dconf/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dconf-service.1
/usr/share/man/man1/dconf.1
/usr/share/man/man7/dconf.7

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/dconf.service
