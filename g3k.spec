#
# spec file for package gulkan
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define _libver 0.16

Name:           g3k
Version:        0.16.0
Release:        0
Summary:        A 3DUI widget toolkit
License:        MIT
Url:            https://gitlab.freedesktop.org/xrdesktop/g3k
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:  libstdc++-devel
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(gxr-0.16)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(libcanberra)

%description
A 3DUI widget toolkit

%package devel
Summary:        A 3DUI widget toolkit
Requires:       %{name} = %{version}

%description devel
A 3DUI widget toolkit

%prep
%setup -q

%build
export SUSE_ASNEEDED=0
%meson
%meson_build

%install
export SUSE_ASNEEDED=0
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%dir %{_datadir}/glib-2.0/schemas
%{_libdir}/lib%{name}-%{_libver}.so.*
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml

%files devel
%dir %{_includedir}/%{name}-%{_libver}
%{_includedir}/%{name}-%{_libver}/*.h
%{_libdir}/pkgconfig/%{name}-%{_libver}.pc
%{_libdir}/lib%{name}-%{_libver}.so

%changelog
