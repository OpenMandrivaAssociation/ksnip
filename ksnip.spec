%define gitbranch master
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')
%define gitdate 20250515

Name:		ksnip
Version:	1.11.0%{?gitdate:~0.%{gitdate}.}
Release:	1
Summary:	Screenshot tool
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/ksnip
Source:		https://github.com/ksnip/ksnip/archive/%{?gitdate:%{gitbranch}}%{!?gitdate:v%{version}}.tar.gz#/%{name}-%{?gitdate:%{gitbranchd}-%{gitdate}}%{!?gitdate:%{version}}.tar.gz

BuildSystem:   cmake
BuildOption:   -DBUILD_WITH_QT6:BOOL=ON

BuildRequires: cmake(ECM)
BuildRequires: cmake(kColorPicker-Qt6)
BuildRequires: cmake(kImageAnnotator-Qt6)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb-xfixes)

%description
Ksnip is a Qt based cross-platform screenshot tool that provides many
annotation features for your screenshots.

%find_lang %{name} --with-qt

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/org.ksnip.ksnip.appdata.xml
%{_datadir}/applications/org.ksnip.ksnip.desktop
%{_iconsdir}/hicolor/scalable/apps/ksnip.svg
