Name:		ksnip
Version:	1.6.1
Release:	1
Summary:	Screenshot tool
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/ksnip
Source:		https://github.com/ksnip/ksnip/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(ECM)
BuildRequires: cmake(kColorPicker)
BuildRequires: cmake(kImageAnnotator)

BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb-xfixes)

%description
Ksnip is a Qt based cross-platform screenshot tool that provides many
annotation features for your screenshots.

%prep
%setup -q

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
