%define name	qtemu
%define version	1.0.5
%define release	%mkrel 2
%define qtemudir %{_datadir}/qtemu

Summary:	A graphical user interface for QEMU
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source10:	qtemu.png
Source11:	qtemu.16.png
Source12:	qtemu.48.png
Patch2:		qtemu-qemu-accelerators.patch
Source2:	processor.png
License:	GPLv2
Group:		Emulators
Url:		http://www.qtemu.org/
Requires:	qemu >= 0.9.0-%{mkrel 3}
BuildRequires:	cmake, qt4-devel >= 4.1, qt4-linguist
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
QtEmu is a graphical user interface for QEMU written in Qt4. It has
the ability to run virtual operating systems on native systems. This
way you can easily test a new operating system or try a Live CD on
your system without any troubles and dangers.

%prep
%setup -q
%patch2 -p0 -b .qemu-accelerators
cp %{SOURCE2} images/

# fix qtemu data location
perl -pi -e \
	's|QCoreApplication::applicationDirPath\(\)|QString("%{qtemudir}")|g' \
	helpwindow.cpp main.cpp

%build
mkdir objs
cd objs

export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake \
	-DCMAKE_INSTALL_PREFIX=%{qtemudir} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std -C objs

# move files around
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{qtemudir}/bin/qtemu $RPM_BUILD_ROOT%{_bindir}/
rmdir $RPM_BUILD_ROOT%{qtemudir}/bin

# install icons
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}
install -m644 %{SOURCE10} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
install -m644 %{SOURCE11} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
install -m644 %{SOURCE12} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

# install menu entries

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QtEmu
Comment=A graphical user interface for QEMU
Exec=%{_bindir}/qtemu
Icon=%{name}
Type=Application
Terminal=false
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/qtemu
%dir %{qtemudir}
%{qtemudir}/*
# desktop integration
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/mandriva-%{name}.desktop




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2011.0
+ Revision: 614681
- the mass rebuild of 2010.1 packages

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Rediff patch2
    - Remove patch1 : Merged upstream
      Uncomment Patch2 in the top of the spec file

* Tue Mar 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.5-1mdv2010.1
+ Revision: 516850
- update to 1.0.5
- fix license

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4-7mdv2010.0
+ Revision: 442613
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.0.4-6mdv2009.1
+ Revision: 350143
- 2009.1 rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-5mdv2009.0
+ Revision: 259978
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-4mdv2009.0
+ Revision: 247785
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2008.1
+ Revision: 148339
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- do not harcode icon extension
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.4-2mdv2008.0
+ Revision: 53227
- Bump Release
- Readd patch2

* Wed Jul 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 53135
- Remove two patches, not needed


* Wed Mar 28 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0.3-1mdv2007.1
+ Revision: 149322
- 1.0.3
- enable QEMU Accelerator ("kqemu") by default if available

* Sun Mar 18 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0.2-2mdv2007.1
+ Revision: 145692
- add support for accelerators (kqemu, kvm)
- make it build with qt4.1 (Laurent Montel)
- requires qemu >= 0.9.0-3mdv so that "qemu" can use accelerators on x86_64

* Sat Mar 17 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0.2-1mdv2007.1
+ Revision: 145608
- initial mandriva linux package

