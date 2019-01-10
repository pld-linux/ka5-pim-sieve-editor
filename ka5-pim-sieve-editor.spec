%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		pim-sieve-editor
Summary:	Sieve editor
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	24898ae4f7f5d3c7ed61120b7c0f72b5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-kimap-devel >= 18.12.0
BuildRequires:	ka5-kmailtransport-devel >= 18.12.0
BuildRequires:	ka5-kpimtextedit-devel >= 18.12.0
BuildRequires:	ka5-libksieve-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kbookmarks-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sieve Editor is an editor for Sieve scripts used for email filtering
on a mail server.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/sieveeditor.categories
/etc/xdg/sieveeditor.renamecategories
%attr(755,root,root) %{_bindir}/sieveeditor
%attr(755,root,root) %ghost %{_libdir}/libsieveeditor.so.5
%attr(755,root,root) %{_libdir}/libsieveeditor.so.5.*.*
%{_desktopdir}/org.kde.sieveeditor.desktop
%{_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg
%attr(755,root,root) %{_datadir}/kconf_update/sieveeditor-15.08-kickoff.sh
%{_datadir}/kconf_update/sieveeditor.upd
%{_datadir}/metainfo/org.kde.sieveeditor.appdata.xml
