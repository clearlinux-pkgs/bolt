#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bolt
Version  : 0.5
Release  : 1
URL      : https://gitlab.freedesktop.org/bolt/bolt/-/archive/0.5/bolt-0.5.tar.gz
Source0  : https://gitlab.freedesktop.org/bolt/bolt/-/archive/0.5/bolt-0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: bolt-bin = %{version}-%{release}
Requires: bolt-config = %{version}-%{release}
Requires: bolt-data = %{version}-%{release}
Requires: bolt-libexec = %{version}-%{release}
Requires: bolt-license = %{version}-%{release}
Requires: bolt-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(polkit-gobject-1)

%description
bolt
====
Userspace system daemon to enable security levels for *Thunderboltâ¢ 3*
on GNU/LinuxÂ®.

%package bin
Summary: bin components for the bolt package.
Group: Binaries
Requires: bolt-data = %{version}-%{release}
Requires: bolt-libexec = %{version}-%{release}
Requires: bolt-config = %{version}-%{release}
Requires: bolt-license = %{version}-%{release}
Requires: bolt-services = %{version}-%{release}

%description bin
bin components for the bolt package.


%package config
Summary: config components for the bolt package.
Group: Default

%description config
config components for the bolt package.


%package data
Summary: data components for the bolt package.
Group: Data

%description data
data components for the bolt package.


%package libexec
Summary: libexec components for the bolt package.
Group: Default
Requires: bolt-config = %{version}-%{release}
Requires: bolt-license = %{version}-%{release}

%description libexec
libexec components for the bolt package.


%package license
Summary: license components for the bolt package.
Group: Default

%description license
license components for the bolt package.


%package services
Summary: services components for the bolt package.
Group: Systemd services

%description services
services components for the bolt package.


%prep
%setup -q -n bolt-0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542390728
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/bolt
cp COPYING %{buildroot}/usr/share/package-licenses/bolt/COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/boltctl

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/90-bolt.rules

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.freedesktop.bolt.xml
/usr/share/dbus-1/system-services/org.freedesktop.bolt.service
/usr/share/polkit-1/actions/org.freedesktop.bolt.policy
/usr/share/polkit-1/rules.d/org.freedesktop.bolt.rules

%files libexec
%defattr(-,root,root,-)
/usr/libexec/boltd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bolt/COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/bolt.service
