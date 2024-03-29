#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython-sql
Version  : 0.4.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/f9/6a/286fa8e95db0567b50e2e207f9e45d65223b51b43fc5614729e4275c074b/ipython-sql-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/6a/286fa8e95db0567b50e2e207f9e45d65223b51b43fc5614729e4275c074b/ipython-sql-0.4.0.tar.gz
Summary  : RDBMS access via IPython
Group    : Development/Tools
License  : MIT
Requires: ipython-sql-license = %{version}-%{release}
Requires: ipython-sql-python = %{version}-%{release}
Requires: ipython-sql-python3 = %{version}-%{release}
Requires: SQLAlchemy
Requires: ipython
Requires: ipython_genutils
Requires: prettytable
Requires: six
Requires: sqlparse
BuildRequires : SQLAlchemy
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : prettytable
BuildRequires : six
BuildRequires : sqlparse
Patch1: 0001-Add-missing-NEWS.rst-file.patch
Patch2: 0002-Unpin-prettytable-dependency.patch

%description
ipython-sql
        ===========

%package license
Summary: license components for the ipython-sql package.
Group: Default

%description license
license components for the ipython-sql package.


%package python
Summary: python components for the ipython-sql package.
Group: Default
Requires: ipython-sql-python3 = %{version}-%{release}

%description python
python components for the ipython-sql package.


%package python3
Summary: python3 components for the ipython-sql package.
Group: Default
Requires: python3-core
Provides: pypi(ipython_sql)
Requires: pypi(ipython)
Requires: pypi(ipython_genutils)
Requires: pypi(prettytable)
Requires: pypi(six)
Requires: pypi(sqlalchemy)
Requires: pypi(sqlparse)

%description python3
python3 components for the ipython-sql package.


%prep
%setup -q -n ipython-sql-0.4.0
cd %{_builddir}/ipython-sql-0.4.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635742653
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipython-sql
cp %{_builddir}/ipython-sql-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/ipython-sql/1c9900f6ca015de4cf1c4f0ef5b9be5361c90a15
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipython-sql/1c9900f6ca015de4cf1c4f0ef5b9be5361c90a15

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
