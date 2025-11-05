#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Standard library cgi redistribution. "dead battery"
Summary(pl.UTF-8):	Redystrybucja "zużytej baterii" - cgi z biblioteki standardowej
Name:		python3-standard-cgi
Version:	3.13.0
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/standard-cgi/
Source0:	https://files.pythonhosted.org/packages/source/s/standard-cgi/standard_cgi-%{version}.tar.gz
# Source0-md5:	5d46e0506f01cbcb9719aad4d3c778b6
URL:		https://pypi.org/project/standard-cgi/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:75.0
%if %{with tests}
BuildRequires:	python3-test >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python is moving forward! Python finally started to remove dead
batteries. For more information, see PEP 594.

If your project depends on a module that has been removed from the
standard, python-deadlib project provides the redistribution of the
dead batteries.

%description -l pl.UTF-8
Python idzie do przodu! W końcu zaczął usuwać "zużyte baterie". Więcej
informacji w PEP 594.

Jeśli projekt zależy od modułu, który został usunięty ze standardu,
projekt python-deadlib prowadzi redystrybucję "zużytych baterii".

%prep
%setup -q -n standard_cgi-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m tests.test_cgi
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/cgi
%{py3_sitescriptdir}/standard_cgi-%{version}.dist-info
