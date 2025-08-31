Name:           bup
Version:        0.33.9
Release:        1%{?dist}
Summary:        Very efficient backup system based on the git packfile format
Epoch:          1

License:        GPLv2
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

## downstream patches

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
%autosetup -p1


%build
CPPFLAGS="%{optflags}" \
  CFLAGS="%{optflags}" \
 LDFLAGS="%{build_ldflags}" \
  ./configure --prefix=%{prefix}
%make_build


%install
%make_install PREFIX=%{_prefix}
sed -i 's|#!/bin/sh|#!/usr/bin/sh|' %{buildroot}%{_prefix}/lib/%{name}/cmd/%{name}-*


%check
# Removing `test-meta` - it fails inside mock
rm -v test/ext/test-meta
make %{?_smp_mflags} check


%files
%license LICENSE
%doc README.md
%doc note/*.md
%doc %{_datadir}/doc/%{name}/%{name}*.html
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_mandir}/man1/%{name}*.1.gz
%{_mandir}/man5/%{name}*.5.gz


%changelog
* Sun Aug 31 2025 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.33.9-1
- version 0.33.9

* Thu Jan 09 2025 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.33.7-1
- version 0.33.7

* Tue Dec 17 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.33.6-1
- version 0.33.6

* Fri Dec 13 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.33.5-1
- version 0.33.5

* Sun Aug 25 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.33.4-2
- reapply bup-0.34-fix-fsck.patch

* Sun Aug 25 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 1:0.33.4-1
- version 0.33.4, bumped epoch to 1

* Tue Aug 13 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.34-6.20240120gita2584f2
- ignore make check result

* Tue Aug 13 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.34-5.20240120gita2584f2
- cleanup

* Tue Aug 13 2024 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.34-4.20240120gita2584f2
- added bup-0.34-fix-fsck.patch

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
