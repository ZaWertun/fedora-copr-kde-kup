%global real_name kup

#global git_rev   3937544afe0c4b2fe4565fb648da999fab641e66
#global git_date  20240302
#global git_short %(c=%{git_rev}; echo ${c:0:7})

Name:           kde-kup
Epoch:          1
Version:        0.10.0
Release:        1%{?dist}
Summary:        Backup scheduler for the Plasma desktop

License:        GPLv2+
URL:            https://invent.kde.org/system/%{real_name}
%if 0%{?git_rev}
Source0:        https://invent.kde.org/system/%{real_name}/-/archive/%{git_rev}/%{real_name}-%{real_name}-%{git_short}.tar.gz
%else
Source0:        https://invent.kde.org/system/%{real_name}/-/archive/%{real_name}-%{version}/%{real_name}-%{real_name}-%{version}.tar.gz
%endif

## upstream patches

## upstreamable patches

BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Plasma)
BuildRequires: cmake(Plasma5Support)

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6CoreTools)

BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6WidgetsAddons)

BuildRequires: pkgconfig(libgit2)

Requires:      bup
Requires:      rsync
Requires:      hicolor-icon-theme

Requires:      kf6-kservice
Requires:      plasma-workspace
Requires:      plasma-workspace-libs

%description
%{summary}.


%prep
%if 0%{?git_rev}
%autosetup -p1 -n %{real_name}-%{git_rev}
%else
%autosetup -p1 -n %{real_name}-%{real_name}-%{version}
%endif


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install
%find_lang %{real_name} --with-qt


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_%{real_name}.desktop


%files -f %{real_name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_bindir}/%{real_name}-daemon
%{_kf6_bindir}/%{real_name}-filedigger
%{_kf6_bindir}/%{real_name}-purger
%{_kf6_plugindir}/kio/kio_bup.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_%{real_name}.so
%{_kf6_qtplugindir}/plasma5support/dataengine/plasma_engine_%{real_name}.so
%{_qt6_settingsdir}/autostart/%{real_name}-daemon.desktop
%{_kf6_metainfodir}/org.kde.%{real_name}.appdata.xml
%{_kf6_metainfodir}/org.kde.%{real_name}applet.appdata.xml
%{_kf6_datadir}/applications/kcm_%{real_name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{real_name}.svg
%{_kf6_datadir}/knotifications6/%{real_name}daemon.notifyrc
%{_kf6_datadir}/plasma/plasmoids/org.kde.kupapplet/
%{_kf6_datadir}/plasma5support/services/%{real_name}daemonservice.operations
%{_kf6_datadir}/plasma5support/services/%{real_name}service.operations
%{_kf6_datadir}/qlogging-categories6/%{real_name}.categories


%changelog
* Fri May 31 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.10.0-1
- version 0.10.0

* Tue Dec 07 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.9.1-1
- first spec for version 0.9.1
