# which plugins to actually build and install
%global extdirs ext/faac

Summary:        GStreamer 1.0 streaming media framework "bad" non-free plug-ins
Name:           gstreamer1-plugins-bad-nonfree
Version:        1.10.5
Release:        1%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faac-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that depend on libraries which use a non-free
license.


%prep
%autosetup -n gst-plugins-bad-%{version}


%build
# Note we don't bother with disabling everything which is in Fedora, that
# is unmaintainable, instead we selectively run make in subdirs
%configure --disable-static \
    --with-package-name="gst-plugins-bad 1.0 nonfree rpmfusion rpm" \
    --with-package-origin="http://rpmfusion.org/" \
    --enable-debug \
    --enable-experimental
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
for i in %{extdirs}; do
    pushd $i
    %make_build V=2
    popd
done


%install
for i in %{extdirs}; do
    pushd $i
    %make_install V=2
    popd
done
rm %{buildroot}%{_libdir}/gstreamer-1.0/*.la


%files
%doc AUTHORS NEWS README RELEASE
%license COPYING.LIB
# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgstfaac.so


%changelog
* Fri Jun 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.10.5-1
- Update to 1.10.5

* Mon Feb 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.10.4-1
- Update to 1.10.4

* Fri Feb 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.10.3-1
- Update to 1.10.3

* Wed Nov 30 2016 leigh scott <leigh123linux@googlemail.com> - 1.10.2-1
- Update to 1.10.2

* Fri Nov 11 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Sat Jul  9 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Sat Jul  9 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.4-1
- Update to 1.6.4

* Sat Aug 22 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-1
- Initial gstreamer1-plugins-bad-nonfree rpmfusion package
