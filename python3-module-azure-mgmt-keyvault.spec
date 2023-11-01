%define pypi_name azure-mgmt-keyvault

%def_without check

Name:    python3-module-%pypi_name
Version: 10.2.3
Release: alt1

Summary: Microsoft Azure Keyvault Management Client Library for Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/azure-mgmt-keyvault/

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-azure-devtools
BuildRequires: python3-module-azure-mgmt-resource
BuildRequires: python3-module-azure-sdk-tools
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-dotenv
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/azure/
%python3_sitelibdir/azure_mgmt_keyvault-%version.dist-info/


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 10.2.3-alt1
- Initial build for Sisyphus
