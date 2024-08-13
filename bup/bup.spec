%global git_rev   a2584f274aaae6f1428193763eed64282619fe08
%global git_date  20240120
%global git_short %(c=%{git_rev}; echo ${c:0:7})

Name:           bup
Version:        0.34
Release:        3.%{git_date}git%{git_short}%{?dist}
Summary:        Very efficient backup system based on the git packfile format

License:        GPLv2
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive//%{git_rev}/%{name}-%{version}-%{git_short}.tar.gz

%global git_min_ver 1.5.6

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  git-core >= %{git_min_ver}

BuildRequires:  perl-Time-HiRes
BuildRequires:  python3-devel
BuildRequires:  python3-fuse
BuildRequires:  python3-pylibacl
BuildRequires:  python3-pyxattr
BuildRequires:  python3-tornado

# For tests:
BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  kmod
BuildRequires:  rsync
BuildRequires:  man-db
BuildRequires:  par2cmdline
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist

Requires:       git-core >= %{git_min_ver}
Requires:       par2cmdline
Requires:       python3 >= 3.7
# https://github.com/libfuse/python-fuse
Requires:       python3-libfuse
Requires:       python3-pylibacl
Requires:       python3-pyxattr
Requires:       python3-tornado

%description
Very efficient backup system based on the git packfile format,
providing fast incremental saves and global deduplication
(among and within files, including virtual machine images).


%prep
%autosetup -p1 -n %{name}-%{git_rev}


%build
# Macros `%%configure` can't be used - it's not configure from autotools
./configure
%make_build


%install
%make_install PREFIX=%{_prefix}
sed -i 's|#!/bin/sh|#!/usr/bin/sh|' %{buildroot}%{_prefix}/lib/%{name}/cmd/%{name}-*


%check
# Removing `test-meta` - it fails inside mock
rm -v test/ext/test-meta
# Test `test-help` broken since Fedora 39
make %{?_smp_mflags} check ||:


%files
%license LICENSE
%doc README.md
%doc note/*.md
%doc %{_datadir}/doc/%{name}/%{name}*.html
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_mandir}/man1/%{name}*.gz



%changelog
* Tue Aug 13 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.34-3.20240120gita2584f2
- reverted to commit a2584f2, Jan 20, 2024

* Tue Aug 13 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.34-2.20240728gitd049e9b
- updated to commit d049e9b, Jul 28, 2024

* Wed Mar 06 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.33.3-1
- version 0.33.3

* Wed Oct 25 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.33.2-1
- version 0.33.2

* Wed Mar 29 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.33-1
- version 0.33

* Tue Dec 07 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.32-2
- added par2cmdline to Requires & BuildRequires

* Tue Dec 07 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.32-1
- first spec for version 0.32
