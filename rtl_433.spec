%global         github_owner merbanan
%global         github_name  rtl_433
%global         github_commit 22.11
%global         debug_package %{nil}
%define         build_timestamp %(date +"%Y%m%d")

Name:           %{github_name}
Version:        %{build_timestamp}
Release:        %{github_commit}
Summary:        Program to decode radio transmissions from devices on the ISM bands (and other frequencies)
License:        GPL-2.0-only

URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/refs/tags/%{github_commit}/%{name}-%{github_commit}.tar.gz

BuildRequires: cmake
%if 0%{?fedora} >= 37
BuildRequires: libusb1-devel
%else
BuildRequires: libusb-devel
%endif
BuildRequires: rtl-sdr-devel
BuildRequires: make
BuildRequires: gcc-c++

Requires:      rtl-sdr-devel

%description
Program to decode radio transmissions from devices on the ISM bands (and other frequencies)

%prep
%setup -n %{name}-%{github_commit}

%build
./do_build.sh

%install
# The do_build.sh does not output to _bindir.
install -p -D -m 755 ./build/src/rtl_433 %{buildroot}%{_bindir}/rtl_433

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/rtl_433

%changelog
* Sat Apr 11 2020 Thomas Vassilian <tvassili@redhat.com> - 1-1
- initial build for fc31
