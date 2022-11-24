%define qtemudir %{_datadir}/qtemu

Summary:	A graphical user interface for QEMU
Name:		qtemu
Version:	2.1
Release:	1
Source0:	https://gitlab.com/qtemu/gui/-/archive/%{version}/gui-%{version}.tar.bz2
Source10:	qtemu.png
Source11:	qtemu.16.png
Source12:	qtemu.48.png
#Patch2:		qtemu-qemu-accelerators.patch
Source2:	processor.png
License:	GPLv2
Group:		Emulators
Url:		http://www.qtemu.org/
Requires:	qemu
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
QtEmu is a graphical user interface for QEMU written in Qt4. It has
the ability to run virtual operating systems on native systems. This
way you can easily test a new operating system or try a Live CD on
your system without any troubles and dangers.

%prep
%autosetup -n gui-%{version}

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
install -d %{buildroot}/%{_bindir}
install -m 0755 qtemu %{buildroot}%{_bindir}
install -d %{buildroot}/%{_datadir}/applications
install -m 0644 qtemu.desktop %{buildroot}%{_datadir}/applications/
install -d %{buildroot}/%{_datadir}/pixmaps
install -m 0644 qtemu.png %{buildroot}%{_datadir}/pixmaps/




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

