Name:    kde-artwork-active
Summary: Additional artwork (themes, sound themes, icons,etc...) for  Plasma Active
Version: 0.2
Release: 2
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/active/1.0/src/%{name}-%version.tar.bz2
BuildRequires: kdelibs4-devel

BuildArch: noarch


%description
Additional artwork (themes, sound themes, icons,etc...) for  Plasma Active

%files
%_kde_appsdir/ksplash/Themes/ActiveAir
%_kde_appsdir/kscreenlocker/main.qml
%_kde_appsdir/kscreenlocker/lockscreen-active.qml
%_kde_appsdir/kscreenlocker/unlock-normal.png
%_kde_appsdir/kscreenlocker/unlock-pressed.png
%_kde_appsdir/kscreenlocker/wallpaper.png
%_kde_datadir/wallpapers/*.*

#----------------------------------------------------------------------

%prep
%setup -q -n %{name}
%autopatch -p1

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build



%changelog
* Sat Apr 28 2012 Crispin Boylan <crisb@mandriva.org> 0.2-1
+ Revision: 794328
- New release

* Thu Dec 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-1
+ Revision: 737119
- imported package kde-artwork-active

