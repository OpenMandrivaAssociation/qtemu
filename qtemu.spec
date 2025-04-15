%define qtemudir %{_datadir}/qtemu
%global git_commit d6c2d66ae88f38f8ed529c56f5c2b446e9dc3eb1
%global shortcommit %(c=%{git_commit}; echo ${c:0:7})

Summary:	A graphical user interface for QEMU
Name:		qtemu
Version:	2.2.git%{shortcommit}
Release:	1
# Original version:
# http://www.qtemu.org/
# https://gitlab.com/qtemu/gui
# seems dead-ish, let's use a fork that is at least maintained enough
# to be ported to Qt6

#Arch ins using https://gitlab.com/qtemu/gui for the git version
# Newest release of MateuszKrawczuk/QtEmu will not build with qt6.9
Source0:	https://gitlab.com/qtemu/gui/-/archive/d6c2d66ae88f38f8ed529c56f5c2b446e9dc3eb1/gui-d6c2d66ae88f38f8ed529c56f5c2b446e9dc3eb1.tar.gz
Source10:	qtemu.png
Source11:	qtemu.16.png
Source12:	qtemu.48.png
#Patch2:		qtemu-qemu-accelerators.patch
Source2:	processor.png
License:	GPL-2.0
Group:		Emulators
Url:		https://www.qtemu.org/
Requires:	qemu
BuildRequires:	cmake ninja
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)

%description
QtEmu is a graphical user interface for QEMU written in Qt4. It has
the ability to run virtual operating systems on native systems. This
way you can easily test a new operating system or try a Live CD on
your system without any troubles and dangers.

%prep
%autosetup -p1 -n gui-%{git_commit}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
install -d %{buildroot}/%{_bindir}
install -m 0755 build/qtemu %{buildroot}%{_bindir}
install -d %{buildroot}/%{_datadir}/applications
install -m 0644 qtemu.desktop %{buildroot}%{_datadir}/applications/
install -d %{buildroot}/%{_datadir}/pixmaps
install -m 0644 qtemu.png %{buildroot}%{_datadir}/pixmaps/

%files
%{_bindir}/qtemu
%{_datadir}/applications/qtemu.desktop
%{_datadir}/pixmaps/qtemu.png
