Name:		ksnip
Version:	1.7.1
Release:	1
Summary:	Screenshot tool
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/ksnip
Source:		https://github.com/ksnip/ksnip/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(ECM)
BuildRequires: cmake(kColorPicker) >= 0.1.4
BuildRequires: cmake(kImageAnnotator) >= 0.3.1

BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb-xfixes)

Obsoletes:    %{_lib}kcolorpicker%{major} =< 0.1.1-1
Obsoletes:    %{_lib}kimageannotator%{major} =< 0.2.1-1

%description
Ksnip is a Qt based cross-platform screenshot tool that provides many
annotation features for your screenshots.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc CHANGELOG.md CODINGSTYLE README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.??g
