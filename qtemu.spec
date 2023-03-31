%define qtemudir %{_datadir}/qtemu

Summary:	A graphical user interface for QEMU
Name:		qtemu
Version:	2.1
Release:	3
Source0:	https://gitlab.com/qtemu/gui/-/archive/%{version}/gui-%{version}.tar.bz2
Source10:	qtemu.png
Source11:	qtemu.16.png
Source12:	qtemu.48.png
# Don't use obsolete -soundhw
Patch0:		https://gitlab.com/qtemu/gui/-/merge_requests/6.patch
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
%autosetup -p1 -n gui-%{version}
%qmake_qt5 PREFIX=/usr

%build
%make_build

%install
install -d %{buildroot}/%{_bindir}
install -m 0755 qtemu %{buildroot}%{_bindir}
install -d %{buildroot}/%{_datadir}/applications
install -m 0644 qtemu.desktop %{buildroot}%{_datadir}/applications/
install -d %{buildroot}/%{_datadir}/pixmaps
install -m 0644 qtemu.png %{buildroot}%{_datadir}/pixmaps/

%files
%{_bindir}/qtemu
%{_datadir}/applications/qtemu.desktop
%{_datadir}/pixmaps/qtemu.png
