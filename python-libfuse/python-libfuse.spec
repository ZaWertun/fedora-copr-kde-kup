%global srcname   fuse
%global real_name python-%{srcname}

Name:    python-lib%{srcname}
Version: 1.0.7
Release: 1%{?dist}
Summary: Python 2.x/3.x bindings for libfuse 2.x

License: LGPL-v2.1
URL:     https://github.com/libfuse/%{real_name}
Source0: https://github.com/libfuse/%{real_name}/archive/refs/tags/v%{version}/%{real_name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: pkgconfig(fuse)
BuildRequires: gcc

%global _description %{expand:
This is a Python interface to libfuse (https://github.com/libfuse/libfuse).}

%description %_description

%package -n python3-lib%{srcname}
Summary:       %{summary}

%description -n python3-lib%{srcname} %_description

%prep
%autosetup -n %{real_name}-%{version}


%build
%py3_build


%check
%{python3} setup.py test


%install
%py3_install


%files -n python3-lib%{srcname}
%doc README.md
%license COPYING
%{python3_sitearch}/%{srcname}.py
%pycached %{python3_sitearch}/%{srcname}.py
%{python3_sitearch}/%{srcname}parts/
%{python3_sitearch}/%{srcname}_python-*.egg-info/


%changelog
* Tue Mar 19 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.7-1
- initial spec for version 1.0.7


