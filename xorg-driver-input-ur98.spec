Summary:	X.org input driver for Union Reality UR-F98 headtracker
Summary(pl):	Sterownik wej¶ciowy X.org dla trackera Union Reality UR-F98
Name:		xorg-driver-input-ur98
Version:	1.0.0.5
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-input-ur98-%{version}.tar.bz2
# Source0-md5:	7cdfe15fdd8e04e3d440b7fdd96bf811
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Union Reality UR-F98 headtracker.

%description -l pl
Sterownik wej¶ciowy X.org dla trackera Union Reality UR-F98.

%prep
%setup -q -n xf86-input-ur98-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/ur98_drv.so
%{_mandir}/man4/ur98.4*
