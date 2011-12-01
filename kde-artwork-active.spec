Name:    kde-artwork-active
Summary: Additional artwork (themes, sound themes, icons,etc...) for  Plasma Active
Version: 0.1
Release: 1
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/active/1.0/src/%{name}-%version.tar.bz2
BuildRequires: kdelibs4-devel

BuildArch: noarch


%description
Additional artwork (themes, sound themes, icons,etc...) for  Plasma Active

%files
%_kde_appsdir/ksplash/Themes/activeair
%_kde_appsdir/kwin/lockscreen/main.qml
%_kde_appsdir/kwin/lockscreen/unlock-normal.png
%_kde_appsdir/kwin/lockscreen/unlock-pressed.png
%_kde_appsdir/kwin/lockscreen/wallpaper.png
%_kde_datadir/wallpapers/*.*

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

