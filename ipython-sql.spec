#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython-sql
Version  : 0.3.9
Release  : 13
URL      : https://pypi.python.org/packages/83/ed/f6c8ece48f0f10a7543c971cdb1a62e6f91b374e31f6b579b7a37fb0a6a3/ipython-sql-0.3.9.tar.gz
Source0  : https://pypi.python.org/packages/83/ed/f6c8ece48f0f10a7543c971cdb1a62e6f91b374e31f6b579b7a37fb0a6a3/ipython-sql-0.3.9.tar.gz
Summary  : RDBMS access via IPython
Group    : Development/Tools
License  : MIT
Requires: ipython-sql-python3
Requires: ipython-sql-python
Requires: SQLAlchemy
Requires: ipython
Requires: ipython_genutils
Requires: prettytable
Requires: six
Requires: sqlparse
BuildRequires : SQLAlchemy
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : pbr
BuildRequires : pip
BuildRequires : prettytable

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : sqlparse

%description
ipython-sql
        ===========

%package python
Summary: python components for the ipython-sql package.
Group: Default
Requires: ipython-sql-python3

%description python
python components for the ipython-sql package.


%package python3
Summary: python3 components for the ipython-sql package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipython-sql package.


%prep
%setup -q -n ipython-sql-0.3.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522982379
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
