Name:           openhantek
Version:        git
Release:		0
Summary:        The official Hantek DSO software for linux
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Source:      	%{name}
BuildRequires:  cmake, fftw3-devel, libusb-1_0-devel, libqt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

#Default directory for udev on SuSe
%define udevdir /etc/udev/rules.d
%define firmwares_directory /usr/local/share/hantek/


%description
OpenHantek is a free software for Hantek (Voltcraft/Darkwire/Protek/Acetech) USB DSOs based on HantekDSO.
The UI is written in C++/Qt 4 and uses OpenGL to draw the graphs. It was tested with the DSO-2090,
test results with other models are welcome.

OpenHantek has started as an alternative to the official Hantek DSO software for Linux users.
At the moment it's basically running under Mac OS X too, but since this lacks udev you'll have
to load the firmware by hand up too now.


%package -n %{name}-firmwares
Requires: %{name}
Summary: OpenHantek firmwares

%description -n %{name}-firmwares
Firmwares and for OpenHantek supported oscilloscopes


%package -n %{name}-udev
Requires: %{name}
Summary: OpenHantek udev rules

%description -n %{name}-udev
Udev rules for OpenHantek supported oscilloscopes.
The group have been changed to users.


%prep
%setup -c -T
cp -R %{_sourcedir}/%{name}/* .

%{__mkdir} build
cd build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" ..


%build
cd build
%{__make} -j4

%install
cd build
%{__rm} -rf "%{buildroot}"
%{__make} %{?_smp_mflags} DESTDIR="%{buildroot}" install

# copy udev rules
mkdir -p %{buildroot}/%{udevdir}/
cp %{_sourcedir}/%{name}/firmware/90-hantek.rules %{buildroot}/%{udevdir}/
sed -i 's/plugdev/users/g' %{buildroot}/%{udevdir}/90-hantek.rules
# copy firmwares
mkdir -p %{buildroot}/usr/local/share/hantek/
cp %{_sourcedir}/%{name}/firmware/*.hex %{buildroot}/usr/local/share/hantek/


%files
%defattr(-,root,root)
%{_bindir}/OpenHantek
%{_prefix}/images/*

%files -n %{name}-firmwares
%defattr(-,root,root)
%{firmwares_directory}/*.hex

%files -n %{name}-udev
%defattr(-,root,root)
%{udevdir}/90-hantek.rules





