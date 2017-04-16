Name:           ros-kinetic-geodesy
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS geodesy package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/geodesy
Source0:        %{name}-%{version}.tar.gz

Requires:       pyproj
Requires:       ros-kinetic-geographic-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-unique-id
Requires:       ros-kinetic-uuid-msgs
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geographic-msgs
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-unique-id
BuildRequires:  ros-kinetic-uuid-msgs

%description
Python and C++ interfaces for manipulating geodetic coordinates.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Apr 16 2017 Jack O'Quin <jack.oquin@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Sat Apr 15 2017 Jack O'Quin <jack.oquin@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

* Fri Apr 15 2016 Jack O'Quin <jack.oquin@gmail.com> - 0.4.0-0
- Autogenerated by Bloom
