%define __python %{_bindir}/python2.4
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python2.4-openid
Version:        2.0.1
Release:        %mkrel 1
Summary:        Python OpenID libraries
Group:          Development/Python
License:        Apache License
URL:            http://www.openidenabled.com/python-openid/
Source0:	http://openidenabled.com/files/python-openid/packages/python-openid-%{version}.tar.bz2
%if %{mdkversion} <= 200800
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
%endif
BuildArch:      noarch
Requires:	python2.4
BuildRequires:	python2.4-setuptools
BuildRequires:  python2.4-elementtree

%description
The OpenID library with batteries included.

Features of the 2.x.x series include:

 * Refined and easy-to-use API.

 * Extensive documentation.

 * Many storage implemetations including file-based, sqlite,
   postgresql, and mysql.

 * Simple examples to help you get started.

 * Licensed under the Apache Software License.

 * Includes a Simple Registration API

 * Versions 1.x.x supports protocol version 1; versions 2.x.x support
   both major OpenID protocol versions transparently


%prep
%setup -q -n python-openid-%{version}
find . -type f | xargs chmod a-x

%build
%{__python} -c 'import setuptools; execfile("setup.py")' build
%{__python} admin/runtests

%install
rm -rf %{buildroot}
%{__python} -c 'import setuptools; execfile("setup.py")' install \
	--skip-build --root %{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc background-associations.txt CHANGELOG LICENSE NEWS README doc examples
%{python_sitelib}/*

