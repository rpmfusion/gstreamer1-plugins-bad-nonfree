# which plugins to actually build and install
%global extdirs ext/faac ext/fdkaac

Summary:        GStreamer 1.0 streaming media framework "bad" non-free plug-ins
Name:           gstreamer1-plugins-bad-nonfree
Version:        1.16.0
Release:        1%{?dist}
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        %url/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faac-devel
BuildRequires:  fdk-aac-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that depend on libraries which use a non-free
license.


%prep
%autosetup -p1 -n gst-plugins-bad-%{version}


%build
# Note we don't bother with disabling everything which is in Fedora, that
# is unmaintainable, instead we selectively run make in subdirs
%configure \
    --disable-static \
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
rm -fv %{buildroot}%{_libdir}/gstreamer-1.0/*.la


%files
%doc AUTHORS NEWS README RELEASE
%license COPYING.LIB
# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgstfaac.so
%{_libdir}/gstreamer-1.0/libgstfdkaac.so

%changelog
* Wed Apr 24 2019 Leigh Scott <leigh123linux@gmail.com> - 1.16.0-1
- 1.16.0

* Mon Mar 18 2019 Sérgio Basto <sergio@serjux.com> - 1.15.2-1
- Update to 1.15.2

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Feb 09 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.15.1-1
- 1.15.1

* Sat Nov 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14.4-2
- Rebuild for new fdk-aac

* Tue Oct 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.4-1
- 1.14.4

* Tue Sep 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14.3-1
- 1.14.3

* Sat Aug 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.2-1
- 1.14.2

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.1-1
- 1.14.1

* Sun Apr 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.14.0-1
- Update to 1.14.0

* Sun Mar 04 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.13.1-1
- 1.13.1

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.4-1
- Update to 1.12.4

* Thu Sep 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.3-1
- Update to 1.12.3

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.2-1
- Update to 1.12.2

* Fri Jun 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.1-1
- Update to 1.12.1

* Fri May 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.0-1
- Update to 1.12.0

* Tue Apr 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.90-1
- Update to 1.11.90

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.2-1
- Update to 1.11.2

* Mon Jan 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.1-2
- Enable fdk-aac

* Mon Jan 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.1-1
- Update to 1.11.1

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
