%define name	qtemu
%define version	1.0.4
%define release	%mkrel 1
%define qtemudir %{_datadir}/qtemu

Summary:	A graphical user interface for QEMU
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source10:	qtemu.png
Source11:	qtemu.16.png
Source12:	qtemu.48.png
Patch1:		qtemu-fix-compile-qt4.1.patch
Patch2:		qtemu-qemu-accelerators.patch
Source2:	processor.png
License:	GPL
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
#%patch1 -p1 -b .fix-compile-qt4.1
#%patch2 -p1 -b .qemu-accelerators
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
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): \
 needs="x11" \
 section="More Applications/Emulators" \
 title="QtEmu" \
 longtitle="A graphical user interface for QEMU" \
 command="qtemu" \
 icon="%{name}.png"\
 xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=QtEmu
Comment=A graphical user interface for QEMU
Exec=%{_bindir}/qtemu
Icon=%{name}.png
Type=Application
Terminal=false
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%{_bindir}/qtemu
%dir %{qtemudir}
%{qtemudir}/*
# desktop integration
%{_menudir}/%{name}
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/mandriva-%{name}.desktop

