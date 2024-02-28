%define gitbranch master
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')
%define gitdate 20240228

Name:		ksnip
Version:	1.11.0
Release:	%{?gitdate:0.%{gitdate}.}1
Summary:	Screenshot tool
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/ksnip
Source:		https://github.com/ksnip/ksnip/archive/%{?gitdate:%{gitbranch}}%{!?gitdate:v%{version}}/%{name}-%{?gitdate:%{gitbranchd}}%{!?gitdate:%{version}}.tar.gz
Patch0:		ksnip-compile.patch

BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(kColorPicker-Qt5)
BuildRequires: cmake(kImageAnnotator-Qt5)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb-xfixes)

%description
Ksnip is a Qt based cross-platform screenshot tool that provides many
annotation features for your screenshots.

%prep
%autosetup -p1 -n %{name}-%{?gitdate:%{gitbranchd}}%{!?gitdate:%{version}}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-qt

%files
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/org.ksnip.ksnip.appdata.xml
%{_datadir}/applications/org.ksnip.ksnip.desktop
%{_iconsdir}/hicolor/scalable/apps/ksnip.svg
